#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    n_matrx = []
    for row in matrix:
        n_row = []
        for col in row:
            n_row.append(col**2)
        n_matrx.append(n_row)
    return n_matrx
