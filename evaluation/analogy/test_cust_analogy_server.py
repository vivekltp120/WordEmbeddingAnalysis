import os



#german
# os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_w2v_cbow_500_02_mar_18.vec --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_w2v_cbow_hs_1_w_10_v_500_i_5_10_april_18.vec --m3 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_w2v_cbow_with_t8corpus_hs_1_w_10_v_500_i_5_05_april_18.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_german_w2v_skip_with_t8corpus_500_05_april_18.vocab.txt ')
# os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_telco_original_w2v_alpha_0.025_hs_1_iter_10_min_count_3_negative_10_sample_0.0001_sg_0_size_400_window_5_workers_16_28_Jun_18.vec --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_telco_original_w2v_alpha_0.025_hs_1_iter_10_min_count_3_negative_10_sample_0.0001_sg_1_size_400_window_5_workers_16_28_Jun_18.vec --m3 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/german/german_telco_glove_v_400_X_MAX_10_w_5_i_10_26_june_18.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_german_w2v_skip_with_t8corpus_500_05_april_18.vocab.txt ')
#
#
# #english
# #w2v variant
# os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki12GB_w2v_line_cbow_hs_1_ns_0_w_5_v_300_i_1_14_june_18.vec --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki12GB_w2v_line_sg_hs_0_ns_5_w_5_v_300_i_5_14_june_18.vec --m3 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki8_w2v_line_cbow_hs_1_ns_0_w_5_v_400_i_5_08_june_18.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/evaluation/evaluation_inventory/various/profanity_en_de_txt.txt_eval.txt')
# # #different WEM models
# os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki12GB_w2v_line_cbow_hs_1_ns_0_w_5_v_300_i_1_14_june_18.vec --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/english/english_wiki12GB_glove_v_300_i_5_w_5_15_june_18.txt --m3 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/FasttextModel/english/english_wiki_fasttext_sg_ns_5_i_5_v_300_16_june_18.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/evaluation/evaluation_inventory/various/profanity_en_de_txt.txt_eval.txt')
# # #different data models
# os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/existing_wem/iamplus_en_amz-stack-others_400.model.vec --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/english/English_Amazon_Glove_aa_500_19_Jan_2018.vec --m3 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/existing_wem/GoogleNews_vectors_negative300.bin.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/evaluation/evaluation_inventory/various/profanity_en_de_txt.txt_eval.txt')



#for words which are present in vocab


#german
#
#
# #english
# profanity_en_de_txt
# os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki12GB_w2v_line_cbow_hs_1_ns_0_w_5_v_300_i_1_14_june_18.vec --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki12GB_w2v_line_sg_hs_0_ns_5_w_5_v_300_i_5_14_june_18.vec --m3 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki8_w2v_line_cbow_hs_1_ns_0_w_5_v_400_i_5_08_june_18.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_english_wiki12GB_w2v_line_cbow_hs_1_ns_0_w_5_v_300_i_1_14_june_18.vocab.txt')
# #different WEM models
os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/english/english_wiki12GB_glove_v_300_i_5_w_5_15_june_18.txt --m2 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/FasttextModel/english/english_wiki_fasttext_sg_ns_5_i_5_v_300_16_june_18.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_english_wiki12GB_w2v_line_cbow_hs_1_ns_0_w_5_v_300_i_1_14_june_18.vocab.txt')
# #different data models
os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/existing_wem/iamplus_en_amz-stack-others_400.model.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_iamplus_en_amz-stack-others_400.model.vocab.txt ')
os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/english/English_Amazon_Glove_aa_500_19_Jan_2018.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_english_amazon_glove_aa_500.vocab.txt  ')
os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/existing_wem/GoogleNews_vectors_negative300.bin.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_GoogleNews_vectors_negative300.vocab.txt')
os.system('python3 general_custom_analogy.py --m1 /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/amazon_english_size_400_window_5_iter_5_min_count_3_sg_1_hs_0_negative_10.vec --eval /media/silpa/vivek/ML_Sep_2017/WordVectorTraining/words_identification/profanity/common_words_for_profanity_en_de_txt_in_english_wiki12GB_w2v_line_cbow_hs_1_ns_0_w_5_v_300_i_1_14_june_18.vocab.txt')



