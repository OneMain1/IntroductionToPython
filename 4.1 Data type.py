# type()

print(type(6))
print(type('A'))


a = 100_000_000
print(a)
print(type(a))



# Numbers

## int
print(type(100))

## float
print(type(3.6))

## complex
print(type(3+4j))
# print(type(3+4i)), 'i' cannot be used in complex data type.
print((1j) ** 2)


# Sequence

## str
print(type("Love your enemies, for they tell you your Faults."))

## list
print(type(['love', 'enemy', 'fault']))

## tuple
print(type(('love', 'enemy', 'fault')))


# Slicing

p = 'Python'
print(p[0:2])
print(p[:2])
print(p[-2:])
print(p[:])
print(p[::-1])



# Mapping (dictionary, key and value)

print(type({'one' : 1, 'two' : 2, 'three' : 3}))


# Bool

print(type(False))
print(type(3 >= 1))
print(type(True == 'True'))


# Set

fruits = {'apple', 'banana', 'orange'}



# 4.1.1 Problems

## Problem 1    [::0-1]

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome('anna'))
print(palindrome('banana'))


## Problem 2    str.lower()

def palindrome_with_lower(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

print(palindrome_with_lower('Anna'))


## Problem 3    str.replace('', '')

def palindrome_with_lower_except_blank(word):
    word = word.replace(' ', '')
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False

print(palindrome_with_lower_except_blank('My gym'))