#组织列表
#1、使用方法 sort()对列表进行永久性排序，按字母顺序排列
#方法sort()永久性地修改了列表元素的排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#向sort()方法传递参数 reverse=True,实现倒序，永久性的
cars.sort(reverse=True)
print(cars)

#使用函数 sorted()对列表进行临时排序
print(sorted(cars))
print(cars)

#反转列表元素的排列顺序，可使用方法reverse()，非按字母顺序
cars.reverse()
print(cars)

#确定列表的长度
print(len(cars))

#for循环遍历列表的所有元素
magicians = ['alice', 'david', 'carolina']
for magician  in magicians:
    print(magician.title())
