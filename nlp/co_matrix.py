#!/usr/bin/env python3

import numpy as np
from common.util import preprocess, cos_similarity

def create_co_occurence_matrix(corpus, vocab_size, window_size=1):

    """
        corpus: list of word id (e.g., [0 1 2 3 4 5 1 5 6] for "you say goodbye and I say hello .").
    """
    corpus_size = len(corpus)
    matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32) # initialize 2d array by zero

    for idx, word_id in enumerate(corpus):
        for i in range(1, window_size + 1):
            left_idx = idx - i
            right_idx = idx + i

            if left_idx >= 0:
                left_word_id = corpus[left_idx]
                matrix[word_id, left_word_id] += 1
            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                matrix[word_id, right_word_id] += 1
    return matrix

if __name__ == '__main__':
    text = "You say goodbye and I say hello."
    corpus, word_to_id, id_to_word = preprocess(text)
    print("corpus:", corpus)
    co_matrix = create_co_occurence_matrix(corpus, len(word_to_id))
    print(co_matrix)

    # cosine similarity を計算してみる
    print('cosine similarities...')
    vec_you = co_matrix[word_to_id['you']]
    vec_I = co_matrix[word_to_id['i']]
    print('you and i:', cos_similarity(vec_you, vec_I))

    vec_hello = co_matrix[word_to_id['hello']]
    print('you and hello:', cos_similarity(vec_you, vec_hello))
    print('i and hello:', cos_similarity(vec_I, vec_hello))
