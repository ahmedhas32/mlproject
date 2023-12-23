# name = input("please enter your name").strip().capitalize()
# theEmail = input('what\'s your email')

# print(f'your name is {name}')

# theUserName = theEmail[:theEmail.index('@')]
# theSite = theEmail[theEmail.index('@')+1:]


# print(f'your username is {theUserName} and your site is {theSite}')


# age = float(input('what\'s your age?'))

# ageInMonths = int(age*12)

# print(f'your age in months is :{ageInMonths}')

# uName = input("what is your name:")
# country = input("where are you from :").strip().capitalize()

# Price = 100

# isStudent = input("Are You Student").strip().capitalize()

# studentDiscount=0.2

# if country == "Egypt":
#     if isStudent =='Yes':

#         print(f"Hello {uName} because you are from {country} and student \ncourse price is {Price*0.3*(1-studentDiscount)}")
#     else :
#         print(f"Hello {uName} because you are from {country} \ncourse price is {Price*0.3}")

# elif country == "KSA" :
#     print(f"Hello {uName} because you are from {country} \ncourse price is {Price*0.5}" if isStudent != "Yes" else f"Hello {uName} because you are from {country} and student \ncourse price is {Price*0.3*(1-studentDiscount)}")
# else :
#    print(f"Hello {uName} because you are from {country} and student \ncourse price is {Price*0.7}")

def get_user_input(message,options):
    while True:
        print("Select an option:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        try:
            choice = input(message).strip()
            #if choice.isupper() == False : choice = choice.capitalize()  
            #else: choice = choice
            if options.index(choice) <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid entry.")
        except ValueError:
            print("Invalid input. Please enter a valid entry")


#cnt = get_user_input(['Egypt','KSA',"Kuwait" , "UAE" , "Oman","Bahrain"])
# #print(cnt)

# Age = int(input(("Please input your age:")).strip())
# item_list =  ['weeks','months','days','hours','minuites']

# item = get_user_input("Please choose age items: ",
#                       ['weeks','months','days','hours','minuites'])

# months = Age*12
# weeks = Age*52
# days=Age*365
# hours = days*24
# minuites = hours*60

# for i , j in zip(item_list,[weeks,months,days,hours,minuites]):
#     if i == item:
#         print(f"because you chose {i} \nyour age is {j} {i}")

# admins =['Ahmed' , 'Mohamed' , 'Mostafa']

# name = input("please enter your name :").strip().capitalize()

# if name in admins:
#     print(f'Hello {name} Welcome back')
    
#     while True:
#         option = input('delete or update your name').strip().capitalize()
        
      

#         if option == 'Update':
#             theNewName = input("please inter your new name").strip().capitalize()
        

#             admins[admins.index(name)] = theNewName
#             print(f'name updated from {name} to {theNewName}')
#             break
#         elif option == 'Delete':
#             admins.remove(name)
#             print(f'name {name} deleted ')
#             print(admins)
#             break
#         else : 
#             print("please insert valid option else 'update' or 'delete'")
# else :
#     while True:
#         status = input("you are not in admins , add you Y or N ").strip().capitalize()
#         if status in ['Y' , 'Yes']:
#             admins.append(name)
#             print(f'name {name} added admins now are {admins}')
#             break
#         elif status in ['N' , 'No'] :
#             print('Thank you ')
#             break
#         else :
#             print("please insert a valid option")


# myList=['A','B' ,'C','D','E']
# a=0
# while a < 5:
    
#     print(f'{str(a + 1).zfill(3)} . {myList[a]}')
#     a+=1

# import re
# myFavouriteWebs=[]
# url_pattern = re.compile(r'\S+\.(com|net|org)\S*')
# maximumWebs=5

# while maximumWebs > 0 :
#     web= input("input your web url without https://")
#     match = bool(re.match(url_pattern, web))
#     if match == True:
#         full_link=f"https://{web.strip().lower()}"
#         maximumWebs -= 1
#         myFavouriteWebs.append(full_link)
        
#         print(f"{full_link} added remaining {maximumWebs} sites to add")

#         Decision = get_user_input('Would you like to continue',['Yes' , 'No'])
#         if Decision == 'No':
#             print(f"bookmark list contains {len(myFavouriteWebs)} sites , thank you")
#             myFavouriteWebs.sort()
#             index=0
#             print("Printing the list of your bookmarks")
#             while index < len(myFavouriteWebs):

                
#                 print(myFavouriteWebs[index])
#                 index +=1          
#             break
            
#         else : continue


#     else :
#         print("please enter a valid website")
#         Decision = get_user_input('Would you like to continue',['Yes' , 'No'])
#         if (Decision == 'No') & (len(myFavouriteWebs) > 0 ):
#             print(f"bookmark list contains {len(myFavouriteWebs)} sites , thank you") 
#             print(f"bookmark list is full and contain {myFavouriteWebs}")
#             myFavouriteWebs.sort()
#             index=0
#             print("Printing the list of your bookmarks")
#             while index < len(myFavouriteWebs):

                
#                 print(myFavouriteWebs[index])
#                 index +=1          
#             break
#         elif (Decision == 'No') & (len(myFavouriteWebs) == 0) :
#             print(f"bookmark list is empty , thank you") 
#             break
            
#         else : continue



# else :
#     print(f"bookmark list is full and contain {len(myFavouriteWebs)} sites")
    
#     myFavouriteWebs.sort()
#     index=0
#     print("Printing the list of your bookmarks")
#     while index < len(myFavouriteWebs):

        
#         print(myFavouriteWebs[index])
#         index +=1 


# mainPassword="pAssword$"
# input_pasword = input("please type your password")
# tries=4
# while input_pasword != mainPassword and tries > 0 :

#     tries -=1 
#     print(f"incorrect password , you have {tries} remaining trials")
#     input_pasword = input("please type your password")


# else:
#         if input_pasword == mainPassword:

#            print("welcome , password is correct")
#         else:
#             print("trials finished")




# Creating a nested dictionary
employee_details = {
    'employee1': {
        'name': 'John Doe',
        'age': 30,
        'position': 'Software Engineer'
    },
    'employee2': {
        'name': 'Jane Smith',
        'age': 28,
        'position': 'Data Scientist'
    },
    'employee3': {
        'name': 'Bob Johnson',
        'age': 35,
        'position': 'Project Manager'
    }
}

# for employee in employee_details:
#     print(f"data of {employee}")
#     for field in employee_details[employee].keys():
         
#         print(f"employee {employee} has {field} of {employee_details[employee][field]}")


# for item , value in employee_details.items():
#     print (f"details of {item} are :")
#     for child_item , child_value in value.items():
#         print(f"   {child_item} of {item} is {child_value}")

# def salute(*args ):
#     #myList = [i for i in args]
#     #print(f" good afternoon guys {', '.join(myList)}")
#     for skill in args:
#         print(f"{skill}")

# salute("sfdgs","sfdgsd","asdfasdgf")


# def salute(**args ):
#     #myList = [i for i in args]
#     #print(f" good afternoon guys {', '.join(myList)}")
#     for skill , value in args.items():
#         print(f"Hello {value} {skill}")

# salute(sfdgs = "Mr",sfdgsd = "Ms",asdfasdgf = "Mr")


# def show_skills(name , *unlevskills ,**levskills ):
#     #myList = [i for i in args]
#     #print(f" good afternoon guys {', '.join(myList)}")
#     for skill in unlevskills:
#         print(f"{name} has {skill} skill")
#     for skill , level in levskills.items():
#         print(f"{name} has {skill} skill with level {level}")


# levelskills= {
#         "Python": "Advanced",
#         "JavaScript": "Intermediate",
#         "Java": "Beginner",
#         "C++": "Intermediate",
#     }

# show_skills("Ahmed" , *levelskills.keys() , **levelskills)


# x = 1

# def one():
#     print(x)

# def two():
#     x=3
#     print(x)

# def three():
#     global x
#     x=2
#     print(x)


# def four():
#     print(x)

# one()
# two()
# three()
# four()

# def remove_duplicates(word):
#     if len(word) ==1 :
#         return word
#     print(f"word before applying function : {word}")
#     if word[0]==word[1]:
#         return remove_duplicates(word[1:])
#     print(f"word after checking condition function : {word}")
        
#     return word[0] + remove_duplicates(word[1:])

# print(remove_duplicates("wwoooooorrrlldd"))

import os

#os.curdir

# myFile = open('ahmed.txt','w')
# myFile.writelines(['Hello\n' , 'it is me \n'])
# #myFile.write('hi all')
# myFile = open('ahmed.txt','a')
# myFile.write('hi all')


# -----------------------------------------------
# -- File Handling => Write and Append In File --
# -----------------------------------------------

# myFile = open("D:\Python\Files\osama.txt", "w")
# myFile.write("Hello\n")
# myFile.write("Third Line")

# myFile = open(r"D:\Python\Files\fun.txt", "w")
# myFile.write("Elzero Web School\n" * 1000)

# myList = ["Oasma\n", "Ahmed\n", "Sayed\n"]

# myFile = open("D:\Python\Files\osama.txt", "w")
# myFile.writelines(myList)

# myFile = open("D:\Python\Files\osama.txt", "a")
# myFile.write("Elzero")

# myFile = open('ahmed.txt','a')

# print(myFile.tell())


# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ")

print("First Line", end=" ")
print("Second Line")
print("Third Line")

# myFile = open('ahmed.txt','r')

# myFile.seek(12)

# print(myFile.read())


# print(bin(100))

# a = 1
# b = 2

# print(id(a))
# print(id(b))

# names = ['Ahmed' , 'Hassan' , "Solly"]

# for name in map(lambda name : name.strip().upper() , names):
#     print(name)



# def checkNumber(num):

#   return num > 10

# myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

# myResult = filter(checkNumber, myNumbers)
# print(list(myResult))
# for number in myResult:

#   print(number)

# print("#" * 50)



# myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]

# for p in filter(lambda name: name.startswith("A"), myNames):

#   print(p)
  
  
# from functools import reduce

# def sumAll(num1, num2):

#   return num1 + num2

# numbers = [1, 8, 2, 9, 100]

# result = reduce(sumAll, numbers)

# result = reduce(lambda num1, num2: num1 + num2, numbers)

# print(result)



# myString = "Elzero"

# print(reversed(myString))

# for letter in reversed(myString):

#   print(letter)

# import random
# print(dir(random))

# import datetime

# print(datetime.datetime(1982, 10, 25, 10, 45, 55, 150364))

# print(datetime.datetime.now().date().day)
# print(datetime.datetime.now().time().hour)


# myBirthDay = datetime.datetime(1993, 2, 12)
# dateNow = datetime.datetime.now()

# print(f"My Birthday is {myBirthDay} And ", end="")
# print(f"Date Now Is {dateNow}")

# print(f" I Lived For {(dateNow - myBirthDay).days//365.25} years")
# print(f" I Lived For {(dateNow - myBirthDay).days} Days.")

# print(myBirthDay.strftime("%B"))
# print(myBirthDay.strftime("%d, %B, %Y"))


# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

# myString = "Osama"

# myList = [1, 2, 3, 4, 5]

# for letter in myString:

#   print(letter, end=" ")

# for number in myList:

#   print(number, end=" ")

# myIterator = iter(myString)

# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

# for letter in iter("Elzero"):

#   print(letter, end=" ")


# ----------------
# -- Generators --
# ----------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------

def myGenerator():
   yield 2
   yield 4 
   yield 6 


print(myGenerator())

gen = myGenerator()

print(next(gen))
print(next(gen))


# -------------------------
# -- Decorators => Intro --
# -------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------

# def myDecorator(func):  # Decorator

#   def nestedFunc():  # Any Name Its Just For Decoration

#     print("Before")  # Message From Decorator

#     func()  # Execute Function

#     print("After")  # Message From Decorator

#   return nestedFunc  # Return All Data

# @myDecorator

# def sayHello():

#   print("Hello From Say Hello Function")

# @myDecorator

# def sayHowAreYou():

#   print("Hello From Say How Are You Function")

# afterDecoration = myDecorator(sayHello)

# afterDecoration()

# sayHello()







# sayHowAreYou()
print("#" * 50)




def myDecorator1(func):  # Decorator

  def nestedFunc(*args):  # Any Name Its Just For Decoration

    for number in args:

      if number < 0:

        print("Beware One Of The Numbers Is Less Than Zero")

    func(*args)  # Execute Function

  return nestedFunc  # Return All Data






@myDecorator1
def sumAll(*args):
   return sum(args)


print(sumAll(1,-1,2,4))


# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

# from time import time

# def myDecorator(func):  # Decorator

#   def nestedFunc(*numbers):  # Any Name Its Just For Decoration

#     for number in numbers:

#       if number < 0:

#         print("Beware One Of The Numbers Is Less Than Zero")

#     func(*numbers)  # Execute Function

#   return nestedFunc  # Return All Data

# @myDecorator

# def sumAll(*args):
#    return sum(args)


# print(sumAll(1,-1,2,4))



# def speedTest(func):

#   def wrapper():

#     start = time()

#     func()

#     end = time()

#     print(f"Function Running Time Is: {end - start}")

#   return wrapper

# @speedTest

# def bigLoop():

#   for number in range(1, 20000):

#     print(number)

# bigLoop()

# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# --       Advanced Example        --
# -----------------------------------


# the_File= None

# the_tries=5

# while the_tries > 0  :
#      try:
#           print("please enter absolute path to your file")
#           print(f"you have{the_tries} trials to enter")
#           print("Example: D:\Python\Files\yourfile.extension")

#           file_name_and_path = input("File Name => : ").strip()    
#           the_file = open(file_name_and_path, 'r')

#           print(the_file.read())

#           break
#      except FileNotFoundError :
#           the_tries -= 1
#           print(f"file not found you have {the_tries} trials")
#           if the_tries ==0 :
#                print("trials finished , please check file name")
   

# ---------------------------------------
# -- Regular Expressions => Assertions --
# ---------------------------------------
# ^	  Start of String
# $	  End of string
# -------------------------
# Match Email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$

import re






# Email_Pattern = r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)"

# def search_email():
#         the_tries=5
    
#         while the_tries > 0 :
#             try:
 
#                 email = input("please enter your email")
#                 is_email=bool(re.search(Email_Pattern,email))
#                 if is_email ==True:
#                     print("valid email, welcome back")
#                     break
#                 else: 
#                     the_tries -= 1
                    
#                     raise ValueError 
#             except :
                
#                 print ("please insert a valid email")
                
                
#         else : 
#             print("no tries")

    


# def search_email():
#         the_tries=5
    
#         while the_tries > 0 :
        
 
#                 email = input("please enter your email")
#                 is_email=bool(re.search(Email_Pattern,email))
#                 if is_email ==True:
#                     print("valid email, welcome back")
#                     break
#                 else: 
#                     the_tries -= 1
                    
#                     print ("please insert a valid email")
                
#                     continue
#         else : 
#             print("no tries")



# string_one = "I Love Python Programming Language"

# search_one = re.split(r"\s", string_one, 1)

# print(search_one)

# print("#" * 50)

# string_two = "How-To_Write_A_Very-Good-Article"

# search_two = re.split(r"-|_", string_two)

# print(search_two)

# print("#" * 50)

# # Get Words From URL

# for counter, word in enumerate(search_two, 1):

#   if len(word) == 1:

#     continue

#   print(f"Word Number: {counter} => {word.lower()}")

# print("#" * 50)

# my_string = "I Love Python"

# print(re.sub(r"\s", "-", my_string, 1))


# site_regex = r"(http)?(s?)(://)?(w{3})?\.?(\w+\.(com|org|net|info))(:)?(\d+)?/?(.+)?"

# my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

# search = re.search(site_regex,my_web)

# print(search.groups())

# for group in search.groups():

#   print(group)

# print(f"Protocol: {search.group(1)}")
# print(f"Sub Domain: {search.group(2)}")
# print(f"Domain Name: {search.group(3)}")
# print(f"Top Level Domain: {search.group(4)}")
# print(f"Port: {search.group(5)}")
# print(f"Query String: {search.group(6)}")

class Member() :
   def __init__ (self):
      print("hello member")


#member1=Member()

#print(dir(member1))

# print(member1.__class__)


# class Member() :
#    def __init__ (self):
#       self.name="ahmed"


# member1 = Member()
# member2 = Member()

# # print(member2.name)

# class Member() :
#    def __init__ (self,first_name , last_name , gender=None):
#       self.name=first_name
#       self.last = last_name
#       self.gender = gender

#    def callMember(self):
#       if self.gender == 'female':
#           return (f"Hello Ms. {self.name} {self.last:.5s}")
#       else:
#          return (f"Hello Member. {self.name} {self.last:.5s}")
         

# member1 = Member('ahmed' , 'Hassan' )
# member2 = Member('Alia','Ahmed' , 'female')

# # print(member2.name)

# print(member1.callMember())


# print(member2.callMember())

def input_must_chk(message):
    while True:
        input_value = input(message)
        if len(input_value) > 2:
            return input_value
        
        else:
            continue
    


class Member_chk:
   members_list=[]
   #userNum = 0 
   not_allowed_names = ['kharboush','kevin']
   def __init__ (self,name,last):
      #self.name=input_must_chk("please insert your name")
      self.name = name
      if self.name in Member_chk.not_allowed_names:
             raise ValueError ("insert a valid name")
      else :
          pass
      self.last = last
      #self.last = input_must_chk("please insert your last name")
      #self.gender = get_user_input("Please select your gender",['male' , 'female'])
      self.gender = "male"
      self.full_name = f"{self.name.capitalize()} {self.last.capitalize()}"

      Member_chk.members_list.append(self.full_name)


   def salutation(self):
       if self.gender == 'female':
          return 'Ms.'
       else :
          return 'Mr.'
       


   def callMember(self):
             return (f"Hello {self.salutation()} {self.name} {self.last:.5s}")
   
   def deleteMember(self):
        Member_chk.members_list.remove(self.full_name)
        print(f"user {self.full_name} is deleted")
   @classmethod
   def show_users_count(cls):
       print(f"we have {len(cls.members_list)} members in our site")
   @staticmethod
   def obama():
       print(f"كسم حياتي")
       
       


member1 = Member_chk('ahmed','hassan')
member2 = Member_chk('ali','alex')
member3 = Member_chk('omar','ezzat')

# member4 = Member_chk()

# member5 = Member_chk()


# # # print(member2.name)

# print(member1.callMember())

# print(member2.callMember())

# print(Member_chk.members_list)

member3.deleteMember()

print(Member_chk.members_list)
Member_chk.show_users_count()
Member_chk.obama()

print(member1.__class__)

print(type(member1.last))