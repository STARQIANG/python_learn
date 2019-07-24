#if语句

names = ['york','gary','colla','star']
for name in names:
    if name == 'gary':
        print(name.upper())
    else:
        print(name.title())

#if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
    price = 0
elif age < 18:
    print("Your admission cost is $5.")
    price = 5
else:
    print("Your admission cost is $10.")
    price = 10
print("Your admission cost is $" + str(price) + ".")



