# -*- coding: utf-8 -*-

import csv
import config
import re
import glob
import urllib
from bs4 import BeautifulSoup
import os.path
import json
import atexit
import pprint

pp = pprint.PrettyPrinter(indent=4)


proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

filename = "IVDETAIL"

def importData(f):
    lines = [line.rstrip('\n') for line in open(f, encoding="ISO-8859-1")]
    return lines

def main():
    lines = importData(filename + '.txt')
    finalFloats = []
    datas = []

    #get stock cat
    catAfile = ['STOCK_CAT/A1_sugar.txt', 'STOCK_CAT/A2_pakorn.txt', 'STOCK_CAT/A3_special.txt']
    catBfile = ['STOCK_CAT/B1_normal.txt', 'STOCK_CAT/B2_sdgbb.txt', 'STOCK_CAT/B3_mdgbb.txt', 'STOCK_CAT/B4_motor.txt', 'STOCK_CAT/B5_ucp.txt', 'STOCK_CAT/B6_housingseal.txt', 'STOCK_CAT/B7_mapro.txt', 'STOCK_CAT/B8_ybearing.txt']
    catA = []
    catB = []
    for a in catAfile:
        a = importData(a)
        catA.append(a)
    for b in catBfile:
        b = importData(b)
        catB.append(b)

    for line in lines:
        p = re.compile(r'[0-9][0-9,.]+')
        fakeFloats = []
        for i in p.findall(line):
            try:
                f = float(i.replace(',', ''))
                fakeFloats.append(f)
            except:
               continue
        if len(fakeFloats) > 3:
            #print line
            floats = []
            for i in p.findall(line):
                try:
                    f = float(i.replace(',', ''))
                    floats.append(f)
                except:
                   continue
            if len(floats) == 3:
                finalFloats = floats
            else:
                floats = floats[len(floats)-3: len(floats)]
                finalFloats = floats
            #print finalFloats
            title = line.split('            ')[0]
            isSKF = re.search(r'SKF', title)
            if not isSKF:
                continue
            title = title.split('SKF')[1]
            title = title.replace('.', '')
            title = title.replace('$', '')
            title = title.replace(',', '')
            title = title.replace('@', '')
            title = title.replace('"', '')
            title = title.strip()
            parentheses = re.search(r'\(.*\)', line)
            data = {}
            data['QUANTITY'] = finalFloats[0]
            if parentheses:
                data['QUANTITY'] = -1*data['QUANTITY']
            data['DESIGNATION'] = title
            data['PRICE'] = finalFloats[1]
            data['AMOUNT'] = finalFloats[2]

            data["CODE1"] = ""
            data["CODE2"] = ""
            count = 1
            for a in catA:
                if data["DESIGNATION"] in a:
                    data["CODE1"] = count
                count = count + 1
            count = 1
            for b in catB:
                if data["DESIGNATION"] in b:
                    data["CODE2"] = count
                count = count + 1

            datas.append(data)
    toCSV(datas)

def toCSV(datas):
    keys = datas[0].keys()
    print(keys)
    try:
        with open('data_updated_'+filename+'.csv','w',encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(datas)
    except Exception as e:
        raise e

main()
