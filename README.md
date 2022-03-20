# DigiMOF-database-master

Tools for automatically creating a MOF Synthesis Database

Please first install the latest version of ChemDataExtractor

```
conda install -c chemdataextractor chemdataextractor
```

Then install all the packages required:

```
pip install -r requirements.txt
```

### Usage

To automatically extract the data, provide the folder that the XML of HTML files are stored in, the folder where the records will be saved, the starting
and ending index of the articles, and the file name. 

Example:

```
python extract.py '\test' '\save\' 0 1 'raw_data'
```

Once the data is extracted, it can be converted to an Excel file using this online conversion tool: https://www.convertcsv.com/json-to-csv.htm. 

The data can then be visualized by uploading it to Wiz: https://wiz.shef.ac.uk/

