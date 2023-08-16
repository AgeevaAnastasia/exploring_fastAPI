"""Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте потоки."""

import os.path

import requests
import threading
import time


def count_words(dir_, file):
    file_ = os.path.join(dir_, file)
    with open(file_, 'r', encoding='utf-8') as f:
        file = f.read()
    count = len(file.split())
    print(f"Количество слов в файле {file_}: {count}"
          f"\nПосчитано за {time.time() - start_time:.2f} секунд\n")


threads = []
start_time = time.time()
dir_ = 'threads'
files = os.listdir(dir_)
for file in files:
    thread = threading.Thread(target=count_words, args=[dir_, file])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
