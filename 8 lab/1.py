def print_map1(function, iterable):
    print (*map(function, iterable), sep = '\n')

def print_map2(function, iterable):
    arr = iter(iterable)
    try:
        while 1:
            print(abs(next(arr)))
    except:
        return

print_map1(abs, arr)
print('-----------------------------')
print_map2(abs, arr)