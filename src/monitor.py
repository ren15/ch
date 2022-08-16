import psutil
import time
import csv

mem = psutil.virtual_memory()

while True:

    with open("mem_info.csv", 'a+') as f:
        spamwriter = csv.writer(
            f, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([mem.total, mem.available, mem.used, mem.free])

    time.sleep(0.1)
