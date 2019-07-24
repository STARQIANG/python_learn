#创建数值列表
#使用函数 range()可以生成一系列数字，打印1-4
for  value in range(1,5):
    print(value)

#range()创建数字列表，使用函数list()将range()的结果直接转换为列表
numbers = list(range(1,6))
print(numbers)

#使用函数range()时，还可指定步长，下列步长为2
enen_numbers = list(range(2,11,2))
print(enen_numbers)

#例：创建一个列表，其中包含前 10个整数（即1~10）的平方，在Python中，两个星号（**）表示乘方运算
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
print('------------------------------')
#不使用临时变量square，简洁
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#最小元素
min(digits)
#最大元素
max(digits)
#求元素和
sum(digits)

#*列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value**2 for value in range(1,11)]
print(squares)

