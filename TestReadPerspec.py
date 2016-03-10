import json
import time
import xlwt
import requests
from pprint import pprint
n = 1
def main():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Website Activity')
    ws.write(0,0,'Date')
    ws.write(0,1,'IP Address')
    ws.write(0,2,'Page Visited')

    jsonDump = []
    def collect():
        Running = 1
        while Running == 1:
            temp = str(input('Enter file path to next JSON DUMP for this week, or if there are no more JSONDumps type "done": '))
            if temp == 'done':
                Running -= 1
            elif temp == '':
                print('Nothing was entered')
            else:
                jsonDump.append(temp)
        print(jsonDump)
    collect()
    def addToXLS(data):
        global n
        for x in data['hits']:
            # pprint(x)
            date = x["accessOnShort"][0:5:1] + '/2016'
            # print(date)
            ws.write(n,0,date)
            ws.write(n,1,x["ipAddress"])
            ws.write(n,2,x["targetName"])
            n += 1

    for dump in jsonDump:
        with open(dump) as datafile:
            data = json.load(datafile)
            addToXLS(data)

    ws.write(0,3,(time.strftime("%m:%d:%Y")))
    T = (time.strftime("%d/%m/%Y"))
    wb.save('/Users/hgoscenski/Desktop/WebsiteStats.xls')
main()
