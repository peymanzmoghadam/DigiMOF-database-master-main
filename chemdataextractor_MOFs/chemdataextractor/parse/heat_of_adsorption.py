from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging
import re

from . import R, I, W, T, Optional, merge, join, Any, OneOrMore, Not, ZeroOrMore, SkipTo
from .base import BaseParser
from ..utils import first
from .cem import cem, chemical_label, lenient_chemical_label, solvent_name
from .common import lbrct, dt, rbrct, comma
from ..model import Topology, Compound, AdsorptionEnthalpy
from .extract import extract_value, extract_capa_units

delim = R('^[,:;\.\[\]\(\)\{\}/]$').hide()
symbol_prefix = (Optional(cem) +W(u'ΔHads')+Optional(I('of')) ).hide()#this matches with just heat
of_prefix = Optional(cem) +(I(u'heat')|I(u'enthalpy')) + I(u'of') + Optional(cem) + I(u'adsorption') + Optional(I('of')) + Optional(delim) + Optional(I('Qst'))
standard_prefix = Optional(cem) + I(u'adsorption') + (I(u'heat')|I(u'enthalpy')) + Optional(lbrct) + Optional(I('Qst')) + Optional(rbrct)
standard_prefix_of = standard_prefix + Optional(I('of')|I(u'for')) + Optional(lbrct) + Optional(I('Qst')) +Optional(rbrct)
prefix_cem_after = symbol_prefix|of_prefix|standard_prefix_of + Optional(cem)
prefix_cem_before = Optional(cem)+ symbol_prefix|of_prefix|standard_prefix_of
prefix = (prefix_cem_after|prefix_cem_before)
prefix_of= prefix + Optional(I('of')) +  Optional(I('was')) + Optional(I('is')) + Optional(('determined')) + Optional(('to')) + Optional(I('be'))
#this combined prefix matches all of them without instances of cems
unit_spaces = ((I('kj') +Optional(I(u'/'))+ I('mol-1')|I('mol−1')|I('mol'))|(I('j') +Optional(I(u'/'))+ I('mol-1')|I(u'mol−1'))| I('kj') +Optional(I(u'/'))+ I('mol−1'))(u'units').add_action(merge)
unit_nospaces = (Optional(I(u'k'))+I(u'jmol-1')|I(u'kjmol-1')|I('jmol−1'))(u'units').add_action(merge)
unit_slashes = ((I('kj') +(I(u'/'))+ I('mol'))|(I('j') +(I(u'/'))+ I('mol')))(u'units').add_action(merge)
units = unit_spaces|unit_nospaces|unit_slashes
#units = (I(u'kj') + I('mol-1'))(u'units').add_action(merge)
value = R(u'^\d+(\.\d+)?$')(u'value')
ads_nodescriptor = (Optional(cem)+(prefix_of|prefix)+ Optional(I('of')|I(u'for'))+Optional(cem)+ Optional(I('of'))+ Optional(I('was')) + Optional(lbrct).hide() + value + units+ Optional(rbrct).hide())(u'ads')
ads_descriptor = ads_nodescriptor + ZeroOrMore(Not(ads_nodescriptor) + Not(cem) +Any())+cem
ads = (ads_nodescriptor|ads_descriptor)(u'ads')

class AdsParser(BaseParser):
    root = ads

    def interpret(self, result, start, end):
        compound = Compound(
            adsorption_enthalpies=[
                AdsorptionEnthalpy(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        cem_el = first(result.xpath('./cem'))
        if cem_el is not None:
            compound.names = cem_el.xpath('./name/text()')
            compound.labels = cem_el.xpath('./label/text()')
        yield compound