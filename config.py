import os.path
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    'Accept' : 'text/html, image/jpeg, image/png, text/*, image/*, */*',
    'Accept-Language': 'en-us',
    'Accept-Charset' : 'utf-8',
    #'Accept-Charset' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
    'Accept-Encoding': 'utf-8',
    'Keep-Alive': '300',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}

keys = ["designation",
        "title",
        "url",
        "category1",
        "category2",
        "category3",
        "Dimensions",
        "Calculation data",
        "images",
        "Mass",
        "done"
       ]

database = 'database.csv'
fastmoving = 'fastmoving.csv'
