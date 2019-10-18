"""
 File Name: Learn08.py
 Version  : 1.0
 Author   : Gary
 Date     : 2019/7/24 14:57
 Software : PyCharm
 
"""
#用户输入，函数input()

#例一：
name = input("Please enter your name: ")
print("Hello, " + name + "!")
#例二：演示了一种创建多行字符串的方式“+=”

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is you first name? "
name = input(prompt)
print("\nHello, " + name + "!")

#例三：使用int()来获取数值输入
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little order.")


#例四：求模运算符（%），它将两个数相除并返回余数
#判断一个数是奇数还是偶数
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + "  is even.")
else:
    print("\nThe number " + str(number) + "  is odd.")
