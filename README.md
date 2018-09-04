1.  Functions of each document
    
    All the documents start with "example" run on the example dataset.

    main document: example_search.py (search.py) example_tagging.py (tagging.py)
    
    example_search.py (search.py):
    The document builds a search algorithm based on the dataset. Since the json
    in the data set has many different elements. For example, categories, 
    attributes and hours etc. We evaluate weight of each result based on how well
    they match and usually prints out the ten most related results.
    
    example_tagging.py (tagging.py):
    The document takes in the json dataset about reviews, tokenize and parse the
    reviews. Finally pick few words that fit the place best to tag the place. 
    The tags in the dataset weigh a lot during research.
    
    copy_paste.py:
    Since it takes at least five hours to run the tagging process for the whole
    dataset. I use the function to take only around 300,000 reviews from the 
    review dataset so that the time costs to process is about fifteen minutes.
    
    demo.py:
    The document I use to mess around to see what exactly happens for each function.
    
    example_business.json:
    The original dataset about business places without tags.
    
    example_new_business.json:
    The new business dataset created that contains tagging information.
    
    example_review.json:
    The part of review dataset that takes less time for us to tag.
    
    executer.c:
    After compiling the c file, there will be a executable program runs two main
    python functions automatically.
    
    print_info.py:
    The function I use to print out tag and other json information to see whether
    the program is running well.
    
    stopwords.txt:
    An improved version that comes with more stop word compare to the one in MP1.
    
2. For the project, there are basically only two important files, search.py and
tagging.py. In tagging.py, first of all, we take in each line of json file as a 
dictionary and only take the text information in the review part. Then we use 
tokenization method with stopword removal, Length_filter where max is 10 and min
is 2 and lowercase etc. Since tagging only needs one word, we use 1 as the parameter
for the NGramAnalyzer. After tokenization, there are only few words left. We store
the count of word for each place in the dictionary in case there are other people
may use the same words. At the end, based on the number of reviewers, the program
decides how many high frequency words are chosen to be the tag. Then it reads
business.json again, add tag information thus writes into new_business.json. In 
the search function, we took stdin as the key words that users are searching. 
Every time the program gets new key words, it iterates through the dataset to 
evaluate the weight, which represents whether the place is related to the key
words. Every time, the keys in the business information or the words in the 
categories matches the key words, the weight increases by 1. The information in 
the attributes is more significant, therefore the weight increases by 2 every 
time the information matches the key words. Since the tag is the most important 
information since it comes from a lot of people, every time the key word is in 
the tag, the weight of the place would double up. However, we set a condition 
that the weight would only double up when the place is sort of related to the 
key words such as matching categories. After evaluating the weight, we pick the 
top ten places to print its name and address. To avoid printing non-relevant places,
we would stop when the place's weight is 0, which is the condition that usually
happens in a smaller dataset.

3. It is quite easy to run the analyzer. All we need is the dataset written by
json. Then we can run it in the terminal simply by typing './run', then the program
will ask you to type in the dataset of reviews and business dataset that needs to
be updated. Then a new dataset named 'example_new_business.json' will be generated
automatically. Then the search function will ask you to describe to place and then
it starts to give away the results.

4. Each of us finished half part of the project. Yijie Lu figured out the tagging
part so that we get an updated dataset. Yue Yin finished the searching algorithm
so that we have the search engine for searching. And for the documentation, it was
also half half. 