import argparse
import numpy as np
import datetime
import os
import logging


input_from_result=None
inputFile=None
eval_file=None
current_time=datetime.datetime.now().strftime('%d_%b_%y')
OOV=None
total_input_word=0
predict_word=0
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)


#get common word between two dict
def get_common_word(filepath1,filepath2):
    file1=open(filepath1,'r')
    file2=open(filepath2,'r')
    x=[x.rstrip().split(' ')[0] for x in file1.readlines()]
    y=[x.rstrip().split(' ')[0] for x in file2.readlines()]
    xuy=list(set(x).union(set(y)))
    xuy.append('EXIT')
    print(xuy)
    return xuy

#similarity for words
def similarity(a,b):
    # write_to_file(eval_file,"Model_1 - "+ str(a) + '\n')
    # write_to_file(eval_file,"Model_2 - "+ str(b) + '\n')
    a=set(a)
    b=set(b)
    inter=a.intersection(b)
    union=a.union(b)
    sim =len(inter)/len(union)
    # write_to_file(eval_file,"Common Words or Intersection - "+ str(list((inter))) + '\n')
    # write_to_file(eval_file,"Union - "+ str(list(union)) + '\n')
    # write_to_file(eval_file,"Similarity - " + str(sim))
    return sim

#write the content on file
def write_to_file(fp,content):
     fp.write(content)

#output file name
def get_outfile_name(model_path_1,model_path_2):
    outfile='default_closure_file_'+current_time+".txt"
    if model_path_1 and model_path_2:
        m1=os.path.basename(model_path_1)
        m2=os.path.basename(model_path_2)
        # print(m1)
        # print(m2)
        outfile_eval = '_'.join(m1.split('_')[0:8])+'_'.join(m2.split('_')[0:8])+'_'+str(N)+ "_similarity_" + current_time + ".txt"
        outfile = open(outfile_eval, 'w')
    return outfile

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
    N = 100          # number of closest words that will be shown
    count_word=0
    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab_file_1', default=None, type=str)
    parser.add_argument('--vectors_file_1', default=None, type=str)
    parser.add_argument('--vocab_file_2', default=None, type=str)
    parser.add_argument('--vectors_file_2', default=None, type=str)
    parser.add_argument('--input_file', default=None, type=str)
    args = parser.parse_args()

    W1, vocab1, ivocab1 = generate(args.vocab_file_1,args.vectors_file_1)
    W2, vocab2, ivocab2 = generate(args.vocab_file_2,args.vectors_file_2)
    input_term=None
    avg_sim=0
    eval_file=get_outfile_name(args.vectors_file_1,args.vectors_file_2)
    write_to_file(eval_file,'WEM_1 - '+os.path.basename(args.vocab_file_1)+'\n')
    write_to_file(eval_file,'WEM_2 - '+os.path.basename(args.vocab_file_2)+'\n')
    if args.input_file!=None:
     inputFile=open(args.input_file,'r')
    else:
     v1uv2 = get_common_word(args.vocab_file_1, args.vocab_file_2)

    i=0
    while True:
        if inputFile != None:
            input_term = inputFile.readline().rstrip().split(' ')[0]
            # print (input_term)
        else:
            input_term=v1uv2[i]
            i=i+1

        if input_term == 'EXIT':
            # print('input term is: '+input_term)
            break
        else:
            total_input_word+=1
            # eval_file.write("Input words - %s" %(input_term)+'\n')
            mc1=distance(W1, vocab1, ivocab1, input_term)
            mc2=distance(W2, vocab2, ivocab2, input_term)
            if mc1 is not None and mc2 is not None:
                predict_word+=1
                sim=similarity(mc1,mc2)
                avg_sim=avg_sim+sim
                print('predict_word-'+str(predict_word)+' avg_sim-'+str(avg_sim))
            # write_to_file(eval_file,'\n\n')
# try:
avg_sim=(avg_sim/predict_word)
write_to_file(eval_file,"Total Input Words - " +str(total_input_word))
write_to_file(eval_file,"\nNumber of words for which closure exist - " +str(predict_word))
write_to_file(eval_file,"\nWord percentage for which closure exist - " +str((predict_word/total_input_word)*100))
write_to_file(eval_file,"\nAverage Similarity - " +str(avg_sim))
eval_file.close()
inputFile.close()
