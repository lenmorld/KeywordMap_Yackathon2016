from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="04-oPqIVQE085yKYHNpn9Q",
    consumer_secret="4bRs-oBARaBFfQdAWgjTdhdJXPU",
    token="ec7SmRYyo8kAR6wNgeHwOTvITzC1jYAi",
    token_secret="Uu9qBWo7olB6lmp2nsQ9g0xHSPE"
)

client = Client(auth)

params = {
    'term': 'food',
    'lang': 'fr'
}

response = client.search('San Francisco', **params)

print(response.businesses)

print("============================")

print(response.businesses[0].name)
print(response.businesses[1].name)
print(response.businesses[1].rating)
