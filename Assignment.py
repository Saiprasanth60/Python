#  Write a program for grading system of marks?

# Marks = int(input("Enter marks here :- "))
# if Marks >= 70:
#     print("Your Grade is A")
# elif Marks >= 60 and Marks < 70:
#     print ("Your Grade is B")
# elif Marks > 50 and Marks < 60:
#     print ("Your Grade is C") 1996 2000 2004
# else:
#     print ("Your not upto the mark")

#  Write a program that check for leap year?

# Year = int(input("Enter the Year:-"))
# if (Year % 4 and Year % 100 and Year % 400) == 0:
#  print ("It is leap year")
# else:
#  print ("It is not leap year")

# Write a program that checks the number is even or odd?

# Number = int(input("Enter Number:-"))
# if Number % 2 == 0:
#     print("Even")
# else:
#     print ("Odd")

# Write a program that takes country, state and print number of districts by users?
# country1 = "india"
# state1 = 29
# country2 = "usa"
# state2 = 50
# if (country1 == input("Enter country:- ")) and (int(input("Enter State:- ")) == state1):
#      print ("India have 29 states")
# if (country2 == input("Enter country:-")) and (int(input("Enter State:- ")) == state2):
#      print ("Usa have 50 states")
# else:
#     print ("Check you entered")


# country1 = "India"
# state1 = 29
# country2 = "Usa"
# state2 = 50
# country = input("Enter Country:- ")
# if country1 == country:
#     if state1 == int(input("Enter state1:- ")):
#         print ("India has 29 states")
#     else:
#         print ("Something went wrong")
# elif country2 == country:
#     if state2 == int(input("Enter state2:- ")):
#         print ("Usa has 50 states")
# else:
#     print ("Something went wrong")


# 5) Write a program for finding largest of Three numbers?
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#  print a
# elif b > a and b > c:
#     print b
# elif c > a and c > b:
#     print c
# else:
#     print("some are equal")

# 6) Check the bank credentials
# accountno = 12345
# typeofaccount = "savings"
# accountname = "sai"
# pin = 3558
# for i in range(4):
#     if  accountno == int(input("Enter number:- ")):
#         if typeofaccount == input("Enter type:- "):
#             if accountname == input("Enter name:- "):
#                 if pin == int(input("Enter pin:- ")):
#                  moneyrequired = int(input("Enter amount:- "))
#                  print(moneyrequired,"debited from your account")
#                 else:
#                     print("Wrong pin")
#             else:
#                 print("Wrong name")
#         else:
#             print("Wrong accounttype")
#     else:
#         print ("Wrong number")


# 7)  Enter then number and power the same number and make a flow

# number = int(input("Enter number here: "))
# for i in range(2,number+1):
#     b = (("{}*".format(i))*i).rstrip('*')
#     print(b.rstrip('*'),'=',i**i)

# 8) Find how many characteries and find out the given character index

# findchar = "currently python is my addict"
# a = input("Enter the character: ")
# b = int(input("Enter the position: "))
# c = findchar.find(a,b)
# print("c {} position is on index {}".format(b,c))


# 9) if duplicates key then those add value into the one key
# c = {}
# loop = int(input("Enter the number of loop:- "))
# for i in range(loop):
#     a = input("Enter the name:- ")
#     b = input("Enter the age:- ")
#     if a in c:
#      c[a] = c[a] + (b,)
#     else:
#      c[a] = (b,)
# print(c)

#10)
a = 20

