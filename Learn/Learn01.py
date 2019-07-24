
#1、使用方法修改字符串的大小写
name = "aba lovelace"
#将每个单词的首字母都改为大写
print(name.title())
#将字符串先转换为大写
print(name.upper())
#将字符串先转换为小写
print(name.lower())

#2、合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
massage = "Hello, "  +full_name.title() + "!"
print(massage)

#3、删除空白
favorite_language = ' python '
#剔除字符串结尾空白
favorite_language = favorite_language.rstrip()
print(favorite_language)
#剔除字符串开头空白
favorite_language = favorite_language.lstrip()
print(favorite_language)
#剔除字符串两端空白
favorite_language = favorite_language.strip()
print(favorite_language)

#测试
names_case = "eric"

massage = "Hello " + names_case.title() + "，would you like to learn some Python today?"

print(massage)

#使用函数 str()避免类型错误
age = 28

massage = "Happy " + str(age) + "rd Birthday!"

print(massage)
