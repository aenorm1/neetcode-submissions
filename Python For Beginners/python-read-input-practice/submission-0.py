def add_two_numbers() -> int:
    a = input()
    b = a.split(',')
    c = []
    for i in b:
        c.append(int(i))
    d = sum(c)
    return d



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
