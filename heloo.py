
# print("~-~-~-~-~-~-~ Stanford Schooling System ~-~-~-~-~-~-~")
# 
# print("")
# 
# print("~-~-~-~-~-~-~ Student Details ~-~-~-~-~-~-~")
# 
# name=input("Enter your Full Name: ")
# roll=input("Enter your Roll No.: ")
# clasS=input("Enter your Class: ")
# 
# print("")
# 
# print("~-~-~-~-~-~-~ Obtained Marks Details ~-~-~-~-~-~-~")
# 
# eng=int(input("English Obtained marks: "))
# maths=int(input("Maths Obtained marks: "))
# pys=int(input("Physics Obtained marks: "))
# chem=int(input("Chemistry Obtained marks: "))
# isl=int(input("Islamiat Obtained marks: "))
# 
# 
# 
# totalMarks = 500
# obtainedMarks = eng + maths + pys + chem + isl
# 
# 
# percentage = (obtainedMarks / totalMarks) * 100
# 
# 
# print("")
# 
# 
# 
# if percentage >= 90 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> A+ Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
# elif percentage >= 80 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> A Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
# elif percentage >= 70 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> A Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
# elif percentage >= 60 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> B Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
# elif percentage >= 50 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> C Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
# elif percentage >= 40 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> D Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
# elif percentage >= 30 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> E Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
#     
# elif percentage < 30 and percentage < 100:
#     print(f"{name}, You got {percentage}% -> Failed \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
#     
# 
# else:
#     print(f"{name}, Write the marks or details properly.")


# marks=eval(input("Enter Total Marks -> (out of 100): "))
# att=eval(input("Enter Attendence in % : "))
# quiz=eval(input("Enter Quiz Marks: "))
# assignment=eval(input("Enter Assignment Marks: "))
# mid=eval(input("Enter Mids Marks: "))
# final=eval(input("Enter Final Marks: "))
# 
# print("\n")
# 
# if (marks >= 80 and marks < 100) and att >= 85 and quiz >= 7 and assignment >=7 and mid >=25 and final >= 45:
#     print(f"Excellent Performance - Eligible for 100% Scholarship.")
# elif (marks >= 70 and marks < 100) and att >= 80 and quiz >= 6 and assignment >= 6 and mid >= 20 and final >= 40:
#     print(f"Best Performance - Eligible for 90% Scholarship.")
# elif (marks >= 60 and marks < 100) and att >= 70 and quiz >= 5 and assignment >= 5 and mid >= 18 and final >= 35:
#     print(f"Very Good Performance - Eligible for 70% Scholarship.")
# elif  att < 70 :
#     print(f"Attendance should be greater than 70% - Not Eligible for Scholarship and in warnings of SOA.")
# else:
#     print(f"Enter the details properly!")


# print("-_-_- Sign Up -_-_- \n\n")
# 
# eUsername=input("username: ").lower()
# ePassword=input("password: ").lower()
# 
# print("")
# 
# print("-_-_- Log In User -_-_- \n\n")
# 
# username=input("Enter your name: ").lower()
# password=input("Enter your password: ")
# 
# 
# print("")
# 
# if (username == eUsername or username == eUsername or username == eUsername) and (password == ePassword):
#     print(f"Logged In Successfully.. \n\n Welcome {username}, to Business Giants, Where we manage businesses \n")
# elif (username == eUsername or username == eUsername or username == eUsername) and (password == ePassword):
#     print(f"Logged In Successfully.. \n\n Welcome {username}, to Business Giants, Where we manage businesses \n")
# else:
#     print(f"Invalid User")








# Data Varialbles of User -> Tariq Rasheed of different palatforms


# # NetFlix Data
# 
# NetFlixUserName="tariqrasheed006"
# NetFlixPassword="fa108ok31"
# 
# # Facebook Data
# 
# FaceBookUserName="tariq_17"
# FaceBookPassword="Admin12"
# 
# 
# # Youtube Data
# 
# YoutubeUserName="tariq2003"
# YoutubePassword="helloWorld2003"
# 
# 
# 
# print("~_~_~_~_~_~_~_~ Write Your credintials of platform you want to login ~_~_~_~_~_~_~_~ \n\n")
# 
# username=input("Enter Your Userame of -> (Netflix, Youtube, Facebook): ")
# password=input("Enter Your Password of -> (Netflix, Youtube, Facebook): ")
# 
# print("\n\n")
# 
# if username == NetFlixUserName and password == NetFlixPassword:
#     print(f"welcome {username}, You are Logged in to Netflix")
# elif username == FaceBookUserName and password == FaceBookPassword:
#     print(f"welcome {username}, You are Logged in to Facebook")
# elif username == YoutubeUserName and password == YoutubePassword:
#     print(f"welcome {username}, You are Logged in to YouTube")
# 
# else:
#     print("Invalid credintials.")


#Nested Decisions in Python
#multi-decisions program!


# User Data Base:

# tariqEmail = "tariq.official1712@gmail.com"
# tariqPassword = "admin123"
# 
# rafayEmail = "rafayShaikh@gmail.com"
# rafayPassword = "fa108ok31"
# 
# shamasEmail = "shamas123@gmail.com"
# shamasPassword = "helloworld123"
# 
# 
# 
# 
# print("********Welcome to Netflix********\n\n")
#  
# name=input("Enter your Name: ") 
# email=input("Enter your Email: ") 
# password=input("Enter your Password: ") 
# age=eval(input("Enter your age: ")) 
#  
# print("\n") 
#  
# 
# if age >= 18:
#     print(f"Dear {name}, Welcome to Netflix! ")
#     if email == tariqEmail and password == tariqPassword :
#         print(f"{name}, You can watch movies or series now ->  please select category")
#     elif email == rafayEmail and password == rafayPassword :
#         print(f"{name}, You can watch movies or series now ->  please select category")
#     elif email == shamasEmail  and password == shamasPassword:
#         print(f"{name}, You can watch movies or series now ->  please select category")  
#     else:
#         print(f"Your Login credentials are invalid!")
# else:
#     print(f"Dear {name}, Please watch pogo!")
 
 

 
 
 
print("************** Multiple App Player **************\n")
 
select=int(input("Select an App you want to work:\n \n1.Calculator \n2.Clothing Store \n3.Student Marksheet \n4.Marriage Lawn Recommendation System  \n\n ->  "))

print("\n")

if select == 1:
    print("~_~_~_~_~ Calculator ~_~_~_~_~ \n")
    
    method=eval(input("What you want to do?:\n \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n\n -> "))
    num1=eval(input("Enter number 1 to proceed: "))
    num2=eval(input("Enter number 2 to proceed: "))
    print("\n")
    if method == 1:
        print(f"This is your Addition: {num1 + num2}")
    elif method == 2:
        print(f"This is your Substraction: {num1 - num2}")    
    elif method == 3:
        print(f"This is your Multiplication: {num1 * num2}") 
    elif method == 4:
        print(f"This is your Division: {num1 / num2}")
    else:
        print(f"Invalid input")
        
elif select == 2:
    print("~_~_~_~_~ Mehboob Suggestion Clothing Platform ~_~_~_~_~ \n")
    
    print("~_~_~_~_~ Customer Details ~_~_~_~_~ \n")
    
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    contact=input("Enter your contact: ")
    
    print("\n")
    
    budget=int(input("Enter your budget: "))
    
    if budget <= 10000 and budget > 5000:
        print(f"Dear {name}, According to the details you have provided you are eligible for Casual Wear")
    elif budget <= 50000 and budget > 10000:
        print(f"Dear {name}, According to the details you have provided you are eligible for Formal Wear")
    elif budget <= 1000000 and budget > 50000:
        print(f"Dear {name}, According to the details you have provided you are eligible for Party Wear")     
    else:
         print("We are not able to provide clothes in this budget")
         
elif select == 3 :
    
    print("~-~-~-~-~-~-~ Stanford Schooling System ~-~-~-~-~-~-~")
 
    print("")
 
    print("~-~-~-~-~-~-~ Student Details ~-~-~-~-~-~-~")
 
    name=input("Enter your Full Name: ")
    roll=input("Enter your Roll No.: ")
    clasS=input("Enter your Class: ")
 
    print("")
 
    print("~-~-~-~-~-~-~ Obtained Marks Details ~-~-~-~-~-~-~")
 
    eng=int(input("English Obtained marks: "))
    maths=int(input("Maths Obtained marks: "))
    pys=int(input("Physics Obtained marks: "))
    chem=int(input("Chemistry Obtained marks: "))
    isl=int(input("Islamiat Obtained marks: "))
 
    totalMarks = 500
    obtainedMarks = eng + maths + pys + chem + isl
 
    percentage = (obtainedMarks / totalMarks) * 100
 
    print("")
 
    if percentage >= 90 and percentage < 100:
        print(f"{name}, You got {percentage}% -> A+ Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
    elif percentage >= 80 and percentage < 100:
        print(f"{name}, You got {percentage}% -> A Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
    elif percentage >= 70 and percentage < 100:
        print(f"{name}, You got {percentage}% -> A Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
    elif percentage >= 60 and percentage < 100:
        print(f"{name}, You got {percentage}% -> B Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
    elif percentage >= 50 and percentage < 100:
        print(f"{name}, You got {percentage}% -> C Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
    elif percentage >= 40 and percentage < 100:
        print(f"{name}, You got {percentage}% -> D Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
    elif percentage >= 30 and percentage < 100:
        print(f"{name}, You got {percentage}% -> E Grade \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}") 
    elif percentage < 30 and percentage < 100:
        print(f"{name}, You got {percentage}% -> Failed \n Obtained Marks : {obtainedMarks} Total Marks: {totalMarks}")
     
    else:
        print(f"{name}, Write the marks or details properly.")


elif select == 4:
    
    print("_~_~_~_~_~_~_~_~_~_~_~_~_Lawn Recommandation System_~_~_~_~_~_~_~_~_~_~_~_~_\n\n")
    
    
    print("_~_~_~_~_~_~_~_~_~_~_~_~_User Details_~_~_~_~_~_~_~_~_~_~_~_~_\n")
    
    name=input("Enter Your Name: ").capitalize()
    email=input("Enter Your Email: ")
    contact=input("Enter Your Contact Number: ")
    
    print("")
    
    print("_~_~_~_~_~_~_~_~_~_~_~_~_Lawn Details_~_~_~_~_~_~_~_~_~_~_~_~_\n")
    
    budget=eval(input("Enter your budget -> (min: 500000, max: 2500000): "))
    guest=int(input("Enter guests -> (min: 300, max: 800): ")) 
    ac=input("Enter AC required or not -> (Yes/No): ").lower()
    parking=input("Enter Parking required or not -> (Yes/No): ").lower()
    hallType=input("Enter Hall Type -> (Outdoor/Indoor): ").lower()
    
    print("")
    
    if (budget <= 500000 and budget > 100000) and (guest <= 300) and (ac == "no") and (parking == "no") and (hallType == "outdoor"):
        print(f"Welcom {name}, to Mustaqbil Wedding Lawn Recommendation System -> \n\n According to the details your have provided: \n\n -Budget: {budget}\n -Guests: {guest} \n -AC: {ac} \n -Parking: {parking} \n -Hall Type: {hallType} \n\n There are the lawns you could consider -> (Subhan Palace, The Avenue, Casamento) ")
    elif (budget <= 1000000 and budget > 500000) and (guest <= 500) and (ac == "yes") and (parking == "yes") and (hallType == "indoor"):
        print(f"Welcom {name}, to Mustaqbil Wedding Lawn Recommendation System -> \n\n According to the details your have provided: \n\n -Budget: {budget}\n -Guests: {guest} \n -AC: {ac} \n -Parking: {parking} \n -Hall Type: {hallType} \n\n There are the lawns you could consider -> (City Lawn, Hilton Grand Banquet, Al-Mehmil Banquet)")
    elif (budget <= 2500000 and budget > 1000000) and (guest <= 800) and (ac == "yes") and (parking == "yes") and (hallType == "indoor"):
        print(f"Welcom {name}, to Mustaqbil Wedding Lawn Recommendation System -> \n\n According to the details your have provided: \n\n -Budget: {budget}\n -Guests: {guest} \n -AC: {ac} \n -Parking: {parking} \n -Hall Type: {hallType} \n\n There are the lawns you could consider -> (Dream Banquet, Grand Palace, Luxury Marquee)")
    else:
        print(f"Dear {name}, Unfortunately We don't have any lawn reccomendation according to the details you have provided so far. Thank You")

    
    
else:
    print("Invalid Input")















