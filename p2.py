import json
from pprint import pprint
from itertools import islice

#with open('yelp_academic_dataset_review.json') as data_file:    
#    data = json.load(data_file)

#with open("yelp_academic_dataset_review.json") as myfile:
#   head = [next(myfile) for x in xrange(100)]
#print (head)


with open("yelp_academic_dataset_review.json") as myfile:
    #head = list(islice(myfile, 5))
    contents = myfile.read()
    result = json.loads(contents)

print(result)
    




#pprint(data)

#data["maps"][0]["id"]
#data["masks"]["id"]
#data["om_points"]
