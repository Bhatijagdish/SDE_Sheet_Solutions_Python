import sys
import numpy as np


def set_matrix_zero(matrix):
    dummy_rows = []
    dummy_cols = []
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    for index in range(total_rows):
        dummy_rows.append(1)
    for index in range(total_cols):
        dummy_cols.append(1)
    for rows in range(total_rows):
        for cols in range(total_cols):
            if matrix[rows][cols] == 0:
                dummy_rows[rows] = 0
                dummy_cols[cols] = 0

    for rows in range(total_rows):
        for cols in range(total_cols):
            if dummy_rows[rows] == 0 or dummy_cols[cols] == 0:
                matrix[rows][cols] = 0

    return matrix


if __name__ == '__main__':
    matrix = sys.argv[1]
    limit = int(sys.argv[2])
    sys_arr = matrix.split(",")
    for i in range(len(sys_arr)):
        sys_arr[i] = int(sys_arr[i])
    test_array = np.array(sys_arr)
    new_arr = test_array.reshape(limit, int(len(sys_arr)/limit))
    print(f"After changing the rows and cols to zeros new matrix is:\n{set_matrix_zero(new_arr)}")
