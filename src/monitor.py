import psutil
import time
import csv


while True:

    mem = psutil.virtual_memory()
    with open("mem_info.csv", 'a+') as f:
        spamwriter = csv.writer(
            f, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([mem.total, mem.available, mem.used, mem.free])

    time.sleep(0.1)
