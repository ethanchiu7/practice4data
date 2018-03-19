#! -*- coding: UTF-8 -*-
#
#   @author zhaoxin
#   @date 2018-03-19
#


import tensorflow as tf
import pandas as pd
import numpy as np


def basic_op():
    city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
    population = pd.Series([852469, 1015785, 485199])
    pd.DataFrame({ 'City name': city_names, 'Population': population })

def read_csv():
    print("开始加载文件")
    california_housing_dataframe = pd.read_csv("california_housing_train.csv", sep=",")
    print("加载完成")

    # 数据概览
    # print(california_housing_dataframe.describe())

    # 头5行
    print(california_housing_dataframe.head())

    # 借助 DataFrame.hist，您可以快速了解一个列中值的分布
    # print(california_housing_dataframe.hist('housing_median_age'))


def main():

    print("BEGIN")
    # basic_op()
    read_csv()

    print("END")


if __name__ == '__main__':

    main()
