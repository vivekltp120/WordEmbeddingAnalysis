import  gensim.models.word2vec as w2v
import sys

model=w2v.Word2VecKeyedVectors.load_word2vec_format(sys.argv[1])


evalfile1= open('../translated_eval_file/questions-words.txt','r')
evalfile2= open('../translated_eval_file/de_split_evalaa','r')





# First Approach

for line in evalfile1.readlines():
 w_list=line.strip().split()
 if len(w_list) > 3:
  print('\nFirst word--'+str(w_list[0]))
  print(model.most_similar(positive=w_list[0],restrict_vocab=500000))
  print(model.similar_by_word(w_list[0]))








