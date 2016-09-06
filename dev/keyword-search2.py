#! python3

import requests, sys, webbrowser, bs4
import json
import csv
from pprint import pprint
from itertools import islice

#+ (sys.argv[1:])
#print ("PYTHON is working " + str(sys.argv[1:]))

keyword = str(sys.argv[1:])

keyword = keyword.replace("[", "")
keyword = keyword.replace("]", "")
keyword = keyword.replace("'", "")

print(str)