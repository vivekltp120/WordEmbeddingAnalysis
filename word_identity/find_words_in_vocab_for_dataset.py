#create model and convert it to text vector file..
import os
import re
import time
from string import digits, punctuation

import sys

def word_info(vocab_path,data_path):
    vocab_words=get_word_list(vocab_path)
    data_words=get_word_list(data_path)
    common_words = get_words_in_vocab(vocab_words, data_words)
    oov_list = oov_words(vocab_words, data_words)
    outfile_file.write('\nTotal number of words in particular dataset -' + str(len(data_words)))
    outfile_file.write('\nTotal number of words in vocab for the particular dataset -' + str(len(common_words)))
    outfile_file.write('\nOOV wrt the particular dataset -' + str(len(oov_list)))
    outfile_file.write('\n Words in Vocab - \n' + str(common_words))
    outfile_file.write('\n Words is OOV - \n' + str(oov_list))
    for x in common_words:
        commonwords_file.write(x+'\n')
    commonwords_file.write('EXIT')
def get_words_in_vocab(a,b):
    return list(set(a).intersection(set(b)))

def oov_words(a,b):
    return set(b).difference(set(a).intersection(set(b)))

def get_word_list(path):
    file = open(path, 'r')
    word_list = [x.rstrip().split()[0] for x in file.readlines()]
    return word_list


if __name__=="__main__":
    vocab_path=sys.argv[1]
    data_path=sys.argv[2]
    outfile_file = open('words_info_for_' +os.path.basename(data_path).split('.')[0]+'_in_'+ os.path.basename(vocab_path) + '.txt', 'w')
    commonwords_file = open('common_words_for_' +os.path.basename(data_path).split('.')[0]+'_in_'+ os.path.basename(vocab_path) + '.txt', 'w')
    word_info(vocab_path,data_path)
