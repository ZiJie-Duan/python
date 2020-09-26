# -*- coding:utf-8 -*-
import requests
import xlwt
import json 


def get_ch(data=""):
    
    string = data
    data = {
    'doctype': 'json',
    'from': 'AUTO',
    'i':string,
    }
    url = "http://fanyi.youdao.com/translate"
    while True:
        try:
            r = requests.get(url,params=data, timeout=3)
            break
        except:
            s = input("Try again 链接超时（p=pass）:")
            if s == "p":
                return str("err")

    r = requests.get(url,params=data)
    result = r.json()
    feedback = result["translateResult"][0][0]["tgt"]
    print(feedback)
    return str(feedback)



def save(data):
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    js = 0 
    for en, ch in data.items():
        worksheet.write(js,0, label = en)
        worksheet.write(js,1, label = ch)
        js += 1
    workbook.save('Excel_test.xls')

def main():
    coredata = {}
    while True:
        data = input("英文>>")
        if data == "s":
            save(coredata)
        elif data != "":
            fd = get_ch(data)
            coredata[data] = fd
        
main()