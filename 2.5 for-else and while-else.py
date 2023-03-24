for xx in [1, 2, 3, 4]:
    print(xx)
else:
    print("All elements are printed.")

# After the operation of for, else block are executed.



for xxx in [1, 2, 3, 4]:
    if xxx % 3:
        print(xxx)
    else:
        break
else:
    print("All elements are printed.")

# In this case, for block are not totally executed. So, else block are also not executed.



countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1
    if input() == 'stop':
        break
else:
    print("Launch!")

# While is also operated by the same way. 