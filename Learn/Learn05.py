
players = ['charles', 'martina', 'michael', 'florence', 'eli']

#切片
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[3:])
print(players[-3:])

#遍历切片，遍历前三名队员
for player in players[:3]:
    print(player.title())


#############################
#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)

#证明此时现在有两个列表
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

#定义元组,Python将不能修改的值称为不可变的，而不可变的列表被称为元组
number = (100,50)
print(number[0])
print(number[1])

#number[0] = 200
#错误：TypeError: 'tuple' object does not support item assignment

#遍历元组中的所有值
for num in number:
    print(num)