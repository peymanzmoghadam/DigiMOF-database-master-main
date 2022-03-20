from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
import time


e = Document(
    Paragraph(
        'A solvothermal reaction of Compound 1 and Cu(NO3)2 in N,N-dimethylformamide (DMF) in the presence of a small amount of HNO3 at 75 °C for 3 days afforded block blue crystals of NTU-105-NH2, having the framework formula [Cu3(1)(H2O)3]n. The phase purity of a bulk sample was confirmed from powder X-ray diffraction (PXRD) measurements.'))
start = time.time()
print(start)
print(e.records.serialize())

