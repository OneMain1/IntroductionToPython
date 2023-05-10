# Tuple utilization

c = 20
d = 10
c, d = d, c

print(c, d)



# *parameter -> insert this into tuple

def magu_print(x, y, *rest):
    print(x, y, rest)

magu_print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# output: 1 2 (3, 5, 6, 7, 9, 10)


# Grammar of tuple

t = ('a', 'b', 'c')
t1 = 'a', 'b', 'c'

print(t)
print(t1)

empty = ()



# tuple with only one element.
one = 5,

print(one)



# List -> changeable, Tuple -> unchangeable

p = (1, 2, 3)
q = p[:1] + (5, ) + p[2:]
print(q)

r = p[:1], (5,), p[2:]
print(r)


p = (1, 2, 3)
q = list(p)

print(q)

r = tuple(q)
print(r)



# Problem 4.3.1

# 1

# Pass