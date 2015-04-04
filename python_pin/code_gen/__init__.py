#!/usr/bin/env python

from os import path

import codecs

import requests

from bs4 import BeautifulSoup

from python_pin.utils import pp


(lambda first_space: first_space)(lambda s: s.find(' ', 1))


def cache():
    if path.isfile('cache.html'):
        return BeautifulSoup(codecs.open('cache.html', encoding='utf-8'))

    soup = BeautifulSoup(requests.get('https://pin.net.au/docs/api/charges').content)
    s = soup.prettify()

    with codecs.open('cache.html', 'w', encoding='utf-8') as f:
        f.write(s)

    return soup


def main():
    soup = cache()
    pp(soup.find_all(class_='endpoint'))


if __name__ == '__main__':
    main()
