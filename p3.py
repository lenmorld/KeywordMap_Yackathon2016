import json
from pprint import pprint
from itertools import islice

'''
{
  "full_address" : "5185, rue Charleroi\nMontréal-Nord\nMontreal-Nord, QC H1G 3A2",
  "name" : "Da Bologna",
  "text" : "Good default order-in type of place.\n\nA bit on the pricey side when you can get a 2 for1 pizza for $30,
  feeding a family of 4 will cost you about $15-$20 per person.\n\nThe food and delivery time are always spot-on.
  I've been a regular for the last 5 years, my last order was a few nights ago.\n\nMy favorite dish: the veal parmegiana with any pasta rose.
  All dressed pizza with extra mushrooms, well done. Yum!"
} 
'''


#need a function check if address contains a given postal code string
def hasPostal( postal, address ):
    if postal not in address:
        return False
    else:
        return True

#####################################################


#number of results obtained (from the dataset) at this moment
N=100 
numOfAreas=3

with open('./output3/0_0_0.json') as data_file:    
    data = json.load(data_file)

#pprint(data)


#H1A, Pointe-aux-Trembles



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
        };



dictWordRank = {'H1A' : 'Pointe Aux Tremblay' , 
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
        }; 

dictItems = dict.items()
#print (dict['H2L'], dict['H3L'])


#print "dict['H2L']: "

#init Review-Area dictionary

reviews_area = {}

for dictItem in dictItems:
    reviews_area[dictItem[0]] = " "
    #print (dictItem)
    for num in range(0,N-1):
        #print("Area:", dictItem[1])
        if hasPostal(dictItem[0], data["results"][num]["full_address"]):
            #--->print("Postal:", dictItem[0])
            #then we need to group this review for this area
            #concatenate them
            reviews_area[dictItem[0]] = reviews_area[dictItem[0]]  + data["results"][num]["text"]
            #print ("=======================")
            #print(dictItem[0])
            #print(reviews_area[dictItem[0]])
            #--->print(reviews_area[dictItem[0]])
            #also do calculations here
            #initialize words
            #dictWordRank[dictItem[0]]
            #print(dictItem[0])
            
#---------------->
#now we have dict. of review-area
#we have to get keyword and count the frequency of each one

for key in reviews_area:
    print (key +  'correspods to' + reviews_area[key])
    print ("=======================")

for dictItem in dictItems:
    #dictWordRank[dictItem[0]] = "good_great_amazing_bad_worst";
    string = reviews_area[dictItem[0]]
    good = string.count("good")
    great = string.count("great")
    awesome = string.count("awesome")
    bad = string.count("bad")
    worst = string.count("worst")
    
    print(dictItem[0] + " " + str(good) + "_" + str(great) + "_" + str(awesome) + "_" + str(bad)+ "_" + str(worst))


'''
for num in range(0,10):
    print(hasPostal('H2L', ' dasdasdas H2L dasdas'))
    print(data["results"][num]["full_address"])
'''


