import json
import xlwt
from pathlib import Path
n = 1
def main():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Website Activity')
    ws.write(0,0,'Date')
    ws.write(0,1,'IP Address')
    ws.write(0,2,'Page Visited')

    jsonDump = []
    p = Path(str(input('Input directory of JSONDumps: ')))
    for child in p.iterdir():
        child = str(child)
        jsonDump.append(child)

    def addToXLS(data):
        global n
        for x in data['hits']:
            date = x["accessOnShort"][0:5:1] + '/2016'
            ws.write(n,0,date)
            ws.write(n,1,x["ipAddress"])
            ws.write(n,2,x["targetName"])
            n += 1

    for dump in jsonDump:
        with open(dump) as datafile:
            data = json.load(datafile)
            addToXLS(data)

    wb.save('/Users/hgoscenski/Desktop/WebsiteStats.xls')
    print('Saved XLS file to desktop! Have a great day!')
main()
