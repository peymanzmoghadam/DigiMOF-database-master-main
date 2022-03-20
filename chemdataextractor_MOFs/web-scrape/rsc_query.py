import pandas as pd
from rsc import *


tmp = pd.DataFrame()

#Executes the search query "Metal Organic Framework" on the RSC website and stores all the DOIs in df
for n in range(500):
    dois = [get_doi("Metal organic framework", n)]
    df = pd.DataFrame(dois).transpose()
    tmp = tmp.append(df)

#All the dois are added to a csv file
tmp.to_csv('MOF-dois.csv', index=False, header = ['dois'])


