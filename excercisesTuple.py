# sum multi elements
def sum_multi(input_tuple):
    # TODO
    sum_elements = 0
    multi_elements = 1
    for i in input_tuple:
        sum_elements += i
        multi_elements *= i
    return sum_elements, multi_elements


# sum 2 tuples

def zip_tuple(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Error!")
    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result


# insert tuple

def insert_value_front(input_tuple, value_to_insert):
    lst = list(input_tuple)
    lst.insert(0, value_to_insert)
    return tuple(lst)


def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple


# connect element in tuple:

def connect_strings(input_tuple):
    return ' '.join(input_tuple)


# get diagonal in tuple:
def get_diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))

# same elements in tuple:


def same_elements(tuple1, tuple2):
    return tuple([i for i in tuple1 if i in tuple2])


def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))