import sys
from gensim.models.keyedvectors import KeyedVectors
import sklearn.cluster.k_means_ as K_Means

model=KeyedVectors.load_word2vec_format(sys.argv[1],binary=False)
word_vectors=model.wv.syn0
num_clusters = 20 #number of clusters for the corpus
kmeans_clustering=K_Means.KMeans(n_clusters=num_clusters)
idx = kmeans_clustering.fit_predict( word_vectors )

word_centroid_map =[list(a) for a in zip(model.wv.index2word, idx)]
word_centroid_map=dict(word_centroid_map)
inputFile=open('/home/vivek/ML_Sep_2017/WordVectorTraining/closurewords/english_closure/100_frequent_word.txt','r')
outfile=open('cluster_info.txt','w')


if __name__ == "__main__":
    N = 10;  # number of closest words that will be shown
    input_term = None
    cluster_words=[]
    while True:

        if inputFile != None:
            input_term = inputFile.readline().rstrip().split(' ')[0]
            print(input_term)
        else:
            input_term = input("\nEnter word  (EXIT to break): ")

        if input_term == 'EXIT' or None:
            break
        else:
            cluster_id = word_centroid_map[input_term]
            print('cluster for the word ' + input_term + ' is ' + str(cluster_id))
            outfile.write('\ncluster for the word ' + input_term + ' is ' + str(cluster_id))
            # Print the cluster number
            print("Cluster %d" % (cluster_id))
            # outfile.write("\nCluster %d" % (cluster_id))

            for key, value in word_centroid_map.items():
                if (value == cluster_id):
                    cluster_words.append(key)
            # print('Words in the cluster is:' + str(cluster_words))
            outfile.write('\nWords in the cluster is:\n' + str(cluster_words))

            # for w in words:
            #     print('Index of ' + w +'-'+ str(list[(cluster_words.index(w))]) )






