# 函数的参数:
#
# ( )表示调用, 传参
#
# 参数:参数是给函数传递的信息. 分为实参和形参
#
# 注意:在函数调用的时候,必须保证所有的形参都有值
#
# 形参:在函数声明的位置写的变量
def regist(name, age, edu, gender="男"):
    print("name:",name)
    print("age:",age)
    print("edu:",edu)
    print("gender:",gender)
regist('gary', 20, '本科')


#实参:在函数调用的时候给函数传递的具体的值
def chi(zhushi,fushi,tang,tiandian):
    print('主食：%s' % zhushi)
    print('副食：%s' % fushi)
    print('汤：%s' % tang)
    print('甜点：%s' % tiandian)
#1.位置参数：按照位置给形参传递信息
chi('牛肉板面','豆皮','鸡蛋汤','蛋糕')

# 2.关键字参数: 按照形参声明的变量名进行传参
chi(zhushi='牛肉板面',fushi='豆皮',tang='鸡蛋汤',tiandian='冰激凌')

# 3.混合参数: 位置 + 关键字(规定:关键字必须在最后)
# chi(tang='鸡蛋汤',tiandian='冰激凌', '牛肉板面', '豆皮', )   # 报错

chi('牛肉板面', '豆皮', tang='鸡蛋汤',tiandian='冰激凌')
chi('牛肉板面', '豆皮', tiandian='冰激凌',tang='鸡蛋汤')