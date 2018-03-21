motorcycles = ['honda', 'yamaha', 'suzuki', 'gary', 'york']

first_owned = motorcycles.pop(0)

print(motorcycles)
print(first_owned)

print('The fist motorcucle I owned was a '  + first_owned.title() + '.')

#让Python确定'ducati'出现在列表的什么地方，并将该元素删除
motorcycles.remove('yamaha')

print(motorcycles)

too_expensive = 'gary'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


#使用方法 sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#向sort()方法传递参数 reverse=True,实现倒序
cars.sort(reverse=True)
print(cars)

#使用函数 sorted()对列表进行临时排序

print(sorted(cars))

print(cars)
cars.reverse()
print(cars)

print(len(cars))

