#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            k = element*element
            print(" ".join("{:d}".format(k)))
