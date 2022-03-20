from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading


f = open('C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\top_PR_corpus_test2\\40.html', 'rb')
doc = Document.from_file(f)
print(doc.records.serialize())

'''
#d = Document(Paragraph('[Ni2(hfipbb)2(2,2′-bipy)2(H2O)4] (1), [Ni(4,4′-bipy)(hfipbb)(H2O)]·0.5DMF (2), [Ni2(hfipbb)2(BPE)1.5(H2O)(μ2-H2O)]·DMF·2H2O (3) and Zn(hfipbb)(2,2′-bipy)·0.5DMF (4) (H2hfipbb = 4,4′-(hexafluoroisopropylidene)bis(benzoic acid); 2,2′-bipy = 2,2′-bipyridine; 4,4′-bipy = 4,4-bipyridine; BPE = 1,2-di(4-pyridyl)ethane; DMF = N,N-dimethylformamide) have been synthesized under solvothermal conditions based on the V-shaped H2hfipbb ligand and different auxiliary linear N-containing ligands. Compound 1 exhibits a three dimensional (3D) supramolecular network built from 0D rings linked through hydrogen bonds and π–π packing interactions. Compound 2 displays a 3D 3-fold interpenetrating diamond network with a point symbol of (66). Compound 3 gives a double layer structure with (44·62)sql topology built from {Ni2} clusters bridged by BPE and hfipbb2− ligands. Compound 4 is a 3D array formed by interdigitated 1D zigzag [Zn2(hfipbb)2]n ribbons, in which the Zn2(COO)4 paddle-wheel SBUs are linked by two hfipbb2− ligands. '))
d = Document(Paragraph('Solvothermal reaction between H3BTN and Cu(NO3)2·2.5H2O in a DEF/H2O mixture under acidic conditions at 90 °C for 24 h afforded blue polyhedral-shaped single crystals of UTSA-28-Cu ([Cu3(BTN)2(H2O)3]·14DEF).'))
print(d.records.serialize())'''