# https://code.google.com/codejam/contest/6364486/dashboard#s=p2

import numpy as np, re

def compute_fun( R,C, matrix, words ):
    def count(arr, word ):
        return len(re.findall(word, str(arr[::-1]))) + len(re.findall(word, str(arr)))

    fun_value = 0
    matrix = np.array(matrix)
    for word in words:
        total_count = 0
        if len(word) <= R:
            for r in range(R):
                total_count += count(matrix[r:,], word)
        if len(word) <= C:
            for c in range(C):
                total_count += count(matrix[:,c], word)
        fun_value += total_count*len(word)

    return fun_value / (R+C)

def get_subgrids(R,C,matrix):
    matrix = np.array(matrix)
    for r in range(R):
        for c in range(C):
            pass

    return