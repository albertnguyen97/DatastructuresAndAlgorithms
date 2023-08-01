# count same element in list add to the dict

def count_word(words):
    # TODO
    my_dict_8 = dict()
    words_set = list(set(words))
    for i in words_set:
        my_dict_8[i] = words.count(i)
    return my_dict_8


# merge two dicts

dict1_1 = {'a': 1, 'b': 2}
dict2_1 = {'a': 2, 'c': 3}


def merge_dict(dict1, dict2):
    for key in dict1.keys():
        if key in dict2.keys():
            dict2[key] += dict1[key]
        else:
            dict2[key] = dict1[key]
    print(dict2)


# max value dict

sorted_list = list(dict1_1.values())
sorted_list.sort(reverse=True)
for key in dict1_1.keys():
    if dict1_1[key] == sorted_list[0]:
        print(key)


# option 2
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


# reverse key_dict

def reverse_dict(my_dict):
    my_dict = {value: key for key, value in my_dict.items()}


# define a conditional

def filter_dict(input_dict, condition):
    input_dict = {k: v for k, v in input_dict.items() if condition(k, v)}
    return input_dict


my_dict = {'a': 4}
filter_dict(my_dict, lambda k, v: v % 2 == 0)


# check same frequency

def check_same_frequency(list1, list2):
    def count_in_list(lst):
        counter = {}
        for key in lst:
            counter[key] = counter[key] + 1
        return counter

    return count_in_list(list1) == count_in_list(list2)
