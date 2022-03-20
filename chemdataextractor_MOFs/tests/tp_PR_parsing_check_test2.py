from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
score = 0
no_sentences = 0

#From 50.html
#None

#From 49.html
d = Document(Paragraph('''
A series of highly porous 4,8-connected isoreticular MOFs of the scu topology [Cu4(L1)(H2O)4]·20DEF, 
[Cu4(L2)(H2O)4]·16DMF·5H2O, and [Cu4(L3)(H2O)4]·14DMF (L1–L3 are (R)-1,1′-binaphthyl-derived octacarboxylate bridging ligands) were synthesized and characterized by single-crystal X-ray crystallography. 
'''))

b=str(d.records.serialize())
a=str([{'names': ['[Cu4(L2)(H2O)4]·16DMF·5H2O']}, {'names': ['[Cu4(L3)(H2O)4]·14DMF']}, {'names': ['(R)-1,1′-binaphthyl-derived octacarboxylate']}, {'names': ['[Cu4(L1)(H2O)4]·20DEF'], 'topologies': [{'abrv': 'scu'}]}])
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

#From 47.html
#None

#From 48.html
#None

#From 45.html
#None

#From 44.html
#None

#from 43.html
#None


#from 42.html
d = Document(Paragraph(
    '''Topologically, MMPF-9 possesses a rare (4,12)-connected dinodal net (Fig. S5, ESI†) with a new topology of smy'''
))
print(d.records.serialize())

b=str(d.records.serialize())
a=str([{'names': ['MMPF-9'], 'topologies': [{'abrv': 'smy'}]}])
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

#from 41.html
d = Document(Paragraph(
    '''design and synthesis of two copper-based MOFs with nbo (Cu2(DBIP)(H2O)2, 1) and agw (Cu3(CPEIP)2(H2O)3, 2) topologies using the tetracarboxylate 
    ligand H4DBIP and the tricarboxylate ligand 5-[(4-carboxyphenyl)ethynyl]isophthalic acid (H3CPEIP)'''
))

b=str(d.records.serialize())
a=str([{'names': ['copper']}, {'names': ['tetracarboxylate']}, {'names': ['tricarboxylate']}, {'names': ['5-[(4-carboxyphenyl)ethynyl]isophthalic acid']}, {'linker_routes': [{'linker': "['5-[(4-carboxyphenyl)ethynyl]isophthalic acid']"}]}, {'names': ['Cu2(DBIP)(H2O)2'], 'topologies': [{'abrv': 'nbo'}]}, {'names': ['Cu3(CPEIP)2(H2O)3'], 'topologies': [{'abrv': 'agw'}]}])
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

#from 40.html
d = Document(Paragraph(
    '''
    Three isostructural interwoven 3,4-connected mesoporous metal–organic frameworks of pto-a topology (UTSA-28-Cu, UTSA-28-Zn, and UTSA-28-Mn)
    '''
))

b=str(d.records.serialize())
a=str([{'names': ['UTSA-28-Zn']}, {'names': ['UTSA-28-Mn']}, {'names': ['UTSA-28-Cu'], 'topologies': [{'abrv': 'pto-a'}]}])
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