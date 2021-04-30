# import os 
# import time 
# print("\nWelcome to the Login Signup Page ")
# print("\n \n1. For Sign_up\n2. For Login")
# def login_page(a):
#     if a == 1:
#         name=input('\nEnter Your Name: ')
#         e=1
#         while e<=3:
#             username  = input("\nEnter a username:")
#             if username.isdigit():
#                 print("\nYou write the only integer :\n \nPlease enter valid username :")  
#             else:
#                 password  = input("\nEnter a password:")
#                 l, u,d,s = 0,0,0,0
#                 for i in password:
#                     if i.isdigit():
#                         l+=1
#                     if i.islower():
#                         u+=1
#                     if i.isupper():
#                         d+=1
#                     if i in ("@"or "#"):
#                         s+=1
#                 if (l >=1 and u>=1 and d>=1 and s>=1):
#                     file1 = open("lsp.txt", "w")
#                     file1 = open("lsp.txt", "w")
#                     file1.write(name+':'+username+':'+password)
#                     file1.close()
#                     print('\nYou Successfully SignUp !')
#                     a=int(input("2. For login:\n \n1. for back :\n \n please write, what do you want to do? :"))
#                     if a == 2:
#                         f=1
#                         while f<=3:
#                             login1 = input("\nUserName : ")
#                             file1 = open("lsp.txt", "r")
#                             fi=file1.read()
#                             fil=fi.split(':')
#                             if login1 == fil[1]:
#                                 print()
#                                 z=0
#                                 while z < 3:
#                                     c=0
#                                     for i in fil:
#                                         password=input("\nEnter your password :")
#                                         if password in fil:
#                                             print("\nYour login is succeesfully :")
#                                             exit()         
#                                         else:
#                                             print("\nYou write the wrong password : \nPlease try again:")
#                                         c+=1
#                                         if c==3:
#                                             os.system('cls' if os.name == 'nt' else 'clear') 
#                                             second = 30
#                                             for i in range (second):
#                                                 print(str(second-i))
#                                                 time.sleep(1)
#                                                 os.system('cls' if os.name == 'nt' else 'clear')
#                                             print("\nTime is Up")
#                                     z+=1
#                             elif f != 3:
#                                 print("\n \nYou did not write the valid user name \n \nTry again:_you have only",3-f,"more chance :")
#                             else:
#                                 print("\n \nTry after some times :")
#                             f+=1
#                     else:
#                         print("\n \nYou choose the back options : \n \nThanks for visit this page :")
#                         exit()
#                 else:
#                     print("\n \nYou did write the valid password :\n \n try again after some times :")
#             e+=1
#     if a == 2:
#         f=1
#         while f<=3:
#             login1 = input("\nUserName : ")
#             file1 = open("lsp.txt", "r")
#             fi=file1.read()
#             fil=fi.split(':')
#             if login1 == fil[1]:
#                 print()
#                 z=0
#                 while z < 3:
#                     c=0
#                     for i in fil:
#                         password=input("\nEnter your password :")
#                         if password in fil:
#                             print("\nYour login is succeesfully :")
#                             exit()         
#                         else:
#                             print("\nYou write the wrong password : \nPlease try again:")
#                         c+=1
#                         if c==3:
#                             os.system('cls' if os.name == 'nt' else 'clear') 
#                             second = 30
#                             for i in range (second):
#                                 print(str(second-i))
#                                 time.sleep(1)
#                                 os.system('cls' if os.name == 'nt' else 'clear')
#                             print("\nTime is Up")
#                     z+=1
#             elif f != 3:
#                 print("\n \nYou did not write the valid user name \n \nTry again:_you have only",3-f,"more chance :")
#             else:
#                 print("\n \nTry after some times :")
#             f+=1
# me = int(input("\nWhat do you want to do ?"))
# login_page(me)

