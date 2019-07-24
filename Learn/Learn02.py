#1、列表>>>>用方括号（[]）来表示列表，并用逗号来分隔其中的元素
bicycles = ['trek', 'connondale', 'redline', 'specialized']

#提取第一个元素，并首字母大写， 索引从0而不是1开始
print(bicycles[0].title())

#提取第三个元素
print(bicycles[2].upper())

#-1代表列表倒数第一个元素
print(bicycles[-1])

#代入列表的值
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


#2、修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#修改列表元素
motorcycles[0] = 'ducati'

print(motorcycles)

#列表末尾添加元素，方法append()将元素'ducati'添加到了列表末尾
motorcycles.append('yorkboy')
print(motorcycles)


#在列表中间插入元素，使用方法insert()可在列表的任何位置添加新元素
motorcycles.insert(0, 'Gary')
print(motorcycles)

#使用del语句删除元素，如果知道要删除的元素在列表中的位置，可使用del语句
del motorcycles[2]
print(motorcycles)

#使用方法pop()删除元素，方法pop()可删除列表末尾的元素，并让你能够接着使用它
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#弹出列表中任何位置处的元素
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#注：如果你不确定该使用del语句还是pop()方法，下面是一个简单的判断标准：
# 如果你要从列表 中删除一个元素，且不再以任何方式使用它，就使用del语句；如果你要在删除元素后还能继续 使用它，就使用方法pop()

#根据值删除元素
motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
