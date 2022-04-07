# if xxx :
#     yyy #xxx == True then do yyy
user_id = input("id?")
user_pwd = input("password?")

'''
if user_input == "111111":
    print("Hello master")
else:
    print("who are you?")
'''
if user_id == "egoing" and user_pwd == "111111":
    print("Hello master")
elif user_id == "yahi" and user_pwd == "222":
    print("Hello master")
else:
    print("who are you?")
