import sys
from gensim.models.keyedvectors import KeyedVectors
import sklearn.cluster.k_means_ as K_Means
import argparse
import numpy as np
import datetime

input_from_result = None
inputFile = None
current_time = datetime.datetime.now().strftime('%d_%b_%y')
cluster_words = []
parser = argparse.ArgumentParser()
parser.add_argument('--vocab_file', default=None, type=str)
parser.add_argument('--vectors_file', default=None, type=str)
parser.add_argument('--input_file', default=None, type=str)
args = parser.parse_args()
model_name=args.vectors_file


def generate():
    global inputFile
    global closureWord
    global model_name

    with open(args.vocab_file, 'r') as f:
        words = [x.rstrip().split(' ')[0] for x in f.readlines()]
    with open(args.vectors_file, 'r') as f:
        vectors = {}
        for line in f:
            vals = line.rstrip().split(' ')
            vectors[vals[0]] = [float(x) for x in vals[1:]]

    if args.input_file != None:
        inputFile = open(args.input_file, 'r')
    if args.vocab_file:
        vo_name = args.vectors_file
        # vo_name=vo_name.split('/')[::-1][0].split('_')
        vo_name = vo_name.split('/')[::-1][0].split('.')[0]
        outfile_name = vo_name + "_" + "_closure_words_" + current_time + ".txt"

        print(outfile_name)
        closureWord = open(outfile_name, 'w')

    vocab_size = len(words)
    vocab = {w: idx for idx, w in enumerate(words)}
    ivocab = {idx: w for idx, w in enumerate(words)}

    vector_dim = len(vectors[ivocab[0]])
    W = np.zeros((vocab_size, vector_dim))
    for word, v in vectors.items():
        if word == '<unk>':
            continue
        try:
            W[vocab[word], :] = v
        except:
            print('Word Not Found Error')
    # normalize each word vector to unit variance
    W_norm = np.zeros(W.shape)
    d = (np.sum(W ** 2, 1) ** (0.5))
    W_norm = (W.T / d).T
    return (W_norm, vocab, ivocab)


# evaluate the distance of closure words for the given words
def distance(W, vocab, ivocab, input_term):
    for idx, term in enumerate(input_term.split(' ')):
        if term in vocab:
            print('Word: %s  Position in vocabulary: %i' % (term, vocab[term]))
            if idx == 0:
                vec_result = np.copy(W[vocab[term], :])
            else:
                vec_result += W[vocab[term], :]
        else:
            print('Word: %s  Out of dictionary!\n' % term)
            return

    vec_norm = np.zeros(vec_result.shape)
    d = (np.sum(vec_result ** 2, ) ** (0.5))
    vec_norm = (vec_result.T / d).T

    dist = np.dot(W, vec_norm.T)

    for term in input_term.split(' '):
        index = vocab[term]
        dist[index] = -np.Inf

    a = np.argsort(-dist)[:N]

    print("\n                           Word       Cosine distance\n")
    closureWord.write("\n                       Word       Cosine distance\n")
    print("                 ---------------------------------\n")
    closureWord.write("                 ---------------------------------\n")
    for x in a:
        closureWord.write("%30s\t\t%f\n" % (ivocab[x], dist[x]))
        print("%30s\t\t%f\n" % (ivocab[x], dist[x]))

    closureWord.write("\n")

model=KeyedVectors.load_word2vec_format(model_name,binary=False)
word_vectors=model.wv.syn0
num_clusters=20 #number of clusters for the corpus
kmeans_clustering=K_Means.KMeans(n_clusters=num_clusters)
idx = kmeans_clustering.fit_predict( word_vectors )

word_centroid_map =[list(a) for a in zip(model.wv.index2word, idx)]
word_centroid_map=dict(word_centroid_map)

outfile=open('cluster_info.txt','w')


if __name__ == "__main__":
    N = 10;  # number of closest words that will be shown
    W, vocab, ivocab = generate()
    input_term = None
    while True:
        if inputFile != None:
            input_term = inputFile.readline().rstrip().split(' ')[0]
            print(input_term)
        else:
            input_term = input("\nEnter word  (EXIT to break): ")

        if input_term == 'EXIT' or None:
            break
        else:
            closureWord.write("Input word                " + input_term + '\n')
            distance(W, vocab, ivocab, input_term)
            cluster_id = word_centroid_map[input_term]
            print('cluster for the word ' + input_term + ' is ' + str(cluster_id))
            outfile.write('\ncluster for the word ' + input_term + ' is ' + str(cluster_id))
            # Print the cluster number
            print("\nCluster %d" % (cluster_id))
            # outfile.write("\nCluster %d" % (cluster_id))

            for key, value in word_centroid_map.items():
                if (value == cluster_id):
                    cluster_words.append(key)
            print('Words in the cluster is:' + str(cluster_words))
            outfile.write('\nWords in the cluster is:\n' + str(cluster_words))

            # for w in words:
            #     print('Index of ' + w +'-'+ str(list[(cluster_words.index(w))]) )






