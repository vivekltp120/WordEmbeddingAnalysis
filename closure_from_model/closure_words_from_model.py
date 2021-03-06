import argparse
import numpy as np
import datetime
import os


input_from_result=None
inputFile=None
current_time=datetime.datetime.now().strftime('%d_%b_%y')


parser = argparse.ArgumentParser()
parser.add_argument('--vocab_file', default=None, type=str)
parser.add_argument('--vectors_file', default=None, type=str)
parser.add_argument('--input_file', default= None , type=str)
parser.add_argument('--topn', default= 10 , type=int)
args = parser.parse_args()
def generate():
    global inputFile
    global closureWord

    with open(args.vocab_file, 'r') as f:
        words = [x.rstrip().split(' ')[0] for x in f.readlines()]
    with open(args.vectors_file, 'r') as f:
        vectors = {}
        for line in f:
            vals = line.rstrip().split(' ')
            vectors[vals[0]] = [float(x) for x in vals[1:]]

    if args.input_file !=None:
        inputFile=open(args.input_file, 'r')
    if args.vocab_file:
        vo_name=args.vectors_file
        # vo_name=vo_name.split('/')[::-1][0].split('_')
        vo_name= os.path.split(vo_name)[1].split('.')[0]
        outfile_name = vo_name+"_" + "_closure_words_" + current_time + ".output"

        print(outfile_name)
        closureWord=open(outfile_name,'w')

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
            print ('Word Not Found Error')
    # normalize each word vector to unit variance
    W_norm = np.zeros(W.shape)
    d = (np.sum(W ** 2, 1) ** (0.5))
    W_norm = (W.T / d).T
    return (W_norm, vocab, ivocab)

#evaluate the distance of closure words for the given words
def distance(W, vocab, ivocab, input_term):
    for idx, term in enumerate(input_term.split(' ')):
        if term in vocab:
            print('Word: %s  Position in vocabulary: %i' % (term, vocab[term]))
            if idx == 0:
                vec_result = np.copy(W[vocab[term], :])
            else:
                vec_result += W[vocab[term], :]
        else:
            print('Word: %s  Out of dictionary!\n' % term )
            return

    vec_norm = np.zeros(vec_result.shape)
    d = (np.sum(vec_result ** 2,) ** (0.5))
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


if __name__ == "__main__":
    N = args.topn;          # number of closest words that will be shown
    W, vocab, ivocab = generate()
    input_term=None
    while True:
        if inputFile != None:
            input_term = inputFile.readline().rstrip().split(' ')[0]
            print (input_term)
        else:
            input_term = input("\nEnter word or sentence (EXIT to break): ")

        if input_term == 'EXIT':
            break
        else:
            closureWord.write("Input word                "+ input_term+'\n')
            distance(W, vocab, ivocab, input_term)


    closureWord.close()
    inputFile.close()
