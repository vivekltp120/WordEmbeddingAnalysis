#create model and convert it to text vector file..

import gensim
import os, sys,nltk
from os.path import isdir
from nltk.tokenize import RegexpTokenizer
from gensim.models.word2vec import Text8Corpus
from gensim.models import Word2Vec
import codecs
from gensim.models.word2vec import PathLineSentences
w2v_params = {
    'alpha': 0.025,
    'size': 400,
    'window': 5,
    'iter': 1,
    'min_count': (3),
    # 'sample': 1e-4,
    'sg': 1,
    'hs': 0,
    'negative': 10,
    # 'word_gram' : (1,2),
    # 'context_gram' : (1,2),
    'workers' : 10

}

sentences = []
class MySentences(object):
    def __init__(self,datapath):
        datapath=datapath
        pass

    def __iter__(self):

        amazon_review_data = codecs.open(self.datapath, encoding='utf-8')
        for row in amazon_review_data:
            yield(row.lower().split())

# MySentences(sys.argv[1])
#for directory
sentences=PathLineSentences(sys.argv[1])
bigram_transformer = gensim.models.Phrases(sentences)
bigram_model = Word2Vec(bigram_transformer[sentences], w2v_params)
bigram_model.wv.save_word2vec_format(sys.argv[2]+'.vec',sys.argv[2]+'.vocab', binary=False)
