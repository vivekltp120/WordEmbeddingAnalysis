

#Create the word to vec model for the data
#create model and convert it to text vector file..
import gensim
import argparse
import sys
import datetime
import logging
import os
from itertools import combinations

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
common_file_name='eval.temp'
current_time= datetime.datetime.now().strftime('%d_%b_%y_%H_%M')
#get combination of words for particular words
def get_combination_of_words(efile):
    inpath = (os.path.split(efile)[0])
    filename = os.path.basename(efile)
    inputfile = open(efile, 'r')
    outfile = open(common_file_name, 'w')
    wordlist = [x.strip() for x in inputfile.readlines()]
    print(wordlist)
    outfile.write(': no relation between pair of words' + '\n')
    outline = combinations(wordlist, 4)
    count = 0
    for i in outline:
        print(i)
        words = ' '.join(i)
        outfile.write(words + '\n')
        count += 1
        if count == 200000:
            break
    outfile.close()


#output file name
def get_file_name(model_path):
    outfile_eval='output.temp'
    if model_path:
        m1=os.path.basename(model_path)
        print(m1)
        outfile_eval = m1+'_'+ "_custom_accuracy_" + current_time + ".txt"

    return outfile_eval
# write the content on file
def write_to_file(fp,content):
     fp.write(content)

def load_and_print_accuracy(mPath, questions_file):
    print('\nAccuracy for Model - ')
    write_to_file(outfile,'\nAccuracy for Model - '+ os.path.basename(mPath))
    model = gensim.models.KeyedVectors.load_word2vec_format(mPath)
    acc = model.accuracy(questions_file,restrict_vocab=3000000,case_insensitive=False)
    print(acc)
    try:
        sem_correct = sum((len(acc[i]['correct']) for i in range(1)))
        sem_total = sum((len(acc[i]['correct']) + len(acc[i]['incorrect'])) for i in range(1))
        sem_acc = 100*float(sem_correct)/sem_total
        print('\nSemantic: {:d}/{:d}, Accuracy: {:.2f}%'.format(sem_correct, sem_total, sem_acc))
        write_to_file(outfile,'\nSemantic: {:d}/{:d}, Accuracy: {:.2f}%'.format(sem_correct, sem_total, sem_acc))
    except ZeroDivisionError:
        write_to_file(outfile,'\nZeroDivisionError '+'\nsem_correct '+str(sem_correct)+'\nsem_total '+str(sem_total))


    # return (sem_acc)


# word_analogies_file = '/home/vivek/ML_Sep_2017/DataCorpus/English/questions-words-modified.txt'
accuracies = []

parser = argparse.ArgumentParser()
parser.add_argument('--eval', default=None, type=str)
parser.add_argument('--m1', default=None, type=str)
parser.add_argument('--m2', default=None, type=str)
parser.add_argument('--m3', default=None, type=str)
args = parser.parse_args()

word_analogies_file=args.eval

outfile_name=os.path.basename(word_analogies_file) + "_analogy_accuracy_"+current_time+".txt"
outfile=open(outfile_name,'w')


get_combination_of_words(word_analogies_file)


if(args.m1):
    accuracies.append(load_and_print_accuracy(args.m1, common_file_name))
else:
    print('Model not given or exist')

if(args.m2):
    accuracies.append(load_and_print_accuracy(args.m2, common_file_name))
else:
    print('Model not given or exist')


if(args.m3):
    accuracies.append(load_and_print_accuracy(args.m3, common_file_name))
else:
    print('Model not given or exist')

os.system('rm eval.temp')
outfile.close()