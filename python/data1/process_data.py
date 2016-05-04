import os

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

