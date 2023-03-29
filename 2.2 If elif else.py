a = 1234 * 4
b = 13456 / 2

if a > b:
    print('a')
else:
    print('b')



c = 15 * 5
d = 15 * 3 + 30

if c > d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c < d:
    print('c is less than d')
else:
    print('I don\'t know')


max = 10

while True:
    num = int(input())
    if num > max:
        print(num, 'is too big!')
        break



# Practice problem 1

num = int(input())

if num == 1:
    print('one')
elif num == 2:
    print('two')
elif num == 3:
    print('three')
else:
    print('not defined')


# Practice problem 2

age2 = int(input('What year were you born? '))

if age2 <= 1924:
    print('You\'re The Greatest Generation')
elif age2 <= 1945:
    print('You\'re The Silent Generation')
elif age2 <= 1964:
    print('You\'re a baby boomer')
elif age2 <= 1980:
    print('You\'re a Gen X')
elif age2 <= 1996:
    print('You\'re millennial')
else:
    print('You\'re a Gen Z')


# Practice problem 3

num3 = int(input())
result3 = str(num3)

if num3 >= 1000000000:
    num3 = num3 // 1000000000
    result3 = str(num3) + 'G'
elif num3 >= 1000000:
    num3 = num3 // 1000000
    result3 = str(num3) + 'M'
elif num3 >= 1000:
    num3 = num3 // 1000
    result3 = str(num3) + 'K'

print(result3)


# Practice problem 4

result4 = 0

while True:
    num4 = int(input())
    if num4 < 0:
        break;
    else:
        result4 += num4

print(result4)


# Practice problem 5

num5 = int(input())

if num5 % 4 == 0:
    if num5 % 100 == 0:
        if num5 % 400 == 0:
            print(num5, 'year is leap year.')
        else:
            print(num5, 'year is not leap year.')
    else:
        print(num5, 'year is leap year.')
else:
    print(num5, 'year is not leap year.')


# Another answer

if num5 % 4 != 0:
    print(num5, 'year is not leap year.')
elif num5 % 100 != 0:
    print(num5, 'year is leap year.')
elif num5 % 400 != 0:
    print(num5, 'year is not leap year')
else:
    print(num5, 'year is leap year')


# and/or

a = 3
b = 0

(a * b) > 0 and (a / b) > 0     # It is okay.
# (a / b) > 0 and (a * b) > 0   # It is not okay.


# in

s = 'banana'
if 'a' in s:
    print('\'banana\' is include \'a\'')


# Practice problem 6

age3 = int(input('What year were you born? '))
nationality = str(input('Are you Korean? '))

if nationality == 'n':
    if age3 <= 1924:
        print('You\'re The Greatest Generation')
    elif age3 <= 1945:
        print('You\'re The Silent Generation')
    elif age3 <= 1964:
        print('You\'re a baby boomer')
    elif age3 <= 1980:
        print('You\'re a Gen X')
    elif age3 <= 1996:
        print('You\'re millennial')
    else:
        print('You\'re a Gen Z')
elif nationality == 'y':
    if age3 <= 1924:
        print('You\'re The Greatest Generation')
    elif age3 <= 1954:
        print('You\'re The Silent Generation')
    elif age3 <= 1963:
        print('You\'re a baby boomer')
    elif age3 <= 1980:
        print('You\'re a Gen X')
    elif age3 <= 1996:
        print('You\'re millennial')
    else:
        print('You\'re a Gen Z')
else:
    print()