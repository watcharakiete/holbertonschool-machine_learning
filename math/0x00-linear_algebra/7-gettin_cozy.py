#!/usr/bin/env python3
"""
Module that concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Needs a matrix as input
    Returns a list of matrices concatenated
    """
    concat = []
    if (len(mat1[0]) == len(mat2[0])) and (axis == 0):
        concat.append([ele.copy() for ele in mat1])
        concat.append([ele.copy() for ele in mat2])
        return concat
    elif len(mat1) == len(mat2):
        concat = [mat1[j] + mat2[j] for j in range(len(mat1))]
        return concat
    else:
        return None