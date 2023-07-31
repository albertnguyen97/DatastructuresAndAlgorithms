import numpy as np

# 1
np_array = np.array([], dtype=int)
print(np_array)
np_array1 = np.array([1, 2, 5, 4])
print(np_array1)

# 2
arr = [1, '1', 3, 4, 6]
print(arr)

# insert
arr.insert(2, 3)
# insert with numpy
new_array = np.insert(np_array1, 3, 10)
print(arr)
print(new_array)
# append with numpy
new_array = np.append(new_array, 3)
print(new_array)


# accessing an element:
def accessElement(array, index):
    if index > len(array):
        print("don't have this index")
    else:
        print(arr[index])


# linear_search element:
def linear_search(array, element):
    for i in range(len(array)):
        if arr[i] == element:
            return i
    return -1


# remove
arr.remove(6)
print(arr)
# remove with numpy
new_array = np.delete(new_array, 0)
print(new_array)