# example

carList = ['BMW', 'MAZDA', 'TOYOTA', 'AUDI', 'HUYNDAI']
print(carList[1])
mylist = list()
# insert

carList.insert(3, 'MERCEDES')
print(carList)
# append
carList.append('SUZUKI')


# change element

def changeIndex(input_list, index, target):
    input_list[index] = target
    print(input_list)


changeIndex(carList, 1, 'PORSCHE')

# delete
del carList[0:1]
carList.pop(1)
carList.remove('SUZUKI')

# extend
newList = ['ROLL ROYCE']
carList.extend(newList)
print(carList)


# searching:
def searchInList(input_list, target):
    if target in input_list:
        print(f"have {target} in the list")
    else:
        print("don\'t have the target !")
    # enumerate
    for i, value in enumerate(input_list):
        if value == target:
            return i
    return -1


searchInList(carList, 'ROLL ROYCE')

while True:
    input_string = input("Enter string:")
    if input_string == 'done': break
    mylist.append(input_string)

print(mylist)

# split
string_line = 'a-b-c-d-e'
new_split_list = string_line.split('-')
# new_split_list.sort()
print(new_split_list)
new_list_2 = [i for i in new_split_list]
new_list_3 = [i for i in new_split_list if i == 'a']
print(new_list_2)
print(new_list_3)