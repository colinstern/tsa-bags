import csv
with open('claims-data-2015-as-of-feb-9-2016-ADDEDLATLONG.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	data = list(spamreader)
	for row in data:
		print(row)
