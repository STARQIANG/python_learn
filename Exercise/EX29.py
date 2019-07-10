"""
 File Name: EX29.py
 Version  : 1.0
 Author   : Gary
 Date     : 2018/11/26 10:59
 Software : PyCharm
 
"""
import os
import time

def main():
    content = '北京欢迎为你开天辟地.....'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content =content[1:] + content[0]
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    main()