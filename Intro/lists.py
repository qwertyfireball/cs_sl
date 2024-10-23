my_list = [
    3,
    4,
    5,
    6,
]
print(list)
print(type(list))
print(len(my_list))

# iterate over list values
for i in my_list:
    print(i)


# idicies and values
def print_list(l: list):
    for v, i in enumerate(my_list):
        print(f"mylist[{i}] = {v}")


for v, i in enumerate(my_list):
    print(f"l[{i}] = {v}")

# modifying elements
my_list[3] = 39
print_list(my_list)

# reference to an index
last = len(my_list) - 1
my_list[last] = -10
print_list(my_list)

# emptying a list
my_list.clear()
print_list(my_list)

# putting things at back of list
for i in range(10, 21):
    my_list.append(i)

# remove last element:
my_list.pop()

# removes at provided index
my_list.pop(3)

# remove the provided value if found, only removes first instance
my_list.remove(6)

# try and find the value
idx = my_list.index(5)
print(idx)

# add one list to the other
list_a = [4, 5, 45, 439]
list_b = [32, 34, 5, 64, 3]
list_c = list_a.__add__(list_b)

# multiplication in list
my_list = [1, 2, 4] * 10
print(my_list)

# for loop in list
my_list = [i for i in range(1, 31)]
print(my_list)

# excluding for loop in list
enclude = [7, 2, 11]
my_list = [i for i in range(1, 31) if i not in enclude]
print(my_list)


def transform(i: int):
    while i > 1 and i % 2 == 0:
        i //= 2
    if i == 1:
        return "power of two"
    else:
        return "no"


# shuffle list
my_list = [i for i in range(1, 31)]
from random import shuffle

shuffle(my_list)

#sort
my_list.sort()
print(my_list)

#slicing in string
my_list = [i for i in range(1, 31)]
sublist = my_list[10:]
sublist = my_list[:15]
sublist = my_list[::2]
sublist = my_list[5:25]
sublist = my_list[5:25:2]