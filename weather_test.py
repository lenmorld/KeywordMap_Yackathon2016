import csv

weather = [];

with open('./weather2015.csv') as csvfile:
    data3 = csv.DictReader(csvfile)
    for row3 in data3:
        if (row3['Tm'] != '' ):
            weather.append( row3['Tm'] );


print(weather)
