import math
integer = 0
pi=math.pi
while True:
    try:
        integer = float(input("what is the diameter\n"))/2
    except ValueError:
        print("Please, enter a number")
        continue
    else:
        pi = math.pi
        c = 2 * pi * integer
        a = pi * (integer ** 2)
        print(f'circumference = ',c)
        print(f'area = ',a)
        break
