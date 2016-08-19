from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from gensim import models
from gensim.corpora import Dictionary, MmCorpus
import gensim
import pyLDAvis.gensim as gensimvis
import pyLDAvis
import os
import re

# Documents array
articles = []

# Preprocessing
path = "/home/mark/temp/articles/"

for filename in os.listdir(path):
    with open(path + filename, "r") as article_file:
        article_text = article_file.read().replace("\n", "")
        remove_html_tags = re.compile("<.*?>")
        articles_text_stripped = re.sub(remove_html_tags, " ", article_text)
        articles.append(articles_text_stripped)

# Stop words
stopswords = []
with open("../resources/stopwords.txt") as stopwords_file:
    stopwords = stopwords_file.read().splitlines()

# Tokenizer for creating word tokens
tokenizer = RegexpTokenizer(r'\w+')

# Stemmer for the danish language
stemmer = SnowballStemmer("danish")


docs = []

for i in articles:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    stopped_tokens = [i for i in tokens if not i in stopwords]

    stemmed_tokens = [stemmer.stem(i) for i in stopped_tokens]

    docs.append(stopped_tokens)


dictionary = Dictionary(docs)
dictionary.compactify()
dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=None)
dictionary.compactify()

corpus = [dictionary.doc2bow(doc) for doc in docs]

MmCorpus.serialize("articles.mm", corpus)
dictionary.save("articles.dict")


lda = models.ldamodel.LdaModel(corpus=corpus, id2word = dictionary, num_topics=100, passes=30)
lda.save("articles_100_lda.model")

vis_data = gensimvis.prepare(lda, corpus, dictionary)
pyLDAvis.display(vis_data)
