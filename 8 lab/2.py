def Fibbo(n):
    current, next = 0, 1
    while True:
        yield current
        current, next = next, current + next
        n -= 1
        if n == 0:
            break

for el in Fibbo(12):
    print(el, end = ' ')
