from chemdataextractor.scrape.clean import Cleaner
from chemdataextractor.reader.acs import AcsHtmlReader
import os
from urllib.request import urlopen
import codecs
from chemdataextractor import Document

'''
#Creates the Document object then writes it to a text file
f = open('C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\test_MOF_clean\\testing_ACS.html', encoding='utf-8)')
acs_reader = AcsHtmlReader()
#print(acs_reader.detect(f))
d = acs_reader.read(f)
a = open('clean.txt', 'x', encoding= 'UTF-8')
a.write(str(d.records.serialize()))
'''

#print(d.records.serialize())

cleaner = Cleaner()
acs_reader = AcsHtmlReader()
f = open('C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\test_MOF_clean\\testing_ACS.html', encoding='utf-8')
#print(acs_reader.read(f))

clean_acs = cleaner.clean_html(f.read())

save_path = 'C:\\Users\\gubsc\\OneDrive\\Documents\\Sheffield\\Semester 1\\Research Project\\GitHub\\batterydatabase-master-updated\\batterydatabase-master\\test_MOF'
file_name = "clean_test.txt"
complete_name = os.path.join(save_path, file_name)
print(complete_name)

test_file = open(complete_name, "w", encoding='utf-8')
test_file.write(clean_acs)
test_file.close()





