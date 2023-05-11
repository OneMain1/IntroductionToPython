dic = {}

dic['a'] = 'A'
dic['b'] = 'B'

print(dic['a'])


smalldic = {'dictionary': 'reference', 'python': 'snake'}
print(smalldic['python'])



# delete the element

del smalldic['dictionary']



# dict -> list

family = {'boy': 'choi', 'girl': 'kim', 'baby': 'choi'}

family_keys = family.keys()
family_values = family.values()

print(family_keys)
print(family_values)



# in, dict

print('boy' in family)
print('sister' in family)


# Problem 4.4.1

# 1, Pass


# Problem 4.4.2

# 1, Pass

# ord() chr()

print(ord('A'))

print(chr(65))


# split(), splitlines()

print('hello world'.split())

love = '''L is for the way you look at me
O is for the only one I see
V is very, very extraordinary
E is even more than anyone that you adore can'''

print(love.split('\n'))
print(love.splitlines())




# Problem 4.4.3

# 1

rule = {}
rule = {'111'}

colwidth = 31
rule90 = {'000':'0', '001':'1', '010':'0', '011':'1', '100':'1', '101':'0', '110':'1', '111':'0'}

half = colwidth // 2
line11 = '0' * half + '1' + '0' * half
print(line11)

while line11[1] == '0':
    prev = line11
    line11 = '0' * colwidth
    for i in range(1, colwidth - 1):
        line11 = line11[:i] + rule90[prev[i-1:i+2]] + line11[i+1:]
    print(line11)