import argparse
import numpy as np
import datetime
import os
import gensim
from itertools import combinations

import logging
import os

input_from_result=None
inputFile=None
evalfp=None
current_time= datetime.datetime.now().strftime('%d_%b_%y_%H_%M')

#get accuracy
def write_accuracy(model_path,word_analogies_file):
    model = gensim.models.KeyedVectors.load_word2vec_format(model_path)
    print_accuracy(model, word_analogies_file)

#print the accuracy
def print_accuracy(model, questions_file):
    print('Evaluating Custom Analogy Accuracy...\n')
    acc = model.accuracy(questions_file,restrict_vocab=500000,case_insensitive=False,most_similar=20)
    print(acc)
    sem_correct = sum((len(acc[i]['correct']) for i in range(1)))
    sem_total = sum((len(acc[i]['correct']) + len(acc[i]['incorrect'])) for i in range(1))
    sem_acc = 100*float(sem_correct)/sem_total
    print('\nSemantic: {:d}/{:d}, Accuracy: {:.2f}%'.format(sem_correct, sem_total, sem_acc))
    write_to_file(evalfp,'\nSemantic: {:d}/{:d}, Accuracy: {:.2f}%'.format(sem_correct, sem_total, sem_acc))
    return (sem_acc)

# write the content on file
def write_to_file(fp,content):
     fp.write(content)

#combination of words or analogy eval file
def analogy_eval(wordlist):
    outline = combinations(wordlist, 4)
    for i in outline:
        combi= " ".join(list(i))
        # print(combi)
        write_to_file(evalfp, combi + '\n')

#output file name
def get_outfile_name(model_path):
    outfile_eval='default_closure_file_'+current_time+".txt"
    if model_path:
        m1=os.path.basename(model_path)
        print(m1)
        outfile_eval = m1+'_'+str(N)+ "_closure_and_accuracy_" + current_time + ".txt"

    # out_file = open(outfile_eval, 'w')
    return outfile_eval

#genrate the norm vector and return the vocab vector and weighted norm
def generate(vocab_path,vec_path):
    with open(vocab_path, 'r') as f:
        words = [x.rstrip().split(' ')[0] for x in f.readlines()]
    with open(vec_path, 'r') as f:
        vectors = {}
        for line in f:
            vals = line.rstrip().split(' ')
            vectors[vals[0]] = [float(x) for x in vals[1:]]

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
            # print('Word: %s  Position in vocabulary: %i' % (term, vocab[term]))
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
    cw=[]
    for x in a:
        # write_to_file(eval_file,ivocab[x])
        cw.append(ivocab[x])


    # closureWord.write("\n")
    return cw

if __name__ == "__main__":
    N = 5          # number of closest words that will be shown
    input_term = None
    avg_sim = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab_file', default=None, type=str)
    parser.add_argument('--vectors_file', default=None, type=str)
    parser.add_argument('--input_file', default=None, type=str)
    args = parser.parse_args()

    W, vocab, ivocab = generate(args.vocab_file,args.vectors_file)
    outfile=get_outfile_name(args.vectors_file)
    evalfp=open(outfile, 'w')
    write_to_file(evalfp,': custom relation'+'\n')
    logging.basicConfig(filename=evalfp, format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logging.basicConfig(filename=evalfp, format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

    # write_to_file(evalfp, 'WEM - ' + os.path.basename(args.vectors_file) + '\n')
    inputFile=open(args.input_file,'r+')
    while True:
        if inputFile != None:
            input_term = inputFile.readline().rstrip().split(' ')[0]
            print (input_term)
        else:
            input_term = input("\nEnter word or sentence (EXIT to break): ")

        if input_term == 'EXIT':
            inputFile.close()
            break
        else:
            # evalfp.write("Input words - %s" % (input_term) + '\n')
            ms=distance(W, vocab, ivocab, input_term)
            if ms != None and len(ms)>= 3   :
                ms.append(input_term)
                analogy_eval(ms)



    # outfile=os.path.join(os.getcwd()+'/'+outfile)
    print(outfile)
    write_accuracy(args.vectors_file,outfile)
    evalfp.close()