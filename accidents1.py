import csv

'''
with open('./CAR-CRASHES-2007.csv') as csvfile:
    data = csv.reader(csvfile, delimiter = ',', quotechar='|')
    for row in data:
        #print (', ' + str(row))
'''

with open('./CAR-CRASHES-2007.csv') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        print (row['RUE_ACCDN'])
        
