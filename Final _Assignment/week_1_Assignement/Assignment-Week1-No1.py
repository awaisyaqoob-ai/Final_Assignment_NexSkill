# Week 1 - Assignment No. 1
# All 17 beginner-friendly Python solutions in one file.
# Run this file and answer the questions one by one.


#######################################################

# Question 1: Convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

print("---------------------------------------------")


#######################################################

# Question 2: Calculate the area of a rectangle.
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area of rectangle:", area)

print("---------------------------------------------")


#######################################################

# Question 3: Calculate compound interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))
interest = principal * (1 + rate / 100) ** time - principal
print("Compound interest:", round(interest, 2))

print("---------------------------------------------")


#######################################################

# Question 4: Calculate the perimeter of a rectangle.
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
print("Perimeter of rectangle:", perimeter)

print("---------------------------------------------")


#######################################################

# Question 5: Find the average of three numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average:", average)

print("---------------------------------------------")


#######################################################

# Question 6: Display the square and cube of a number.
number = float(input("Enter a number: "))
print("Square:", number ** 2)
print("Cube:", number ** 3)

print("---------------------------------------------")


#######################################################

# Question 7: Distribute candies equally among students and find leftovers.
candies = int(input("Enter number of candies: "))
students = int(input("Enter number of students: "))
if students > 0 and candies >= 0:
    each = candies // students
    leftover = candies % students
    print("Candies per student:", each)
    print("Candies left:", leftover)
else:
    print("Enter a non-negative number of candies and at least one student.")

print("---------------------------------------------")


#######################################################

# Question 8: Calculate profit or loss from cost and selling prices.
cost = float(input("Enter cost price: "))
selling = float(input("Enter selling price: "))
if selling > cost:
    print("Profit:", selling - cost)
elif selling < cost:
    print("Loss:", cost - selling)
else:
    print("No Profit No Loss")

print("---------------------------------------------")


#######################################################

# Question 9: Find total marks, percentage and average for 5 subjects.
# Assume each subject is out of 100 marks.
m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))
total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
average = total / 5
print("Total marks:", total)
print("Percentage:", percentage, "%")
print("Average marks:", average)

print("---------------------------------------------")


#######################################################

# Question 10: Calculate HRA (20%), DA (15%) and total salary.
basic = float(input("Enter basic salary: "))
hra = basic * 20 / 100
da = basic * 15 / 100
total = basic + hra + da
print("HRA:", hra)
print("DA:", da)
print("Total salary:", total)

print("---------------------------------------------")


#######################################################

# Question 11: Convert age in years to months and approximate days.
age = int(input("Enter your age in years: "))
months = age * 12
days = age * 365
print("Age in months:", months)
print("Approximate age in days:", days)

print("---------------------------------------------")


#######################################################

# Question 12: Convert US dollars to Pakistani rupees using a fixed rate.
# Example rate for this exercise only: 1 USD = 280 PKR.
usd = float(input("Enter amount in USD: "))
rate = 280
pkr = usd * rate
print("Amount in PKR:", pkr)

print("---------------------------------------------")


#######################################################

# Question 13: Find the sum of the first n natural numbers.
n = int(input("Enter a positive whole number: "))
if n >= 1:
    total = n * (n + 1) // 2
    print("Sum of first", n, "natural numbers:", total)
else:
    print("Please enter a positive whole number.")

print("---------------------------------------------")


#######################################################

# Question 14: Calculate percentage of correct answers.
total = int(input("Enter total questions: "))
correct = int(input("Enter correct answers: "))
if total > 0 and 0 <= correct <= total:
    percentage = correct / total * 100
    print("Score:", percentage, "%")
else:
    print("Please enter valid numbers of questions and answers.")

print("---------------------------------------------")


#######################################################

# Question 15: Calculate speed using distance and time.
distance = float(input("Enter distance in kilometers: "))
time = float(input("Enter time in hours: "))
if time > 0:
    speed = distance / time
    print("Speed:", speed, "km/h")
else:
    print("Time must be greater than zero.")

print("---------------------------------------------")


#######################################################

# Question 16: Calculate Body Mass Index (BMI).
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
if height > 0:
    bmi = weight / (height ** 2)
    print("BMI:", round(bmi, 2))
else:
    print("Height must be greater than zero.")

print("---------------------------------------------")


#######################################################

# Question 17: Convert minutes to hours and remaining minutes.
minutes = int(input("Enter total minutes: "))
if minutes >= 0:
    hours = minutes // 60
    remaining = minutes % 60
    print(hours, "hours and", remaining, "minutes")
else:
    print("Minutes cannot be negative.")

print("---------------------------------------------")
