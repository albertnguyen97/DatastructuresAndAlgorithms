# create
my_dict = dict()
my_dict2 = {}
# key and value
my_dict3 = dict(one=1, two=2, three=3)
my_dict4 = {'one': 1, 'two': 2, 'three': 3}
print(my_dict3.values())  # 1 2 3
print(my_dict3.keys())  # one two three
print(my_dict3.items())
# key need to hash() to value

# change/create new key/value

my_dict3['four'] = 4

for key in my_dict3:
    print(key, my_dict3[key])


# search in dict

def searchInDict(input_dict, value):
    for key in input_dict:
        if input_dict[key] == value:
            print(key, value)
    return 'not exist'


searchInDict(my_dict3, 1)

# delete element in dict

my_dict3.pop('one')
my_dict3.popitem()
my_dict3.pop('one', 'two')

# my_dict3.clear() #delete all elements

# set value in dict
my_dict3.setdefault('five', 5)
print(my_dict3)

# update dict
my_dict5 = {'seven': 7}
my_dict3.update(my_dict5)
print(my_dict3)

# sort dict
sorted(my_dict3)

# dict comprehension
list = [1, 2, 3]
new_dict6 = {item: None for item in list}
new_dict7 = {key: value for (key, value) in my_dict3.items()}
