# Python Programming Assignment: Fundamentals
# 50 Beginner-Friendly Solutions
# Use print() for output and input() wherever required.

print('\nPART 1: INPUT AND OUTPUT FUNCTIONS')

# Question 1: Print Hello, World! and a name on separate lines.
print('\nQ1')
print('Hello, World!')
print('Ali')

# Question 2: Ask for favorite color.
print('\nQ2')
color = input('Enter your favorite color: ')
print('Your favorite color is', color)

# Question 3: Three words separated by a hyphen in one print statement.
print('\nQ3')
print('Python', 'is', 'fun', sep='-')

# Question 4: Calculate age from birth year, assuming the year is 2026.
print('\nQ4')
birth_year = int(input('Enter your birth year: '))
print('Your age is', 2026 - birth_year)

# Question 5: Print the sum in the requested format.
print('\nQ5')
print('The sum of 5 and 5 is', 5 + 5)

# Question 6: Join two print statements with a space using end.
print('\nQ6')
print('Hello', end=' ')
print('World')

# Question 7: Join two user-entered strings.
print('\nQ7')
first_text = input('Enter first string: ')
second_text = input('Enter second string: ')
print(first_text + second_text)

# Question 8: Uppercase welcome greeting.
print('\nQ8')
name = input('Enter your name: ')
print(('Welcome, ' + name + '!').upper())

# Question 9: Print city and country.
print('\nQ9')
city = input('Enter your city: ')
country = input('Enter your country: ')
print(city + ', ' + country)

# Question 10: Fix adding a string and integer using str().
print('\nQ10')
# print('My age is ' + 20)  # This would raise a TypeError.
print('My age is ' + str(20))

print('\nPART 2: VARIABLES AND DATA TYPES')

# Question 11: Integer and float data types.
print('\nQ11')
age = 20
height = 5.8
print(type(age))
print(type(height))

# Question 12: Complex number and its type.
print('\nQ12')
complex_number = 3 + 4j
print(complex_number)
print(type(complex_number))

# Question 13: Boolean variable.
print('\nQ13')
is_python_fun = True
print(is_python_fun)

# Question 14: Assign three different values on one line.
print('\nQ14')
a, b, c = 10, 20, 30
print(a, b, c)

# Question 15: Assign the same value to three variables.
print('\nQ15')
x = y = z = 5
print(x, y, z)

# Question 16: Convert numeric input to float.
print('\nQ16')
number = float(input('Enter a number: '))
print(number)
print(type(number))

# Question 17: Convert string input into integer.
print('\nQ17')
number_text = input('Enter 100: ')
number = int(number_text)
print(number)
print(type(number))

# Question 18: Print the real part of a complex number.
print('\nQ18')
value = 6 + 7j
print(value.real)

# Question 19: Length of a paragraph.
print('\nQ19')
paragraph = 'Python is a simple programming language. It is useful for many tasks.'
print('Paragraph length:', len(paragraph))

# Question 20: Swap two values without an extra variable.
print('\nQ20')
a = 10
b = 20
a, b = b, a
print('a =', a, 'b =', b)

print('\nPART 3: ARITHMETIC OPERATORS')

# Question 21: Calculate rectangle area.
print('\nQ21')
length = 8
width = 5
print('Rectangle area:', length * width)

# Question 22: Calculate first number raised to second number.
print('\nQ22')
a = float(input('Enter base: '))
b = float(input('Enter exponent: '))
print('Power:', a ** b)

# Question 23: Division and floor division.
print('\nQ23')
print('Division:', 10 / 3)
print('Floor division:', 10 // 3)

# Question 24: Remainder of 25 divided by 4.
print('\nQ24')
print('Remainder:', 25 % 4)

# Question 25: Average of five user-entered numbers.
print('\nQ25')
n1 = float(input('Enter number 1: '))
n2 = float(input('Enter number 2: '))
n3 = float(input('Enter number 3: '))
n4 = float(input('Enter number 4: '))
n5 = float(input('Enter number 5: '))
print('Average:', (n1 + n2 + n3 + n4 + n5) / 5)

# Question 26: Convert minutes into hours and minutes.
print('\nQ26')
minutes = int(input('Enter total minutes: '))
hours = minutes // 60
remaining_minutes = minutes % 60
print(hours, 'hour(s) and', remaining_minutes, 'minute(s)')

# Question 27: Circle area with pi = 3.14.
print('\nQ27')
radius = float(input('Enter circle radius: '))
print('Circle area:', 3.14 * radius ** 2)

# Question 28: Find the cube of a user-entered number.
print('\nQ28')
number = float(input('Enter number for cube: '))
print('Cube:', number ** 3)

# Question 29: Prove multiplication happens before addition (PEMDAS).
print('\nQ29')
print('10 + 5 * 2 =', 10 + 5 * 2)
print('(10 + 5) * 2 =', (10 + 5) * 2)

# Question 30: Simple interest.
print('\nQ30')
principal = float(input('Enter principal: '))
rate = float(input('Enter annual interest rate (%): '))
time = float(input('Enter time in years: '))
print('Simple interest:', principal * rate * time / 100)

print('\nPART 4: COMPARISON AND LOGICAL OPERATORS')

# Question 31: Check if the first number is greater than the second.
print('\nQ31')
first = float(input('Enter first number: '))
second = float(input('Enter second number: '))
print('First is greater:', first > second)

# Question 32: Check whether a number is even.
print('\nQ32')
number = int(input('Enter an integer: '))
print('Even:', number % 2 == 0)

# Question 33: Check whether a number is between 10 and 50, inclusive.
print('\nQ33')
number = float(input('Enter a number: '))
print('Between 10 and 50:', number >= 10 and number <= 50)

# Question 34: Check if a string equals 'Python'.
print('\nQ34')
text = input('Enter a word: ')
print('Equals Python:', text == 'Python')

# Question 35: Check whether user is Admin or Superuser.
print('\nQ35')
role = input('Enter user role: ')
print('Allowed role:', role == 'Admin' or role == 'Superuser')

# Question 36: Reverse a Boolean using not.
print('\nQ36')
is_active = True
print('Original:', is_active)
print('Reversed:', not is_active)

# Question 37: Floating-point comparison.
print('\nQ37')
print('0.1 + 0.2 == 0.3:', 0.1 + 0.2 == 0.3)
print('Explanation: Some decimals cannot be represented exactly in binary floating-point.')

# Question 38: Check user is NOT under 18.
print('\nQ38')
age = int(input('Enter age: '))
print('Not under 18:', not (age < 18))

# Question 39: Check positive and odd.
print('\nQ39')
number = int(input('Enter an integer: '))
print('Positive and odd:', number > 0 and number % 2 != 0)

# Question 40: Compare lengths of two strings.
print('\nQ40')
text1 = input('Enter first string: ')
text2 = input('Enter second string: ')
print('First string length:', len(text1))
print('Second string length:', len(text2))
print('Same length:', len(text1) == len(text2))

print('\nPART 5: ASSIGNMENT OPERATORS')

# Question 41: Add 5 to x with +=.
print('\nQ41')
x = 10
x += 5
print(x)

# Question 42: Subtract 3 from price with -=.
print('\nQ42')
price = 20
price -= 3
print(price)

# Question 43: Double balance with *=.
print('\nQ43')
balance = 50
balance *= 2
print(balance)

# Question 44: Divide total by 4 with /=.
print('\nQ44')
total = 100
total /= 4
print(total)

# Question 45: Square a number with **=.
print('\nQ45')
number = 6
number **= 2
print(number)

# Question 46: Increment counter by 1.
print('\nQ46')
counter = 0
counter += 1
print(counter)

# Question 47: Find remainder with %=.
print('\nQ47')
number = 9
number %= 2
print(number)

# Question 48: Floor division with //=.
print('\nQ48')
number = 17
number //= 3
print(number)

# Question 49: Change n from 2 to 20 with three assignment-operator lines.
print('\nQ49')
n = 2
n += 3
n *= 2
n += 10
print(n)

# Question 50: Add 10 to user-entered number using +=.
print('\nQ50')
number = float(input('Enter a number: '))
number += 10
print('Final result:', number)

print('\nAll 50 questions completed!')
