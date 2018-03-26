# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import requests


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
