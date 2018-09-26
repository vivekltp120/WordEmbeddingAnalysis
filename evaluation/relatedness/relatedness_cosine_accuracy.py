# from vocabulary.vocabulary import Vocabulary as vb
import json
import csv
import datetime
import os
import sys
from gensim.models.keyedvectors import KeyedVectors
import sklearn.cluster.k_means_ as K_Means
import argparse


current_time=datetime.datetime.now().strftime('%d_%b_%y')

#parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--eval', default=None, type=str)
parser.add_argument('--model', default=None, type=str)
args = parser.parse_args()

#user arguments
eval_file=args.eval
model_name=args.model
module_path='/home/vivek/ML_Sep_2017/WordVectorTraining'
split_model_name=model_name.split('/')[::-1][0].split('_')
outfile=eval_file.split('/')[::-1][0].split('_')[0].split('.')[0]+"_"+ split_model_name[0] + "_models_relatedness_accuracy_"+current_time+".csv"
WEM=model_name.split('/')[-1]


outfile=open(outfile, 'w')
eval_file=open(eval_file,'r')


readCSV = csv.reader(eval_file, delimiter=',')
writeCSV = csv.writer(outfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# fieldnames = ['word_1', 'word_2','closeness' 'pearson', 'spearman', 'OOV']
fieldnames = ['word_1', 'word_2', 'cosine_closeness' ]


model=KeyedVectors.load_word2vec_format(model_name,binary=False)

# writeCSV.writerow(['WEM',WEM])
# writeCSV.writerow(['Time ',current_time])

for row in readCSV:

     try:
         # pearson, spearman, oov_ratio = model.evaluate_word_pairs([row[0],row[1]], delimiter=',', case_insensitive=False)
         cosine_sim=model.similarity(row[0],row[1])
         writeCSV.writerow([row[0], row[1], cosine_sim]) #, pearson, spearman , oov_ratio])


     except KeyError:
         pass

resultRead=readCSV = csv.reader(outfile, delimiter=',')

pearson, spearman, oov_ratio = model.evaluate_word_pairs(os.path.join(module_path, 'evaluation',outfile), delimiter=',', case_insensitive=False)
print('pearson-'+str(pearson)+'\nspearman-'+str(spearman)+'\noov_ratio-'+str(oov_ratio))










