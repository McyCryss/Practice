import os

"""

OBJECTIVE.  To go from:

"TIMESTAMP","PAYLOAD"
"2016-05-04 00:10:22.00","01,F0,ED,01,96,1D,00,34,00,01,FF,DD"
"2016-05-04 00:10:22.01","01,F0,ED,01,96,1D,00,34,00,01,FF,DD"
"2016-05-04 00:10:22.02","01,E7,A0,01,E3,65,00,35,00,01,FF,DD"


To something like:

"TIMESTAMP","PAYLOAD"
"2016-05-04 00:10:22.00","123456","123456","1234","1234","1234"
"2016-05-04 00:10:22.01","123456","123456","1234","1234","1234"
"2016-05-04 00:10:22.02","123456","123456","1234","1234","1234"

i.e.   3 pairs, 3 pairs, 2 pairs, 2 pairs, 2 pairs
e.g.:  01F0ED   01961D   0034     0001     FFDD

"""


dataFilesDir = "./rawData/"
availableDataFiles = os.listdir(dataFilesDir);
availableCSVDataFiles = filter(lambda fn: fn.endswith('csv'), availableDataFiles)

# Will have the keys '.csv', 'Abs.csv', 'Flipped.csv'
groupedCsvFileContents = {}

for csvFileName in list(availableCSVDataFiles):
  groupFileName = csvFileName[:21]
  groupedCsvFileContents.setdefault(groupFileName, {})

  specificFileName = csvFileName[21:]
  with open(dataFilesDir + csvFileName, 'r') as f:
    groupedCsvFileContents[groupFileName][specificFileName] = f.read()


for groupFileName, csvFileContents in groupedCsvFileContents.items():
  # exclude the first line of the file
  rawCsv = csvFileContents['.csv'].split('\n')[1:]
  for row in rawCsv:
    # drop the start and end " character
    row = row[1:len(row)-1]
    if(not row): continue
    parts = row.split('","')
    values = parts[1].split(',')

    ppg = values[0:3]
    ambient = values[3:6]
    accelX = values[6:8]
    accelY = values[8:10]
    accelZ = values[10:12]
    print(row, ppg)

