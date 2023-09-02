user = "Carlos"
password = "carlos1923"
oportunities = 3

# if(len(user and password) >= 6):
#     print('your username or password are fine')
    
#     if(user == "Carlos" and password == "123456"):
#         print("Welcome to my first real programm")
#     else:
#         print("Your datas are not satisfactories")
    
# else:
#     print('Your password is short and unsafe')
#     if(user != "Carlos" and password != "123456"):
#         print ('Your password or username is not correct')
    
for i in range(oportunities):
    get_user = input("User: ")
    get_pass = input("Password: ")
    
    if(len(get_pass and get_user)>=6):
        print("Your datas are strong")
        if(get_user == user and get_pass == password):
            print("Welcome have a nice day")
        else:
            oportunities-=1
            print(f"But the password or user is incorrect, try again {oportunities}")
    else:
        print("The information is weak, please try something strongest")