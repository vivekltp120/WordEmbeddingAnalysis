

#Create the word to vec model for the data
#create model and convert it to text vector file..
import gensim
import argparse
import sys
import datetime
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
current_time= datetime.datetime.now().strftime('%d_%b_%y')

def print_accuracy(model, questions_file):
    print('Evaluating...\n')
    acc = model.accuracy(questions_file)
    # print(acc)
    sem_correct = sum((len(acc[i]['correct']) for i in range(5)))
    sem_total = sum((len(acc[i]['correct']) + len(acc[i]['incorrect'])) for i in range(5))
    sem_acc = 100*float(sem_correct)/sem_total
    print('\nSemantic: {:d}/{:d}, Accuracy: {:.2f}%'.format(sem_correct, sem_total, sem_acc))
    outfile.write('\nSemantic: {:d}/{:d}, Accuracy: {:.2f}%'.format(sem_correct, sem_total, sem_acc))

    syn_correct = sum((len(acc[i]['correct']) for i in range(5, len(acc)-1)))
    syn_total = sum((len(acc[i]['correct']) + len(acc[i]['incorrect'])) for i in range(5,len(acc)-1))
    syn_acc = 100*float(syn_correct)/syn_total
    print('Syntactic: {:d}/{:d}, Accuracy: {:.2f}%\n'.format(syn_correct, syn_total, syn_acc))
    outfile.write('Syntactic: {:d}/{:d}, Accuracy: {:.2f}%\n'.format(syn_correct, syn_total, syn_acc))

    return (sem_acc, syn_acc)


word_analogies_file = '/home/vivek/ML_Sep_2017/DataCorpus/English/questions-words-modified.txt'
accuracies = []

parser = argparse.ArgumentParser()
parser.add_argument('--eval', default=None, type=str)
parser.add_argument('--w2v', default=None, type=str)
parser.add_argument('--glove', default=None, type=str)
parser.add_argument('--fasttext', default=None, type=str)
args = parser.parse_args()

word_analogies_file=args.eval

outfile_name=word_analogies_file.split('/')[::-1][0].split('_')[0] + "_models_accuracy_"+current_time+".txt"
outfile=open(outfile_name,'w')



if(args.glove):
    print('\nAccuracy for Glove embeddings')
    outfile.write('\nLoading for Glove'+'\nAccuracy for glove :')
    text8_gs = gensim.models.KeyedVectors.load_word2vec_format(args.glove)
    accuracies.append(print_accuracy(text8_gs, word_analogies_file))
else:
    print('Glove model not given or exist')

if(args.fasttext):
    print('\nLoading for Fasttext')
    text8_ft = gensim.models.KeyedVectors.load_word2vec_format(args.fasttext)
    print('Accuracy for Fasttext (with n-grams):')
    outfile.write('\nLoading for Fasttext'+'\nAccuracy for Fasttext :')
    accuracies.append(print_accuracy(text8_ft, word_analogies_file))
else:
    print('fasttext model not given or exist')

if (args.w2v):
    print('\nLoading for gensim')
    print('Accuracy for gensim by gensim inbuilt converter:')
    outfile.write('\nLoading for gensim' + '\nAccuracy for gensim :')
    wv_model = gensim.models.KeyedVectors.load_word2vec_format(args.w2v)
    accuracies.append(print_accuracy(wv_model, word_analogies_file))

else:
    print('Word2vec model not given or exist')

outfile.close()