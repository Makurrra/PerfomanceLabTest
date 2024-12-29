n = int(input("n = "))
m = int(input("m = "))
i = 1
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break