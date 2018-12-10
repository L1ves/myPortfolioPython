#!/usr/bin/dev/env python3

import urllib.request
from bs4 import BeautifulSoup
#import csv

BASE_URL = 'https://www.weblancer.net/jobs/'

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html)
    table = soup.find('div' , {'class' : 'container-fluid cols_table show_visited'})
    print(table.prettify())

#if __name__ == '__main__':
#    main()
