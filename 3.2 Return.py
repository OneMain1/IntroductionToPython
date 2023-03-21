def f1(x):
    a = 3
    b = 5
    y = a * x + b
    return y


c = f1(10)
print(c)




# The function calculates the area of triangle.

def tri_area(a, b):
    base = a
    height = b
    area = base * height / 2
    return area

tri1 = tri_area(3, 6)
print(tri1)



# 3.2.1 Practice problem

def read_number(a):
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return num_list[a - 1]

three = read_number(3)
print(three)



# 3.2.2 Practice problem

# 1
def triple(x):
    return x + x + x

print(triple(2))
print(triple('x'))


# 2
from datetime import datetime

def Korean_age(y):
    age = datetime.today().year - y + 1
    return age

my_age = Korean_age(1997)
print(my_age)




# 3.2.3 Practice problem

# 1
def simple_interest(p, r, t):
    interest = p * r * t
    return interest

print(simple_interest(10000000, 0.03875, 5))


# 2
def simple_interest_amount(p, r, t):
    interest = p * r * t
    return p + interest

print(simple_interest_amount(10000000, 0.03875, 5))



# 3.2.4 Practice problem

def compound_interest_amount(p, r, t, n):
    pp = p * (1 + r / n) ** (n * t)
    return pp

print(compound_interest_amount(1500000, 0.043, 6, 4))


# Done