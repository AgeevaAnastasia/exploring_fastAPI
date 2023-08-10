"""Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте асинхронный подход."""

import asyncio
import os
import aiohttp
import time


urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://netology.ru',
        'https://practicum.yandex.ru',
        'https://antiplagiat.ru',
        'https://skillbox.ru',
        'https://ru.wikipedia.org'
        ]


async def download(url):
    dir_name = 'async'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = dir_name + '/' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def main():
    tasks = []
    for url in urls:
        # либо так asyncio.create_task(download(url))
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # либо
    # asyncio.run(main())
