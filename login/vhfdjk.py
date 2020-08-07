

while True:
    user_option=input("Enter Signup/Login? \n")

    if user_option=="Signup":
        user_name=input("Enter username\n")
        password1=str(input("Enter Your Password\n"))
        password2=str(input("Enter Re-Again Password\n"))
        if password1!=password2:
            print("Both passsword is not same")
        else:
            print("Congurational your new id")
            break
    elif user_option=="Login":
        user_name1=input("Enter Username\n")
        password=str(input("Enter Your Password\n"))
        if user_name==user_name1 and password==password1:
            print("Your username and password both is same")
        else:
            print("Your username and password is not correct")
        break