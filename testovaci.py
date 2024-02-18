users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user = input("Enter your user name: ")
password = input("Enter your password: ")

if user in users and password == users[user]:
    print(f"Welcome to the app, {user}")
else:
    print("Unregistered user, terminating the program...")