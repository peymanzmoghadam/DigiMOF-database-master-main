from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging
import re
from lxml import etree

from . import R, I, W, T, Optional, merge, join, Any, OneOrMore, Not, ZeroOrMore, SkipTo
from .base import BaseParser
from ..utils import first
from .cem import cem, chemical_label, lenient_chemical_label, solvent_name, chemical_name, MOF_name, MOF_formula
from .common import lbrct, dt, rbrct, comma
from ..model import Topology, Compound


from .extract import extract_value, extract_capa_units
delim = R('^[:;\.,-]$')

#Words that commonly come before or after MOF compound names
top_specifier = (I(u'topology') | I('net') | I('topologies') |(Optional(delim) + I('connected'))).hide()

#Most common topologies
topology = (Optional(R('^\(.....\)-')) + Optional(delim) + I('sql-a')|R('^tfz-?d?$')|R('^gme$')|R('^acs$') | I('aea') | I('alb') | I('bnn') | R('^bon$') | I('crs') | I('ctn') | I('dmd') | I('edq') | I('gra') |
            I('fcu-c') | I('fgl') | I('fgh') | I('fmj') | I('fns') | I('fof') | I('fon') | I('frf') | I('gar') | I('gea') | I('gee') | I('hbk') | I('hbr') | I('hcb') |
            I('hex') | I('hey') | I('hfp') | I('htp') | I('hms') | I('hxg-b') | I('hyb') | I('hyx') | I('iab') | I('ith-d') | I('jea') | I('jjt') | I('kag') | I('kce') | I('kex') | I('kgm') |
            I('kom') | R('^lim$') | I('lon-e') | I('llj') | I('lqm') | I('mfj') | I('mab') | I('ncb') | I('nha') | I('nht') | I('nia') | I('nou') | I('nun') | I('ntt') | I('ott') |
            I('pek') | I('pfm') | I('pto') | I('pts') | I('pyr') | I('rtl') | R('^she$') | I('shp') | I('soc') | I('sod') | I('sph') | I('sqc') | I('sra') | (R('sql')) | I('ssa') | R('^stp$') | I('sra') |
            I('sty') | I('sur') | I('tam') | I('tbo') | I('tfb') | I('tfe') | I('the-a') | I('ths') | I('ths-z') | I('toz') | I('tph') | I('tto') | I('ttp') |
            I('ttu') | I('tty') | I('ttz') | I('ubt') | I('ucp') | I('umt') | I('urj') | I('urx') | I('usf') | I('xmz') | I('yav') | I('ybh') | I('zyg') | I('zfy') |
            I('lvt') | I('ssb') | I('pto-a') | I('pto') | I('bct') | I('mtn') | I('bcu') | I('fcu') | I('ith') | R('^srs$') | I('sqc124') | I(u'pcu') | I('reo') | I(u'dia') |
           I('csq-a') | I(u'kat') | R('^scu$') | I(u'tbo') | I(u'dia-a') | I('spn') | I('kgd') | (I('ftw-a')) | I('ftw') | I('PTS') | I('PTs-x')
            | I('qom') | I(u'rht')| I(u'pcu-a') | I('nbo-a') | I('fsc') | I('fla') | I('flu') | I('nbo') | I('agw') | I('smy')  + Optional(delim)
              + Optional(R('^[a-zA-Z0-9]+$')) + Optional('type'))(u'abrv').add_action(merge)

#common words that come before or after the MOF compound name or topology
prefix = (Optional(I('and')).hide() + Optional(I('with')).hide() + Optional('in').hide() +
    Optional(I('the') | I('a') | I('an') | I('its') | I('with')).hide() + Optional(delim).hide() + Optional('same').hide() + Optional(I('connected')).hide() +
    Optional(I('isoreticular')).hide() + Optional(I('structures')).hide() + Optional(I('of')).hide() + Optional(top_specifier).hide() + Optional('for').hide() +
    Optional(I('the')).hide() + Optional(I('following')).hide() + Optional(I('eight')).hide() + Optional(I('compounds')).hide() + Optional(I('inherently')).hide() +
    Optional(I('is')).hide() + Optional('rod-packing').hide() +
    Optional(I('excellent') | I('high') | I('low') | I('stable') | I('superior') | I('maximum') | I('highest')).hide() +
    Optional(I('initial')).hide() +
    Optional(I('varies') + I('from')).hide() +
    Optional(W('=') | W('~') | W('≈') | W('≃') | I('of') | I('was') | I('is') | I('at') | I('as') |
             I('near') | I('above') | I('below')).hide() +
    Optional(top_specifier).hide() +
    Optional(I('reported') | I('determined') | I('measured') | I('calculated') | I('known') | I('found') | I('has')).hide() +
    Optional(I('as') | (I('to') + I('be'))).hide() + Optional(comma).hide() + Optional(I('as')).hide() + Optional(I('exemplified')).hide() + Optional(I('by')).hide() + Optional(I('the')).hide() +
    Optional( I('in') + I('the') + I('range') | I('ranging')).hide() +
    Optional(I('of')).hide() + Optional(I('planar')) +
    Optional(I('about') | I('from') | I('approximately') | I('around') |
             (I('high') + I('as')) | (I('higher') | I('lower') + I('than'))
             | (I('up') + I('to') | I('in') + I('excess') + I('of'))).hide())

#topology parsing rule
tp = (Optional(delim).hide() + Optional(prefix).hide() + topology + Optional(top_specifier).hide() + Optional(prefix).hide() + Optional(delim).hide())(u'tp')

#Accounts for different versions of chemical entity mentions in the text
cem_prefix = ( Optional(lbrct).hide() +
    cem('cem') +
    Optional(rbrct).hide() +
    Optional(delim).hide())

#Accounts for when there are multiple chemical entity mentions
multi_cem = ZeroOrMore(cem_prefix + Optional(comma).hide()) + Optional(delim) + Optional(I('and') | comma).hide() + cem_prefix

#Accounts for when there is a prefix followed by chemical entity mention followed by topology
prefix_cem_top = (
                Optional(prefix).hide()  +
                Optional(I('the') | I('a') | I('an') | I('these') | I('those') | I('this') | I('that')).hide() + Optional(W('[')).hide() +
                (Optional(lbrct) + SkipTo(MOF_name|MOF_formula|lenient_chemical_label) +
                 cem|lenient_chemical_label + Optional(rbrct)) + Optional(W(']')) +
                Optional(lbrct +Optional(cem_prefix | lenient_chemical_label | multi_cem | chemical_label) + rbrct) +
                Optional(I('is') | I('was') | I('were') | I('occurs') | I('of') | I('could') | I('can')
                | I('remained') | (I('can') |I('has')|I('with') + I('be') + I('assigned') + Optional(I('at') | I('to')))).hide() +
                Optional(I('reach') | I('reaching') | I('observed') | I('determined') | I('measured') |
                I('calculated') | I('found') | I('increased') | I('expected')).hide() +
                Optional(I('in') + I('the') + I('range') + I('of') | I('ranging') + I('from') | I('as')
                | I('to') | I('to') + I('be') | I('about') | I('over') | ( I('higher') | I('lower')) + I('than') |
                I('above')).hide() + Optional(delim) +
                Optional(lbrct).hide() + SkipTo((tp)) +
                (tp) +
                Optional(rbrct).hide())('top_phrase')

#Accounts for when there are multiple topologies and MOF compound names in a sentence
multiple_top = (SkipTo(MOF_name | MOF_formula) +  OneOrMore(cem) + OneOrMore(tp))('top_phrase')

#Accounts for when there is a prefix followed by a topology followed by chemical entity mention
prefix_top_cem = (Not(I('zinc')) +
                 Optional(prefix).hide() + SkipTo(tp) + tp + Optional(delim) + Optional(I('type')) + Optional(I('acylamide'))
                    + Optional(I('functionalized')) +
                 Optional(I('MOF')) + Optional(lbrct) + SkipTo(MOF_name|MOF_formula|chemical_label) + cem + Optional(rbrct)
                    )('top_phrase')

#Accounts for when the chemical entity is labelled then followed by a prefix followed by topology
cem_prefix_top_labelled = (Not(I('zinc')) +
                Optional(cem | chemical_label) + Optional(comma) + Optional(prefix) +Optional(I('has')) + Optional(delim)
                  + tp + Optional(top_specifier) +Optional(I('functionalized'))
                  + Optional(I('MOF')) + Optional(delim)
)('top_phrase')

#Accounts for when there is a cehmical entity mention followed by a prefix followed by topology
cem_prefix_top_unlabelled = (Not(I('zinc')) + SkipTo(MOF_name|MOF_formula|chemical_label|lenient_chemical_label) +
                Optional(cem | chemical_label) + Optional(comma) + Optional(prefix) +Optional(I('has')) + Optional(delim)
                  + tp + Optional(top_specifier) +Optional(I('functionalized'))
                  + Optional(I('MOF')) + Optional(delim)
)('top_phrase')

#Complete parsing rule for recognizing MOF compound names and topologies
tp_phrase = multiple_top | prefix_top_cem | cem_prefix_top_labelled | prefix_cem_top | cem_prefix_top_unlabelled

#Topology parsing class
class cem_TpParser(BaseParser):
    """"""
    root = tp_phrase

    def interpret(self, result, start, end):
        compound = Compound(
            topologies=[
                Topology(
                    abrv =first(result.xpath('./tp/abrv/text()')) #text() selects the text nodes
                )
            ]
        )
        cem_el = first(result.xpath('./cem'))
        #Associates compound name with the topology
        if cem_el is not None:
            compound.names = cem_el.xpath('./name/text()')
            compound.labels = cem_el.xpath('./label/text()')
        yield compound