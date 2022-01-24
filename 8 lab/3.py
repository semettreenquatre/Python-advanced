def my_map(function, iterable):
    iter_iterable = iter(iterable)
    while True:
        try:
            current = function(next(iter_iterable))
        except StopIteration:
            return
        yield current

def my_zip(*args):
    iter_args = [iter(arg) for arg in args]
    n = 0
    while True:
        try:
            current = []
            for iter_arg in iter_args:
                current.append(next(iter_arg))
        except StopIteration:
            return
        yield tuple(current)

def my_enumerate(iterable, start=0):
    iter_iterable = iter(iterable)
    index = start
    while True:
        try:
            current = (index, next(iter_iterable))
            index += 1
        except StopIteration:
            return
        yield current


lst = [1, -2, 3, -4, 5]
print('------Проверка my_map------------------------')
for i in my_map(abs, lst):
    print(i)


names = ["Alex", "Bob", "Alice", "John", "Ann"]
age = [25, 17, 34, 24]
sex = ["M", "M", "F", "M", "F"]
print('------Проверка my_zip------------------------')
for values in my_zip(names, age, sex):
    print("name: {:>10} age: {:3} sex: {:2}".format(*values))


print('------Проверка my_enumerate------------------------')
for idx, elem in my_enumerate(names, 99):
    print("{:02}: {:>7}".format(idx, elem))
