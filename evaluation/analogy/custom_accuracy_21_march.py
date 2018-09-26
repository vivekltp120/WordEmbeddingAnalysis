import argparse
import numpy as np
import datetime



input_from_result=None
inputFile=None
current_time=datetime.datetime.now().strftime('%d_%b_%y')

def generate():
    global inputFile
    global closureWord
    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab_file', default=None, type=str)
    parser.add_argument('--vectors_file', default=None, type=str)
    parser.add_argument('--input_file', default= None , type=str)
    args = parser.parse_args()

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
        vo_name=vo_name.split('/')[::-1][0].split('_')
        outfile_name = vo_name[0]+'_'+vo_name[1] + "_closure_words_" + current_time + ".txt"

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
    close_arr=[]
    for x in a:
        closureWord.write("%30s\t\t%f\n" % (ivocab[x], dist[x]))
        print("%30s\t\t%f\n" % (ivocab[x], dist[x]))
        close_arr.append(ivocab[x])

    closureWord.write("\n")

    return  close_arr


if __name__ == "__main__":
    N = 10;          # number of closest words that will be shown
    W, vocab, ivocab = generate()
    input_term=None
    correct=0
    total=0
    while True:
        if inputFile != None:
            input_words = inputFile.readline().rstrip().split(' ')
            print (str(input_words))

        if input_term == 'EXIT':
            break

        else:
            # closureWord.write("Input word                "+ input_term+'\n')
            res_arr = distance(W, vocab, ivocab,input_words[0])
            if res_arr != None and input_words[1] in res_arr :
                res_arr=distance(W, vocab, ivocab,input_words[1])
                if res_arr != None and input_words[0] in res_arr:
                    correct=correct+1;
            else:
                print("Synonyms Not Exist")
        total=total+1

    print('Accuracy--'+ str((correct/total)*100) +'%')
    closureWord.close()
    inputFile.close()