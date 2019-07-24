#字典
alien = {'color': 'green', 'points': 5}

print(alien['color'])
print(alien['points'])

new_points = alien['points']
print("You just carned " + str(new_points) + " points! ")

#添加键-值对
alien = {}
alien['color'] = 'red'
alien['points'] = '6'
alien['x'] = 0
alien['y'] = 25
print(alien)

#修改字典中的值
alien['color'] = 'yellow'
print("The alien is now " + alien['color'] +".")

#删除键-值对
print(alien)
del alien['points']
print(alien)

#遍历字典
#遍历所有的键-值对
User = {
    'Username': 'gary',
    'first': 'york',
    'last': 'star',
    }

#方法items()，它返回一个键—值对列表
print(User.items())
for key, value in User.items():
    print("\nKey: " + key)
    print("Value: " + value)


#遍历字典中所有的键，不需要使用字典中的值，方法keys().
languages = {
    'gary': 'python',
    'york': 'c',
    'jen': 'ruby',
    'feibi': 'python',
    }
friends = ['york', 'gary']
for name in languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              languages[name].title() + "!")

#按顺序遍历字典中的所有键

for name in sorted(languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#遍历字典中的所有值,使用方法values()，它返回一个值列表

for language in languages.values():
    print(language.title())

#对包含重复元素的列表调用set(),剔除重复项
print("\nThe following languages have been mentioned:")
for language in set(languages.values()):
    print(language.title())


##嵌套-字典列表

#创建一个空列表
aliens = []
#创建30个
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
#显示前五个
for alien in aliens[0:5]:
    print(alien)
print("...")
print("Total number of aliens:" + str(len(aliens)))

#在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

