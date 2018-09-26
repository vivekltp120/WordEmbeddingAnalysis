import sys
import os
from gensim.models.keyedvectors import KeyedVectors
from gensim.models import Word2Vec

m_path=sys.argv[1]
filepath=os.path.split(m_path)[0]
filename=os.path.split(m_path)[1].split('.')[0]
outmodel=os.path.join(filepath,filename)
#save into standard w2v text format
model=KeyedVectors.load_word2vec_format(m_path,binary=False)
# model.wv.save_word2vec_format(m_path+'.vec',m_path+'.vocab', binary=False)

#into npy format
model=Word2Vec.load(m_path)
model.save(outmodel+'.model')

