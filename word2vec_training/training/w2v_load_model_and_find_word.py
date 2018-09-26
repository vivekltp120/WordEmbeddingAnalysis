import sys
from gensim.models.keyedvectors import KeyedVectors
model=KeyedVectors.load_word2vec_format(sys.argv[1],binary=False)


if __name__ == "__main__":
    N = 10;          # number of closest words that will be shown
    while True:
        input_term = input("\nEnter word or sentence (EXIT to break): ")
        if input_term == 'EXIT':
            break
        else:
            try:
                words = model.similar_by_word(input_term,10)
                index=model.vocab[input_term].index
                print(index)
                word=model.index2word[index]
                print ('index--'+str(index)+'word--'+str(word))
            except KeyError:
                print("Key not find")