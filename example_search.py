import os
import ast
import sys
import json
import nltk
import metapy
import operator
from pprint import pprint

# Search Function for the example data set
# Take in input, prints results with name and address

# Count weight
business_info = {}
file_stream = open('example_new_business.json')
for line in file_stream.readlines():
    info = json.loads(line)
    business_info[info['business_id']] = line

for line in sys.stdin:
    if (line == '\n'):
        continue
    weight = {}
    line = line.replace('\n', '')
    words = line.split(' ')
    for text_info in business_info.values():
        js_info = json.loads(text_info)
        weight[js_info['business_id']] = 0;
        is_similar = 0
        attributes = js_info['attributes']
        category = js_info['categories']
        for word in words:
            for keys in attributes:
                if type(attributes[keys]) == dict:
                    for keys_2 in attributes[keys]:
                        if (keys_2.lower() == word.lower() and attributes[keys][keys_2] == True):
                            weight[js_info['business_id']] += 2
                            is_similar = 1
                elif (keys.lower() == word.lower() and attributes[keys] == True):
                    weight[js_info['business_id']] += 2
                    is_similar = 1
            for types in category:
                if (word.lower() in types.lower()):
                    weight[js_info['business_id']] += 1
                    is_similar = 1
            for types in js_info:
                if (word.lower() in types.lower()):
                    weight[js_info['business_id']] += 1
                    is_similar = 1
        if (is_similar == 0):
            continue
        else:
            tags = js_info['tags']
            for word in words:
                if (word in tags):
                    weight[js_info['business_id']] *= 2
    temp = {}
    for elements in sorted(weight.items(), key=operator.itemgetter(1), reverse = True):
        temp[elements[0]] = elements[1]
    weight = temp
    count = 0
    for keys in weight.keys():
        if (weight[keys] == 0):
            print('End of search, only ', count, 'results searched')
            break
        js_info = json.loads(business_info[keys])
        sys.stdout.write(js_info['name'])
        sys.stdout.write(' ')
        sys.stdout.write(js_info['address'])
        sys.stdout.write('\n')
        count += 1
        if (count == 10):
            break
