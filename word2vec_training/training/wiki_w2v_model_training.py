#create model and convert it to text vector file..

import gensim
import os, sys,nltk
from os.path import isdir
from nltk.tokenize import RegexpTokenizer
from gensim.models.word2vec import Text8Corpus
from gensim.corpora import WikiCorpus
from gensim.corpora import wikicorpus
from gensim.corpora import textcorpus
from gensim.models.word2vec import PathLineSentences
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import time
import logging
import codecs

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
tokenizer = RegexpTokenizer(r'\w+')


w2v_params = {
    'alpha': 0.025,
    'size': 400,
    'window': 5,
    'iter': 5,
    'min_count': (3),
    # 'sample': 1e-4,
    'sg': 1,
    'hs': 0,
    'negative': 10,
    # 'word_gram' : (1,2),
    # 'context_gram' : (1,2),
    'workers' : 16

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

        # wiki_data = codecs.open(, encoding='utf-8')
        # for row in wiki_data:
        #     yield(row.lower().split())

sentences=wikicorpus.remove_markup(sys.argv[1])
sentences=wikicorpus.remove_template(sentences)
sentences=wikicorpus.tokenize(sentences)


model = Word2Vec(sentences, **w2v_params)

model.wv.save_word2vec_format(sys.argv[2]+'.vec',sys.argv[2]+'.vocab', binary=False)
