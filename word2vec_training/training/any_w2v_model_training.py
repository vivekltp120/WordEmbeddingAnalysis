#create model and convert it to text vector file..

import gensim
import os, sys,nltk
from os.path import isdir
from nltk.tokenize import RegexpTokenizer
from gensim.models.word2vec import Text8Corpus
from gensim.models.word2vec import PathLineSentences
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import datetime
import logging
import codecs

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
tokenizer = RegexpTokenizer(r'\w+')
current_time=datetime.datetime.now().strftime('%d_%b_%y')
#For amazon model
# w2v_params = {
#     'alpha': 0.025,
#     'size': 400,
#     'window': 5,
#     'iter': 5,
#     'min_count': (3),
#     # 'sample': 1e-4,
#     'sg': 1,
#     'hs': 0,
#     'negative': 10,
#     # 'word_gram' : (1,2),
#     # 'context_gram' : (1,2),
#     'workers' : 16
#
# }


w2v_params = {
    'alpha': 0.025,
    'size': 400,
    'window': 5,
    'iter': 1,
    'min_count': (3),
    # 'sample': 1e-4,
    'sg': 1,
    'hs': 0,
    'negative': 30,
    # 'word_gram' : (1,2),
    # 'context_gram' : (1,2),
    'workers' : 16

}

outfile=[]
for key,value in sorted(w2v_params.items()):
    if key=='alpha':
        continue
    outfile.append(key+'_'+str(value))
outfile="_".join(outfile)

outputfile=str(sys.argv[2])+'_w2v_'+str(outfile)+'_'+str(current_time)
print(outputfile)
sentences = []


class MySentences(object):
    def __init__(self,datapath):
        datapath=datapath
        pass

    def __iter__(self):
        for fname in os.listdir(self.datapath):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

        #
        # amazon_review_data = codecs.open(self.datapath, encoding='utf-8')
        # for row in amazon_review_data:
        #     yield(row.lower().split())

        # wiki_data = codecs.open(, encoding='utf-8')
        # for row in wiki_data:
        #     yield(row.lower().split())

#effective with bigram model due to some contexual things(have to verify)
# MySentences(sys.argv[1])
#With file
# sentences = LineSentence(sys.argv[1])
#with directory
sentences= PathLineSentences(sys.argv[1])
model = Word2Vec(sentences, **w2v_params)

model.wv.save_word2vec_format(outputfile+'.vec',outputfile+'.vocab', binary=False)
