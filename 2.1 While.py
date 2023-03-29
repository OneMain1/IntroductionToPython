#num = 1
#num2 = 1
#while num <= 100:
#    print(num, end='\n')
#    num = num + 1
#    num2 += 1


# Practice problem 1

num = int(input())

i = 0

while i < num:
    print(num, end = '\n')
    i += 1


# Practice problem 2

num2 = int(input())

j = 1

while j <= num2:
    print(j, j * j, end = '\n')
    j += 1


# Practice problem 3

num3 = 100
k = 0

while k < 10:
    print(k + 1, round(num3 * 3 / 5, 4))
    k += 1;
    num3 = num3 * 3 / 5


# Practice problem 4

# What is the correct result of excuting below the code?

number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

print(rev)

#rem = 8
#rev = 8
#number = 35

#rem = 5
#rev = 85
#number = 3

#rem = 3
#rev = 853
#number = 0

#853
