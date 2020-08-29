"""
  @author Lucas
  @date 2020/4/4 10:24
  产生指定数量的正态分布数据
"""
# 载入包为scipy统计包中的norm
from scipy.stats import norm
import numpy as np
import pylab as pl
import random
import xlwt

# 预设字体格式，并传给rc方法
font = {'family': 'SimHei', "size": 12}
pl.rc('font', **font)  # 一次定义终身使用
np.set_printoptions(threshold=np.inf)


def create_defect():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(1200):
        num = int(random.normalvariate(16, 8)*random.uniform(0.8, 1.2))
        while num < 0:
            num = int(random.normalvariate(16, 8)*random.uniform(0.8, 1.2))
            # 写入excel
            # 参数对应 行, 列, 值
        worksheet.write(i, 0, num)
    workbook.save('船舶缺陷分布.xls')


def create_ship():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(1200):
        num = int(random.normalvariate(85, 4)*random.uniform(0.9, 1.1))
        while num < 0:
            num = int(random.normalvariate(85, 4)*random.uniform(0.9, 1.1))
        while num > 100:
            num = int(random.normalvariate(85, 4)*random.uniform(0.9, 1.1))
            # 写入excel
            # 参数对应 行, 列, 值
        worksheet.write(i, 0, num)
    workbook.save('船舶风险评分分布.xls')


def create_company():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(120):
        num = int(random.normalvariate(82, 4)*random.uniform(0.9, 1.1))
        while num < 0:
            num = int(random.normalvariate(82, 4)*random.uniform(0.9, 1.1))
        while num > 100:
            num = int(random.normalvariate(82, 4)*random.uniform(0.9, 1.1))
            # 写入excel
            # 参数对应 行, 列, 值
        worksheet.write(i, 0, num)
    workbook.save('船管公司评分分布.xls')


def create_all():
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(600):
        num = int(random.normalvariate(84, 5)*random.uniform(0.9, 1.1))
        while num < 0:
            num = int(random.normalvariate(84, 5)*random.uniform(0.9, 1.1))
        while num > 100:
            num = int(random.normalvariate(84, 5)*random.uniform(0.9, 1.1))
            # 写入excel
            # 参数对应 行, 列, 值
        worksheet.write(i, 0, num)
    workbook.save('船舶综合风险评分分布.xls')


if __name__ == '__main__':
    # create_defect()
    # create_ship()
    create_company()
    # create_all()