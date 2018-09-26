from vocabulary.vocabulary import Vocabulary as vb
import json
import csv
import datetime

import sys
from gensim.models.keyedvectors import KeyedVectors
import sklearn.cluster.k_means_ as K_Means
import argparse


current_time=datetime.datetime.now().strftime('%d_%b_%y')

#parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--eval', default=None, type=str)
parser.add_argument('--model', default=None, type=str)
parser.add_argument('--clusters', default=5, type=str)
args = parser.parse_args()

#user arguments
eval_file=args.eval
model_name=args.model
num_clusters =int(args.clusters)  #number of clusters for the corpus

split_model_name=model_name.split('/')[::-1][0].split('_')
outfile = split_model_name[0]+"_"+split_model_name[1]+'_'+ eval_file.split('/')[::-1][0].split('_')[0].split('.')[0] + "_categorization_accuracy_cluster_"+str(num_clusters)+'_'+current_time+".csv"
WEM=model_name.split('/')[-1]


outfile=open(outfile, 'w')
eval_file=open(eval_file,'r')


readCSV = csv.reader(eval_file, delimiter=',')
writeCSV = csv.writer(outfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
fieldnames = ['word_1','cluster_1', 'word_2','cluster_2','result']


model=KeyedVectors.load_word2vec_format(model_name,binary=False)

word_vectors=model.wv.syn0
kmeans_clustering=K_Means.KMeans(n_clusters=num_clusters)
idx = kmeans_clustering.fit_predict( word_vectors )

word_centroid_map =[list(a) for a in zip(model.wv.index2word, idx)]
word_centroid_map=dict(word_centroid_map)
correct_count=0
total_count=0

writeCSV.writerow(['WEM',WEM,'Time ',current_time])



for row in readCSV:

     try:
        cluster_id_1 = word_centroid_map[row[0]]
        cluster_id_2 = word_centroid_map[row[1]]
        if cluster_id_1==cluster_id_2:
            correct_count=correct_count+1
            writeCSV.writerow([row[0], cluster_id_1, row[1], cluster_id_2, 'Same Cluster' ])
        else:
            writeCSV.writerow([row[0], cluster_id_1, row[1], cluster_id_2, 'Different Cluster' ])

     except KeyError:
         pass
     total_count=total_count+1

accuracy=((correct_count/total_count)*100)
writeCSV.writerow(['Accuracy  ',accuracy])
writeCSV.writerow(['Number Of Clusters  ',num_clusters])


print('Accuracy for categorical evaluation -- '+str(accuracy))






