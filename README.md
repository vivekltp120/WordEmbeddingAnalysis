# WordVectorTraining
This is to contain training for word vectors and all the other 
research and experiment script for various word embedding models.





#any_w2v_model_training.py

This file train the word2vec model with following parameter in script predefined you can change:
#vector_size=500, alpha=0.05, window=10, min_count=3, sample=0.001, seed=1, workers=32, min_alpha=0.0001, sg=0, hs=0,negative=5, cbow_mean=1, iter=100
   negative=5, cbow_mean=1, iter=100

#Command For Linux:
   python3 any_w2v_model_training.py <path_for_data_corpus> <output_file_name>

#Output:
    1.word vector file for data - output_file_name.vec
    2.vocabulary for data -   output_file_name.vocab



#model_acuracy.py

This file evaluate the accuracy of the word embedding models(word2vec,glove,fasttext) :
#Command For Linux:
   python3 models_accuracy.py --eval <'path to evaluation file'> --w2v <'path to w2v model'> --glove <'path to glove model'> --fasttext <'path to fasttext model'>


#Output:
   print out the semantic and syntatic accuracy of model


#closure_words_from_model
This is the file which take input words file and give the closure words of that file

#Command For Linux:
   python3 closure_words_from_model --vectors_file <'word embedding file'> --vocab_file <'vocabulary file of model'> --input_file <'evaluation file'>
   

#Output:
    1.closure words file for the given words




