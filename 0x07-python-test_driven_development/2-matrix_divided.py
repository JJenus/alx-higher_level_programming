#!/usr/bin/python3

def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    n_mat = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        n_row = []
        for i in row:
            if type(i) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            n_row.append(float("{:.2f}".format(i/div)))
        n_mat.append(n_row)
    return n_mat
