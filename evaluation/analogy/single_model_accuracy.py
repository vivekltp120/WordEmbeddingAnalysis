

#Create the word to vec model for the data
#create model and convert it to text vector file..
import gensim
import argparse
import sys
import datetime
import logging


current_time= datetime.datetime.now().strftime('%d_%b_%y')

def print_accuracy(model, questions_file):
    print('Evaluating...\n')
    try:
        acc = model.accuracy(questions_file,restrict_vocab=1000030)
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
    except ZeroDivisionError:
        print ("ZeroDivisionError")
    return (sem_acc, syn_acc)


word_analogies_file = '/home/vivek/ML_Sep_2017/DataCorpus/English/questions-words-modified.txt'
accuracies = []

parser = argparse.ArgumentParser()
parser.add_argument('--eval', default=None, type=str)
parser.add_argument('--model', default=None, type=str)
args = parser.parse_args()

word_analogies_file=args.eval
model_name=args.model
split_model_name=model_name.split('/')[::-1][0].split('_')
outfile_name=word_analogies_file.split('/')[::-1][0].split('_')[0].split('.')[0] + "_models_accuracy_"+current_time+".txt"
# model_name=split_model_name[0]+'_' + split_model_name[1] + "_models_accuracy_"+current_time+".txt"
model_name=split_model_name[0]+'_'+ "_models_accuracy_"+current_time+".txt"
outfile=open(outfile_name,'w')
logging.basicConfig(filename=outfile_name,format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if(args.model):
    print('\nAccuracy for the model -- '+ str(model_name) )
    outfile.write('\nLoading the model'+'\nAccuracy for model :' + str(model_name))
    text8_gs = gensim.models.KeyedVectors.load_word2vec_format(args.model,binary=True)
    accuracies.append(print_accuracy(text8_gs, word_analogies_file))
else:
    print('Model not exist')


outfile.close()