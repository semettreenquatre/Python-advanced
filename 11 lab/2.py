import os, re
import threading
import time

def thread_job(ip):
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
a = time.clock()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

threads = []
for suffix in range(20, 30):
    ip = "192.168.178." + str(suffix)
    threads.append(threading.Thread(target=thread_job(ip)))
for thread in threads:
    thread.start()
print(time.clock() - a)
#for thread in threads:
#    thread.join()
print()


a = time.clock()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

for suffix in range(20, 30):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
print(time.clock() - a)