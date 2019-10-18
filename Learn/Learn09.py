"""
 File Name: Learn09.py.py
 Version  : 1.0
 Author   : Gary
 Date     : 2019/7/24 15:20
 Software : PyCharm
 
"""
# while循环
#例一： 利用while循环来数数：
number = 1
while number <= 5:
    print(number)
    number += 1
#例二：定义退出值，让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
#例三：利用if不打印退出值‘quit’

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#例四：使用标志,定义一个变量（标志），用于判断整个程序是否处于活动状态
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    messgae = input(prompt)
    if messgae == 'quit':
        active = False
    else:
        print(messgae)
#例五：使用break退出循环，立即退出循环，不在运行循环中余下代码
prompt = "\n请告诉我你喜欢的一个东西："
prompt += "\n输入'quit'退出程序"
while True:
    abc = input(prompt)
    if abc == 'quit':
        break
    else:
        print("我喜欢" + abc.title() + "！")

#例五：在循环中使用continue,并根据条件测试结果决定是否继续执行循环
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)
#注：避免无限循环，避免遗漏

#例六：在列表之间移动元素

#创建一个待验证用户列表
unconfirmed_users = ['gary', 'york', 'calla']
#用于存储已验证用户的空列表
confirmed_uesrs = []
#验证每个用户，直到没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_uesrs.append(current_user)
#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for  confirmed_user in confirmed_uesrs:
    print(confirmed_user.title())

#例七：删除包含特定值的所有列表元素,利用函数remove()来循环删除列表中的特定值
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#例八：使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
    #提示输入呗调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #将回答存储在字典中
    responses[name] = response

    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no' :
        polling_active = False

#调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " Would like to climb " + response +  ".")

