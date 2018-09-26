import gensim
import argparse
import sys
import datetime
import logging


current_time= datetime.datetime.now().strftime('%d_%b_%y')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


parser = argparse.ArgumentParser()
parser.add_argument('--eval', default=None, type=str)
parser.add_argument('--model', default=None, type=str)
args = parser.parse_args()

word_analogies_file=args.eval
model_name=args.model
split_model_name=model_name.split('/')[::-1][0].split('_')
outfile_name=word_analogies_file.split('/')[::-1][0].split('_')[0] + "_models_accuracy_"+current_time+".txt"
model_name=split_model_name[0]+'_' + split_model_name[1] + "_models_pso_accuracy_"+current_time+".txt"
outfile=open(model_name,'w')

model = gensim.models.KeyedVectors.load_word2vec_format(args.model)

pearson, spearman, oov_ratio=model.evaluate_word_pairs(word_analogies_file,delimiter=',',case_insensitive=False)
print(pearson, spearman, oov_ratio)
outfile.write('Pearson-'+str(pearson)+'Spearman-'+str(spearman)+'OOV-'+str(oov_ratio))
# model.evaluate_word_pairs('play','cricket')

