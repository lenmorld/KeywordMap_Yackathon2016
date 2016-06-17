#! python3

import sys
import json
import csv

#need a function check if address contains a given postal code string
def hasPostal( postal, address ):
    if postal not in address:
        return False
    else:
        return True

#need a function check if address contains a given avenue/stree string
def hasStreet( street, address ):
    if street.lower() not in address.lower():
        return False
    else:
        return True


#number of results obtained (from the dataset) at this moment
N=1724
#num of accidents
M=7000
#num of Areas
Z=121


# 0_0_0.json is generated from apache_drill.sql
# apache_drill treats the (gigantic) dataset as a DB that we can query
# might have to rerun it for accuracy
# refer to "apache_drill.sql"

with open('./output4/0_0_0.json', encoding="utf8") as data_file:
    data = json.load(data_file)

dict = {'H1A' : 'Pointe Aux Tremblay' ,
 'H2A' : 'Saint-Michel' ,
 'H3A' : 'Downtown Montréal North' ,
 'H4A' : ' Notre-Dame-de-Grâce Northeas' ,
 'H5A' : ' Place Bonaventure' ,
 'H7A' : 'Duvernay-Est' ,
 'H9A' : 'Dollard-des-Ormeaux Northwest' ,
 'H1B' : 'Montreal East' ,
 'H2B' : 'Ahuntsic North' ,
 'H3B' : 'Downtown Montreal East' ,
 'H4B' : 'Notre-Dame-de-Grâce Southwest' ,
 'H5B' : 'Place Desjardins' ,
 'H7B' : 'Saint-François' ,
 'H9B' : 'Dollard-des-Ormeaux' ,
 'H1C' : 'Rivière-des-Prairies Northeast' ,
 'H2C' : 'Ahuntsic Central' ,
 'H3C' : 'Griffintown' ,
 'H4C' : 'Saint-Henri' ,
 'H7C' : 'Saint-Vincent-de-Paul' ,
 'H9C' : "L'Île-Bizard Northeast" ,
 'H1E' : 'Rivière-des-Prairies Southwest' ,
 'H2E' : 'Villeray Northeast' ,
 'H3E' : "LÎle-Des-Soeurs" ,
 'H4E' : 'Ville Émard' ,
 'H7E' : 'Duvernay' ,
 'H9E' : "L'Île-Bizard Southwest" ,
 'H1G' : 'Montréal-Nord North' ,
 'H2G' : 'Petite-Patrie Northeast' ,
 'H3G' : 'Downtown Montreal Southeast (Concordia University)' ,
 'H4G' : 'Verdun North' ,
 'H7G' : 'Pont-Viau' ,
 'H9G' : 'Dollard-des-Ormeaux Southwest' ,
 'H1H' : 'Montréal-Nord South' ,
 'H2H' : 'Plateau Mont-Royal North' ,
 'H3H' : 'Downtown Montreal Southwest' ,
 'H4H' : 'Verdun South' ,
 'H7H' : 'Auteil West' ,
 'H9H' : 'Sainte-Geneviève / Pierrefonds' ,
 'H1J' : 'Anjou West' ,
 'H2J' : 'Plateau Mont-Royal North Central' ,
 'H3J' : 'Petite-Bourgogne' ,
 'H4J' : 'Cartierville Central' ,
 'H7J' : 'Auteuil Northeast' ,
 'H9J' : 'Kirkland' ,
 'H1K' : 'Anjou East' ,
 'H2K' : 'Centre-Sud North' ,
 'H3K' : 'Pointe-Saint-Charles' ,
 'H4K' : 'Cartierville Southwest' ,
 'H7K' : 'Auteuil South' ,
 'H9K' : 'Senneville' ,
 'H1L' : 'Mercier North' ,
 'H2L' : 'Centre-Sud South' ,
 'H3L' : 'Ahuntsic Southwest' ,
 'H4L' : 'Saint-Laurent Inner Northeast' ,
 'H7L' : "Sainte-Rose" ,
 'H1M' : 'Mercier West' ,
 'H2M' : 'Ahuntsic East' ,
 'H3M' : 'Cartierville Northeast' ,
 'H4M' : 'Saint-Laurent East' ,
 'H7M' : 'Vimont' ,
 'H1N' : 'Mercier Southeast' ,
 'H2N' : 'Ahuntsic Southeast' ,
 'H3N' : 'Parc-Extension ' ,
 'H4N' : 'Saint-Laurent Outer Northeast' ,
 'H7N' : 'Laval-des-Rapides' ,
 'H8N' : 'LaSalle Northwest' ,
 'H1P' : 'Saint-Léonard North' ,
 'H2P' : 'Villeray West' ,
 'H3P' : 'Mount Royal North' ,
 'H4P' : 'Mount Royal South' ,
 'H7P' : 'Fabreville' ,
 'H8P' : 'LaSalle Southeast' ,
 'H9P' : 'Dorval Outskirts' ,
 'H1R' : 'Saint-Léonard West' ,
 'H2R' : 'Villeray Southeast' ,
 'H3R' : 'Mount Royal Central' ,
 'H4R' : 'Saint-LaurentCentral' ,
 'H7R' : 'Laval-sur-le-Lac' ,
 'H8R' : 'Ville Saint-Pierre' ,
 'H9R' : 'Pointe-Claire',
  'H1S' : 'Saint-Léonard Southeast',
  'H2S' : 'Petite-Patrie Southwest',
  'H3S' : 'Côte-des-Neiges North',
  'H4S' : 'Saint-Laurent Southwest',
  'H7S' : 'Chomedey Northeast',
  'H8S' : 'Lachine East',
  'H9S' : "Dorval / L'Île-Dorval",
  'H1T' : 'Rosemont North',
  'H2T' : 'Plateau Mont-Royal West',
  'H3T' : 'Côte-des-Neiges Northeast',
  'H4T' : 'Saint-Laurent Southeast',
  'H7T' : 'Chomedey Northwest',
  'H8T' : 'Lachine West',
  'H1V' : 'Maisonneuve',
  'H2V' : 'Outremont',
  'H3V' : 'Côte-des-Neiges East',
  'H4V' : 'Côte Saint-Luc East',
  'H7V' : 'Chomedey East',
  'H1W' : 'Hochelaga',
  'H2W' : 'Plateau Mont-Royal South Central',
  'H3W' : 'Côte-des-Neiges Southwest',
  'H4W' : 'Côte Saint-Luc West',
  'H7W' : 'Chomedey South',
  'H9W' : 'Beaconsfield',
  'H1X' : 'Rosemont Central',
  'H2X' : 'Plateau Mont-Royal Southeast',
  'H3X' : 'Hampstead / Côte Saint-Luc',
  'H4X' : 'Montreal West',
  'H7X' : 'Sainte-Dorothée',
  'H9X' : 'Sainte-Anne-De-Bellevue',
  'H1Y' : 'Rosemont South',
  'H2Y' : 'Old Montreal',
  'H3Y' : 'Westmount North',
  'H4Y' : 'Dorval Central (YUL)',
  'H7Y' : 'Îles-Laval',
  'H8Y' : 'Roxboro',
  'H1Z' : 'Saint-Michel West',
  'H2Z' : 'Downtown Montreal Northeast',
  'H3Z' : 'Westmount South',
  'H4Z' : 'Tour de la Bourse',
  'H8Z' : 'Pierrefonds',
        }

dictKeyword = {'H1A' : 0 ,
 'H2A' : 0,
 'H3A' : 0,
 'H4A' : 0,
 'H5A' : 0,
 'H7A' : 0,
 'H9A' : 0,
 'H1B' : 0,
 'H2B' : 0,
 'H3B' : 0,
 'H4B' : 0,
 'H5B' : 0,
 'H7B' : 0,
 'H9B' : 0,
 'H1C' : 0,
 'H2C' : 0,
 'H3C' : 0,
 'H4C' : 0,
 'H7C' : 0,
 'H9C' : 0,
 'H1E' : 0,
 'H2E' : 0,
 'H3E' : 0,
 'H4E' : 0,
 'H7E' : 0,
 'H9E' : 0,
 'H1G' : 0,
 'H2G' : 0,
 'H3G' : 0,
 'H4G' : 0,
 'H7G' : 0,
 'H9G' : 0,
 'H1H' : 0,
 'H2H' : 0,
 'H3H' : 0,
 'H4H' : 0,
 'H7H' : 0,
 'H9H' : 0,
 'H1J' : 0,
 'H2J' : 0,
 'H3J' : 0,
 'H4J' : 0,
 'H7J' : 0,
 'H9J' : 0,
 'H1K' : 0,
 'H2K' : 0,
 'H3K' : 0,
 'H4K' : 0,
 'H7K' : 0,
 'H9K' : 0,
 'H1L' : 0,
 'H2L' : 0,
 'H3L' : 0,
 'H4L' : 0,
 'H7L' : 0,
 'H1M' : 0,
 'H2M' : 0,
 'H3M' : 0,
 'H4M' : 0,
 'H7M' : 0,
 'H1N' : 0,
 'H2N' : 0,
 'H3N' : 0,
 'H4N' : 0,
 'H7N' : 0,
 'H8N' : 0,
 'H1P' : 0,
 'H2P' : 0,
 'H3P' : 0,
 'H4P' : 0,
 'H7P' : 0,
 'H8P' : 0,
 'H9P' : 0,
 'H1R' : 0,
 'H2R' : 0,
 'H3R' : 0,
 'H4R' : 0,
 'H7R' : 0,
 'H8R' : 0,
 'H9R' : 0,
  'H1S' : 0,
  'H2S' : 0,
  'H3S' : 0,
  'H4S' : 0,
  'H7S' : 0,
  'H8S' : 0,
  'H9S' : 0,
  'H1T' : 0,
  'H2T' : 0,
  'H3T' : 0,
  'H4T' : 0,
  'H7T' : 0,
  'H8T' : 0,
  'H1V' : 0,
  'H2V' : 0,
  'H3V' : 0,
  'H4V' : 0,
  'H7V' : 0,
  'H1W' : 0,
  'H2W' : 0,
  'H3W' : 0,
  'H4W' : 0,
  'H7W' : 0,
  'H9W' : 0,
  'H1X' : 0,
  'H2X' : 0,
  'H3X' : 0,
  'H4X' : 0,
  'H7X' : 0,
  'H9X' : 0,
  'H1Y' : 0,
  'H2Y' : 0,
  'H3Y' : 0,
  'H4Y' : 0,
  'H7Y' : 0,
  'H8Y' : 0,
  'H1Z' : 0,
  'H2Z' : 0,
  'H3Z' : 0,
  'H4Z' : 0,
  'H8Z' : 0
        }

######## ACCIDENTS ##################
accidentAreas = []

with open('./CAR-CRASHES-2007.csv') as csvfile:
    data2 = csv.DictReader(csvfile)
    for row2 in data2:
        accidentAreas.append(row2['RUE_ACCDN'])

bikeAccidentAreas = []

with open('./Montreal bike collisions 2006-10 - Refined.csv') as csvfile:
    data4 = csv.DictReader(csvfile)
    for row4 in data4:
        bikeAccidentAreas.append(row4['Street of accident'])
        bikeAccidentAreas.append(row4['Corner street'])

pedestrianAccidentAreas = []

with open('./Pedestrian-accidents-2007-REFINED.csv') as csvfile:
    data5 = csv.DictReader(csvfile)
    for row5 in data5:
        bikeAccidentAreas.append(row5['STREET OF ACCIDENT'])
        bikeAccidentAreas.append(row5['INTERSECTION'])


########### WEATHER #############
weather = []

with open('./weather2015.csv') as csvfile:
    data3 = csv.DictReader(csvfile)
    for row3 in data3:
        if (row3['Tm'] != '' ):
            weather.append( row3['Tm'] )


accidentPerArea = {'H1A' : 0 ,
 'H2A' : 0,
 'H3A' : 0,
 'H4A' : 0,
 'H5A' : 0,
 'H7A' : 0,
 'H9A' : 0,
 'H1B' : 0,
 'H2B' : 0,
 'H3B' : 0,
 'H4B' : 0,
 'H5B' : 0,
 'H7B' : 0,
 'H9B' : 0,
 'H1C' : 0,
 'H2C' : 0,
 'H3C' : 0,
 'H4C' : 0,
 'H7C' : 0,
 'H9C' : 0,
 'H1E' : 0,
 'H2E' : 0,
 'H3E' : 0,
 'H4E' : 0,
 'H7E' : 0,
 'H9E' : 0,
 'H1G' : 0,
 'H2G' : 0,
 'H3G' : 0,
 'H4G' : 0,
 'H7G' : 0,
 'H9G' : 0,
 'H1H' : 0,
 'H2H' : 0,
 'H3H' : 0,
 'H4H' : 0,
 'H7H' : 0,
 'H9H' : 0,
 'H1J' : 0,
 'H2J' : 0,
 'H3J' : 0,
 'H4J' : 0,
 'H7J' : 0,
 'H9J' : 0,
 'H1K' : 0,
 'H2K' : 0,
 'H3K' : 0,
 'H4K' : 0,
 'H7K' : 0,
 'H9K' : 0,
 'H1L' : 0,
 'H2L' : 0,
 'H3L' : 0,
 'H4L' : 0,
 'H7L' : 0,
 'H1M' : 0,
 'H2M' : 0,
 'H3M' : 0,
 'H4M' : 0,
 'H7M' : 0,
 'H1N' : 0,
 'H2N' : 0,
 'H3N' : 0,
 'H4N' : 0,
 'H7N' : 0,
 'H8N' : 0,
 'H1P' : 0,
 'H2P' : 0,
 'H3P' : 0,
 'H4P' : 0,
 'H7P' : 0,
 'H8P' : 0,
 'H9P' : 0,
 'H1R' : 0,
 'H2R' : 0,
 'H3R' : 0,
 'H4R' : 0,
 'H7R' : 0,
 'H8R' : 0,
 'H9R' : 0,
  'H1S' : 0,
  'H2S' : 0,
  'H3S' : 0,
  'H4S' : 0,
  'H7S' : 0,
  'H8S' : 0,
  'H9S' : 0,
  'H1T' : 0,
  'H2T' : 0,
  'H3T' : 0,
  'H4T' : 0,
  'H7T' : 0,
  'H8T' : 0,
  'H1V' : 0,
  'H2V' : 0,
  'H3V' : 0,
  'H4V' : 0,
  'H7V' : 0,
  'H1W' : 0,
  'H2W' : 0,
  'H3W' : 0,
  'H4W' : 0,
  'H7W' : 0,
  'H9W' : 0,
  'H1X' : 0,
  'H2X' : 0,
  'H3X' : 0,
  'H4X' : 0,
  'H7X' : 0,
  'H9X' : 0,
  'H1Y' : 0,
  'H2Y' : 0,
  'H3Y' : 0,
  'H4Y' : 0,
  'H7Y' : 0,
  'H8Y' : 0,
  'H1Z' : 0,
  'H2Z' : 0,
  'H3Z' : 0,
  'H4Z' : 0,
  'H8Z' : 0
        }

weatherPerArea = {'H1A' : 0 ,
 'H2A' : 0,
 'H3A' : 0,
 'H4A' : 0,
 'H5A' : 0,
 'H7A' : 0,
 'H9A' : 0,
 'H1B' : 0,
 'H2B' : 0,
 'H3B' : 0,
 'H4B' : 0,
 'H5B' : 0,
 'H7B' : 0,
 'H9B' : 0,
 'H1C' : 0,
 'H2C' : 0,
 'H3C' : 0,
 'H4C' : 0,
 'H7C' : 0,
 'H9C' : 0,
 'H1E' : 0,
 'H2E' : 0,
 'H3E' : 0,
 'H4E' : 0,
 'H7E' : 0,
 'H9E' : 0,
 'H1G' : 0,
 'H2G' : 0,
 'H3G' : 0,
 'H4G' : 0,
 'H7G' : 0,
 'H9G' : 0,
 'H1H' : 0,
 'H2H' : 0,
 'H3H' : 0,
 'H4H' : 0,
 'H7H' : 0,
 'H9H' : 0,
 'H1J' : 0,
 'H2J' : 0,
 'H3J' : 0,
 'H4J' : 0,
 'H7J' : 0,
 'H9J' : 0,
 'H1K' : 0,
 'H2K' : 0,
 'H3K' : 0,
 'H4K' : 0,
 'H7K' : 0,
 'H9K' : 0,
 'H1L' : 0,
 'H2L' : 0,
 'H3L' : 0,
 'H4L' : 0,
 'H7L' : 0,
 'H1M' : 0,
 'H2M' : 0,
 'H3M' : 0,
 'H4M' : 0,
 'H7M' : 0,
 'H1N' : 0,
 'H2N' : 0,
 'H3N' : 0,
 'H4N' : 0,
 'H7N' : 0,
 'H8N' : 0,
 'H1P' : 0,
 'H2P' : 0,
 'H3P' : 0,
 'H4P' : 0,
 'H7P' : 0,
 'H8P' : 0,
 'H9P' : 0,
 'H1R' : 0,
 'H2R' : 0,
 'H3R' : 0,
 'H4R' : 0,
 'H7R' : 0,
 'H8R' : 0,
 'H9R' : 0,
  'H1S' : 0,
  'H2S' : 0,
  'H3S' : 0,
  'H4S' : 0,
  'H7S' : 0,
  'H8S' : 0,
  'H9S' : 0,
  'H1T' : 0,
  'H2T' : 0,
  'H3T' : 0,
  'H4T' : 0,
  'H7T' : 0,
  'H8T' : 0,
  'H1V' : 0,
  'H2V' : 0,
  'H3V' : 0,
  'H4V' : 0,
  'H7V' : 0,
  'H1W' : 0,
  'H2W' : 0,
  'H3W' : 0,
  'H4W' : 0,
  'H7W' : 0,
  'H9W' : 0,
  'H1X' : 0,
  'H2X' : 0,
  'H3X' : 0,
  'H4X' : 0,
  'H7X' : 0,
  'H9X' : 0,
  'H1Y' : 0,
  'H2Y' : 0,
  'H3Y' : 0,
  'H4Y' : 0,
  'H7Y' : 0,
  'H8Y' : 0,
  'H1Z' : 0,
  'H2Z' : 0,
  'H3Z' : 0,
  'H4Z' : 0,
  'H8Z' : 0
        }

dictItems = dict.items()

reviews_area = {}
i=0

for dictItem in dictItems:
    reviews_area[dictItem[0]] = " "

    weatherPerArea[dictItem[0]] = float(weather[i])

    i = i + 1

    # print (dictItem)
    for num in range(0, N - 1):
        # print("Area:", dictItem[1])
        if hasPostal(dictItem[0], data["results"][num]["full_address"]):
            # concatenate them
            reviews_area[dictItem[0]] = reviews_area[dictItem[0]] + data["results"][num]["text"]

            for x in accidentAreas:
                if hasStreet(x, data["results"][num]["full_address"]):
                    # increase the number of accidents per area if match
                    accidentPerArea[dictItem[0]] = accidentPerArea[dictItem[0]] + 1
                    # print (data["results"][num]["full_address"])
                    # print (row['RUE_ACCDN'])

            for y in bikeAccidentAreas:
                if hasStreet(y, data["results"][num]["full_address"]):
                    # increase the number of accidents per area if match
                    accidentPerArea[dictItem[0]] = accidentPerArea[dictItem[0]] + 1
                    # print (data["results"][num]["full_address"])
                    # print (row['RUE_ACCDN'])

            for z in pedestrianAccidentAreas:
                if hasStreet(z, data["results"][num]["full_address"]):
                    # increase the number of accidents per area if match
                    accidentPerArea[dictItem[0]] = accidentPerArea[dictItem[0]] + 1
                    # print (data["results"][num]["full_address"])
                    # print (row['RUE_ACCDN'])



'''
print("========ACCIDENTS=======")

accidentPerAreaItem = accidentPerArea.items()
for aItem in accidentPerAreaItem:
    print (aItem[0] + " " + str(int(aItem[1]/1000)))

print("========TEMPERATURE=======")

weatherPerAreaItem = weatherPerArea.items()
for wItem in weatherPerAreaItem:
    print (wItem[0] + " " + str(wItem[1]))
'''

dictJSON = {
'H1A' : ['Pointe Aux Tremblay' , 0.0, 0.0 ],
 'H2A' : ['Saint-Michel' , 0.0, 0.0 ],
 'H3A' : ['Downtown Montréal North' , 0.0, 0.0 ],
 'H4A' : [' Notre-Dame-de-Grâce Northeas' , 0.0, 0.0 ],
 'H5A' : [' Place Bonaventure' , 0.0, 0.0 ],
 'H7A' : ['Duvernay-Est' , 0.0, 0.0 ],
 'H9A' : ['Dollard-des-Ormeaux Northwest' , 0.0, 0.0 ],
 'H1B' : ['Montreal East' , 0.0, 0.0 ],
 'H2B' : ['Ahuntsic North' , 0.0, 0.0 ],
 'H3B' : ['Downtown Montreal East' , 0.0, 0.0 ],
 'H4B' : ['Notre-Dame-de-Grâce Southwest' , 0.0, 0.0 ],
 'H5B' : ['Place Desjardins' , 0.0, 0.0 ],
 'H7B' : ['Saint-François' , 0.0, 0.0 ],
 'H9B' : ['Dollard-des-Ormeaux' , 0.0, 0.0 ],
 'H1C' : ['Rivière-des-Prairies Northeast' , 0.0, 0.0 ],
 'H2C' : ['Ahuntsic Central' , 0.0, 0.0 ],
 'H3C' : ['Griffintown' , 0.0, 0.0 ],
 'H4C' : ['Saint-Henri' , 0.0, 0.0 ],
 'H7C' : ['Saint-Vincent-de-Paul' , 0.0, 0.0 ],
 'H9C' : ["L'Île-Bizard Northeast" , 0.0, 0.0 ],
 'H1E' : ['Rivière-des-Prairies Southwest' , 0.0, 0.0 ],
 'H2E' : ['Villeray Northeast' , 0.0, 0.0 ],
 'H3E' : ["LÎle-Des-Soeurs" , 0.0, 0.0 ],
 'H4E' : ['Ville Émard' , 0.0, 0.0 ],
 'H7E' : ['Duvernay' , 0.0, 0.0 ],
 'H9E' : ["L'Île-Bizard Southwest" , 0.0, 0.0 ],
 'H1G' : ['Montréal-Nord North' , 0.0, 0.0 ],
 'H2G' : ['Petite-Patrie Northeast' , 0.0, 0.0 ],
 'H3G' : ['Downtown Montreal Southeast (Concordia University)' , 0.0, 0.0 ],
 'H4G' : ['Verdun North' , 0.0, 0.0 ],
 'H7G' : ['Pont-Viau' , 0.0, 0.0 ],
 'H9G' : ['Dollard-des-Ormeaux Southwest' , 0.0, 0.0 ],
 'H1H' : ['Montréal-Nord South' , 0.0, 0.0 ],
 'H2H' : ['Plateau Mont-Royal North' , 0.0, 0.0 ],
 'H3H' : ['Downtown Montreal Southwest' , 0.0, 0.0 ],
 'H4H' : ['Verdun South' , 0.0, 0.0 ],
 'H7H' : ['Auteil West' , 0.0, 0.0 ],
 'H9H' : ['Sainte-Geneviève / Pierrefonds' , 0.0, 0.0 ],
 'H1J' : ['Anjou West' , 0.0, 0.0 ],
 'H2J' : ['Plateau Mont-Royal North Central' , 0.0, 0.0 ],
 'H3J' : ['Petite-Bourgogne' , 0.0, 0.0 ],
 'H4J' : ['Cartierville Central' , 0.0, 0.0 ],
 'H7J' : ['Auteuil Northeast' , 0.0, 0.0 ],
 'H9J' : ['Kirkland' , 0.0, 0.0 ],
 'H1K' : ['Anjou East' , 0.0, 0.0 ],
 'H2K' : ['Centre-Sud North' , 0.0, 0.0 ],
 'H3K' : ['Pointe-Saint-Charles' , 0.0, 0.0 ],
 'H4K' : ['Cartierville Southwest' , 0.0, 0.0 ],
 'H7K' : ['Auteuil South' , 0.0, 0.0 ],
 'H9K' : ['Senneville' , 0.0, 0.0 ],
 'H1L' : ['Mercier North' , 0.0, 0.0 ],
 'H2L' : ['Centre-Sud South' , 0.0, 0.0 ],
 'H3L' : ['Ahuntsic Southwest' , 0.0, 0.0 ],
 'H4L' : ['Saint-Laurent Inner Northeast' , 0.0, 0.0 ],
 'H7L' : ["Sainte-Rose" , 0.0, 0.0 ],
 'H1M' : ['Mercier West' , 0.0, 0.0 ],
 'H2M' : ['Ahuntsic East' , 0.0, 0.0 ],
 'H3M' : ['Cartierville Northeast' , 0.0, 0.0 ],
 'H4M' : ['Saint-Laurent East' , 0.0, 0.0 ],
 'H7M' : ['Vimont' , 0.0, 0.0 ],
 'H1N' : ['Mercier Southeast' , 0.0, 0.0 ],
 'H2N' : ['Ahuntsic Southeast' , 0.0, 0.0 ],
 'H3N' : ['Parc-Extension ' , 0.0, 0.0 ],
 'H4N' : ['Saint-Laurent Outer Northeast' , 0.0, 0.0 ],
 'H7N' : ['Laval-des-Rapides' , 0.0, 0.0 ],
 'H8N' : ['LaSalle Northwest' , 0.0, 0.0 ],
 'H1P' : ['Saint-Léonard North' , 0.0, 0.0 ],
 'H2P' : ['Villeray West' , 0.0, 0.0 ],
 'H3P' : ['Mount Royal North' , 0.0, 0.0 ],
 'H4P' : ['Mount Royal South' , 0.0, 0.0 ],
 'H7P' : ['Fabreville' , 0.0, 0.0 ],
 'H8P' : ['LaSalle Southeast' , 0.0, 0.0 ],
 'H9P' : ['Dorval Outskirts' , 0.0, 0.0 ],
 'H1R' : ['Saint-Léonard West' , 0.0, 0.0 ],
 'H2R' : ['Villeray Southeast' , 0.0, 0.0 ],
 'H3R' : ['Mount Royal Central' , 0.0, 0.0 ],
 'H4R' : ['Saint-LaurentCentral' , 0.0, 0.0 ],
 'H7R' : ['Laval-sur-le-Lac' , 0.0, 0.0 ],
 'H8R' : ['Ville Saint-Pierre' , 0.0, 0.0 ],
 'H9R' : ['Pointe-Claire' , 0.0, 0.0 ],
  'H1S' : ['Saint-Léonard Southeast' , 0.0, 0.0 ],
  'H2S' : ['Petite-Patrie Southwest' , 0.0, 0.0 ],
  'H3S' : ['Côte-des-Neiges North' , 0.0, 0.0 ],
  'H4S' : ['Saint-Laurent Southwest' , 0.0, 0.0 ],
  'H7S' : ['Chomedey Northeast' , 0.0, 0.0 ],
  'H8S' : ['Lachine East' , 0.0, 0.0 ],
  'H9S' : ["Dorval / L'Île-Dorval" , 0.0, 0.0 ],
  'H1T' : ['Rosemont North' , 0.0, 0.0 ],
  'H2T' : ['Plateau Mont-Royal West' , 0.0, 0.0 ],
  'H3T' : ['Côte-des-Neiges Northeast' , 0.0, 0.0 ],
  'H4T' : ['Saint-Laurent Southeast' , 0.0, 0.0 ],
  'H7T' : ['Chomedey Northwest' , 0.0, 0.0 ],
  'H8T' : ['Lachine West' , 0.0, 0.0 ],
  'H1V' : ['Maisonneuve' , 0.0, 0.0 ],
  'H2V' : ['Outremont' , 0.0, 0.0 ],
  'H3V' : ['Côte-des-Neiges East' , 0.0, 0.0 ],
  'H4V' : ['Côte Saint-Luc East' , 0.0, 0.0 ],
  'H7V' : ['Chomedey East' , 0.0, 0.0 ],
  'H1W' : ['Hochelaga' , 0.0, 0.0 ],
  'H2W' : ['Plateau Mont-Royal South Central' , 0.0, 0.0 ],
  'H3W' : ['Côte-des-Neiges Southwest' , 0.0, 0.0 ],
  'H4W' : ['Côte Saint-Luc West' , 0.0, 0.0 ],
  'H7W' : ['Chomedey South' , 0.0, 0.0 ],
  'H9W' : ['Beaconsfield' , 0.0, 0.0 ],
  'H1X' : ['Rosemont Central' , 0.0, 0.0 ],
  'H2X' : ['Plateau Mont-Royal Southeast' , 0.0, 0.0 ],
  'H3X' : ['Hampstead / Côte Saint-Luc' , 0.0, 0.0 ],
  'H4X' : ['Montreal West' , 0.0, 0.0 ],
  'H7X' : ['Sainte-Dorothée' , 0.0, 0.0 ],
  'H9X' : ['Sainte-Anne-De-Bellevue' , 0.0, 0.0 ],
  'H1Y' : ['Rosemont South' , 0.0, 0.0 ],
  'H2Y' : ['Old Montreal' , 0.0, 0.0 ],
  'H3Y' : ['Westmount North' , 0.0, 0.0 ],
  'H4Y' : ['Dorval Central (YUL)' , 0.0, 0.0 ],
  'H7Y' : ['Îles-Laval' , 0.0, 0.0 ],
  'H8Y' : ['Roxboro' , 0.0, 0.0 ],
  'H1Z' : ['Saint-Michel West' , 0.0, 0.0 ],
  'H2Z' : ['Downtown Montreal Northeast' , 0.0, 0.0 ],
  'H3Z' : ['Westmount South' , 0.0, 0.0 ],
  'H4Z' : ['Tour de la Bourse' , 0.0, 0.0 ],
  'H8Z' : ['Pierrefonds' , 0.0, 0.0 ],
        }

dictItemsJ = dictJSON.items()
data = ""

for dictItem in dictItemsJ:
    # data += str(dictItem[0] + " " + dictItem[1][0])
    dictItem[1][1] = accidentPerArea[dictItem[0]]
    dictItem[1][2] = weatherPerArea[dictItem[0]]

with open('public_data.json', 'w') as outfile:
    json.dump(dictJSON, outfile)
