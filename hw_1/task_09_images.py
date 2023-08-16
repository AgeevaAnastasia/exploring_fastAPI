"""Написать программу, которая скачивает изображения с заданных URL-адресов
и сохраняет их на диск.
Каждое изображение должно сохраняться в отдельном файле, название которого
соответствует названию изображения в URL-адресе.
Например URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
Программа должна иметь возможность задавать список URL-адресов через аргументы командной
строки.
Программа должна выводить в консоль информацию о времени скачивания каждого изображения
и общем времени выполнения программы."""

import threading
from multiprocessing import Process
import asyncio
import time
import os
import re
import requests
import aiohttp
import aiofiles
import argparse

parser = argparse.ArgumentParser(description='Parse url')
parser.add_argument('url', metavar='u', type=str, nargs='*', help='Please, enter images url: ')


def download_images_threads(url):
    response = requests.get(url)
    dir_name = 'threads'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/' + url.split('/')[-1]
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url.split('/')[-1]} in {time.time() - start_time:.2f} seconds")


def download_images_multiproc(url):
    response = requests.get(url)
    dir_name = 'multiproc'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    filename = dir_name + '/' + url.split('/')[-1]
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)
    print(f"Downloaded {url.split('/')[-1]} in {time.time() - start_time:.2f} seconds")


async def download_images_async(url):
    dir_name = 'async'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            image = await request.read()
            filename = dir_name + '/' + url.split('/')[-1]
            with open(filename, "wb") as f:
                f.write(image)
            print(f"Downloaded {url.split('/')[-1]} in {time.time() - start_time:.2f} seconds")


def start_threads(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_images_threads, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


def start_multiproc(urls):
    processes = []
    for url in urls:
        process = Process(target=download_images_multiproc, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()


async def start_async(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_images_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()


if __name__ == "__main__":
    #urls = [parser.parse_args()]
    # для быстроты запуска:
    urls = [
        'https://news.sponli.com/en/wp-content/uploads/2014/05/meteorsbryce_lane_1800.jpg',
        'https://news.sponli.com/en/wp-content/uploads/2014/02/9504976899_e6a39a1f85_o.jpg',
        'https://i.imgur.com/fMRP5ed.jpg',
        'https://i.imgur.com/fMRP5ed.jpg https://i.pinimg.com/originals/7f/f2/ba/7ff2ba78f3d767e4b022d505f46d7690.jpg',
        'https://get.wallhere.com/photo/landscape-night-galaxy-stars-Milky-Way-atmosphere-spiral-galaxy-astronomy-camping-star-1920x1200-px-outer-space-astronomical-object-geological-phenomenon-623747.jpg'
    ]
    #start_threads(urls)
    #start_multiproc(urls)
    asyncio.run(start_async(urls))


