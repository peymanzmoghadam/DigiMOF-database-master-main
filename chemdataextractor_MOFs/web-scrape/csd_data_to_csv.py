from ccdc.io import EntryReader
import pandas as pd
import numpy as np
csd_reader = EntryReader('CSD')

df = pd.read_csv('PATH TO CSV')
data = []
for refcode in df['Ref Codes']:
    values_dict = {'Ref Code' : csd_reader.entry(refcode).identifier,
                   'Chemical Name': csd_reader.entry(refcode).chemical_name,
                   'Chemical Formula': csd_reader.entry(refcode).formula,
                    'Solvent' : csd_reader.entry(refcode).solvent,
                   'Pressure': csd_reader.entry(refcode).pressure,
                   'Temperature': csd_reader.entry(refcode).temperature,
                   'Melting Point': csd_reader.entry(refcode).melting_point,
                   'Density': csd_reader.entry(refcode).calculated_density,
                   'DOI' : csd_reader.entry(refcode).publication.doi,
                   'Journal': csd_reader.entry(refcode).publication.journal,
                   'Publication' : csd_reader.entry(refcode).publication,
                   'Molecule' : csd_reader.entry(refcode).crystal.molecule
                   }
    data.append(values_dict)

data_df = pd.DataFrame(data).fillna('None')
data_df.to_csv('all_MOFs.csv')

