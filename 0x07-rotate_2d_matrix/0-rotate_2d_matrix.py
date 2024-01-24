#!/usr/bin/python3
"""Implement rotate_2d_matrix function"""

import copy


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in place by 90 degrees clockwise.

    Args:
        matrix (list of lists): The 2D matrix to be rotated.

    Returns:
        None
    """

    cp_mx = copy.deepcopy(matrix)

    row_number = 0

    index = 0

    len_mtx = (len(matrix) - 1)

    while index <= len_mtx:
        index_cp_mx = (len(matrix) - 1)

        for row in matrix:
            row[len_mtx - index] = cp_mx[row_number][len_mtx - index_cp_mx]
            index_cp_mx -= 1

        row_number += 1
        index += 1
