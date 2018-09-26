

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
parser.add_argument('--m1', default=None, type=str)
parser.add_argument('--m2', default=None, type=str)
parser.add_argument('--m3', default=None, type=str)
parser.add_argument('--m4', default=None, type=str)
parser.add_argument('--m5', default=None, type=str)
parser.add_argument('--m6', default=None, type=str)
args = parser.parse_args()

word_analogies_file=args.eval

outfile_name=word_analogies_file.split('/')[::-1][0].split('_')[0] + "_models_accuracy_"+current_time+".txt"
outfile=open(outfile_name,'w')


if (args.m1):
    print('\nLoading for gensim skip gram model with our "my sentence" code')
    print('Accuracy for gensim by gensim inbuilt converter:')
    outfile.write('\nLoading for gensim' + '\nAccuracy for gensim :')
    wv_model = gensim.models.KeyedVectors.load_word2vec_format(args.w2v_sg)
    accuracies.append(print_accuracy(wv_model, word_analogies_file))

else:
    print('Word2vec model not given or exist')
if (args.m2):
    print('\nLoading for gensim skip gram model with our text8corpus module')
    print('Accuracy for gensim by gensim inbuilt converter:')
    outfile.write('\nLoading for gensim' + '\nAccuracy for gensim :')
    wv_model = gensim.models.KeyedVectors.load_word2vec_format(args.w2v_sg_t8)
    accuracies.append(print_accuracy(wv_model, word_analogies_file))

else:
    print('Word2vec model not given or exist')

if (args.m3):
    print('\nLoading for gensim CBOW model with our "my sentence" code')
    print('Accuracy for gensim by gensim inbuilt converter:')
    outfile.write('\nLoading for gensim' + '\nAccuracy for gensim :')
    wv_model = gensim.models.KeyedVectors.load_word2vec_format(args.w2v_cbow)
    accuracies.append(print_accuracy(wv_model, word_analogies_file))

else:
    print('Word2vec model not given or exist')

if (args.m4):
    print('\nLoading for gensim CBOW model with our text8data corpus module')
    print('Accuracy for gensim by gensim inbuilt converter:')
    outfile.write('\nLoading for gensim' + '\nAccuracy for gensim :')
    wv_model = gensim.models.KeyedVectors.load_word2vec_format(args.w2v_cbow_t8)
    accuracies.append(print_accuracy(wv_model, word_analogies_file))

else:
    print('Word2vec model not given or exist')


if(args.m5):
    print('\nAccuracy for Glove embeddings')
    outfile.write('\nLoading for Glove'+'\nAccuracy for glove :')
    text8_gs = gensim.models.KeyedVectors.load_word2vec_format(args.glove)
    accuracies.append(print_accuracy(text8_gs, word_analogies_file))
else:
    print('Glove model not given or exist')

if(args.m6):
    print('\nLoading for Fasttext')
    text8_ft = gensim.models.KeyedVectors.load_word2vec_format(args.fasttext)
    print('Accuracy for Fasttext (with n-grams):')
    outfile.write('\nLoading for Fasttext'+'\nAccuracy for Fasttext :')
    accuracies.append(print_accuracy(text8_ft, word_analogies_file))
else:
    print('fasttext model not given or exist')



outfile.close()


# python3 models_w2v_variant_accuracy.py --w2v_sg ../../WordEmbeddingModels/gensim/english_text8_w2v_sg_v_400_hs_1_09_apr_18.vec --w2v_sg_t8 ../../WordEmbeddingModels/gensim/english_text8_w2v_sg_t8corpus_v_400_hs_1_09_apr_18.vec --w2v_cbow ../../WordEmbeddingModels/gensim/english_text8_w2v_cbow_v_400_hs_1_09_apr_18.vec --w2v_cbow_t8 ../../WordEmbeddingModels/gensim/english_text8_w2v_cbow_t8corpus_v_400_hs_1_09_apr_18.vec  --glove ../../WordEmbeddingModels/GloveModel/text8_Glove_500_17_Jan_18.vec --fasttext ../../WordEmbeddingModels/FasttextModel/text8_Fasttext_500.vec --eval ../../DataCorpus/English/questions-words.txt
