#Assignment 1
#section 1 Variables and Types 
movie_title = "Akwasi"
release_year = 2022
rating = 6.9
is_blockbuster = True

print(movie_title, type(movie_title))
print(release_year, type(release_year))
print(rating, type(rating))
print(is_blockbuster, type(is_blockbuster))

#section 2 Userinput and Math
name =input("what is your name?")
year_of_birth  = int(input("which year were you born?"))
years_old = str(2026 - year_of_birth)
print( "Hi, " + name, "You are approximately " + years_old,  "years old")


#Section 3: Type Conversion and f-strings
print ("Hi John!,Welcome to Philip Assignment i need you to Enter two numbers")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
total_num = (num1 * num2) 
print(f"total is : {total_num} ")


#Section 4: Formatted Receipt
item_name = "Text Books"
Price = 5.99
Quantity = 4
total = Price * Quantity
print("====================")
print("   RECEIPT     ")
print("====================")
print(f"item_name: {item_name}")
print(f"Price: {Price}")
print(f"Quantity: {Quantity}")
print("--------------------")
print(f"total: {total}")
print("====================")


#Section 5: Mini-Project — Profile Card

name = input("what is your name? ")
hometown = input("what is your hometown name? ")
hobby = input("what is your favorite hobby? ")
fun_fact = input("what is one fun fact about yourself? ")
birth_year = int(input("which year were you born? "))
age = str(2026 - birth_year)
print("====================")
print(f"   PROFILE: {name}     ")
print("====================")
print(f"hometown: {hometown}")
print(f"hobby: {hobby}")
print(f"fun_fact: {fun_fact}")
print(f"age: {age}")
print("====================")

#video URL https://youtu.be/xwjxSNzmh3s
