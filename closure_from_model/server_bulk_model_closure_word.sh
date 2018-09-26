#!/usr/bin/env bash
#word2vec models closure files
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/spanish/spanish_w2v_line_sg_hs_1_w_5_v_400_i_50_1_may_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/spanish/spanish_w2v_line_sg_hs_1_w_5_v_400_i_50_1_may_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/spanish_closure/spanish_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/albania/albania_w2v_line_sg_hs_1_w_5_v_400_i_50_1_may_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/albania/albania_w2v_line_sg_hs_1_w_5_v_400_i_50_1_may_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/albanian_closure/albanian_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/french/french_w2v_line_sg_hs_1_w_5_v_400_i_5_16_april_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/french/french_w2v_line_sg_hs_1_w_5_v_400_i_5_16_april_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/french_closure/french_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_w2v_sg_v_400_line_sentence_17_apr_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_w2v_sg_v_400_line_sentence_17_apr_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/german_closure/german_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki8__w2v_line_sg_hs_1_w_5_v_400_i_50_16_may_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki8__w2v_line_sg_hs_1_w_5_v_400_i_50_16_may_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/english_closure/english_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/urdu/urdu_update_w2v_500_12_feb_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/urdu/urdu_update_w2v_500_12_feb_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/arabic_closure/arabic_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/arabic/arabic_crawl_oc_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/arabic/arabic_crawl_oc_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/urdu_closure/urdu_frequent_words.txt
#python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/car_model/car_w2v_line_sg_hs_1_w_5_v_400_i_50_18_may_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/car_model/car_w2v_line_sg_hs_1_w_5_v_400_i_50_18_may_18.vec  --profanity_input /media/silpa/vivek/ML_Sep_2017/closurewords/car_closure/car_frequent_words.txt



#glove models closure files
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/swedish/swedish_glove_500_05_feb_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/GloveModel/swedish/swedish_glove_500_05_feb_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/swedish_closure/swedish_frequent_words.txt










#w2v model closure files for hs=0 ns=10 sg=1 v=400
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/spanish/spanish_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/spanish/spanish_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/spanish_closure/spanish_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/albania/albania_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/albania/albania_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/albanian_closure/albanian_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/french/french_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/french/french_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/french_closure/french_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/german/german_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/german_closure/german_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki8_w2v_line_sg_hs_1_w_5_v_400_i_50_16_may_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/english/english_wiki8_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/english_closure/english_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/urdu/urdu_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/urdu/urdu_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/arabic_closure/arabic_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/arabic/arabic_crawl_oc_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/arabic/arabic_crawl_oc_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/urdu_closure/urdu_frequent_words.txt
python3 closure_words_from_model_with_translater.py  --vocab_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/car_model/car_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vocab --vectors_file /media/silpa/vivek/ML_Sep_2017/WordEmbeddingModels/Word2Vec/car_model/car_crawl_w2v_line_sg_hs_0_ns_10_w_5_v_400_i_5_07_june_18.vec  --input_file /media/silpa/vivek/ML_Sep_2017/closurewords/car_closure/car_frequent_words.txt
















exit