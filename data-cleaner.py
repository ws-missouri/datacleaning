import csv

# Open our input and output files
csvfile = open('./cleanme.csv', 'r')
cleanfile = open('./consider-it-clean.csv', 'w')

# DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(cleanfile, reader.fieldnames)

# headers
writer.writeheader()

# Clean and write
for row in reader: 
	amount = int(row['amount'])
	if amount < 1000:
		pass
	else:
		row['first_name'] = row['first_name'].upper()
		row['city'] = row['city'].replace("&nbsp;", " ")
		row['zip'] = str(row['zip'].zfill(5))
		writer.writerow(row)