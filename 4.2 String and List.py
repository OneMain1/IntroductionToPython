# String

from re import L


x = 'banana'
print(x[0])

# [i:j] means that the part from [i] to [j - 1].
print(x[2:4])

# [:j] means that the part from [0] to [j - 1].
print(x[:3])

# [i:] means that the part from [i] to end.
print(x[3:])


# The alphabet in the string cannot be changed.
# x[0] = 'n'
# Error!

# Possible!
x = 'n' + x[1:]


# find(): finds the first occurrence of the specified value.
s = "hello Python!"
sf = s.find('P')
print(sf)

s1 = "Hello Python python Python!"
sf1 = s1.find('P')
sf11 = s1.find('p')
print(sf1)
print(sf11)



# strip([chars]), lstrip([chars]), rstrip([chars])
text = ' Water boils at 100 degrees '

print('[' + text.rstrip() + ']')
print('[' + text.lstrip() + ']')
print('[' + text.strip() + ']')

print(text.split()[0])
print(text.split()[1])





# List


# append(): add the element at the end of the list.
prime = [3, 7, 11]
prime.append(5)
print(prime)


# sort(): sort the list.
prime.sort()
print(prime)


# insert(index, element): insert the element at the index of the list.
prime.insert(0, 2)
print(prime)

# del: delete the element of the list.
del prime[4]
print(prime)

# pop(): pop the last element of the list.
a = prime.pop()
print(prime)
print(a)

# Allocating new value is possible.
prime[0] = 1
print(prime)

# The list in the list.
orders = ['potato', ['pizza', 'Coke', 'salad'], 'hamburger']
print(orders[1])
print(orders[1][2])


# Can express the matirx with list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Change a string to a list.
characters = []             # list
sentence = 'Be happy!'      # string
for char in sentence:
    characters.append(char)

print(characters)



# Get a string from the number.
my_int = 123
print(type(my_int))
print(str(my_int))


# Get a number from the string.
print(int('123'))


# The sum of the element in the list.
one_to_ten = list(range(1, 11))
print(one_to_ten)

print(sum(one_to_ten))




# Problem 4.2.1

# 1

def digits(num):
    str1 = str(num)
    # print(str1)
    list1 = []
    for char in str1:
        list1.append(int(char))
    # print(list1)
    return list1

num1 = int(input())

print(sum(digits(num1)))


def sumOfDigits(num):
    sum = 0
    for c in list(str(num)):
        sum += int(c)

    return sum




# Problem 4.2.2

# 1

score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
print(score)

stem_leaf = [[],[],[]]
stem_leaf2 = [[],[],[]]

for num in score:
    stem = num // 10
    leaf = num - (10*stem)
    stem_leaf[stem].append(leaf)

for num in score:
    stem, leaf = divmod(num, 10)
    stem_leaf2[stem].append(leaf)

print(stem_leaf)
print(stem_leaf2)


# 2

for i in range(len(stem_leaf)): 
    print(f'{i}: {stem_leaf[i]}')


# f-string formatting
month = 1
while month <= 12:
    print(f'2020, {month}')
    month = month + 1




# Problem 4.2.3

#1

# using map()
def sumOfDigitss(num):
    digits = map(int, list(str(num)))
    return sum(digits)

print(sumOfDigitss((int(input()))))




# Problem 4.2.4

