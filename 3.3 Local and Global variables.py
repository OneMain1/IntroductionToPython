from cmath import e


jjang = '09'                    # global variable
jjang = 'pig dad'               # global variable

print(jjang)

def ban():
    jjang = '07'                # local variable
    print('jjang = ', jjang)

ban()


def d_is_10():
    d = 10
    print('A value of d is ', d)


d_is_10()


x = 10
def printx():
    print(x)

printx()


def e_is_10():
    global e
    e = 10
    print('A value of e is', e)


e_is_10()
print(e)