from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption
#test1
from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
#this test file should be used after a refinement is made to a parser, new sentences can be added and the score should be checked to make sure old sentences can still be passes
#a test fail does not necessarily mean the sentence isn't being parsed correctly if a refinement has been made, the record should be checked and if the parser is performing better
#the new record string should be copied in and the test can be taken to be passed
#f = open('C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\ZrO_MOF_Test1_Corpus\\33.html', 'rb')
#doc = Document.from_file(f)
#print(doc.records.serialize())
score=0
no_sentences=0
#test2
e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(u' MIL-25 was made from a reaction of trimesic acid with precursor the precursor employed utilising salt as the metal mixture reagent component constituent inorganic precursor is ZrOCl2·8H2O, 5-HIPA, DMF and formic acid by solvothermal method [1]. ' ))
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['trimesic acid']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['5-HIPA']}, {'names': ['DMF']}, {'names': ['formic acid']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['trimesic acid']", 'metal_precursor': 'ZrOCl2·8H2O', 'MOF': 'MIL-25'}]}, {'names': ['MIL-25'], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
print(a)
print(b)

if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)
e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(u'strut precursor used was reagent bib (0.20 g), 0.5 g (3.96 mmol) of melamine, ligand fumaric acid , 25 mL of DMSO, and 5 mL of distilled water')
)
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['melamine']}, {'names': ['fumaric acid']}, {'names': ['DMSO']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['fumaric acid']"}, {'linker': "['bib']", 'linker_quantifier': '0.20g'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)
e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(u' MIL-25 was made from a reaction of trimesic acid with ZrOCl2·8H2O, 5-HIPA, DMF and formic acid by solvothermal method [1]. ' ))
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['MIL-25']}, {'names': ['trimesic acid']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['5-HIPA']}, {'names': ['DMF']}, {'names': ['formic acid']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['trimesic acid']", 'metal_precursor': 'ZrOCl2·8H2O', 'MOF': 'MIL-25'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)
e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u'UiO-66 was synthesized by reflux method of H2BDC with ZrOCl2·8H2O, DMF, BA and HCl [2].')
)
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['UiO-66']}, {'names': ['H2BDC']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['DMF']}, {'names': ['HCl']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['H2BDC']", 'metal_precursor': 'ZrOCl2·8H2O', 'MOF': 'UiO-66'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)

e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u'''.3 Synthetic Procedures
Gravimetric concentration determination for zirconium acetate solution in dilute acetic
acid: Since the concentration of the used zirconium acetate solution in dilute acetic acid from
Sigma Aldrich can vary between 15 and 17 wt% zirconium, the exact concentration was
gravimetrically determined. For this purpose, three porcelain crucibles were heated at 1000 °C
for 10 hours. After cooling down, each crucible was first weighted and then filled with 1 mL of
zirconium acetate solution in dilute acetic acid. The filled crucibles were heated to 80 °C within
1 hour and the temperature was kept for another 5 hours to slowly evaporate the liquid
components. In order to oxidize the remaining solid completely into ZrO2, the temperature was
increased to 1000 °C within 9 hours and subsequently kept for 10 hours. After cooling down,
each crucible was weighted again and the amount of ZrO2 per crucible was determined via
subtraction of the earlier determined empty weights. The resulting amounts of ZrO2 were 293.3,
280.1 and 294.6 mg. The second value was discarded due to its significant deviation and the
arithmetic mean (294.0 mg) was calculated using the remaining two values. 294.0 mg of ZrO2
correspond to 2.385 mmol Zr. Therefore, the zirconium concentration of the used zirconium
acetate solution in dilute acetic acid is 2.385 mol/L or 17.0 wt% considering a density of
1.279 g/mL.
High throughput linker screening: Multiple linker molecules were reacted with zirconium
acetate solution in dilute acetic acid at 160 °C under solvothermal conditions over 24 h (1 h
heat up, 22 h hold, 1 h cooldown), using glacial acetic acid as the solvent. The reactions were
carried out in a sealed high throughput autoclave with 24 Teflon-lined reaction chambers (Vmax
= 2.5 mL). Synthetic details are summarized in Table''')
)
print(e.serialize())
print(e.records.serialize())

e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u'Briefly, TPA-NH2 and metal ion ZrOCl2·8H2O were dissolved in a solvent mixture of water and acetone.')
)
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['TPA-NH2']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['acetone']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['TPA-NH2']", 'metal_precursor': 'ZrOCl2·8H2O'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)

e = Document(    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u'  MIL-434-A was made from a reaction of trimesic acid with metal ion Cr(NO3)3·9H2O and water by hydrothermal method as previously reported [6].')
)
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['MIL-434-A']}, {'names': ['trimesic acid']}, {'names': ['Cr(NO3)3·9H2O']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['trimesic acid']", 'metal_precursor': 'Cr(NO3)3·9H2O', 'MOF': 'MIL-434-A'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)

e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u'   1,3,5-BTC and Fe(NO3)3·9H2O were mixed to water in the 100 mL Teflon-lined autoclave. [6].')
)
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['1,3,5-BTC']}, {'names': ['Fe(NO3)3·9H2O']}, {'names': ['Teflon']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['1,3,5-BTC']", 'metal_precursor': 'Fe(NO3)3·9H2O'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)

e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u'    ZrOCl2·8H2O and bib are dissolved. Zr linked by en dissolved in a solvent mixture of water and acetone. [6].')
)
print(e.serialize())
print(e.records.serialize())
b=str(e.records.serialize())
a=str([{'names': ['ZrOCl2·8H2O']}, {'names': ['Zr']}, {'names': ['acetone']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['en']", 'metal_precursor': 'Zr'}, {'linker': "['bib']", 'metal_precursor': 'ZrOCl2·8H2O'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score=score+1
else:
    print('test failed')
    score=score
print('score=', score)
no_sentences=no_sentences+1
print('number of sentences=', no_sentences)

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'Preparation of MOF-5/COF (M5C).'),
    Paragraph(
        u' In a typical synthesis process, copper nitrate trihydrate (98%) and benzene-1,3,5-tricarboxylic acid (95%) were mixed and heated to 50 °C for 3 h.')
)
print(e.serialize())
print(e.records.serialize())
#this parses  In a typical synthesis process, copper nitrate and benzene-1,3,5-tricarboxylic acid were mixed and heated to 50 °C for 3 h.'
#doi=10.1016/j.pnsc.2018.08.002
b = str(e.records.serialize())
a = str([{'names': ['copper nitrate trihydrate']}, {'names': ['benzene-1,3,5-tricarboxylic acid']}, {'names': ['MOF-5 / COF', 'M5C'], 'roles': ['product'], 'linker_routes': [{'linker': "['benzene-1,3,5-tricarboxylic acid']", 'metal_precursor': 'coppernitratetrihydrate', 'linker_quantifier': '95%', 'metal_quantifier': '98%'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)


#below sentence doesn' take a MOF name?
e = Document(
    Heading(u'Single Crystals of Zr6O4(OH)4(fumarate)6, MOF-801-SC'),
    Paragraph(
        u' Fumaric acid (0.081 g, 0.70 mmol) and ZrOCl2·8H2O (0.23 g, 0.70 mmol) were dissolved in a solvent mixture of DMF/formic acid (35 mL/5.3 mL) in a 60-mL screw-capped glass jar ')
)
print(e.serialize())
print(e.records.serialize())
#doi=10.1021/ja500330a
b = str(e.records.serialize())
a = str([{'names': ['Zr6O4(OH)4(fumarate)6']}, {'names': ['Fumaric acid']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['DMF']}, {'names': ['formic acid']}, {'names': ['MOF-801-SC'], 'linker_routes': [{'linker': "['Fumaric acid']", 'metal_precursor': 'ZrOCl2·8H2O', 'linker_quantifier': '0.081g0.70mmol', 'metal_quantifier': '0.23g0.70mmol'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)

e = Document(
    Heading(u'Single Crystals of Zr6O4(OH)4(fumarate)6, MOF-801-SC'),
    Paragraph(
        u'Self-assembly of a new metalloporphyrin tetracarboxylic ligand Ir(TCPP)Cl reacted with ZrCl4 in MOF-(Zr)SC1-100 the presence of benzoic acid leads to the formation of a three-dimensional (3D) iridium(III)-porphyrin metal–organic framework (UiO-1(Zr)) with the formula of [(Zr6(μ3-O)8(OH)2(H2O)10)2(Ir(TCPP)Cl)3]·solvents (UiO-1(Zr)), which possesses square-shaped channels of 1.9 × 1.9 nm2 (atom-to-atom distances across opposite Ir metal atoms) in three orthogonal directions as disclosed by the single-crystal X-ray diffraction analysis.')
)
print(e.serialize())
print(e.records.serialize())
#doi=10.1039/c6ce00358c
b = str(e.records.serialize())
a = str([{'names': ['Zr6O4(OH)4(fumarate)6']}, {'names': ['Ir(TCPP)Cl']}, {'names': ['ZrCl4']}, {'names': ['zirconium-MOF-1(Zr)']}, {'names': ['benzoic acid']}, {'names': ['iridium(III)']}, {'names': ['porphyrin']}, {'names': ['[(Zr6(μ3-O)8(OH)2(H2O)10)2(Ir(TCPP)Cl)3]·solvents']}, {'names': ['Ir']}, {'names': ['MOF-801-SC'], 'linker_routes': [{'linker': "['Ir(TCPP)Cl']", 'metal_precursor': 'ZrCl4', 'MOF': 'zirconium-MOF-1(Zr)'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'Syntheses and structures of porphyrin Zr and Hf MOFs'),
    Paragraph(
        u'Reaction of H6TBPP with ZrCl4 or HfCl4 modulated by benzoic acid gives rise to dark red crystals of FJI-H6 or FJI-H7.')
)
print(e.serialize())
print(e.records.serialize())
#it can only get one record out of sentences like this
# doi=10.1039/c5sc00213c
b = str(e.records.serialize())
a = str(
    [{'names': ['porphyrin']}, {'names': ['Zr']}, {'names': ['H6TBPP']}, {'names': ['ZrCl4']}, {'names': ['HfCl4']}, {'names': ['benzoic acid']}, {'names': ['FJI-H6']}, {'names': ['FJI-H7']}, {'names': ['Hf'], 'linker_routes': [{'linker': "['H6TBPP']", 'metal_precursor': 'ZrCl4', 'MOF': 'FJI-H6'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)



from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'Synthesis of Zr6O4(OH)4(TCPS)2(OH)4(H2O)4'),
    Paragraph(
        u'TCPS (6.40 mg, 0.0125 mmol), and ZrOCl2·8H2O (16.10 mg, 0.0500 mmol) were dissolved in a solvent mixture of DMF (2 mL) and formic (1.2 mL) acid.')
)
print(e.serialize())
print(e.records.serialize())
# doi=10.1039/C5DT00421G
b = str(e.records.serialize())
a = str([{'names': ['Zr6O4(OH)4(TCPS)2(OH)4(H2O)4'], 'roles': ['product']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['DMF'], 'labels': ['2'], 'linker_routes': [{'linker': "['TCPS']", 'metal_precursor': 'ZrOCl2·8H2O', 'linker_quantifier': '6.40mg0.0125mmol', 'metal_quantifier': '16.10mg0.0500mmol'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)




from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading

e = Document(
Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
Paragraph(
            u'   H2FDCA (80 mg, 0.8 mmol), titanium (71 mg, 0.3 mmol), and 3 mL of acetic acid (HOAc) in 17 mL of DMF was sealed in a 20 mL glass vial and heated at 120 °C for 10 h.')
 )
print(e.serialize())
print(e.records.serialize())
# doi=10.1021/ic5013473
b = str(e.records.serialize())
a = str([{'names': ['[Zr6O4(OH)4(FDCA)6]n·S']}, {'names': ['H2FDCA'], 'labels': ['80']}, {'names': ['acetic acid']}, {'names': ['HOAc']}, {'names': ['DMF']}, {'names': ['titanium'], 'labels': ['71'], 'linker_routes': [{'linker': "['H2FDCA']", 'metal_precursor': 'titanium', 'linker_quantifier': '80mg0.8mmol', 'metal_quantifier': '71mg0.3mmol'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)



e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'MOF-2 was synthesized from of the as-prepared dobdc-d2 ligand for use in INS studies')
)
print(e.serialize())
print(e.records.serialize())
# doi=10.1039/C4SC02064B
b = str(e.records.serialize())
a = str([{'names': ['MOF-2']}, {'names': ['[Zr6O4(OH)4(FDCA)6]n·S'], 'linker_routes': [{'linker': "['dobdc-d2']", 'MOF': 'MOF-2'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)

#116 performance corpus
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'A tri-s-triazine derivative, s-heptazine tribenzoate, is introduced as a ligand for chiral metal−organic framework (MOF) synthesis.')
)
print(e.serialize())
print(e.records.serialize())
# doi=10.1039/C4SC02064B
b = str(e.records.serialize())
a = str([{'names': ['MOF-2']},
         {'names': ['[Zr6O4(OH)4(FDCA)6]n·S'], 'linker_routes': [{'linker': "['dobdc-d2']", 'MOF': 'MOF-2'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)



# 116 performance corpus
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'This synthesis is achieved by borrowing ideas from metal carboxylate cluster chem., where an dicarboxylate linker was used in a reaction that gives supertetrahedron clusters when capped with monocarboxylates.')
)
print(e.serialize())
print(e.records.serialize())
# doi=10.1039/C4SC02064B
b = str(e.records.serialize())
a = str([{'names': ['MOF-2']},
         {'names': ['[Zr6O4(OH)4(FDCA)6]n·S'], 'linker_routes': [{'linker': "['dobdc-d2']", 'MOF': 'MOF-2'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)

# 135 performance corpus
#switch linker a metal prec order
#add between into reaction options
from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
#parsedby lp17
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'The ionothermal reactions between Zn(NO3)2 and H3BTC in a series of IL media resulted in six 3-D zinc MOFs first synthesized in IL systems.')
)
print(e.serialize())
print(e.records.serialize())
# doi=10.1039/C4SC02064B
b = str(e.records.serialize())
a = str([{'names': ['MOF-2']},
         {'names': ['[Zr6O4(OH)4(FDCA)6]n·S'], 'linker_routes': [{'linker': "['dobdc-d2']", 'MOF': 'MOF-2'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score = score + 1
else:
    print('test failed')
    score = score
print('score=', score)
no_sentences = no_sentences + 1
print('number of sentences=', no_sentences)

e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'Series of 2D and 3D Coordination Polymers Based on 1,2,3,4-Benzenetetracarboxylate and N-Donor Ligands: Synthesis, Topological Structures, and Photoluminescent Properties')
)
print(e.serialize())
print(e.records.serialize())
from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'Four porous MOFs were built from new biphenol-derived tetracarboxylate ligands containing dihydroxy and crown ether functionalities, and their topologies, thermal stability, and gas uptake properties were studied.')
)
#performancecorpus 109
print(e.serialize())
print(e.records.serialize())
#performamcecorpus109

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'A molecular, porous crystalline material constructed from neutral helical coordination polymers incorporating manganese(II) ions and two types of bridging ligands, namely the deprotonated form of 2-hydroxy-5-methoxy-3-nitrobenzaldehyde (HL) and isobutyrate (iB–), has been obtained and structurally characterized. ')
)
#performancecorpus 11
print(e.serialize())
print(e.records.serialize())

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'because both organic linkers of h2bde and 4,4′-Bpe in MOF 1 are longer than those of BDC and 4,4′-Bipy in MOF Zn(BDC)(4,4′-Bipy)0.5, the pores in MOF 1 are much larger than the 1D pores of 4.0 × 4.0 Å in Zn(BDC)(4,4′-Bipy)')
)
#performancecorpus 11
print(e.serialize())
print(e.records.serialize())

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
e = Document(
    Heading(u'[Zr6O4(OH)4(FDCA)6]n·S (BUT-10; S = Nonassignable Solvent Molecules)'),
    Paragraph(
        u'MOF 1 was synthesized by the solvothermal reaction of H2NDC, 4,4′-Bpe, and Zn(NO3)2‚6H2O in DMF at 100 °C for 24 h as colorless block-shaped crystals')
)
#performancecorpus 11
print(e.serialize())
e = Document(
Heading(u'Single Crystals of Zr6O4(OH)4(fumarate)6, MOF-801-SC'),
Paragraph(
        u'Self-assembly of a new metalloporphyrin tetracarboxylic ligand Ir(TCPP)Cl (TCPP = tetrakis(4-carboxyphenyl)porphyrin) with ZrCl4 in the presence of benzoic acid leads'
        u' to the formation of a three-dimensional (3D) iridium(III)-porphyrin metal–organic framework (Ir-PMOF) with the formula of [(Zr6(μ3-O)8(OH)2(H2O)10)2(Ir(TCPP)Cl)3]·'
        u'solvents (Ir-PMOF-1(Zr)), which possesses square-shaped channels of 1.9 × 1.9 nm2 (atom-to-atom distances across opposite Ir metal atoms) in three orthogonal directions '
        u'as disclosed by the single-crystal X-ray diffraction analysis.')
)
print(e.records.serialize())



