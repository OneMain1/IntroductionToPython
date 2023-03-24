def hap(x, y):
    return x + y
print(hap(10, 20))



(lambda x,y: x + y) (10, 20)
print((lambda x, y: x + y) (10, 20))



exlist = list(map(lambda x: x ** 2, range(5)))
print(exlist)



# reduce apply the sequence to the function cumulatively

from functools import reduce
value1 = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
print(value1)

value2 = reduce(lambda x, y: x + y, 'abcde')
print(value2)

value3 = reduce(lambda x, y: y + x, 'abcde')
print(value3)




value4 = list(filter(lambda x: x < 5, range(10)))
print(value4)

value5 = list(filter(lambda x: x % 2, range(10)))
print(value5)




# 3.5.1

# Practice problem

def read(text):
    ridename, limit = map(str.strip, text.split(':'))
    
    cmmin = cmmax = None
    if '~' in limit:
        cmmin, cmmax = map(lambda x: int(x.replace('cm', '')), limit.split('~'))
    elif "higher" in limit:
        cmmin = int(limit.split("cm")[0])

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    print("name: ", ridename)
    print("lower bound: ", cmmin)
    print("upper bound: ", cmmax)