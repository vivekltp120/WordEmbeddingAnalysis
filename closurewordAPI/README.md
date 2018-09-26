# WordVectorTraining
This is to contain training for word vectors

# For closure_word_from_model
Description - It takes the vector file and vocabulary for various model like Word2vec,glove, and fasttext and give the
closure word to the given word file(as input file) or manual input by the user.

To run the script:
python3 ./closure_words_from_model.py --vectors_file='vector file created by various word embedding model'  --vocab_file='vocabulary for the data' --input_file='words for which user required the closure words'
--output_file='output file name for the words'
