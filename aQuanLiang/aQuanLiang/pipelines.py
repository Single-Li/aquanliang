# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from time import sleep

import requests
import xlsxwriter as xw

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from requests import request


class AquanliangPipeline:
    count = 2
    workbook = xw.Workbook('测试.xlsx')  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    title = ['标题', '发布日期', '阅读数', '封面图']  # 设置表头

    def open_spider(self, spider):
        self.worksheet1.activate()  # 激活表
        self.worksheet1.write_row('A1', self.title)  # 从A1单元格开始写入表头
        if not os.path.exists('./imgs'):
            os.makedirs('./imgs')
        print('Excel已经初始化完成！！！！！！！！！！！！！！！！！！！！！！！！')

    def process_item(self, item, spider):
        response = requests.get(item["cover"])
        name = item["cover"].split('/')[-1]
        fb = open('./imgs/' + name + '.jpg', 'wb')
        fb.write(response.content)
        # sleep(1)
        fb.close()
        insertData = [item["title"], item["publishTime"], item["readCounts"]]
        row = 'A' + str(self.count)
        self.worksheet1.write_row(row, insertData)
        self.worksheet1.insert_image('D' + str(self.count), './imgs/' + name + '.jpg')
        self.count += 1
        print(str(self.count) + "行数据插入成功！！！！！！！！！！！！！！！！！！！！！！！！")
        return item

    def close_spider(self, spider):
        self.workbook.close()
        print('Excel已经关闭！！！！！！！！！！！！！！！！！！！！！！！！')
