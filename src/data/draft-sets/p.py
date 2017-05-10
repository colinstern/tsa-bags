import csv
with open('test-set-unflattened.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile)
	data = list(spamreader)
	for row in data:
		print(row)
