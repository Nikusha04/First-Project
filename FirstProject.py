my_list = [1, 2, 3, 4, 5]  # creating list with the numbers 1 through 5
print(my_list[2])  # access the third element in a list
print(hex(id(my_list)))

my_list[2] = 10  # modify the second element
print(my_list)
print(hex(id(my_list)))

my_list.append(6)  # appending an element to the end
print(my_list)
print(hex(id(my_list)))

my_list.sort()  # sorting it ascending order
print(my_list)

print(my_list[0:3])  # slicing a list to get the first three element

getSecElements = my_list[0:6:2]  # getting every second element of the list
print(getSecElements)

reversed_list = my_list[::-1]
print(reversed_list)  # reversing a list using slicing

my_list.insert(2, 100)  # inserting the value 100 at the second position
print(my_list)

my_list.sort(reverse=True)  # sorting it descending order
print(my_list)

squares = [number ** 2 for number in my_list]  # list of squares of the numbers coming from my_list
print(squares)

modified_list = []  # creating modified list

for x in my_list:  # using list comprehensions for appending only odd numbers from my_list to modified_list
    if x % 2 == 0:
        modified_list.append(x)

print(modified_list)  # printing this list

mixing_list = my_list + modified_list  # creating new list, which is both my_list and modified_list
print(mixing_list)

mixing_list.sort()  # sorting mixing list
print(mixing_list)

# These are addresses for all three list
print(hex(id(my_list)))
print(hex(id(modified_list)))
print(hex(id(mixing_list)))