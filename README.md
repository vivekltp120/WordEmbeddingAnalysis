# Word Embedding Models

This repository contains scripts for training and evaluating word embedding models. It includes training for Word2Vec, GloVe, and FastText, as well as evaluating their performance and generating closure words from the trained models.

## Overview

### Scripts Included

1. **`any_w2v_model_training.py`**: Trains a Word2Vec model with customizable parameters.
2. **`models_accuracy.py`**: Evaluates the accuracy of Word2Vec, GloVe, and FastText models.
3. **`closure_words_from_model.py`**: Generates closure words based on a given word embedding file.

---

## Script Details

### `any_w2v_model_training.py`

This script trains a Word2Vec model with the following predefined parameters. You can modify these parameters directly in the script:

- `vector_size=500`
- `alpha=0.05`
- `window=10`
- `min_count=3`
- `sample=0.001`
- `seed=1`
- `workers=32`
- `min_alpha=0.0001`
- `sg=0`
- `hs=0`
- `negative=5`
- `cbow_mean=1`
- `iter=100`

#### Command for Linux

```bash
python3 any_w2v_model_training.py <path_for_data_corpus> <output_file_name>


Output
Word Vector File: output_file_name.vec - Contains the trained word vectors.
Vocabulary File: output_file_name.vocab - Contains the vocabulary of the model.





Certainly! Below is a detailed README.md file incorporating the information you provided about training word vectors and evaluating word embedding models. This version includes the description of each script, command-line instructions, and the expected outputs.

markdown
Copy code
# Word Embedding Models

This repository contains scripts for training and evaluating word embedding models. It includes training for Word2Vec, GloVe, and FastText, as well as evaluating their performance and generating closure words from the trained models.

## Overview

### Scripts Included

1. **`any_w2v_model_training.py`**: Trains a Word2Vec model with customizable parameters.
2. **`models_accuracy.py`**: Evaluates the accuracy of Word2Vec, GloVe, and FastText models.
3. **`closure_words_from_model.py`**: Generates closure words based on a given word embedding file.

---

## Script Details

### `any_w2v_model_training.py`

This script trains a Word2Vec model with the following predefined parameters. You can modify these parameters directly in the script:

- `vector_size=500`
- `alpha=0.05`
- `window=10`
- `min_count=3`
- `sample=0.001`
- `seed=1`
- `workers=32`
- `min_alpha=0.0001`
- `sg=0`
- `hs=0`
- `negative=5`
- `cbow_mean=1`
- `iter=100`

#### Command for Linux

```bash
python3 any_w2v_model_training.py <path_for_data_corpus> <output_file_name>
Output
Word Vector File: output_file_name.vec - Contains the trained word vectors.
Vocabulary File: output_file_name.vocab - Contains the vocabulary of the model.







models_accuracy.py
This script evaluates the accuracy of different word embedding models (Word2Vec, GloVe, FastText).

Command for Linux
python3 models_accuracy.py --eval <'path to evaluation file'> --w2v <'path to w2v model'> --glove <'path to glove model'> --fasttext <'path to fasttext model'>



Output
Prints out the semantic and syntactic accuracy of the provided models.



closure_words_from_model.py
This script takes an input words file and generates closure words based on the provided word embedding file and vocabulary file.

Command for Linux
python3 closure_words_from_model.py --vectors_file <'word embedding file'> --vocab_file <'vocabulary file of model'> --input_file <'evaluation file'>
Output
Closure Words File: Contains the closure words for the given words from the input file.






