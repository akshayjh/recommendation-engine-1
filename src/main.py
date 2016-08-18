from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from gensim import corpora, models
import gensim


# Stop words
stopswords = []
with open("../resources/stopwords.txt") as stopwords_file:
    stopwords = stopwords_file.read().splitlines()

# Tokenizer for creating word tokens
tokenizer = RegexpTokenizer(r'\w+')

# Stemmer for the danish language
stemmer = SnowballStemmer("danish")

doc_a = "Det er en god dag idag, vi burde feste alle sammen"
doc_b = "Vi er mange sjove mennesker, som har det sjovt"
doc_c = "Burde man ikke bare skrive en artikel om alt det her, selvom det er underligt"
doc_d = "En lille bitte test, som skal teste om vi rent faktisk kan stemme ting"

doc_set = [doc_a, doc_b, doc_c, doc_d]


texts = []

for i in doc_set:
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    stopped_tokens = [i for i in tokens if not i in stopwords]

    stemmed_tokens = [stemmer.stem(i) for i in stopped_tokens]

    texts.append(stemmed_tokens)


dic = corpora.Dictionary(texts)

corpus = [dic.doc2bow(text) for text in texts]

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dic, passes=20)


# print result
print(ldamodel.print_topics(num_topics = 2, num_words = 2))
