number = 0
num = [1,2,3]
for x in num:
    if x == 1:
        number += 5
        print(number)
    elif x == 2:
        number -= 2
        print(number)
    elif  x == 3:
        number += number
        print(number)
    else:
        break