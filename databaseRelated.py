# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:44:14 2021

@author: jywen
"""

import pyodbc
import numpy as np

conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=10.40.20.80;DATABASE=vervidian;UID=developer;PWD=Passw0rd')

cursor = conn.cursor()

cursor.execute("select top 100 e.empid, e.created as EECreated, c.created as CaseCreated from employee as e inner join [case] as c on e.id = c.employeeid where e.created >= '2016-01-01 00:00:00.000' order by e.empid, c.created desc")

rows = cursor.fetchall()
tempid = 0
templist = []
result = []
for row in rows:
    if(tempid == row.empid):
        continue
    else:      
        tempid = row.empid
        templist.append(row)
for item in templist:
    result.append(item[0] item[2] - item[1])

print(result)


# print(max(result))
# print(np.mean(result))
# print(np.median(result))