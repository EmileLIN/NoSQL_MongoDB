"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        
        gooddata =list()
        baddata = list()
        
        #COMPLETE THIS FUNCTION
        for line in reader:
             valid = True
             startYear = line["productionStartYear"]
             url = line["URI"]
                
             if re.search('^http://dbpedia.org/resource/.*',url) == None:
                    continue
                
                
             #Look if this field contains a year
             res = re.search('^(\d{4})-\d{2}.*',startYear)
             if res == None:
                  valid = False
             else:
                  year = res.group(1)
                       
                  #Look if year is between 1886 and 2014
                  if (int(year) >= 1886) and (int(year) <= 2014):
                            line["productionStartYear"] = year
                  else:
                            valid = False
             
             if valid == True:
                  gooddata.append(line)
             else:
                  baddata.append(line)
         


    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in gooddata:
             writer.writerow(row)

    with open(output_bad, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in baddata:
             writer.writerow(row)

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()