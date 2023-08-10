"""Создать программу, которая будет производить подсчет
количества слов в каждом файле в указанной директории и
выводить результаты в консоль.
� Используйте асинхронный подход."""
import asyncio
import aiofiles
import os
import time


def count_words(dir_, file):
    file_ = os.path.join(dir_, file)
    with open(file_, 'r', encoding='utf-8') as f:
        file = f.read()
    count = len(file.split())
    print(f"Количество слов в файле {file_}: {count}"
          f"\nПосчитано за {time.time() - start_time:.2f} секунд\n")


async def count_words_async(dir_, file):
    file_ = os.path.join(dir_, file)
    async with aiofiles.open(file_, 'r', encoding='utf-8') as f:
        file = await f.read()
    count = len(file.split())
    print(f"Количество слов в файле {file_}: {count}"
          f"\nПосчитано за {time.time() - start_time:.2f} секунд\n")


async def count_words_async1(dir_, file):
    file_ = os.path.join(dir_, file)
    with open(file_, 'r', encoding='utf-8') as f:
        file = f.read()
    count = len(file.split())
    print(f"Количество слов в файле {file_}: {count}"
          f"\nПосчитано за {time.time() - start_time:.2f} секунд\n")


start_time = time.time()
dir_ = 'async'
files = os.listdir(dir_)


def sync(dir_, files):
    for file in files:
        count_words(dir_, file)


async def main():
    tasks = []
#    files = os.listdir(dir_)
    for file in files:
        task = asyncio.create_task(count_words_async(dir_, file))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
#    sync(dir_, files)
#    print(f"Посчитано за {time.time() - start_time:.2f} секунд\n")
    asyncio.run(main())
    print(f"Посчитано за {time.time() - start_time:.2f} секунд\n")


# в этой задаче асинхронное чтение файла делает работу медленнее. А быстрее всего
# работает синхронно


