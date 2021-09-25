#!/usr/bin/python3.7
from random import randint
from pathlib import Path
from urllib import parse
from bs4 import BeautifulSoup
import json
import requests
import os
import time
import re
import shutil

#location_pattern = re.compile("Source:\s(.*)\s\(Difficulty\:\s(.*?)\)")
#
re_restricted = re.compile(" \[Restricted\]")
re_condition = re.compile("\((Perfect|Excellent|Very Good|Good|Fair|Poor|Bad)\)")
re_condition_2 = re.compile(" *\: ")
re_flags = re.compile(" \((kept|hum|dark|glow|blue aura)\)")

data_path = 'buffer_dump'
dirs = os.listdir(data_path)

item_name_list = []
duplicate = []

for item in dirs:
    current = os.path.join(data_path, item)
    with open(current, 'r') as f:
        data = f.readlines()
        f.close()

    item_name = data[0]
    item_name = re.sub(re_restricted, '', item_name)
    item_name = re.sub(re_condition, '', item_name)
    item_name = re.sub(re_condition_2, '', item_name)
    while re.search(re_flags, item_name):
        item_name = re.sub(re_flags, '', item_name)

    # Check for duplicates
    if item_name in item_name_list:
        shutil.move(current, '../duplicate')
    else:
        item_name_list.append([item_name, data])

print(item_name_list[0])
#print(duplicate)
#duplicate = set([x for x in item_name_list if item_name_list.count(x) > 1])
#print(duplicate)
#if len(item_name_list) == len(set(item_name_list)):
#    print('yay')
#else:
#    print('no')
#print(len(item_name_list))
