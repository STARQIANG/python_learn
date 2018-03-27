# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import requests
import sys
from os import mkdir, chdir
from os.path import exists

if len(sys.argv) != 4:
    print('3 arguments were required but only find ' + str(len(sys.argv) - 1) + '!')
    exit()

base_dir = 'wallpapers'
category = sys.argv[1]
try:
    page_start = [int(sys.argv[2])]
    page_end = int(sys.argv[3])
except:
    print('The second and third arguments must be a number but not a string!')
    exit()

if not exists(base_dir):
    mkdir(base_dir)        # /wallpapers
chdir(base_dir)

if not exists(category):
    mkdir(category)        # /wallpapers/<category name>
chdir(category)

PAGE_DOMAIN = 'http://wallpaperswide.com'
PAGE_URL = 'http://wallpaperswide.com/' + category + '-desktop-wallpapers/page/'

def visit_page(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    r = requests.get(url,headers = headers)
    r.encoding = 'utf-8'
    return BeautifulSoup(r.text, 'lxml')


def get_paper_link(page):
    links = page.select('#content > div > ul > li > div > div a')
    return [link.get('href') for link in links]

def download_wallpaper(link, index, total, callback):
    wallpaper_source = visit_page(PAGE_DOMAIN + link)
    wallpaper_size_links = wallpaper_source.select('#wallpaper-resolutions > a')
    size_list = [{
        'size': eval(link.get_text().replace('x', '*')),
        'name': link.get('href').replace('/download/', ''),
        'url' : link.get('href')
    } for link in wallpaper_size_links]

    biggest_one = max(size_list, key= lambda item: item['size'])
    print('Downloadind the ' + str(index + 1) + '/' + str(total) + ' wallpaper: ' + biggest_one['name'])

    result = requests.get(PAGE_DOMAIN + biggest_one['url'])

    if result.status_code == 200:
        open('wallpapers/' + biggest_one['name'], 'wb').write(result.content)

    if index + 1 == total:
        print('Download completed!\n')
        callback()

def start():
    if page_start[0] <= page_end:
        print('Preparing to download the ' + str(page_start[0]) + ' page of all the "' + category + '" wallpapers...')
        PAGE_SOURCE = visit_page(PAGE_URL + str(page_start[0]))
        WALLPAPER_LINKS = get_paper_link(PAGE_SOURCE)
        page_start[0] = page_start[0] + 1

        for index, link in enumerate(WALLPAPER_LINKS):
            download_wallpaper(link, index, len(WALLPAPER_LINKS), start)

if __name__ == '__main__':
     start()