from typing import List

def read_integers() -> List[int]:
    a = input()
    b = a.split(',')
    c = []
    for i in b:
       c.append(int(i))
    return c



# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
