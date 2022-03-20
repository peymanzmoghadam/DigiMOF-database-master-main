from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from . import R, I, Optional, merge, OneOrMore, Not, ZeroOrMore, SkipTo

from ..utils import first
from .cem import cem, chemical_label, solvent_name, MOF_name, MOF_formula, linker_name
from .common import comma, delim


from ..model import Compound, LinkerRoute



from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first

#common words before phrase
conj = (R(u'^[Tt]hrough?$')|R(u'^[Ww]ith?$')|R(u'^[Bb]y?$')|R(u'^[Ff]rom?$')|R(u'^[Vv]ia?$')|R(u'^[Uu]s(ing|es|ed)?$')|R(u'^[Ii]ntroduc(ing|es|ed)?$')|R(u'^[Ee]mploy(ing|s|ed)?$')|R(u'^[Uu]tili[sz](ing|es|ed)?$')|R(u'^[Ee]nlist(ing|s|ed)?$')|R(u'^[Aa]nd?$')).hide() #having and in here may not be restrictive enough

#describes the reaction
adj=(R(u'^[Rr]apid(ly)?$')|R(u'^[eE]fficient(ly)?$')|R(u'^[Nn]ovel?$')|R(u'^[Uu]ltrasonic(ally)?$')).hide()

#Common words before the linker
prefix1 = (Optional(R(u'^[Oo]rganic?$'))+Optional(R(u'^[Bb]ridging?$'))+R(u'^[Ll]ink((er|ers|s|ed|ing))?$')| R(u'^[Ll]igand(s)?$')| R(u'^[Ss]trut(s)?$')+ Optional(R(u'^[Pp]recursor(s)?$'))).hide()
prefix2=(R(u'^[Oo]rganic?$')+R(u'^[Pp]recursor(s)?$')).hide()
linker_prefix=prefix1|prefix2

#common abbreviations for different linkers
commonlinkerabbrv =(Optional(Optional(I(u'h'))+Optional(I(u'3')))+Optional(OneOrMore(R(u'^[0-9]?$')+delim)+Optional(R('^[\-‐‑⁃‒–—―−－⁻]$')))+Optional(R(u'^h$'))+Optional(R(u'^[0-9]?$'))+R('H(2|3)[BDCTANHFPVIMEP]+')|R(u'^[Hh][0-9]{0,5}(\-)[a-zA-Z0-9]{0,5}$')|I(u'Bpe')|I(u'TCPB4')|I(u'bib')|I(u'bipy')|I(u'IPA')|I(u'bdc')|I(u'bpe')|I(u'dicarboxylate')|I(u'tpa')|I(u'ndc')|I(u'5-hipa')|I(u'hipa')|I(u'H2FDCA')|I(u'dobdc-d2')|I(u'dobdc')|I(u'en')| R(u'^[H]*[0-9]*FDCA?$')|I(u'H2BDP')|I(u'TCPS')|I(u'H4TCPS')|I(u'DOTA')|I(u'H6TBPP')|I(u'TPT')|I(u'TazbH4')|I(u'H4DOBDC')|I(u'tcpp')|I(u'BDC')|I(u'bdt')|I(u'H4TCPE')|I(u'H2BDC')|I(u'H3Btc')|I('H3BTN')|I(u'H3btt')|I(u'H2pvia')|I(u'H2Bpdp')|I(u'H2dhbdc')|I(u'Hpymo')|I(u'H4mdip')|I(u'H3Btb')|I(u'H2BDC')|I(u'H2Bbc')|I(u'H2Bte')|I(u'tpa')|I(u'tpa-nh2')|R('^TCBPP'))

#for linkers with an H included in the abbreviation
H_prefix_linkabbrv=((R(u'^[H0-9\,\-′]{0,5}?$'))+commonlinkerabbrv)

#Beginning of a metal precursor
node_ion=R(u'^((Zn|Mn|Cu|Fe|Al|Cd|Zr|Co|Mg|Ti|Pb|Ni|Na|Sc|Cr|Nb|Mo|Hf|Rb)|[Mm]olybdenum|[Nn]iobium|[Hh]afnium|[Yy]ttrium|[Cc]hromium|[Ss]candium|[Ss]odium|[Nn]ickel|[Ll]ead|[Tt]itanium|[Zz]inc|[Mm]anganese|[Vv]anadium|[Mm]agnesium|[Cc]opper|[Ii]ron|[Ff]errous|[Aa]lumin(ium|um|o)|[Cc]admium|[Zz]irconium|[Cc]obalt)(\W|[0-9\+\-A-Z\.ivl\(\)\·\[\\]\\(\\)\\{\\}]+)?$')(u'metal_precursor').add_action(merge)

#Metal precursor blacklist
metal_precursor_blacklist = Not(I('Y.'))

#common words preceding a precurso
metal_precursor1=(ZeroOrMore(R(u'^[Mm]etal(lic)?$').hide()|R(u'^[Ss]alt?$').hide()|R(u'^[Ii]on?$').hide()|R(u'^[Ii]norganic?$').hide()|R(u'^[Pp]recursor(s)?$').hide()|R(u'^[Rr]eagent(s)?$').hide()|R(u'^[Cc]omponent(s)?$').hide()|R(u'^[Cc]onstituent?$').hide()|R(u'^[Ss]olution?$').hide()|R(u'^[Mm]ixture?$').hide()|R(u'^[Ll]iquid?$').hide()|R(u'^[Aa]queous?$').hide()|R(u'^[aA]s?$').hide()|R(u'^[Ff]or?$').hide()|R(u'^[Tt]he?$').hide()|R(u'^[Aa]?$').hide()|R(u'^[Aa]n?$').hide()|conj.hide()|R(u'^[Wwh]ere?$').hide()|R(u'^[Ww]as?$').hide()|R(u'^[Aa]re?$').hide()|R(u'^[Ii]s?$').hide()|adj.hide())+node_ion+Optional(R(u'^[[Ii]so|[Pp]rop|[Oo]xide|oate|[Ss]ul(f|ph)|[Nn]itr|ate|ite|[Pp]er|[Oo]cta|[Tt]etra|ide|[Ii]od|[cC](h)lor|[Mm]angan|[Tt]ri|[Hh]ydrogen|[Cc]arbon|[Hh]ydr|[hH]ypo|[Dd]i|[Pp]hosp|[Ff]luor|[Ff]err|[Cc]arbamate|\W]+?$'))+Optional(R(u'^(\W|[DdTtr]i|[Oo]cta|[Tt]etra|[mM]ono)*[hH][iy]drate?$')))(u'metal_precursor').add_action(merge)

#metal_precursor parse rule
metal_precursor=(OneOrMore(Not(MOF_name|MOF_formula)+ metal_precursor_blacklist + metal_precursor1))(u'metal_precursor').add_action(merge)

#captures quantities of linker and metal
amount = R(u'^[0-9\.]+?$')(u'amount').add_action(merge)

#Captures the units of the linker and metal quantities
units=R(u'^kg|mg|ml|g|cm3|mmol|%?$')(u'units').add_action(merge)

#combined units and amount
quant=(Optional(delim) +amount+units+Optional(delim+amount+units)).add_action(merge)

#quantifier with optional brackets
quantifier1= (ZeroOrMore(R('^[\[\]\(\)\{\}/]$')).hide()+quant+ZeroOrMore(R('^[\[\]\(\)\{\}/]+$')).hide())

#labels the linker amount and units
linker_quantifier=(quantifier1|quant)(u'linker_quantifier')

#labels the metal precursor amount and units
metal_quantifier=(quantifier1)(u'metal_quantifier')

#recognizes solvent names
solvent=(R(u'^[Ii]n?$').hide()+Optional(R(u'^[Aa]|[Tt]he?$').hide())+Optional(R(u'^[Ss]olvent?$').hide())+Optional(R(u'^[Mm]ixture?$').hide())+Optional(R(u'^[Oo]f?$').hide())+solvent_name+Optional(R(u'^[Aa]nd|&?$').hide())+solvent_name)(u'solvent')

#recgonizes names of the linker
linker1 = Not(metal_precursor)+Not(solvent)+Not(quant)+Not(R(u'^[Ww]ater?$')) + linker_name + Not(metal_precursor)

#words that commonly precede the linker name
linker_prefixes= Optional(R('^[wW]ere$'))+ R(u'^[Oo]norganic$').hide()|R(u'^[Pp]recursor(s)?$').hide()|prefix1|R(u'^[Rr]eagent(s)?$').hide()|R(u'^[Cc]omponent(s)?$').hide()|R(u'^[Cc]onstituent$').hide()|R(u'^[Ss]olution$').hide()|R(u'^[Mm]ixture$').hide()|R(u'^[Ll]iquid$').hide()|R(u'^[Aa]queous$').hide()|R(u'^[Rr]eaction$').hide() + Optional(R(u'^[aA]s?$').hide()|R(u'^[Ff]or?$').hide()|R(u'^[Tt]he?$').hide()|R(u'^[Aa]?$').hide()|R(u'^[Aa]n?$').hide()|conj.hide()|R(u'^[Wwh]ere?$').hide()|R(u'^[Ww]as?$').hide()|R(u'^[Aa]re?$').hide()|R(u'^[Ii]s?$').hide()|adj.hide()|R(u'^[Oo]f?$').hide())

#linker name parse rule
linker=(Optional(R(u'^[Aa]n?$').hide()+R(u'^[Dd]eprotonated?$').hide()+R(u'^[Ff]orm?$').hide()+R(u'^[Oo]f?$').hide())+Not(solvent).hide()+Not(R(u'^[Ii]n?$').hide())+Not(R(u'^[Ii]n?$').hide()+Optional(R(u'^[Aa]|[Tt]he?$').hide())+Optional(R(u'^[Ss]olvent(s)?$').hide())+Optional(R(u'^[Mm]ixture|[Ss]olution?$').hide())+Optional(R(u'^[Oo]f?$').hide())+ZeroOrMore(R(u'^\,?$').hide()+cem)+R(u'^[Aa]nd|&?$').hide())+(Not(metal_precursor) +Not(quant) + (Not(R(u'^[Ww]ater?$'))+linker1|commonlinkerabbrv|H_prefix_linkabbrv)+Optional(chemical_label).hide()+Not(R(u'^[Ss]olvent(s)?$'))))(u'linker').add_action(merge)

#Order: metal_precursor + linker + MOF
precursor_linker_MOF =(SkipTo(cem|linker)+metal_precursor +Optional(metal_quantifier)+Not(R(u'^(MOF)|(node)|centre|center|SBU?$')).hide()+ Optional(linker_quantifier)+ SkipTo(linker)+linker + Optional(linker_quantifier) + Optional(delim) + SkipTo(MOF_name | MOF_formula) + cem)(u'lp')

#Order: linker + metal_precursor + MOF
linker_precursor_MOF = (SkipTo(linker) + linker +Optional(linker_quantifier) + Not(R(u'^(MOF)|(node)|centre|center|SBU?$')).hide() + SkipTo(cem)+metal_precursor + Optional(delim) + SkipTo(MOF_name | MOF_formula) + cem)('lp')

#Order: MOF + metal_precursor + linker
MOF_precursor_linker =(SkipTo(MOF_name | MOF_formula) + cem + SkipTo(linker|cem) +metal_precursor +Optional(metal_quantifier)+Not(R(u'^(MOF)|(node)|centre|center|SBU?$')).hide()+ SkipTo(linker)+linker + Optional(linker_quantifier) + Optional(delim))(u'lp')

#Order: MOF + linker + metal_precursor
MOF_linker_precursor = (SkipTo(MOF_name | MOF_formula) + cem + SkipTo(linker)+ linker +Optional(linker_quantifier)+Not(R(u'^(MOF)|(node)|centre|center|SBU?$')).hide()+ Optional(metal_quantifier) + SkipTo(metal_precursor)+metal_precursor + Optional(metal_quantifier) + Optional(delim))('lp')

#Order: MOF + linker
MOF_linker = (SkipTo(MOF_name | MOF_formula) + cem +SkipTo(linker) + linker)(u'lp')

#Order: linker + MOF
linker_MOF = (SkipTo(linker) + linker + Optional(linker_quantifier) + SkipTo(MOF_name | MOF_formula) + cem)(u'lp')

#Order: metal_precursor + MOF
precursor_MOF = (SkipTo(cem) + metal_precursor + Optional(metal_quantifier) + SkipTo(MOF_name | MOF_formula) + cem)(u'lp')

#Order: MOF + metal_precursor
MOF_precursor = (SkipTo(MOF_name | MOF_formula) + cem + SkipTo(metal_precursor) + metal_precursor + Optional(metal_quantifier))(u'lp')

#Recognition with heading
MOF_linker_heading = (Not(I('zinc')) +
                Optional(MOF_name | MOF_formula) + Optional(comma) +Optional(I('has')) + Optional(delim)
                  + OneOrMore(linker + linker_quantifier))('lp')

#Accounts for when there is a MOF name before or after the mention of a linker and metal precursor
lp3 = (Optional(SkipTo(MOF_name | MOF_formula) + cem) + ZeroOrMore(linker_prefixes.hide() + linker_quantifier) + linker + ZeroOrMore(
    linker_prefixes.hide() + linker_quantifier) + R(u'^[Aa]nd|&?$').hide() + Optional(
    metal_quantifier) + metal_precursor + Optional(metal_quantifier) + Optional(
    R(u'^[Ww]ere|[Ww]as|[Aa]re?$').hide()) + Optional(adj) + R(u'^[Dd]issolve(d)|[Mm]ixed|[Rr]eact(ed)?$').hide() +Optional(SkipTo(MOF_name | MOF_formula) + cem))(
    u'lp')

#Accounts for when there is a MOF name followed by a linker and metal precursor
lp7=(SkipTo((MOF_name | MOF_formula)) + cem +R(u'^[Ww]ere|[Ww]as|[Aa]re|[Ii]s?$').hide()+R(u'^[Mm]ade|[Ss]ynthesi[sz]ed|[Pp]repared|Crystalli(sz)ed|[Nn]ucleated|[Ss]ynthesi(sz)ed|[Pp]roduced?$').hide()+conj.hide()+Optional(R(u'^[Aa]|[Tt]he?$')).hide()+R(u'^[Rr]eacti(ing|on)|[Mm]ix(ture|ing)|[Dd]issol(ution|ving)|[Rr]eflux(ing)?$').hide()+Optional(R(u'^[Mm]ethod?$')).hide()+Optional(R(u'^[Oo]f?$')).hide()+ZeroOrMore(linker_prefixes.hide()+linker_quantifier)+linker+ZeroOrMore(linker_prefixes.hide()+linker_quantifier)+R(u'^[Aa]nd|&|[Ww]ith?$').hide()+Optional(metal_quantifier)+metal_precursor+Not(R(u'^(MOF)|(node)|centre|center|SBU?$')).hide()+Optional(metal_quantifier))(u'lp')

#Accounts for when there is a MOF name followed by a linker with optional metal precursor
lp15 = (SkipTo((MOF_name | MOF_formula)) + cem + SkipTo(linker) + linker + linker_prefix + ZeroOrMore(
    linker_prefixes + linker_quantifier) + Optional(
    SkipTo(metal_precursor) + metal_precursor + ZeroOrMore(metal_quantifier)))(u'lp')

#Recognizes when there is a MOF name in the heading followed by a linker with an optional metal precursor
MOF_linker_heading2 = (Optional(MOF_name | MOF_formula) + Optional(chemical_label) + ZeroOrMore(
    linker_prefixes.hide() + linker_quantifier) + OneOrMore(
    linker + ZeroOrMore(linker_prefixes.hide() + linker_quantifier) + Optional(delim)) + Optional(
    metal_quantifier) + metal_precursor + Optional(metal_quantifier) + Not(
    R(u'^(MOF)|(node)|centre|center|SBU?$')).hide())(u'lp')

#Conplete linker parsing phrase
lp=(linker_precursor_MOF | precursor_linker_MOF | MOF_precursor_linker | MOF_linker_precursor | MOF_linker | linker_MOF | precursor_MOF | MOF_precursor | MOF_linker_heading2 | MOF_linker_heading | lp3 | lp7|lp15)(u'lp')


class LinkerParser(BaseParser):
    root = lp

    def interpret(self, result, start, end):
        compound = Compound(
            linker_routes=[
                LinkerRoute(
                    linker=(result.xpath('./linker/text()')),
                    metal_precursor=first(result.xpath('./metal_precursor/text()'))
                )
            ]
        )
        cem_el = first(result.xpath('./cem'))
        #Associates the metal precursor or linker with a chemical entity mention
        if cem_el is not None:
            compound.names = cem_el.xpath('./name/text()')
            compound.labels = cem_el.xpath('./label/text()')
        yield compound