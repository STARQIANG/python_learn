def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['zhangsan', 'liming', 'york']
greet_users(usernames)