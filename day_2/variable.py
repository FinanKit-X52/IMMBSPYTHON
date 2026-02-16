first_name = "Ankit"

last_name = "Kumar"

full_name = "Ankit Kumar"

country = "India"

city = "Delhi"

age = 23

year = 2026

is_married = False

is_true = True

is_light = True

FirstName, LastName, FullName, Country, City, Age, Year, IsMarried, IsTrue, IsLight = "Ankit", "Kumar", "Ankit Kumar", "India", "Delhi", 23, 2026, False, True, True;



# Data Type

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

# Data Type of One Line Variable

print(type(FirstName))
print(type(LastName))
print(type(FullName))
print(type(Country))
print(type(City))
print(type(Age))
print(type(Year))
print(type(IsMarried))
print(type(IsTrue))
print(type(IsLight))



# Lenght of the first_ame 

print(len(first_name))

# Length of the FirstName 

print(len(FirstName))


# Comparing the Length of first_name and last_name

is_equal = len(first_name) == len(last_name)

print(is_equal)


# Comparing the Length of FirstName and LastName

IsEqual = len(FirstName) == len(LastName)

print(IsEqual)




num_one = 5

num_two = 4



total = num_one + num_two

diff = num_one - num_two

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)


import math

radius = 30

area_of_circle = math.pi * (radius ** 2)

circum_of_circle = 2 * math.pi * radius 

print(area_of_circle, circum_of_circle)



# User input to calculate the Area and Circumference of the circle


Radius = float(input("Enter the Radius of the Circle"))

Area_of_cicle = math.pi * (Radius ** 2)

Circum_of_circle = 2 * math.pi * Radius


print(Area_of_cicle, Circum_of_circle)


First_Name = str(input("Tell us your First Name"))
Last_Name = str(input("Tell us your Last Name"))
Country_Name = str(input("Tell us your Country Name"))
Use_Age = int(input("Tell us your Age"))


print(First_Name, Last_Name, Country_Name, Use_Age)


help("keywords")


print("You are Good to go")