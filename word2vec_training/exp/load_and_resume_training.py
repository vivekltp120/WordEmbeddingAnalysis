import sys
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import time
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--current_model', default=None, type=str)
parser.add_argument('--data', default=None, type=str)
parser.add_argument('--new_model', default= None , type=str)
args = parser.parse_args()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model=KeyedVectors.load_word2vec_format(args.current_model,binary=False)

sentences = LineSentence(args.data)
model.train(sentences, epochs=10,workers=4, sg=1, hs=1,negative=2)
model.wv.save_word2vec_format(args.new_model+'.vec',args.new_model+'.vocab', binary=False)


