#列表
bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles[0].title())

print(bicycles[2].upper())

print(bicycles[3])

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#修改列表元素
motorcycles[0] = 'ducati'

print(motorcycles)

#列表末尾添加元素
motorcycles.append('yorkboy')

print(motorcycles)

#在列表中插入元素
motorcycles.insert(0, 'Gary')
print(motorcycles)

#使用del语句删除元素
del motorcycles[2]
print(motorcycles)

#使用方法pop()删除元素
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)