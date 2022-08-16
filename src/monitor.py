import psutil
import time
import sys
import csv

import pandas as pd
import matplotlib.pyplot as plt

CSV_NAME = "mem_info.csv"


def monitor():

    while True:
        mem = psutil.virtual_memory()
        with open(CSV_NAME, 'a+') as f:
            spamwriter = csv.writer(
                f, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(
                [mem.total,
                 mem.used,
                 psutil.swap_memory().used
                 ])

        time.sleep(0.1)


def plot():
    df = pd.read_csv(CSV_NAME)

    plt.plot(df)
    plt.legend(['total', 'used', 'swap'])
    plt.savefig('mem_info.png')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Specify command please")
        exit()
    if sys.argv[1] == 'monitor':
        monitor()
    if sys.argv[1] == 'plot':
        plot()
