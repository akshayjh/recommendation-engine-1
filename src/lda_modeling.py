import logging
import gensim
from argparse import ArgumentParser
from nltk.tokenize import RegexpTokenizer
import os
import re


class LdaModel:
    def __init__(self, path_to_corpora):
        self.path_to_stopwords = "../resources/stopwords.txt"
        self.path_to_corpora = path_to_corpora

        print("Init LDA modeling")
        # Number of topics
        self.nr_of_topics = 40
        # Filter out tokens which appear less then threshold  in all documents
        self.filter_apperance_below_threshold = 50
        # Filter out tokens that appear in more than fraction of total corpus
        self.filter_apperance_above_fraction = 0.3
        # Remove topics where weights is less then threshold
        self.topic_weight_threshold = 0.10
        # Iterations for LDA
        self.lda_iterations = 200
        # Number of total passes
        self.lda_passes = 10
        # Ignore article text with less the nr of characters
        self.minimum_character_limit = 200
        
        print("Done with init")

    def tokenization(self, path_to_corpora):
        """
        Tokenize the corpora, we skip documents with under 200 characters and create a tuple containing
        header and text, here we should try to include the url for the published article. 
        We remove stopwords, which is defined in ../resources/stopwords.txt.
        We return a count off all documents processed and for each document a dict containing a tuple
        of header and title for each document with the count as key and finally the set
        which for each document contains the words which should be trained on
        """
        print("Starting tokenization")
        train_set_pr_document = []
        document_mapping = []
        total_document_count = 0
        
        for filename in os.listdir(path_to_corpora):
            with open(path_to_corpora + filename, "r") as article_file:
                article_text = article_file.readlines()
                if len(article_text) < self.minimum_character_limit:
                    print(len(article_text))
                    continue
                else:
                    print("WUP")


    def _list_to_dict(self, element):
        print("Not Implemented")

    def _save_model(self, lda, document_mapping, corpus):
        print("Not Implemented")

    def _train_model(self):
        print("Not Implemented")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) 
    model = LdaModel("/home/mark/temp/indblik/")
    model.tokenization(model.path_to_corpora)
   
   
    print("Done with LDA modeling")            
            
            # Documents array
#articles = []

# Preprocessingkkk
#path = "/home/mark/temp/shippingwatch/"

#for filename in os.listdir(path):
#    with open(path + filename, "r") as article_file:
#        article_text = article_file.read().replace("\n", "")
#        remove_html_tags = re.compile("<.*?>")
#        articles_text_stripped = re.sub(remove_html_tags, " ", article_text)
#        articles.append(articles_text_stripped)

# Stop words
#stopwords = []
#with open("../resources/stopwords.txt") as stopwords_file:
#    stopwords = stopwords_file.read().splitlines()

# Tokenizer for creating word tokens
#tokenizer = RegexpTokenizer(r'\w+')

# Stemmer for the danish languagkke
#stemmer = SnowballStemmer("danish")


#docs = []

#for i in articles:
#    raw = i.lower()
#    tokens = tokenizer.tokenize(raw)

#    stopped_tokens = [i for i in tokens if not i in stopwords]

#    stemmed_tokens = [stemmer.stem(i) for i in stopped_tokens]

#    docs.append(stopped_tokens)


#dictionary = Dictionary(docs)
#dictionary.compactify()
#dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=None)
#dictionary.compactify()

#corpus = [dictionary.doc2bow(doc) for doc in docs

#MmCorpus.serialize("../output/articles.mm", corpus)
#dictionary.save("../output/articles.dict")


#lda = models.ldamulticore.LdaMulticore(corpus=corpus, id2word = dictionary, num_topics=20, passes=100)
#lda.save("../output/shippingwatch_20_lda.model")

#vis_data = gensimvis.prepare(lda, corpus, dictionary)
#pyLDAvis.save_html(vis_data, "../output/shippingwatch.html")
