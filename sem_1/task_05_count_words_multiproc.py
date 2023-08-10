"""Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте процессы."""

import os
from multiprocessing import Process, Pool
import time


def count_words(dir_, file):
    file_ = os.path.join(dir_, file)
    with open(file_, 'r', encoding='utf-8') as f:
        file = f.read()
    count = len(file.split())
    print(f"Количество слов в файле {file_}: {count}"
          f"\nПосчитано за {time.time() - start_time:.2f} секунд\n")


processes = []
start_time = time.time()
dir_ = 'multiproc'
files = os.listdir(dir_)

if __name__ == '__main__':
    for file in files:
        process = Process(target=count_words, args=(dir_, file))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
