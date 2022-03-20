from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from . import R, I, W, Optional, merge, Not, SkipTo
from .base import BaseParser
from ..utils import first
from .cem import cem, chemical_label, lenient_chemical_label, solvent_name, MOF_name, MOF_formula
from .common import comma
from ..model import Compound, SynthesisRoute



delim = R('^[:;\.,-]$')

#Words commonly used to describe the synthesis method
adj= (R(u'^[Rr]apid(ly)?$')|R(u'^[eE]fficient(ly)?$')|R(u'^[Nn]ovel?$')|R(u'^[sS]calab(ly|e)?$')|I('obtained')|I('similar')).hide()

#Common prefixes before the synthesis method
prefix = (Optional(I('and')).hide() + Optional(I('with')).hide() + Optional('in').hide() +
    Optional(I('the') | I('a') | I('an') | I('its') | I('with')).hide() + Optional(delim).hide() + Optional('same').hide() + Optional(I('connected')).hide() +
    Optional(I('isoreticular')).hide() + Optional(I('structures')).hide() + Optional(I('of')).hide() + Optional('for').hide() +
    Optional(I('the')).hide() + Optional(I('following')).hide() + Optional(I('eight')).hide() + Optional(I('compounds')).hide() + Optional(I('inherently')).hide() +
    Optional(I('is')).hide() + Optional('rod-packing').hide() +
    Optional(I('excellent') | I('high') | I('low') | I('stable') | I('superior') | I('maximum') | I('highest')).hide() +
    Optional(I('initial')).hide() +
    Optional(I('varies') + I('from')).hide() +
    Optional(W('=') | W('~') | W('≈') | W('≃') | I('of') | I('was') | I('is') | I('at') | I('as') |
             I('near') | I('above') | I('below')).hide() +
    Optional(I('reported') | I('determined') | I('measured') | I('calculated') | I('known') | I('found') | I('has')).hide() +
    Optional(I('as') | (I('to') + I('be'))).hide() + Optional(comma).hide() + Optional(I('as')).hide() + Optional(I('exemplified')).hide() + Optional(I('by')).hide() + Optional(I('the')).hide() +
    Optional( I('in') + I('the') + I('range') | I('ranging')).hide() +
    Optional(I('of')).hide() + Optional(I('planar')) +
    Optional(I('about') | I('from') | I('approximately') | I('around') |
             (I('high') + I('as')) | (I('higher') | I('lower') + I('than'))
             | (I('up') + I('to') | I('in') + I('excess') + I('of'))).hide())

#Common words used before the synthesis method
specifier = (prefix + Optional(adj)+R(u'^[Ss]ynthe((si(s|sed|zed|se|ze))|tic)?$')| R(u'^[Pp]repar(ation|ed|e)?$')| R(u'^[Pp]roduc(tion|e|ed)?$')| R(u'^[Mm]a(de|ke)?$')|I('under')|I('similar')+Optional(adj)+Optional(R(u'^[Aa]|[Aa][Nn]?$'))).hide()

#Common words to describe the solvent used with the synthesis method
conj = (R(u'^[Tt]hrough?$')|R(u'^[Ww]ith?$')|R(u'^[Bb]y?$')|R(u'^[Vv]ia?$')|R(u'^[Uu]sing?$')|R(u'^[Ee]mploying?$')|R(u'^[Uu]tili[sz]ing?$')|R(u'^[Ee]nlisting?$')|R(u'^[Aa]nd?$')).hide() #having and in here may not be restrictive enough

#Different words used to describe the synthesis method
descriptor = (Optional(adj)+(R(u'^[Mm]icrowave$')| R(u'^[Ll]iquid$'))+ Optional(R('^[\-‐‑⁃‒–—―−－⁻]$'))+R(u'^[Aa]ssisted$')+Optional(R(u'^[Gg]rinding$')))(u'descriptor').add_action(merge)

#The different types of synthesis methods
synthesis = (Optional(adj)+(R(u'^[SsHh](olv|ydr)othermal(ly)?$')|R(u'^[mMsS](on|echan)ochemical(ly)?$')|R('^hydro\(solvo\)thermal(ly)?$'))|descriptor+Optional(specifier))(u'synthesis').add_action(merge)

#Solvent identifiers
solvent1 = (R(u'^[Ii]n?$').hide()+Optional(R(u'^[Aa]|[Aa][Nn]?$')).hide()+Optional(R(u'^[Tt]he?$')).hide()+Optional(adj)+Optional(R(u'^[Ss]olvent?$')).hide()+cem|solvent_name|chemical_label|lenient_chemical_label+Optional(R(u'^[Ss]olvent?$')))

solvent2=(Optional(conj.hide())+(Optional(R(u'^[Ii]n?$'))).hide()+Optional(R(u'^[Aa]|[Aa][Nn]?$')).hide()+Optional(R(u'^[Tt]he?$')).hide()+Optional(adj).hide()+(R(u'^[Ss]olvent?$')).hide()+cem|solvent_name|chemical_label|lenient_chemical_label)

solvent3=((Optional(R(u'^[Ii]n?$'))).hide()+Optional(R(u'^[Aa]|[Aa][Nn]?$')).hide()+Optional(R(u'^[Tt]he?$')).hide()+Optional(adj).hide()+(R(u'^[Ss]olvent?$')).hide()+cem|solvent_name|chemical_label|lenient_chemical_label)

solvent= (Not(R('^H2O$')) + ((R('^(DMF|DMA|DEF)$') + R('^/$') + R('^H2O$')) | solvent_name))(u'solvent').add_action(merge)

#Word used to describe electrochemical synthesis
electrochemical = (R('^[eE]lectrochemical(ly)?$'))('synthesis')

#Order: MOF name + chemical entity mention + synthesis route + solvent
sr1 = (SkipTo(MOF_name|MOF_formula) + cem + SkipTo(synthesis)+synthesis + SkipTo(solvent) + Optional(solvent))('sr')

#Order: synthesis route + solvent + MOF name + chemical entity mention
sr2 = (synthesis + SkipTo(solvent) + Optional(solvent) + SkipTo(MOF_name | MOF_formula) + cem)('sr')

#Order: MOF name + chemical entity mention + a specifier + electrochemical method
sr3 = (SkipTo(MOF_name | MOF_formula) + cem + Optional(prefix) + specifier + SkipTo(electrochemical) + electrochemical)('sr')

#Order: MOF name + chemical entity mention + synthesis method
sr4 = (SkipTo(MOF_name|MOF_formula) + cem + SkipTo(synthesis)+synthesis)('sr')

#Order: synthesis method + MOF name + chemical entity mention
sr5 = (synthesis + SkipTo(MOF_name | MOF_formula) + cem)('sr')

#Full parsing rule
sr = sr1 | sr2 | sr3 | sr4 | sr5

class SRParser(BaseParser):
    root = sr

    def interpret(self, result, start, end):
        compound = Compound(
            synthesis_routes=[
                SynthesisRoute(
                    synthesis=first(result.xpath('./synthesis/text()')),
                    descriptor=first(result.xpath('./descriptor/text()')),
                    solvent=first(result.xpath('./solvent/text()'))
                )
            ]
        )
        #Associates a synthesis route with a compound name if one is present
        cem_el = first(result.xpath('./cem'))
        if cem_el is not None:
            compound.names = cem_el.xpath('./name/text()')
            compound.labels = cem_el.xpath('./label/text()')
        yield compound
