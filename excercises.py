
# missing number in arr:
def missing_number(arr, n):
    total = n * (n + 1)
    sum_arr = sum(arr)
    missing = total - sum_arr
    return missing


# find max_product
def max_product(arr):
    arr.sort(reverse=True)
    return arr[0] * arr[1]


def middle1(lst):
    lst.pop(0)
    lst.pop(len(lst) - 1)
    return lst


# or

def middle2(lst):
    return lst[1:-1]


# diagonal sum array2d
def diagonal_sum(arr):
    sum_arr = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sum_arr = sum_arr + arr[i][j]
    return sum_arr


# find best score in list:
def first_second(my_list):
    my_list.sort(reverse=1)
    return my_list[0:2]


# remove same element


def remove_duplicates(arr):
    arr1 = list(set(arr))
    return arr1


# compare with sum
def pair_sum(myList, sum_list):
    new_list = []
    for i in range(len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum_list:
                new_list.append(str(myList[i]) + "+" + str(myList[j]))
    return new_list


# contains same element


def contains_duplicate(nums):
    new_list = list(set(nums))
    if new_list == nums:
        return False
    else:
        return True


# rotate matrix

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix