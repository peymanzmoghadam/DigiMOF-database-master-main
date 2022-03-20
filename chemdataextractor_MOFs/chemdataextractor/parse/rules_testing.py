from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading

d = Document(Paragraph(
    '''A solvothermal reaction of amino (1 mol) and Cu(NO3)2 (2 mol) in N,N-dimethylformamide (DMF) in the presence of a 
    small amount of HNO3 at 75 °C for 3 days afforded block blue crystals of PIZOF'''
))

d = Document(Paragraph(
    '''Under solvothermal conditions, the reaction of Cu(NO3)2·2.5H2O and [Co3(BDC)3(DPNDI)(DMF)2]·2CH3CN in dimethylformamide at 65 °C afforded 
    MOF crystals denoted as [Co3(BDC)3(DPNDI)(DMF)2]·2CH3CN'''
))
print(d.records.serialize())

