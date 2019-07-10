"""
File Name: EX24
Version: 1.0
Author: Gary
Date: 2018/9/6
"""
import getpass
username = input('请输入用户名：')
#password = input('请输入密码：')
password = getpass.getpass('请输入密码：' )
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')