from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Caption

from chemdataextractor import Document
from chemdataextractor.doc import Paragraph, Heading

#f = open('C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\ZrO_MOF_Test1_Corpus\\33.html', 'rb')
#doc = Document.from_file(f)
#print(doc.records.serialize())

d = Document(Paragraph('''Like other well-established UiO MOFs, MOF-2 possesses fcu network topology'''))
print(d.records.serialize())

b=str(d.records.serialize())
a=str([{'names': ['MOF-2'], 'topologies': [{'abrv': 'fcu'}]}])
print(a)
print(b)
score = 0
if a == b:
    print('test passed')
    score= score+1
else:
    print('test failed')
    score = score

print('score=', score)
no_sentences = 0
no_sentences= no_sentences+1
print('number of sentences=', no_sentences)

d = Document(Caption('''a) Inorganic and organic building units and symmetry analysis in the
                        mtn type MOF MIL-100. '''))
print(d.records.serialize())

b=str(d.records.serialize())
a=str([{'names': ['MIL-100'], 'topologies': [{'abrv': 'mtn'}]}])
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

d = Document(Heading('''MOF-802'''),
    Paragraph('''MOF-802 is prepared with the bent ditopic PZDC as a linker (Scheme 1). The analysis of the 
    single-crystal diffraction data reveals that MOF-802 crystallizes in the Fdd2 space group, with unit 
    cell parameters a = 39.222(3) Å, b = 26.018(2) Å and c = 27.887(2) Å (section S3, SI). In MOF-802 each 
    inorganic SBU is connected to 10 organic linkers, with formate and DMF ligands occupying the remaining
     two coordination sites. The resulting three-dimensional framework has a bct topology (Figure 2a). In this 
     topology there is only one kind of cavity, which in the case of MOF-802 has a maximum diameter of 5.6 Å 
     (b and c of Figure 2).'''))

b=str(d.records.serialize())
a=str([{'names': ['formate']}, {'names': ['DMF']}, {'names': ['MOF-802'], 'topologies': [{'abrv': 'bct'}]}])
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

d = Document(Paragraph('''Finally, we have evaluated DUT-67, which is prepared with the bent 
                        ditopic TDC linker (Scheme 1) and has a reo 
                        topology, with two types of cavities with diameters of 8.8 Å and 16.6 Å (Table 1).'''))

b=str(d.records.serialize())
a=str([{'names': ['TDC']}, {'names': ['DUT-67'], 'topologies': [{'abrv': 'reo'}]}])
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

d = Document(Paragraph(
u'''Three novel microporous zinc MOFs, [Zn3(EBTC)2]∙2(CH3)2NH2∙ 0.5DMSO∙3H2O (1), [Zn(EBTC)0.5(BPY)]∙2DMSO∙0.5DMF∙2H2O (2) 
and [Zn2(EBTC)(BPP)2]∙3DMSO∙2DMF∙5H2O (3) (EBTC = 1,1′-ethynebenzene-3,3′,5,5′-tetracarboxylate, BPY = 4,4′-bipyridine, 
BPP = 1,3-bi(4-pyridyl)propane), have been synthesized under solvothermal conditions. The versatile coordination modes 
of EBTC are the key to such diverse MOFs. The results of X-ray single diffraction analyses indicate that 3D microporous 
MOF 1 with fla topology possesses 2D [Zn3(EBTC)2]∞ layer built from 1D double-chain-like motif containing trinuclear 
[Zn3(COO)8]2 − SBUs, in which the two phenyls of EBTC are almost perpendicularly arranged. Compound 2 is a 3D layer-pillar 
structure with Zn(II) ions bridged by planar EBTC to generate 2D [Zn(EBTC)0.5]∞ sheet, and the 2D sheets are further 
pillared by rigid BPY to form a 3D porous framework with fsc topology. Complex 3 exhibits a 3D 2-fold interpenetrating
framework with (4.64.8)2(42.64) topology, in which the flexible BPP links the 1D [Zn2(EBTC)]∞ ladder to form a 
2D [Zn2(EBTC)(BPP)2]∞ structure with large 1D channels, which leads the flexible 2D framework to 2-fold interpenetration 
and forms a 3D porous network. Complexes 1 and 3 exhibit good luminescent properties around the blue-violet region.'''
))

b=str(d.records.serialize())
a=str([{'names': ['zinc']}, {'names': ['[Zn3(EBTC)2]∞']}, {'names': ['[Zn3(COO)8]2 − SBUs']}, {'names': ['phenyls']}, {'names': ['Zn(II)']}, {'names': ['[Zn(EBTC)0.5]∞']}, {'names': ['[Zn2(EBTC)]∞']}, {'names': ['[Zn2(EBTC)(BPP)2]∞']}, {'names': ['[Zn2(EBTC)(BPP)2]∙3DMSO∙2DMF∙5H2O'], 'labels': ['3'], 'roles': ['complex']}, {'names': ['[Zn(EBTC)0.5(BPY)]∙2DMSO∙0.5DMF∙2H2O'], 'labels': ['2'], 'roles': ['compound'], 'topologies': [{'abrv': 'fsc'}]}, {'names': ['[Zn3(EBTC)2]∙2(CH3)2NH2∙ 0.5DMSO∙3H2O'], 'labels': ['1'], 'roles': ['mof'], 'topologies': [{'abrv': 'fla'}], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}, {'names': ['EBTC', '1,1′-ethynebenzene-3,3′,5,5′-tetracarboxylate']}])
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

d = Document(Paragraph('''The design and synthesis of highly porous MOFs with excellent framework stability and 
                       optimized supramolecular host–guest interactions is an effective strategy to obtain
                       high-performance MOF materials for targeted applications such as gas storage, separation, 
                       catalysis and so on. Herein, we designed and constructed a microporous (3, 24)-connected 
                       rht-type acylamide functionalized MOF (HNUST-9) from dicopper(II)-paddlewheel clusters 
                       and a novel C2-symmetric acylamide-linking hexacarboxylate. Interestingly, with a 
                       high density of strong CO2 binding sites including open copper(II) sites and acylamide 
                       groups integrated in the framework, although exhibiting moderate porosity (a BET surface
                        area of 2429 m2 g−1), the activated HNUST-9 shows an exceptionally high excess CO2 uptake
                       capacity (21.8 mmol g−1 at 25 bar and 273 K), and efficient CO2 separation ability from CO2/CH4
                       and CO2/N2 binary gas mixtures under dynamic conditions at 1 bar and room temperature. 
                       Moreover, HNUST-9 demonstrates efficient catalytic activity for the CO2 cycloaddition with
                       various epoxides in the presence of tetrabutylammonium bromide as the cocatalyst under mild, 
                       solvent-free conditions.'''
    ))

b=str(d.records.serialize())
a=str([{'names': ['dicopper(II)']}, {'names': ['acylamide-linking hexacarboxylate']}, {'names': ['copper(II)']}, {'names': ['CH4']}, {'names': ['N2']}, {'names': ['epoxides']}, {'names': ['tetrabutylammonium bromide']}, {'names': ['acylamide']}, {'names': ['CO2']}, {'names': ['HNUST-9'], 'topologies': [{'abrv': 'rht'}]}])
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

#From 3.html
d = Document(Paragraph(
'''Optimization of the selective oxidation of sterically non-hindered methyl groups demonstrated on the example of 
2,2′,6,6′-tetramethyl-4,4′-biphenyldicarboxylic acid (H2Me4BPDC) that future work in this direction could make 
carboxylate ligands, including chiral ones, accessible by using polymetylated aromatics as precursors. 
The IRMOF [Zn4O(Me4BPDC)3] · 9 DMF and MOF [Cu2(Me4BPDC)2] · 9 DMF are constructed with a ligand bearing the 
maximum number of methyl groups meta to the carboxylate group on the biphenyl frame. DMF could be used instead 
of DEF which is mostly obligatory for high porous MOF-5 and IRMOF-9 or IRMOF-10 samples. [Zn·(FDA)·bipy]·2H2O with 
pcu-a (cab) topology demonstrates good thermal stability up to 170 °C coupled with the possibility of direct 
degassing of the freshly synthesized sample without the necessity in tedious activation based on solvent exchange.
For [Zn4O(Me4BPDC)3], the N2 BET surface area of 1735 m2/g for the obtained doubly interpenetrated modification is 
slightly lower than that of the BPDC analogue (1904 m2/g, IRMOF-9). The adsorptive properties towards H2, and CO2 
are similar with [Zn4O(BDC)3], MOF-5 (IRMOF-1) and better than for [Zn4O(BPDC)3], IRMOF-9. Coupled with seemingly 
lower sensitivity towards atmospheric moisture, the more hydrophobic [Zn4O(Me4BPDC)3] may have a slight edge as a 
material for applications.'''
))

b=str(d.records.serialize())
a=str([{'names': ['2,2′,6,6′-tetramethyl-4,4′-biphenyldicarboxylic acid']}, {'names': ['[Zn4O(Me4BPDC)3] · 9 DMF']}, {'names': ['[Cu2(Me4BPDC)2]']}, {'names': ['number']}, {'names': ['biphenyl']}, {'names': ['IRMOF-10']}, {'names': ['BPDC']}, {'names': ['H2']}, {'names': ['CO2']}, {'names': ['[Zn4O(BDC)3]']}, {'names': ['IRMOF-1']}, {'names': ['[Zn4O(BPDC)3]']}, {'names': ['methyl']}, {'names': ['carboxylate']}, {'names': ['DMF']}, {'names': ['MOF-5']}, {'names': ['[Zn·(FDA)·bipy]·2H2O'], 'topologies': [{'abrv': 'pcu-a'}]}, {'names': ['[Zn4O(Me4BPDC)3]']}, {'names': ['IRMOF-9']}])
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



#From 3.html of the Parent MOF Corpus
d = Document(Paragraph(
    '''The nbo-a topology in the [Cu2(Me4BPDC)2] complex owes its formation to the 90° twist of the ligand/'s phenyl 
    moieties due to steric repulsion of the methyl substituents. [Cu2(Me4BPDC)2] is mechanically much less stable than 
    [Zn4O(Me4BPDC)3], obviously due to a lower connectivity of the square-planar {Cu2(O2CR)4} paddle-wheel unit compared
    to the octahedrally coordinated {Zn4O(O2CR)6} unit. The also doubly interpenetrated framework [Cu2(Me4BPDC)2] collapses
    easily and only a semi-amorphous sample (SBET = 1041 m2/g) was obtained. [Cu2(Me4BPDC)2] is stable at least until 70 °C
    provided some initial solvate molecules are still in the framework. The adsorptive properties towards N2, H2, and CO2
    are better than for MOF-601, MOF-602, MOF-603 ([Cu2L2] with L = 2,2′-R2-4,4′-biphenyldicarboxylate, R = CN, Me, I,
    respectively).'''))

b=str(d.records.serialize())
a=str([{'names': ['phenyl']}, {'names': ['methyl']}, {'names': ['[Zn4O(Me4BPDC)3]']}, {'names': ['{Cu2(O2CR)4}']}, {'names': ['{Zn4O(O2CR)6}']}, {'names': ['N2']}, {'names': ['H2']}, {'names': ['CO2']}, {'names': ['MOF-601']}, {'names': ['MOF-602']}, {'names': ['MOF-603']}, {'names': ['[Cu2L2]']}, {'names': ['2,2′-R2-4,4′-biphenyldicarboxylate']}, {'names': ['Me']}, {'names': ['[Cu2(Me4BPDC)2]'], 'topologies': [{'abrv': 'nbo-a'}]}])
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

d = Document(Paragraph('''Three novel polymers, [Cd1.5(oba)(pcla)(CH3OH)](1), [Zn (oba)(4,4′-bpy)1.5]4(4,4′-bpy)2(H2O)5 (2)
and [Cu2(oba)2(DMF)](DMF)(H2O)(3) (H2oba = 4,4′-oxydibenzoic acid, Hpcla = picolinic acid) have been solvothermally 
synthesized and structurally characterized. 1 shows 2-D double layer structure with 1-D helix channels, while 2 and 3 
display 3-D porous frameworks with different channels in their shapes and sizes. Moreover, complex 3 displays interesting
hydrogen sorption behaviors and these materials are expected to afford potential applications.'''),
Paragraph('''
Complex 2 is a typical compound constituted by V-shaped ligand (4,4′-oxydibenzoic acid). 2 crystallizes in space group of 
I41/a with one Zn atom, one deprotonated oba2 −, one bpy at the general position, one bpy laying about a two fold axis, 
and one coordinated water molecules, and three lattice water molecules and one isolated 4,4′-bpy molecule in the asymmetric 
unit (Fig. 2a). In contrast to other oba complexes, [28] the oba2 − ligands in 2 link the Zn atoms into a 41 helical chain
along the c-axis. There are also monodentate and bidentate bpy ligand and the terminal bpy ligands point inside and fill 
the inside space of the nanotube (Fig. 2b). Regarding Zn atoms as 3-connected notes, this complex can be simplified as a 
(10,3)-a (srs) net (Fig. 2c). Moreover, a serious view of the structure that an overall six-fold interpenetration was observed. 
To the best of our knowledge, 2 is the second coordination framework with 6-fold interpenetration of srs topology [29].
'''
))

b=str(d.records.serialize())
a=str([{'names': ['[Cd1.5(oba)(pcla)(CH3OH)](1)']}, {'names': ['picolinic acid']}, {'names': ['hydrogen']}, {'labels': ['3'], 'roles': ['complex']}, {'names': ['4,4′-oxydibenzoic acid']}, {'names': ['4,4′-bpy']}, {'names': ['[Cu2(oba)2(DMF)](DMF)(H2O)(3)'], 'synthesis_routes': [{'synthesis': 'solvothermally'}]}, {'names': ['Zn']}, {'names': ['[ Zn (oba)(4,4′-bpy)1.5]4(4,4′-bpy)2(H2O)5'], 'labels': ['2'], 'roles': ['complex'], 'topologies': [{'abrv': 'srs'}]}])
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

d = Document(Paragraph(
'''A dendritic hexacarboxylate ligand featuring amine and triazole groups was rationally designed and synthesized, 
which was employed to construct a (3,24)-connected rht-type copper(II) metal-organic framework (MOF, NTU-105-NH2) 
under solvothermal conditions. The desolvated amine-functionalized MOF demonstrated improved CO2 and H2 uptake capacity 
as well as significant higher selectivity towards CO2 over N2 in comparison to its parent MOF.'''))

b=str(d.records.serialize())
a=str([{'names': ['hexacarboxylate']}, {'names': ['copper(II)']}, {'names': ['CO2']}, {'names': ['H2']}, {'names': ['N2']}, {'names': ['amine']}, {'names': ['NTU-105-NH2'], 'topologies': [{'abrv': 'rht'}], 'synthesis_routes': [{'synthesis': 'solvothermal'}]}])
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

d = Document(Paragraph(
'''We are interested in the design and synthesis of novel organic linkers by using “click reaction”, 
due to its easy manipulation and high reaction yield [4], [5]. Recently, we reported a porous and robust 
triazole-functionalized rht-MOF NTU-105 with exceptionally high CO2 and H2 uptake [4s]. With the purpose of 
optimizing its performance further, herein, we introduce amine into the framework through the pre-design of 
ligand. And a new MOF NTU-105-NH2 was constructed, which was expected to exhibit the improved capacity and 
selectivity for CO2 sorption owing to the interactions between basic amine and gas molecules [6]. On the other hand;
the incorporation of amine moiety offers the opportunity for post-synthetic modification of the MOFs for more other 
applications [3].'''
))

b=str(d.records.serialize())
a=str([{'names': ['H2']}, {'names': ['NTU-105-NH2']}, {'names': ['NTU-105'], 'topologies': [{'abrv': 'rht'}]}, {'names': ['CO2']}, {'names': ['amine']}])
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

d = Document(Paragraph('''With respect to the steric hindrance and electronic effect, the flexible and rigid pillars are 
employed to the construction of structure, respectively. In this work, two novel MOFs have been synthesized, in which 
the flexible bpp results in the robust porous [Zn3·(FDA)3·bpp·H2O]·2H2O (1), and the rigid bipy in 3-/3-D interpenetrated
[Zn·(FDA)·bipy]·2H2O (2).'''
),
    Paragraph(
'''Owing to the symmetrical geometry of 2 (Pccn), two sets of structures 3-dimesionally interpenetrate each other, 
each one of which is reduced to pcu topology with the Zn-dimer as node and FDA/bipy as the connector (Fig. 2b). 
Although every FDA connects three Zn, FDA acts as two-connector because FDA connects two Zn-dimers. Both sets of 
structures consist of such a SBU served as octahedral geometry, in which four 2-c FDAs occupy the equatorial plane
and two pairs of 2-c bipy molecules respectively locate on the apices (Fig. 2a and 2b). Weak π–π interactions exist
between two bipy molecules of every pair with twist φ of 26.7° and stacking h of 3.379 Å. The distances of two Zn-dimers 
linked by bipy and FDA are 11.405 Å and 11.889 Å, respectively. The torsion angle of two furan rings in different set of 
structure is 25.04°.'''
))

b=str(d.records.serialize())
a=str([{'names': ['[Zn3·(FDA)3·bpp·H2O]·2H2O'], 'labels': ['1']}, {'names': ['[Zn·(FDA)·bipy]·2H2O'], 'labels': ['2']}, {'topologies': [{'abrv': 'pcu'}]}, {'names': ['Zn-dimers']}, {'linker_routes': [{'linker': "['bipy']"}]}, {'names': ['furan']}, {'names': ['Zn']}, {'names': ['bipy']}])
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

d = Document(Paragraph('''A new three-dimensional (3D) metal–organic framework (MOF) {Zn5(μ3-OH)2(obb)4[(CH3)2NH]2}·2DMF 
(1; H2obb = 4,4′-oxbisbenzoic acid; DMF = N,N′-dimethyl formamide) with unusual Zn5(μ3-OH)2(COO−)8 secondary building 
units (SBUs) has been solvothermally synthesized and structurally characterized by the aid of single crystal X-ray 
diffraction, powder X-ray diffraction (PXRD), thermogravimetric analysis (TGA), Elemental analysis (EA) and Infrared 
Spectroscopy (IR). The unprecedented pentanuclear Zn5(μ3-OH)2(COO−)8 SBU was formed by two trimeric Zn3(μ3-OH)(COO−)6 SBUs,
which can be simplified as 4-connected node. Correspondingly, complex 1 dia topology.'''
))

b=str(d.records.serialize())
a=str([{'names': ['Zn3(μ3-OH)(COO−)6']}, {'names': ['Zn5(μ3-OH)2(COO−)8']}, {'names': ['{Zn5(μ3-OH)2(obb)4[(CH3)2NH]2}·2DMF'], 'labels': ['1'], 'roles': ['complex'], 'topologies': [{'abrv': 'dia'}], 'synthesis_routes': [{'synthesis': 'solvothermally'}]}])
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

d = Document(Paragraph('''A novel phosphonocarboxylic ligand, 4′-phosphonobiphenyl-3,5-dicarboxylic acid (H4pbpdc),
was synthesized to construct 4 zinc compounds, namely, {[Zn3(pbpdc)2·2R}n (R = C5H12N for 1, C4H10N for 2 and C6H16N 
for 3) and {[Zn2pbpdc]·C6H18N3}n (4), which were characterized by X-ray crystallography, elemental analysis, FTIR and TG. 
Structures 1 ~ 3 have the same 3-dimensional (3-D) frameworks with point symbol of 
{4.6.73.8}2{42.6.72.8}2{42.62.7.8}2{42.62.72}. Structure 4 is constructed from a 6-connected metallic cluster and 
3-connected phosphonocarboxylic building units resulting in a topology of flu-3,6-C2/c. The luminescent properties 
of compounds 1 ~ 4 and organic ligand were studied.'''))

b=str(d.records.serialize())
a=str([{'names': ['phosphonocarboxylic']}, {'names': ['4′-phosphonobiphenyl-3,5-dicarboxylic acid']}, {'names': ['zinc']}, {'names': ['{[Zn3(pbpdc)2·2R}n']}, {'names': ['C5H12N']}, {'names': ['C4H10N']}, {'names': ['C6H16N']}, {'names': ['{[Zn2pbpdc]·C6H18N3}n'], 'labels': ['4']}, {'labels': ['1'], 'roles': ['compounds']}])
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

d = Document(Paragraph(
''' 
The structural topology for the following eight compounds with pcu topology (Fig. 1.) [7]: [Mn(ip)(dma)]n (1), 
[Mn(tdc)(dma)]n 2, [Mn(tdc)(nmp)]n 3, [Mn(tdc)(dmso)]n 4, [Mn(tp)(dmf)]n 5, [Mn(tmtp)(dmf)]n 6, {[Co(ntp)(H2O)]·1.25H2O}n 7 
and [Zn(1,4-ndc)(dmf)]n 8. These compounds were assembled using short ligands (e.g., H2ip and its derivatives ∼5.9 Å as 
well as H2tdc ∼6.4 Å), and medium-length ligands (H2tp and its derivatives ∼7 Å). Metal ions, such as Mn2+, Co2+ and Zn2+,
form Mn metal centres or rod-shaped SBUs composed of corner-sharing octahedra, while the Mn2+ ion with the largest size can
also form edge-sharing octahedral rod-shaped SBUs (Fig. 1a, d). Six of the eight compounds in this group were formed using 
Mn2+ ions, which demonstrates that Mn2+ has a strong tendency to form rod-shaped SBUs. Notably, 2, 3 and 4 were synthesised
in different solvents and are isostructures, which demonstrates that the solvents did not influence the structures. 
Compounds 5 and 6 were synthesised using H2tp and tetramethyl-substituted H2tmtp, and their structures have same topology.
'''
),
Paragraph(
'''The following seven compounds contain dinuclear metal centres with four coordination points: 
[Cu2(tdc)2(NH3)4]n 9, [Cu2(tbip)2(dma)2]n 10, {[Cu2(ip)2(nmp)2{Cu2(ip)2(H2O)2}2]·5NMP·2H2O}n 11, 
[Zn2(tp)2(nmp)2]n 12, [Zn2(2,6-ndc)2(dmf)2]n 13, [Zn2(tdc)2(dma)2]n 14 and [Zn2(tdc)2(py)2]n 15 (Fig. 2).
When the same ligands with short-medium lengths as for group 1 were used (except for 13, which was assembled 
with the long ligand H2(2,6-ndc), Cu2+ and Zn2+ tended to form dinuclear metal centres instead of rod-shaped SBUs,
and the topology of the structures were sql, which is related to a node with four coordination points. Most of the
paddle-wheel M2 metal centres adopted a sql topology, while the structure for 11 was assembled using a bent ligand, 
H2ip, which adopted a kgm net [42].'''
))

b=str(d.records.serialize())
a=str([{'topologies': [{'abrv': 'pcu'}]}, {'names': ['[Mn(ip)(dma)]n'], 'labels': ['1']}, {'names': ['[Mn(tdc)(dma)]n']}, {'names': ['[Mn(tdc)(nmp)]n']}, {'names': ['[Mn(tdc)(dmso)]n']}, {'names': ['[Mn(tp)(dmf)]n']}, {'names': ['[Mn(tmtp)(dmf)]n']}, {'names': ['[Zn(1,4-ndc)(dmf)]n']}, {'names': ['Co2+']}, {'names': ['Mn']}, {'names': ['tetramethyl-substituted H2tmtp']}, {'labels': ['5'], 'roles': ['compounds']}, {'names': ['[Cu2(tdc)2(NH3)4]n 9, [Cu2(tbip)2(dma)2]n 10, {[Cu2(ip)2(nmp)2{Cu2(ip)2(H2O)2}2]·5NMP·2H2O}n 11, [Zn2(tp)2(nmp)2]n 12, [Zn2(2,6-ndc)2(dmf)2]n 13']}, {'names': ['[Zn2(tdc)2(dma)2]n']}, {'names': ['[Zn2(tdc)2(py)2]n 15']}, {'names': ['Cu2+']}, {'names': ['H2ip']}, {'names': ['H2tp']}, {'names': ['Mn2+']}, {'names': ['Zn2+']}])
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

d = Document(Paragraph('''MOF-2 crystallizes in the cubic Fmequation imagem space group. The asymmetric unit consists of 
1/48 of the Zr6O4(OH)4(CO2)12 cluster and 1/8 of the bridging ligands. The SBU comprises six Zr cations, with each Zr 
bridged by μ3-O, μ3-OH, and carboxylate groups. Each SBU is connected to twelve neighboring SBUs by twelve dicarboxylate 
linkers. Like other well-established UiO MOFs, MOF-2 possesses fcu network topology.'''))

b=str(d.records.serialize())
a=str([{'names': ['Zr6O4(OH)4(CO2)12']}, {'names': ['Zr']}, {'names': ['μ3-O']}, {'names': ['μ3-OH']}, {'names': ['carboxylate']}, {'names': ['MOF-2'], 'topologies': [{'abrv': 'fcu'}]}])
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

d = Document(Paragraph('''A single-crystal X-ray diffraction study showed that MOF-1 crystallizes in the tetragonal 
I4/mmm space group (Figure 1). The asymmetric unit consists of 1/16 of the Zr6O8(OH2)8(CO2)8 cluster and 1/4 of the 
bridging ligands. Unlike traditional UiO MOFs, the Zr SBU is only eight-connected, with the formula of 
Zr6O8(OH2)8(L1)4. Compared to a typical Zr6O4(OH)4(L)6 cluster, the four bridging carboxylate groups on the equatorial 
plane of the Zr6 octahedra are missing, substituted by aqua coordination. The resulting MOF possesses bcu network topology
with {424⋅64} connectivity.'''))

b=str(d.records.serialize())
a=str([{'names': ['MOF-1']}, {'names': ['Zr6O8(OH2)8(CO2)8']}, {'names': ['Zr']}, {'names': ['Zr6O8(OH2)8(L1)4']}, {'names': ['Zr6O4(OH)4(L)6']}, {'names': ['carboxylate']}, {'names': ['Zr6']}, {'topologies': [{'abrv': 'bcu'}]}])
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

d = Document(Paragraph('''Although PCN-128W and PCN-128Y belong to the same space group (P6/mmm) and the same topology 
(csq-a), the unit cell parameters, however, are slightly different.'''))

b=str(d.records.serialize())
a=str([{'names': ['PCN-128Y']}, {'names': ['PCN-128W'], 'topologies': [{'abrv': 'csq-a'}]}])
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

d = Document(Paragraph('''A robust and porous zinc metal–organic framework, sal-MOF, of UiO topology was synthesized using
a salicylaldimine (sal)-derived dicarboxylate bridging ligand. Postsynthetic metalation of sal-MOF with iron(II) or 
cobalt(II) chloride followed by treatment with NaBEt3H in THF resulted in Fe- and Co-functionalized MOFs (sal-M-MOF, 
M = Fe, Co) which are highly active solid catalysts for alkene hydrogenation. Impressively, sal-Fe-MOF displayed very 
high turnover numbers of up to 145000 and was recycled and reused more than 15 times. This work highlights the unique 
opportunity of developing MOF-based earth-abundant catalysts for sustainable chemical synthesis.
'''))

b=str(d.records.serialize())
a=str([{'names': ['zinc']}, {'names': ['salicylaldimine (sal)-derived dicarboxylate']}, {'names': ['iron(II)']}, {'names': ['cobalt(II) chloride']}, {'names': ['NaBEt3H']}, {'names': ['THF']}, {'names': ['Fe-']}, {'names': ['sal-M-MOF']}, {'names': ['Fe']}, {'names': ['Co']}, {'names': ['alkene']}, {'names': ['sal-Fe-MOF']}, {'names': ['MOF-based']}, {'names': ['sal-MOF']}])
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

d = Document(''' MOF-8, spn;(11) PCN-777 spn;(12) and UMCM-309, kgd;(13)''')

b=str(d.records.serialize())
a=str([{'names': ['MOF-8'], 'topologies': [{'abrv': 'spn'}]}, {'names': ['PCN-777'], 'topologies': [{'abrv': 'spn'}]}, {'names': ['UMCM-309'], 'topologies': [{'abrv': 'kgd'}]}])
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

d = Document(Paragraph( '''MIL-100 and MIL-101, both of which have zeotype mtn topology (zeotype refers to structures 
sharing the same topology as zeolites), contain super-tetrahedral cages to substitute for the tetrahedral unit in zeolites.
5 '''))

b=str(d.records.serialize())
a=str([{'names': ['MIL-101']}, {'names': ['zeolites']}, {'names': ['MIL-100'], 'topologies': [{'abrv': 'mtn'}]}])
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

d = Document(Paragraph('''
Interestingly, interpenetration is avoided in CPM-99 with ftw topology, while the high stability is retained.
'''))

b=str(d.records.serialize())
a=str([{'names': ['CPM-99'], 'topologies': [{'abrv': 'ftw'}]}])
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

d = Document(Paragraph(
'''Herein, we have investigated the metal–organic framework mechanical properties of two UiO topology Zr-MOFs, the planar UiO-67 
([Zr6O4(OH)4(bpdc)6], bpdc: 4,4′-biphenyl dicarboxylate) and UiO-abdc ([Zr6O4(OH)4(abdc)6]'''
))

b=str(d.records.serialize())
a=str([{'names': ['Zr']}, {'names': ['UiO-67']}, {'names': ['[Zr6O4(OH)4(bpdc)6]']}, {'names': ['bpdc : 4,4′-biphenyl dicarboxylate']}, {'names': ['UiO-abdc']}, {'names': ['[Zr6O4(OH)4(abdc)6]']}])
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

d = Document(Paragraph(
'''Whereas combinations of these SBUs with linear dicarboxylate linkers generally produce (12,2)-connected 
3D nets with face-centered cubic packing and pcu-type topologies, as exemplified by the UiO,12 PIZOF,17 PCN-56, 
to −59 families'''
))

b=str(d.records.serialize())
a=str([{'names': ['UiO,12 PIZOF,17 PCN-56'], 'topologies': [{'abrv': 'pcu'}]}])
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

d = Document(Paragraph(
'''n the course of synthetic experiments we indeed obtained DUT-52 coordination polymer isoreticular to UiO-66,7 
but also found out, that by adjusting only the acetic acid amount in this reaction system, it is possible to switch 
the connectivity of the cluster from 12 in [Zr6O4(OH)4]12+ SBU (DUT-52, fcu topology)27 through 8 in [Hf6O6(OH)2]10+
SBU (DUT-53, bcu topology)27 to 6 in Zr6O8(CH3COO)26+ SBU (DUT-84 (4,4)IIb)'''
))

b=str(d.records.serialize())
a=str([{'names': ['UiO-66,7']}, {'names': ['acetic acid']}, {'names': ['[Zr6O4(OH)4]12+']}, {'names': ['DUT-53']}, {'names': ['Zr6O8(CH3COO)26+']}, {'names': ['DUT-84 (4,4)IIb']}, {'topologies': [{'abrv': 'bcu'}]}, {'names': ['DUT-52'], 'topologies': [{'abrv': 'fcu'}]}])
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

d = Document(
'''Fig. 1 Structural and topological representation of ZrSQU. SQU linkers (a) and Zr6O4(OH)4(C2O2)12 clusters 
(b) stack in an fcu-lattice (c), delineating octahedral (orange, d) and tetrahedral (green, e) cages with triangular 
windows. (Zr = blue; O = red; C = black).'''
)

b=str(d.records.serialize())
a=str([{'names': ['ZrSQU']}, {'names': ['Zr = blue']}, {'names': ['O = red']}, {'names': ['C = black']}, {'names': ['Zr6O4(OH)4(C2O2)12'], 'topologies': [{'abrv': 'fcu'}]}])
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

d = Document(Paragraph(
'''Through a topology-guided strategy, a series of Zr6-containing isoreticular porphyrinic metal–organic frameworks (MOFs),
PCN-228, PCN-229, and PCN-230, with ftw-a topology were synthesized using the extended porphyrinic linkers. '''
))

b=str(d.records.serialize())
a=str([{'names': ['Zr6']}, {'names': ['PCN-229']}, {'names': ['PCN-230']}, {'names': ['PCN-228'], 'topologies': [{'abrv': 'ftw-a'}]}]
)
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
