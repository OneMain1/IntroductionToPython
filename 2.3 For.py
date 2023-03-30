from re import L


family = ['mother', 'father', 'gentleman', 'lady']

for x in family:
    print(x, len(x))


# range()

print(list(range(2, 7)))


a = [4, 5, 6, 7, 8]
for i in a:
    print(i)


# Problem 1

a = int(input())

for i in range(0, a):
    print(a)



# Problem 2

b = int(input())

for i in range(0, b):
    print(i + 1, (i + 1) ** 2)



# Problem 3, str.split()

lower, upper = input().split()

while True:
    a = int(input())
    if a >= 0 and a <= 100:
        print('Nothing to report')
    else:
        print('Alert!')
        break