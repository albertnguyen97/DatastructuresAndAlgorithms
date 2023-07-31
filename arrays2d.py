import numpy as np

# create array2d
array_2d = np.array([[1, 3, 4], [1, 3, 2], [3, 4, 6]])
print(array_2d)

# insert,append array 2d

new_array_2d_1 = np.insert(array_2d, 2, 3, axis=1)
new_array_2d_2 = np.insert(array_2d, [1, 2], 3, axis=0)

print(new_array_2d_1)
print(new_array_2d_2)
new_array_2d_3 = np.append(array_2d, [[1, 2, 3]], axis=0)

new_array_2d_4 = np.append(array_2d, [[1], [2], [3]], axis=1)
print(new_array_2d_3)
print(new_array_2d_4)


# accessing index array 2d

def accessing_array2d(array, row_index, col_index):
    if row_index >= len(array) and col_index >= len(array[0]):
        print('don\'t have the index ')
    else:
        print(array[row_index][col_index])


# search element array2d
def search_element(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                print(f"have {target} in row {i} column {j}")
            else:
                print(f"don't have the target")


# delete element array2d

deleted_array_2d_col = np.delete(array_2d, 0, axis=1)
deleted_array_2d_row = np.delete(array_2d, 0, axis=0)