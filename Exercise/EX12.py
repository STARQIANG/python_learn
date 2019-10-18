#函数
#例一：定义函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
greet_user()

#例二：向函数传递信息
#在函数greet_user()的定义中，变量username是一个形参
def greet_user(username):
    print("Hello, " + username.title() + "!")
#在greet_user('york')中，将实参 'york'传递给了函数greet_user()，这个值被存储在形参username中
greet_user('york')

###传递实参
#例三：位置实参，基于实参的顺序
def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
#根据需要调用函数任意次数，位置实参的顺序很重要
describe_pet('dog', 'willie')
#关键字实参
describe_pet(animal_type='hamster', pet_name='harry')

#例四：默认值，编写函数时，可给每个形参指定默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
#等效的函数调用
describe_pet('hamster', 'harry')

#返回值
#例五：返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name=first_name +  ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#例六：让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' '  + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' '  + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#例七：返回字典，函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#新增了一个可选形参age，并将其默认值设置为空字符串
def build_person(first_name, last_name, age=''):
    person =  {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)


#例七：结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name=first_name +  ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#例八：传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['zhangsan', 'liming', 'york']
greet_users(usernames)

#例九：在函数中修改列表

def print_models(unprinted_desigens,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_desigens:
        current_design =unprinted_desigens.pop()

        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_mobels(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_mobels(completed_models)

#例十：传递任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#例十一：结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " +str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#例十二：使用任意数量的关键字实参,两个星号创建一个空字典
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


