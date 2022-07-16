# _*_ coding: utf-8 _*_
# @Time : 2022/7/6 18:03
# @Author : Michael
# @File : os_environ.py
# @desc :
import os

def get_env_filename():
    srv = os.environ.get('cnf') # 通过环境变量参数读取相关配置
    if srv not in ['online', 'sim', 'qa']:
        raise Exception(f'config error: {srv}')
    return f'.env_{srv}'  # 配置文件名字

if __name__ == '__main__':
    print(get_env_filename())