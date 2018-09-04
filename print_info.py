import os
import ast
import sys
import json
import nltk
import metapy
import operator
from pprint import pprint

# Showing tag information

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

file_stream = open('example_new_business.json')

for i in range(10):
    line = file_stream.readline()
    info = json.loads(line)
    if ('tags' in info):
        print(info['tags'])

file_stream.close()
