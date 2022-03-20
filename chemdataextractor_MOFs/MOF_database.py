# -*- coding: utf-8 -*-
"""
extract.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the raw battery data.

"""

from chemdataextractor import Document
from chemdataextractor.reader.acs import AcsHtmlReader
from chemdataextractor.reader.markup import HtmlReader
from chemdataextractor.parse.cem import MOF_formula
import json
import copy
import re
import time

#Regular expressions that restrict the compounds entering the database to just being MOFs
re_MOF1 = '^(?![aA-zZ]+\-?\d?\d?\-like)(?![aA-zZ]+\-?\d?\d?\-type(s?))(ZJU|SNU|MAF|MCF|Ir-MOF|JUC|FJI|UHM|MUV|BUT|ZJNU|Tb|she|CTH|pek|FDM|MODF|USF|NJFU|ZJU|CMOF|CTH|TPMOF|IZE|pbz|PNMOF|gea|MFM|UNLPF|PIZOF|soc|MOAAF|Y|Ho|CPO|JLU|aea|NOTT|NU|MMPF|UTSA|CPM|U[iI]O|MOF|IRMOF|T-MOF|NTU|MIL|HKUST|HNUST|LIC|PCN|ZIF|CPL|CALF|UMCM|DUT)[:;\[\]\)\{\}\]{0,3}[\-‐‑⁃‒–—―−－⁻][A-Za-z0-9_-]+[:;\[\]\)\{\}\]{0,3}[A-Za-z0-9_-]*[:;\[\]\)\{\}\]{0,3}[A-Za-z0-9_-]*[:;\[\]\)\{\}\]{0,3}[A-Za-z0-9_-]*[:;\[\]\)\{\}\]{0,3}[A-Za-z0-9_-]+$'
re_MOF2 = '^(ZJU|SNU|MAF|MCF|Ir-MOF|JUC|FJI|UHM|MUV|BUT|ZJNU|Tb|she|CTH|pek|FDM|MODF|USF|NJFU|ZJU|CMOF|CTH|TPMOF|IZE|pbz|PNMOF|gea|MFM|UNLPF|PIZOF|soc|MOAAF|Y|Ho|CPO|JLU|aea|NOTT|NU|UTSA|MMPF|CPM|U[iI]O|MOF|T-MOF|IRMOF|NTU|MIL|HKUST|HNUST|LIC|PCN|ZIF|CPL|CALF|UMCM|DUT)([\-‐‑⁃‒–—―−－⁻])([a-zA-Z0-9]+)$'
re_chemical_formula = '^(?![aA-zZ]+\-?\d?\d?\-ligands)(?!(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\d\(CO2\)\d?\(?N?N?\)?)(?!^(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\($)(?!(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\(CH3COO\)\d\s?\d?H?2?O?)(?!M1)(?!(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\dAs\dO\d)(?!(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\d\(μ3-OH\)\d\(CO2\)\d)(?!\[?Zn\d\(μ4-O\)\(O2CR?\)\d\])(?!\[?(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\((AcO|OAc)\)\d?\s?H?2?O?)(?!Me\dNH\d)(?!(\[?Zn\dO?\(O2C))(?!^M\(II\))(?!.*\(OOC\)\d$)(?!Co\(Tt\)\d?$)(?!.*\(COO−?\)\d$)(?!(M|Mn|Cu|Zn|Y|Co|Ni|Fe|Zr|Cd)\((II|i|ii|iii)\)$)(?!\[?(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\d?O?\(CO2\)\d\]?$)(?!(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\dO?\+?.?.?.?$)(?!UiO-type$)(?!\[?(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\(NO\d?\)\d?\]?.?.?.?.?.?.?.?$)(?!\[?(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)\(ClO\d?\)\d?\]?.?.?.?.?.?.?.?$)(?!Cu\(NO\d?\).?.?.?.?.?.?.?.?$)(?!\[Zn3\(EBTC\)2\]∞$)(?!\{?Cu\d\(O2?CR\)\d\}?$)(?!HCl$)(?!Cu\(II\)$)(?!Zr6O8\(CH3COO\)26\+$)(?!Cu\(NO3\)2·3H2O$)(?!Zr6$)(?!Cu\(NO3\)2$)(\[?)(\{)?(\[)?(Mg|M|Ni|Zn|Mn|Cu|Zr|Me|CoCl|Co|Cd)(\s?)(L|\d|\(|\-)'
reobj = re.compile("%s|%s|%s" % (re_MOF1, re_MOF2, re_chemical_formula))



class MOFDataBase():

    def __init__(self, paper_root, save_root, filename):
        self.dic = None
        self.filename = filename
        self.paper_root = paper_root
        self.count = 0
        self.save_root = save_root

    def write_into_file(self):
        with open('{}/{}.json'.format(self.save_root, self.filename), 'a', encoding='utf-8') as json_file:
            json.dump(self.dic, json_file, ensure_ascii=False)
            json_file.write('\n')
        return

#method defined to store extracted data as a dictionary
    def extract(self, file):
        """
        :param file: The parsing files (HTML/XML...)
        :return: Write the record into the documents
        """
        start = time.time()
        f = open(file, 'rb')
        d = Document.from_file(f)
        print(d)
        print('parsing ' + file)
        print(d.metadata)
        print(start)
        rough = d.records.serialize()
        data = []

        for dic in rough:
            if "names" in dic and "topologies" in dic and "synthesis_routes" in dic and "linker_routes" in dic:
                data += dic
                dicts_topologies = dic["topologies"][0]
                dicts_synthesis = dic['synthesis_routes']
                dicts_linker_routes = dic['linker_routes']
                name = dic["names"]
                save = {"MOF_data": {"file":file, "synthesis_route": dicts_synthesis,
                                             "topology":dicts_topologies["abrv"],
                                             "linker": dicts_linker_routes,
                                             "compound": {"Compound": {"names": name}}}}
                self.dic = save
                if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                    self.write_into_file()
                    self.count += 1
            elif "names" in dic and "topologies" in dic and "linker_routes" in dic:
                data += dic
                dicts_topologies = dic["topologies"][0]
                dicts_linker_routes = dic['linker_routes']
                name = dic["names"]
                save = {"MOF_data": {"file": file, "topology":dicts_topologies["abrv"],
                                             "linker": dicts_linker_routes,
                                             "compound": {"Compound": {"names": name}}}}
                self.dic = save
                if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                    self.write_into_file()
                    self.count += 1
            elif "names" in dic and "synthesis_routes" in dic and "linker_routes" in dic:
                data += dic
                dicts_synthesis = dic['synthesis_routes']
                dicts_linker_routes = dic['linker_routes']
                name = dic["names"]
                save = {"MOF_data": {"file":file, "synthesis_route": dicts_synthesis,
                                             "linker": dicts_linker_routes,
                                             "compound": {"Compound": {"names": name}}}}
                self.dic = save
                if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                    self.write_into_file()
                    self.count += 1
            elif "names" in dic and "topologies" in dic and "synthesis_routes" in dic:
                data += dic
                dicts_topologies = dic["topologies"][0]
                dicts_synthesis = dic['synthesis_routes'][0]
                name = dic["names"]
                if "abrv" in dicts_topologies and "synthesis" in dicts_synthesis and "solvent" in dicts_synthesis:
                    save = {"MOF_data": {"file": file, "topology": dicts_topologies["abrv"], "synthesis_route":dicts_synthesis["synthesis"],
                                             "solvent":dicts_synthesis["solvent"], "compound": {"Compound": {"names": name}}}}
                    self.dic = save
                    if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                        self.write_into_file()
                        self.count += 1
                elif "abrv" in dicts_topologies and "synthesis" in dicts_synthesis:
                    save = {"MOF_data": {"file": file, "topology": dicts_topologies["abrv"], "synthesis_route":dicts_synthesis["synthesis"],
                                             "compound": {"Compound": {"names": name}}}}
                    self.dic = save
                    if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                        self.write_into_file()
                        self.count += 1
            elif "names" in dic and "topologies" in dic:
                data += dic
                dicts = dic["topologies"][0]
                name = dic["names"]
                if "abrv" in dicts:
                    save = {"MOF_data": {"file": file, "topology": dicts["abrv"],
                                             "compound": {"Compound": {"names": name}}}}
                    self.dic = save
                    if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                        self.write_into_file()
                        self.count += 1
                else:
                    save = {"MOF_data": {"file": file, "full_topology": dicts["full"], "topology": dicts["abrv"],
                                             "compound": {"Compound": {"names": name}}}}
                    self.dic = save
                    if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                        self.write_into_file()
                        self.count += 1

            elif "names" in dic and "synthesis_routes" in dic:
                data += dic
                dicts = dic["synthesis_routes"][0]
                name = dic["names"]
                if "synthesis" and "solvent" in dicts:
                    save = {"MOF_data": {"file": file, "synthesis_route": dicts["synthesis"], "solvent":dicts["solvent"], "compound": {"Compound": {"names": name}}}}
                    self.dic = save
                    if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                        self.write_into_file()
                        self.count += 1
                elif "synthesis" in dicts:
                    save = {"MOF_data": {"file": file, "synthesis_route": dicts["synthesis"], "compound": {"Compound": {"names": name}}}}
                    self.dic = save
                    if [i for i in save["MOF_data"]["compound"]["Compound"]["names"] if re.search(reobj, i)]:
                        self.write_into_file()
                        self.count += 1
        print(str(self.count) + ' relations in total')
        print(file + ' is done')
        end = (time.time() - start)/60
        print(end)
        f.close()

