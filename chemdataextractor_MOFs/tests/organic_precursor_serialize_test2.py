from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption
#test1
from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading
import time
#this test file should be used after a refinement is made to a parser, new sentences can be added and the score should be checked to make sure old sentences can still be passes
#a test fail does not necessarily mean the sentence isn't being parsed correctly if a refinement has been made, the record should be checked and if the parser is performing better
#the new record string should be copied in and the test can be taken to be passed


f = open('C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\chemdataextractor_batteries\\Relationship Test\\ja208256u.xml', 'rb')
doc = Document.from_file(f)
start = time.time()

print(doc.records.serialize())


'''
d = Document(
    Paragraph('A dendritic hexacarboxylate ligand featuring amine and triazole groups was rationally designed and synthesized, which was employed to construct a (3,24)-connected rht-type copper(II) metal-organic framework (MOF, NTU-105-NH2) under solvothermal conditions. The desolvated amine-functionalized MOF demonstrated improved CO2 and H2 uptake capacity as well as significant higher selectivity towards CO2 over N2 in comparison to its parent MOF.'),
    Paragraph('As a new class of hybrid inorganic–organic porous and crystalline materials, metal-organic frameworks (MOFs) are constructed by the assembly of metal ions or metal-cluster nodes with multitopic bridging organic linkers [1]. Through the judicious combination of metal centers and organic linkers, a large number of MOF with desired properties and well-defined structures have been synthesized over past decades [1]. Moreover, the high degree of tunability for MOFs provides a unique advantage over other conventional porous materials, such as zeolites, in which various functional groups can be readily introduced into the frameworks via either ligand design and/or post-synthetic modifications [2], [3].'),
    Paragraph('Recently, an interesting series of Cu-based isoreticular MOFs with rht-topology has emerged [4], in which the cuboctahedral metal-organic polyhedra (MOP) with chemical formula [Cu(II)2(isophthalate)2S2]12 (S = solvent, typically H2O) is connected by a rigid triangular central core through the 24 vertices from 5-position of each isophthalate moieties, thus generating a three dimensional (3,24)-connected framework. These isoreticular highly-connected rht-MOFs exhibited a lot of unique attributes [4], such as the absence of self-interpenetration induced by lengthening the organic struts, highly stable and robust framework after desolvation, extra-high surface area and pore volume, and high concentration of open-metal sites upon the removal of axially coordinated solvent molecules. These priorities make them highly promising candidates for gas storage and separation, especially for H2 storage and CO2 capture, because of the growing demand to address the persisting challenges in global energy issues and environmental sustainability. In this context, many dendritic hexacarboxylate organic linkers composed of three coplanar isophthalates having an overall C3-symmetry have been synthesized and employed to construct such highly porous isoreticular rht-MOFs [4]. Although the expansion of organic ligands in these MOFs is an effective way to increase their surface area and pore volume, it was found that the gas uptake capacity and selectivity are not always proportional to the surface area, especially in low pressure range [4b–l]. Therefore, several functional polar moieties [4m–s], such as amide and triazole, which favor the interactions between the MOF hosts and the adsorbed gas molecules, have been introduced into the porous rht-frameworks via the pre-design of ligands towards enhanced performance.'),
    Paragraph('We are interested in the design and synthesis of novel organic linkers by using “click reaction”, due to its easy manipulation and high reaction yield [4], [5]. Recently, we reported a porous and robust triazole-functionalized rht-MOF NTU-105 with exceptionally high CO2 and H2 uptake [4s]. With the purpose of optimizing its performance further, herein, we introduce amine into the framework through the pre-design of ligand. And a new MOF NTU-105-NH2 was constructed, which was expected to exhibit the improved capacity and selectivity for CO2 sorption owing to the interactions between basic amine and gas molecules [6]. On the other hand; the incorporation of amine moiety offers the opportunity for post-synthetic modification of the MOFs for more other applications [3].'),
    Paragraph('In order to introduce the amine moiety into the framework, we re-designed and synthesized a new dendritic hexa-carboxylate linker H6-1 by using the “click reaction” between 2,4,6-triethynylbenzenamine and di-tert-butyl 5-azidoisophthalate, followed by hydrolysis in the mixture of trifluoroacetic acid and CH2Cl2 with a high yield (Scheme 1, for more synthetic details see Supplementary data).'),
    Paragraph('A solvothermal reaction of H6-1 and Cu(NO3)2 in N,N-dimethylformamide (DMF) in the presence of a small amount of HNO3 at 75 °C for 3 days afforded block blue crystals of NTU-105-NH2, having the framework formula [Cu3(1)(H2O)3]n. The phase purity of a bulk sample was confirmed from powder X-ray diffraction (PXRD) measurements.'))
print(d.records.serialize())
'''


