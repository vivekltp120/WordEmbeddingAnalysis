
#Server which run on the given address,socket give the closure words for the user of a given word

from flask import Flask
from flask import request

import argparse
import numpy as np
import io
import json
input_from_result=None
inputFile= None
N=10
sampleInput={"word":" ","language":" ","model":" "}
sampleJson=json.dumps(sampleInput)
#Loading model and find the vector for the given word
def generate():
    global inputFile
    global closureWord

    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab_file', default=None, type=str)
    parser.add_argument('--vectors_file', default=None, type=str)
    args = parser.parse_args()

    with open(args.vocab_file, 'r') as f:
        words = [x.rstrip().split(' ')[0] for x in f.readlines()]
    with open(args.vectors_file, 'r') as f:
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

#get the distance of closure words of given word
def distance(W, vocab, ivocab, input_term):
    strBuff=io.StringIO()
    listofwords=[]
    jsontouser='None'
    for idx, term in enumerate(input_term.split(' ')):
        if term in vocab:
            print('Word: %s  Position in vocabulary: %i' % (term, vocab[term]))
            if idx == 0:
                vec_result = np.copy(W[vocab[term], :])
            else:
                vec_result += W[vocab[term], :]
        else:
            print('Word: %s  Out of dictionary!\n' % term)
            jsontouser=json.dumps({"Word Out of Dictionary":"No word of such kind"})
            return jsontouser

    vec_norm = np.zeros(vec_result.shape)
    d = (np.sum(vec_result ** 2,) ** (0.5))
    vec_norm = (vec_result.T / d).T

    dist = np.dot(W, vec_norm.T)

    for term in input_term.split(' '):
        index = vocab[term]
        dist[index] = -np.Inf

    a = np.argsort(-dist)[:N]

    print("\n                           Word       Cosine distance\n")
    strBuff.write("\n                       Word       Cosine distance\n")
    print("                 ---------------------------------\n")
    strBuff.write("                 ---------------------------------\n")
    for x in a:
        strBuff.write("%30s\t\t%f\n" % (ivocab[x], dist[x]))
        print("%30s\t\t%f\n" % (ivocab[x], dist[x]))
        listofwords.append({"distance":dist[x],"word":ivocab[x]})


    jsonwordlist=json.dumps(listofwords)
    jsontouser=json.dumps({'closurewords':jsonwordlist})
    strBuff.write("\n")
    return jsontouser






app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def getClosureWord():

    if request.method=='POST':
        content = request.json
        print (content)
        closureWord='None'
        if content != 'None':
            data=content['word']
            closureWord = distance(W, vocab, ivocab,data)
            print(content['word'])
            return closureWord

    if request.method=='GET':
        return "Put a POST request with body format: "+sampleJson


if __name__ == '__main__':

    W, vocab, ivocab = generate()
    #run the server on the port and address
    app.run(host = '10.0.15.218',port=8000,debug=True)