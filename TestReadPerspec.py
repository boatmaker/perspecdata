import json
import time
import xlwt
import requests
from pprint import pprint
def main():
    openFile = str(input('Type the file path of the item Website JSON file: '))
    # with open('/Users/hgoscenski/Desktop/Test1.json') as datafile:
    with open(openFile) as datafile:
        data = json.load(datafile)
    # print(data['hits'])
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Website Activity')
    ws.write(0,0,'Date')
    ws.write(0,1,'IP Address')
    ws.write(0,2,'Page Visited')
    ws.write(0,3,(time.strftime("%m:%d:%Y")))
    n = 1
    for x in data['hits']:
        # pprint(x)
        date = x["accessOnShort"][0:5:1] + '/2016'
        # print(date)
        ws.write(n,0,date)
        ws.write(n,1,x["ipAddress"])
        ws.write(n,2,x["targetName"])
        n += 1
        # print(x["ipAddress"])
        # print(x["accessOnShort"])
        # print(x["targetName"])
    T = (time.strftime("%d/%m/%Y"))
    wb.save('/Users/hgoscenski/Desktop/WebsiteStats.xls')
main()
