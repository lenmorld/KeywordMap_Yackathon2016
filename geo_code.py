# GEOLOCATION CACHE

# this script uses Google's geolocation API, (by providing a key)
# to map Montreal Postal area codes (e.g. H1A) to latitude, longitude pairs
# this allows us to save the number of geolocation we are allowed per day
# (around 200/day on a free account)

# DONT RUN IT TOO MUCH, ONCE IS PROBABLY ENOUGH
# since geolocation data is unlikely to change

import sys, webbrowser, bs4
import json
import csv
from pprint import pprint
from itertools import islice
import requests


dict = {
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

#note here that dictItems become a pointer to dict, not just a reference
dictItems = dict.items()
data = ""

for dictItem in dictItems:
    #data += str(dictItem[0] + " " + dictItem[1][0])
 
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': str(dictItem[0]), 'key': 'AIzaSyBztqRH0IXenFXQ8S-jWdA1dabJ6Py_H1c'}
    r = requests.get(url, params=params)
    results = r.json()['results']
    if results:
        location = results[0]['geometry']['location']
        dictItem[1][1] = location['lat']
        dictItem[1][2] = location['lng']
    #else:
        #tempDict['Lat'] = 0.0
        #tempDict['Long'] = 0.0      
 
    
#print(data)

#write results to a file    
with open('geo.json', 'w') as outfile:
    json.dump(dict, outfile)