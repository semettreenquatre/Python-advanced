import urllib.request
import time
import threading


urls = [
    'http://www.yandex.ru', 'http://www.google.com',
    'http://habrahabr.ru'
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()

start = time.time()
threads = [threading.Thread(target=read_url, args = (url, )) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print('c потоками: ', time.time() - start) 

start = time.time()
for url in urls:
    read_url(url)
print('без: ', time.time() - start)