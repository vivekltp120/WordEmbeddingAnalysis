import os
# os.system('python3 custom_analogy_pair_from_word_file.py /home/vivek/ML_Sep_2017/WordVectorTraining/evaluation/evaluation_inventory/various/profanity_en_de_txt.txt  ')
os.chdir('/home/vivek/ML_Sep_2017/WordVectorTraining/evaluation/analogy')
os.system('python3 general_custom_analogy.py --m1 /home/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_w2v_cbow_hs_1_w_10_v_500_i_5_10_april_18.vec --eval /home/vivek/ML_Sep_2017/WordVectorTraining/evaluation/evaluation_inventory/various/profanity_en_de_txt.txt_eval.txt')