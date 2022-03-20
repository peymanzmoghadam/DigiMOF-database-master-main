from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
score = 0
no_sentences = 0

#From 51.html
#None

#From 52.html
d = Document(Paragraph('''
MOF-5 was solvothermally synthesized by the reaction of Cu(NO)2·2.5H2O with H4ADDI.‡ Its crystal structure was 
determined by single-crystal X-ray diffraction. The phase purity of the product was confirmed by powder X-ray diffraction (PXRD), where the experimental pattern matches well with the simulated one (Fig. S3, ESI†). Thermogravimetric analysis (TGA) of the as-synthesized 1·nS indicated a weight loss of 50% before about 250 °C, above which the compound starts to decompose (Fig. S5, ESI†).
'''))

b=str(d.records.serialize())
a=str([{'names': ['Cu(NO)2·2.5H2O'], 'synthesis_routes': [{'synthesis': 'solvothermally'}]}])
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

#From 53.html
#None

#From 54.html
#None

#From 55.html


#from 56.html
d = Document(Paragraph('''
NU-108-Cu contains paddlewheel-coordinated copper ions as nodes and is based on a 3,24 network associated with 
an inherently noncatenating rht-topology. Modifications introduced in the hexa-carboxylated struts (uniquely 
placed phenyl spacers) lead to substantial changes in pore sizes, relative to those found in other MOFs based 
on 3,24 networks and paddlewheel-coordinated copper ions. NU-108-Zn features a new net based on (3,3,6)-connecter 
and octadehral Zn4O nodes in which all struts lie in a–b planes.
'''))
print(d.records.serialize())

b=str(d.records.serialize())
a=str([{'names': ['phenyl']}, {'names': ['NU-108-Zn']}, {'names': ['Zn4O']}, {'names': ['NU-108-Cu'], 'topologies': [{'abrv': 'rht'}]}, {'names': ['copper']}])
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
#From 57.html
#None

#From 58.html
#None

#From 59.html
#None

#From 60.html


#From 61.html

#from 42.html
