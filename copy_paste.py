import json
from pprint import pprint
from collections import OrderedDict
import sys
import os
import metapy

# Copy part of the actual dataset to create example dataset

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

os.chdir('dataset')
file_stream = open('review.json')
output = open('example_review.json', 'w+')

for i in range(10000):
    output.write(file_stream.readline())

file_stream.close()
output.close()
