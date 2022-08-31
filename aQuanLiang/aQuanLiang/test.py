# -*- coding: utf-8 -*-
import os
from time import sleep

import requests
import xlsxwriter as xw
from scrapy import cmdline


def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['标题', '发布日期', '阅读数', '封面图']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["id"], data[j]["name"], data[j]["price"], data[j]["cover"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


if __name__ == '__main__':
    # "-------------数据用例-------------"
    '''testData = [
        {"id": 1, "name": "立智", "price": 100, "cover": 1111},
            {"id": 2, "name": "维纳", "price": 200, "cover": 1111},
        {"id": 3, "name": "如家", "price": 300, "cover": 1111},
    ]
    fileName = '测试.xlsx'
    xw_toExcel(testData, fileName)'''
    '''url = 'https://quan-1259287960.cos.ap-guangzhou.myqcloud.com/1000029/b9af56dce4e2446aa1f978162017056d'
    name = url.split('/')[-1]
    response = requests.get(url)
    if not os.path.exists('./imgs'):
        os.makedirs('./imgs')
    fb = open('./imgs/' + name + '.jpg', 'wb')
    fb.write(response.content)
    sleep(1)
    fb.close()
    workbook = xw.Workbook('myexcel.xlsx')  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.insert_image('A1', './imgs/' + name + '.jpg')
    workbook.close()'''
    cmdline.execute(['scrapy', 'crawl', 'aquanliang'])