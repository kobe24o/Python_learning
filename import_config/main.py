# _*_ coding: utf-8 _*_
# @Time : 2022/7/19 12:17
# @Author : Michael
# @File : main.py
# @desc :

import os
import yaml
import time
from table_config.table import mysql_table_name
import os

env = os.environ.get('env')

cnf = yaml.load(open(os.path.join(os.path.dirname(__file__), 'conf_cn.yml')), Loader=yaml.FullLoader)
print(cnf)
while True:
    print(f'main.py env: {env}, table_name: {mysql_table_name}')
    time.sleep(1.3)