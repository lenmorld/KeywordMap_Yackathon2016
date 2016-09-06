from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="04-oPqIVQE085yKYHNpn9Q",
    consumer_secret="4bRs-oBARaBFfQdAWgjTdhdJXPU",
    token="ec7SmRYyo8kAR6wNgeHwOTvITzC1jYAi",
    token_secret="Uu9qBWo7olB6lmp2nsQ9g0xHSPE"
)

client = Client(auth)

#look for Montreal restaurants
#english reviews


params = {
    'term': 'restaurants',
    'lang': 'en'
}

response = client.search('Montreal', **params)

#get their ID

####response.businesses[0].id

print(response.businesses[0].id)

str1 = str(response.businesses[0].id)

#get reviews for this business-id

params_b = {
         'lang' : 'en'
    }

response_b = client.get_business(str1, **params)

#print(response_b.reviews)

'''   
response = client.get_business('yelp-san-francisco', **params)

print(response)
print(response.business.name)
print(response.business.categories)
'''
