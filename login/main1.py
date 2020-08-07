
# def make_account():

#     filename = ("username");
#     with open (filename, "w") as f:
#         f.write (input("Enter a username: "));

#     filename = ("password");
#     with open (filename, "w") as f:
#         f.write (input("Enter a password: "));


# def login():
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     check()

# def check():
#     if username == open("username").read() and passsword == open("password").read():
#         print("Successful login")
#     else:
#         print('Incorrect')
# import os.path
# if os.path.exists("username"):
#     login()
# else:
#     make_account()


username = 'Polly1220'

password = 'Bob'

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")
