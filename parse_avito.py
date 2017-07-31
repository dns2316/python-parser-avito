#!/usr/bin/python3

from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
import urllib.request
from os import system



# url site for parse
url_avito = 'https://www.avito.ru/hanty-mansiysk'

# run script by timer
sched = BlockingScheduler()

# item item_table clearfix js-catalog-item-enum js-item-trackable   item-highlight   

# read html and send to BeautifulSoup.
def html_to_soup(link):
    try:
        with urllib.request.urlopen(link) as response:
            # write html code to variable
            html = response.read()

        return BeautifulSoup(html, 'html.parser')

    except Exception as err:
        print('Error in html_to_soup')
        print(err.args)

# init start script
# if __name__ == '__main__':
#     promo_soup = html_to_soup(url_avito)
#     promo = promo_soup.select(".item")

#     # promo in all promos
#     for item in promo:
#         promo_header = item.select('.item_table-header')

#         # title with remove \n
#         promo_title = item.select('.item_table-header a')[0].get_text().strip()

#         # price with remove \n
#         promo_price = item.select('.item_table-header .about')[0].get_text().strip()

#         print('{}, цена: {}.'.format(promo_title, promo_price))


# funct for scan by time
def scan_by_timer():
    promo_soup = html_to_soup(url_avito)
    promo = promo_soup.select(".item")

    # promo in all promos
    for item in promo:
        promo_header = item.select('.item_table-header')

        # title with remove \n
        promo_title = item.select('.item_table-header a')[0].get_text().strip()

        # price with remove \n
        promo_price = item.select('.item_table-header .about')[0].get_text().strip()

        print('{}, цена: {}'.format(promo_title, promo_price))


# add task to timer
sched.add_job(scan_by_timer, 'interval', minutes=1)

# start timer
sched.start()