from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from gensim import corpora, models
import gensim
import os
import re

# Documents array
docs = []

# Preprocessing
path = "/home/mark/temp/articles/"

for filename in os.listdir(path):
    with open(path + filename, "r") as article_file:
        article_text = article_file.read().replace("\n", "")
        remove_html_tags = re.compile("<.*?>")
        articles_text_stripped = re.sub(remove_html_tags, " ", article_text)
        docs.append(articles_text_stripped)

# Stop words
stopswords = []
with open("../resources/stopwords.txt") as stopwords_file:
    stopwords = stopwords_file.read().splitlines()

# Tokenizer for creating word tokens
tokenizer = RegexpTokenizer(r'\w+')

# Stemmer for the danish language
stemmer = SnowballStemmer("danish")


texts = []

for i in docs:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    stopped_tokens = [i for i in tokens if not i in stopwords]

    #stemmed_tokens = [stemmer.stem(i) for i in stopped_tokens]

    texts.append(stopped_tokens)


dic = corpora.Dictionary(texts)

corpus = [dic.doc2bow(text) for text in texts]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=15, id2word = dic, passes=30)


# print result
print(ldamodel.print_topics(num_topics = 15, num_words = 5))
