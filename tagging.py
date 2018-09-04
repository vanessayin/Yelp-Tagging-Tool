import os
import sys
import json
import nltk
import metapy
import operator
from pprint import pprint

# Tagging function for the actual whole dataset
# Analyze people's comments over a place, then generate a new json recording business
# information with additional tag information

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

def tokens_lowercase(doc):
    #Write a token stream that tokenizes with ICUTokenizer,
    #lowercases, removes words with less than 2 and more than 5  characters
    #performs stemming and creates trigrams (name the final call to ana.analyze as "trigrams")
    '''Place your code here'''
    tok = metapy.analyzers.ICUTokenizer(suppress_tags = True)
    tok = metapy.analyzers.LengthFilter(tok, min=2, max=10)
    tok = metapy.analyzers.Porter2Filter(tok)
    tok = metapy.analyzers.LowercaseFilter(tok)
    tok = metapy.analyzers.ListFilter(tok, "stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
    ana = metapy.analyzers.NGramWordAnalyzer(1, tok)
    trigrams = ana.analyze(doc)
    #leave the rest of the code as is
    tok.set_content(doc.content())
    tokens, counts = [], []
    for token, count in trigrams.items():
        counts.append(count)
        tokens.append(token)
    return tokens

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

print('Please select the review dataset you would like to analyze')
review_name = sys.stdin.readline()
review_name = review_name.replace('\n', '')

print('Please select the business dataset you would like to update')
business_name = sys.stdin.readline()
business_name = business_name.replace('\n', '')

total_review = {}
file_stream = open(review_name)
output_stream = open('new_business.json', 'w+')
for line in file_stream.readlines():
    review = json.loads(line, object_hook = JSONObject)
    doc = metapy.index.Document()
    doc.content(review.text)
    tokens = tokens_lowercase(doc)
    tokens = nltk.pos_tag(tokens)
    review_words = {}
    if review.business_id in total_review:
        review_words = total_review[review.business_id]
    for word in tokens:
        if (word[1] == 'JJ'):
            if (word[0] in review_words):
                review_words[word[0]] += 1
            else:
                review_words[word[0]] = 1
    total_review[review.business_id] = review_words

business_id_list = total_review.keys()
for key in business_id_list:
    temp = {}
    for elements in sorted(total_review[key].items(), key=operator.itemgetter(1), reverse = True):
        temp[elements[0]] = elements[1]
    total_review[key] = temp

business_stream = open(business_name)
for line in business_stream.readlines():
    business_info = json.loads(line)
    if (business_info['business_id'] not in total_review):
        continue
    business_tag_words = total_review[business_info['business_id']]
    business_tag_words_keys = business_tag_words.keys()
    count = 0
    maximum = 0
    review_count = business_info['review_count']
    if (review_count < 10):
        maximum = 1
    elif (review_count > 10 and review_count < 50):
        maximum = 2
    elif (review_count > 50 and review_count < 100):
        maximum = 3
    elif (review_count > 100 and review_count < 500):
        maximum = 4
    else:
        maximum = 5

    new_tag = []
    for tag_word in business_tag_words_keys:
        if (count >= maximum):
            break
        new_tag.append(tag_word)
        count += 1
    business_info['tags'] = new_tag
    output_stream.write(json.dumps(business_info))
    output_stream.write('\n')
file_stream.close()
output_stream.close()
