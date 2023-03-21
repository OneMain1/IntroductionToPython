# Why do we use funtion in programming? because of simplicity, efficiency and utility.

num_list = [3, 4, 5, 26, 52, 84, 192]
print(len(num_list))

# The example of function is that 'len().'


def print_list(d):
    for i in d:
        print(i)

print_list(num_list)

# My len() function.


def boy():
    print('I am a boy.')
    print('Your are a girl.')

# Second example


def compare(a, b):
    if a > b:
        print('a > b')
    elif a < b:
        print('a < b')
    else:
        print('a == b')

compare(2, 40)

# Third example



# Practice problem 3.1.1
# Make the function that get the positive integer. Then, Print out the number of digits.

def numOfDigits(a):
    print(len(str(a)))

numOfDigits(100)
numOfDigits(10024)
numOfDigits(10014124)



# Practice problem 3.1.2 
# Make the multiplication table

def multi(m):
    n = 1
    for n in range(1, 10):
        print(f'{m} * {n} = {m*n:2d}')

for x in range(1, 10):
    multi(x)

# What is the problem?