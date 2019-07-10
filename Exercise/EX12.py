def greet_user():
    print("Hello!")
greet_user()

def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('york')


def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name=first_name +  ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


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


def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)



def build_person(first_name, last_name, age=''):
    person =  {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix',  age=27)
print(musician)



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