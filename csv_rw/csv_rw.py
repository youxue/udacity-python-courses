# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:26:47 2020

@author: jywen
"""
import csv

csv_file = "HireList.csv"
with open(csv_file, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
