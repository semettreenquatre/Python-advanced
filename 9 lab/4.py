class PrintAverage(Exception):
    pass

class PrintCount(Exception):
    pass

class PrintDispersion(Exception):
    pass

def coroutine():
    print("Start")
    n = sum = 0
    numbers = []
    try:
        while True:
            try:
                x = yield
                numbers.append(x)
                n += 1
                sum += x
            except PrintCount:
                yield n
            except PrintAverage:
                yield (sum / n)
            except PrintDispersion:
                average = sum / n
                for number in numbers:
                    quadra_sum = (number - average) ** 2
                yield (quadra_sum / n) ** 0.5
    finally:
        print("Stop")

coroutine = coroutine()
next(coroutine)
print("Welcome to my programm!", '\n', 'Interface:', "\n", '1) To put number  - just type it', '\n', '2) To calculate average - type 01', '\n', '3) To calculate dispersion - type 02', '\n', '4) To count numbers - type 03', '\n', '5) To exit - type exit', '\n')
while True:
    print("Input: ", end = '')
    Input = input()
    try:
        if Input == 'exit':
            coroutine.close()
            break
        elif Input == '01':
            print("Current average: ", coroutine.throw(PrintAverage))
            next(coroutine)
        elif Input == '02':
            print("Current dispersion: ", coroutine.throw(PrintDispersion))
            next(coroutine)
        elif Input == '03':
            print("Current count: ", coroutine.throw(PrintCount))
            next(coroutine)
        else:
            Input = int(Input)
            coroutine.send(Input)
    except Exception:
         print('Wrong input! Try again!')