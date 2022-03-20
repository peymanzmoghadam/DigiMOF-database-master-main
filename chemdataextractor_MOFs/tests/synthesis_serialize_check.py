from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph

score = 0
no_sentences = 0
#Examples below are from the top_PR_corpus_test1
#from 13.html
d = Document(Paragraph(
    '''A solvothermal reaction of H6-1 and Cu(NO3)2 in N,N-dimethylformamide (DMF) in the presence of a 
    small amount of HNO3 at 75 °C for 3 days afforded block blue crystals of NTU-105-NH2'''
))
print(d.records.serialize())
b=str(d.records.serialize())
a=str([{'names': ['Cu(NO3)2']}, {'names': ['N,N-dimethylformamide', 'DMF']}, {'names': ['HNO3']}, {'names': ['NTU-105-NH2'], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)

#from 12.html
d = Document(Paragraph(
    '''Three novel polymers, [Cd1.5(oba)(pcla)(CH3OH)](1), [Zn (oba)(4,4′-bpy)1.5]4(4,4′-bpy)2(H2O)5 (2) and [Cu2(oba)2(DMF)](DMF)(H2O)(3) 
    (H2oba = 4,4′-oxydibenzoic acid, Hpcla = picolinic acid) have been solvothermally synthesized and structurally characterized. '''
))

b=str(d.records.serialize())
a=str([{'names': ['[Cd1.5(oba)(pcla)(CH3OH)](1)']}, {'names': ['[ Zn (oba)(4,4′-bpy)1.5]4(4,4′-bpy)2(H2O)5'], 'labels': ['2']}, {'names': ['picolinic acid']}, {'names': ['[Cu2(oba)2(DMF)](DMF)(H2O)(3)'], 'synthesis_routes': [{'synthesis': 'solvothermally'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)

#from 11.html
d = Document(Paragraph(
    '''The syntheses of the MOFs [Zn4O(Me4BPDC)3] · 9 DMF (2 · 9 DMF) and [Cu2(Me4BPDC)2] · 9 DMF (3 · 9 DMF) were carried out through the classical 
    low temperature solvothermal synthesis in dimethylformamide, DMF,'''
))

b=str(d.records.serialize())
a=str([{'names': ['DMF']}, {'names': ['[Cu2(Me4BPDC)2] · 9 DMF']}, {'names': ['dimethylformamide']}, {'names': ['[Zn4O(Me4BPDC)3]'], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)

#from 9.html
d = Document(Paragraph(
    '''Addition of 5 and 1 equivalents (with respect to the linker) of l-proline and HCl (a known synthetic promoter13) during 
    solvothermal syntheses yielded single crystals of ≈50 μm diameter of both UiO-67 and UiO-abdc'''
))

b=str(d.records.serialize())
a=str([{'names': ['HCl']}, {'names': ['UiO-abdc']}, {'names': ['UiO-67'], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)


#from 8.html
d = Document(Paragraph(
    '''Solvothermal reactions of TCBPP-X (X = H2, Zn, Co, Fe), ZrOCl2·8H2O and benzoic acid in N,N-diethylformamide for 5 days at 120 °C yielded 
    single crystals of CPM-99 series.'''
))

b=str(d.records.serialize())
a=str([{'names': ['H2']}, {'names': ['Zn']}, {'names': ['Co']}, {'names': ['Fe']}, {'names': ['ZrOCl2·8H2O']}, {'names': ['benzoic acid']}, {'names': ['N,N-diethylformamide']}, {'names': ['CPM-99'], 'synthesis_routes': [{'synthesis': 'Solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)

#from 7.html
d = Document(Paragraph(
    '''Solvothermal reaction between TATB, ZrOCl2⋅8 H2O, N,N-diethylformamide (DEF),and TFA gave rise to the formation of the 
    product PCN-77 as a white powder (see the Supporting Information, section 3).'''
))

b=str(d.records.serialize())
a=str([{'names': ['TATB']}, {'names': ['ZrOCl2⋅8 H2O']}, {'names': ['N,N-diethylformamide (DEF),and TFA']}, {'names': ['PCN-77'], 'synthesis_routes': [{'synthesis': 'Solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)

#from 5.html
d = Document(Paragraph(
    '''Colorless, distorted-octahedron-shaped single crystals of PCN-523 [Hf6(μ3-OH)8(OH)8)]L2 were synthesized 
    from a similar solvothermal reaction of HfCl4 and H4L in DEF.'''
))

print(d.records.serialize())
b=str(d.records.serialize())
a=str([{'names': ['HfCl4']}, {'names': ['PCN-523'], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)


#from 4.html
d = Document(Paragraph('''White crystalline powder of PCN-128W was obtained under solvothermal conditions 
with trifluoroacetic acid (TFAA) as the competing reagent.'''))
print(d.records.serialize())

b=str(d.records.serialize())
a=str([{'names': ['trifluoroacetic acid', 'TFAA']}, {'names': ['PCN-128W'], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
print(a)
print(b)
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)




