# _*_ coding: utf-8 _*_
# @Time : 2022/7/19 12:09
# @Author : Michael
# @File : table.py
# @desc :

import os
import time
env = os.environ.get('env')
if env == 'cn':
    mysql_table_name = 'table_cn'
elif env == 'sgp':
    mysql_table_name = 'table_sgp'
else:
    mysql_table_name = 'error'

print(f'table.py env: {env}, table_name: {mysql_table_name}')
time.sleep(1)