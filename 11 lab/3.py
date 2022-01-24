import os, re
import threading
import time
import multiprocessing

arr = list(range(100000))

def summa(arr):
    sum = 0
    for i in arr:
        sum += i

##Один поток
#start = time.time()
#a = summa(0, 100000)
#print(time.time() - start)

##Два потока
#start = time.time()
#threads = [threading.Thread(target=summa, args = (0, 50000)), threading.Thread(target=summa, args = (50000, 100000))]
#for thread in threads:
#    thread.start()
#for thread in threads:
#    thread.join()
#print(time.time() - start)

##Четыре потока
#start = time.time()
#threads = [threading.Thread(target=summa, args = (0, 25000)), threading.Thread(target=summa, args = (25000, 50000)), threading.Thread(target=summa, args = (50000, 75000)), threading.Thread(target=summa, args = (75000, 100000))]
#for thread in threads:
#    thread.start()
#for thread in threads:
#    thread.join()
#print(time.time() - start)
if __name__ == '__main__':
    print("Multiprocessing")
    #---------------------------------------------------

    #Один поток
    start = time.time()
    a = summa(arr[0:100000])
    print(time.time() - start)

    print('Ended 1')
    #Два потока
    start = time.time()
    threads = [multiprocessing.Process(target=summa, args = (arr[0:50000],)), multiprocessing.Process(target=summa, args = (arr[50000:100000],))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)

    print('Ended 2')
    #Четыре потока
    start = time.time()
    threads = [multiprocessing.Process(target=summa, args = (arr[0:25000],)), multiprocessing.Process(target=summa, args = (arr[25000:50000],)), multiprocessing.Process(target=summa, args = (arr[50000:75000],)), multiprocessing.Process(target=summa, args = (arr[75000:100000],))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(time.time() - start)

    print('Ended 4')