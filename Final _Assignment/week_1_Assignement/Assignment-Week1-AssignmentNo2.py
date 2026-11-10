

import math
import random
import re
import string
import sys
from collections import Counter
from itertools import permutations

INTERACTIVE = "--interactive" in sys.argv


def heading(title):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)


def show(question, answer):
    print("\n" + question)
    print("Answer:", answer)


def number(prompt, example):
    """Use sample numbers by default; ask user in interactive mode."""
    return int(input(prompt)) if INTERACTIVE else example


def text_input(prompt, example):
    return input(prompt) if INTERACTIVE else example


# ================================================================
# PAGE 2 - STRING MANIPULATION
# ================================================================
heading("PAGE 2 - STRING MANIPULATION")

# Q1: Create a new string using the first, middle, and last character.
# Logic: Use indexes 0, len(text)//2 and -1.
s = "Python"
result = s[0] + s[len(s) // 2] + s[-1] if s else ""
show("1. First, middle and last character", result)

# Q2: Count occurrences of all characters in a given string.
# Logic: Make a dictionary that counts each character.
s = "programming"
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
show("2. Character occurrences", counts)

# Q3: Reverse a given string.
# Logic: Slicing with -1 step reverses all characters.
s = "Python"
show("3. Reverse string", s[::-1])

# Q4: Split a string on hyphens.
# Logic: The split('-') method separates the words.
s = "apple-banana-orange"
show("4. Split on hyphens", s.split("-"))

# Q5: Remove punctuation/special symbols from a string.
# Logic: Keep only letters, digits and whitespace.
s = "Hello! How are you? #Python@2026"
cleaned = "".join(char for char in s if char.isalnum() or char.isspace())
show("5. Remove punctuation", cleaned)


# ================================================================
# PAGE 2 - LIST MANIPULATION
# ================================================================
heading("PAGE 2 - LIST MANIPULATION")

# Q1: Reverse a list in Python.
# Logic: Slice backwards to create a reversed list.
items = [1, 2, 3, 4, 5]
show("1. Reverse list", items[::-1])

# Q2: Turn every item of a list into its square.
# Logic: Multiply every item by itself.
items = [1, 2, 3, 4]
show("2. Square every item", [x * x for x in items])

# Q3: Remove empty strings from a list.
# Logic: Add only non-empty strings to the new list.
items = ["Ali", "", "Sara", "", "Ayesha"]
show("3. Remove empty strings", [x for x in items if x != ""])

# Q4: Add a new item after a specified item.
# Logic: Find its index, then insert after that position.
items = [10, 20, 30, 40]
if 20 in items:
    items.insert(items.index(20) + 1, 25)
show("4. Insert 25 after 20", items)

# Q5: Replace a list's item if found.
# Logic: Locate the old value and replace it with the new value.
items = ["apple", "banana", "mango"]
if "banana" in items:
    items[items.index("banana")] = "orange"
show("5. Replace banana with orange", items)


# ================================================================
# PAGE 2 - DICTIONARY MANIPULATION
# ================================================================
heading("PAGE 2 - DICTIONARY MANIPULATION")

# Q1: Check if a value exists in a dictionary.
# Logic: Search the values, not the keys.
marks = {"Ali": 75, "Sara": 90, "Ahmed": 80}
show("1. Does value 90 exist?", 90 in marks.values())

# Q2: Get the key of the minimum value in a dictionary.
# Logic: Find the key whose associated value is smallest.
show("2. Key with minimum value", min(marks, key=marks.get))

# Q3: Delete a list of keys from a dictionary.
# Logic: Remove each listed key using pop with a default.
marks = {"Ali": 75, "Sara": 90, "Ahmed": 80}
for key in ["Ali", "Ahmed"]:
    marks.pop(key, None)
show("3. Delete selected keys", marks)


# ================================================================
# PAGE 2 - TUPLE MANIPULATION
# ================================================================
heading("PAGE 2 - TUPLE MANIPULATION")

# Q1: Reverse a tuple.
# Logic: A tuple also supports slicing.
t = (10, 20, 30, 40)
show("1. Reverse tuple", t[::-1])

# Q2: Access value 20 from the tuple.
# Logic: Find the position of 20 and retrieve it.
t = (10, 20, 30, 40)
show("2. Access value 20", t[t.index(20)])

# Q3: Swap two tuples.
# Logic: Python lets us swap values in one assignment.
a, b = (1, 2), (3, 4)
a, b = b, a
show("3. Tuples after swapping", (a, b))


# ================================================================
# PAGE 3 - LOOP MANIPULATION
# ================================================================
heading("PAGE 3 - LOOP MANIPULATION")

# Q1: Print the first 10 natural numbers using while.
# Logic: Start at 1 and increase until 10.
n = 1
natural = []
while n <= 10:
    natural.append(n)
    n += 1
show("1. First 10 natural numbers (while)", natural)

# Q2: Take user input and print even numbers up to that number.
# Logic: Numbers divisible by 2 are even.
limit = number("Enter end number for evens: ", 20)
show("2. Even numbers", [n for n in range(1, limit + 1) if n % 2 == 0])

# Q3: Take user input and print odd numbers up to that number.
# Logic: Numbers not divisible by 2 are odd.
limit = number("Enter end number for odds: ", 20)
show("3. Odd numbers", [n for n in range(1, limit + 1) if n % 2 != 0])

# Q4: Take user input and print prime numbers up to that number.
# Logic: A prime is greater than 1 and has no divisor from 2 to sqrt(n).
def is_prime(value):
    if value < 2:
        return False
    for divisor in range(2, int(value ** 0.5) + 1):
        if value % divisor == 0:
            return False
    return True

limit = number("Enter end number for primes: ", 30)
show("4. Prime numbers", [n for n in range(2, limit + 1) if is_prime(n)])

# Q5: Print the multiplication table of a given number.
# Logic: Multiply the number by 1 through 10.
value = number("Enter number for multiplication table: ", 5)
print("\n5. Multiplication table:")
for n in range(1, 11):
    print(f"{value} x {n} = {value * n}")





# ================================================================
# PAGE 4 - ASSIGNMENT 3: STRING OPERATIONS
# ================================================================
heading("PAGE 7 - ASSIGNMENT 3: STRING OPERATIONS")

# Q1: Check if a given string is a pangram.
# Logic: Check if all 26 alphabet letters occur at least once.
s = "The quick brown fox jumps over the lazy dog"
show("1. Is the text a pangram?", set(string.ascii_lowercase).issubset(set(s.lower())))

# Q2: Replace every blank space with a hyphen.
# Logic: Replace each literal space character.
s = "I love Python programming"
show("2. Spaces replaced by hyphens", s.replace(" ", "-"))

# Q3: Display letters in either of two strings but not both.
# Logic: Symmetric difference of the two sets of letters.
a, b = "apple", "grape"
letters1 = {c for c in a.lower() if c.isalpha()}
letters2 = {c for c in b.lower() if c.isalpha()}
show("3. Letters in one string only", sorted(letters1 ^ letters2))

# Q4: Find longer string without built-in functions.
# Logic: Count each string's letters by iterating, not using len().
a, b = "python", "programming"
count_a = count_b = 0
for char in a:
    count_a += 1
for char in b:
    count_b += 1
longer = a if count_a > count_b else b if count_b > count_a else "Equal length"
show("4. Longer string (without len)", longer)

# Q5: Count uppercase and lowercase letters.
# Logic: Increase the suitable counter for alphabetic characters.
s = "Hello PYTHON World"
upper = lower = 0
for char in s:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
show("5. Uppercase and lowercase counts", {"uppercase": upper, "lowercase": lower})

# Q6: Check whether two strings are anagrams.
# Logic: Normalize case and spaces; compare sorted characters.
a, b = "Listen", "Silent"
normalize = lambda s: sorted(c.lower() for c in s if c.isalnum())
show("6. Are the strings anagrams?", normalize(a) == normalize(b))

# Q7: Check whether a substring is present in a string.
# Logic: Use the in operator.
s, sub = "I am learning Python", "Python"
show("7. Is substring present?", sub in s)

# Q8: Print all string permutations in lexicographic order without recursion.
# Logic: Generate each arrangement, remove duplicates, and sort.
s = text_input("Enter a short string (3-6 letters): ", "ABC")
if len(s) > 8:
    print("8. Please use 8 or fewer characters to avoid huge output.")
else:
    show("8. Permutations (non-recursive)", sorted({"".join(p) for p in permutations(s)}))

# Q9: Calculate length of string without library functions.
# Logic: Count characters in a loop.
s = "Hello World"
length = 0
for char in s:
    length += 1
show("9. String length without len()", length)

# Q10: Make a string from first two and last two characters.
# Logic: Concatenate slices; if shorter than 2, use an empty string.
s = "Programming"
show("10. First two and last two", s[:2] + s[-2:] if len(s) >= 2 else "")


# ================================================================
# PAGES 5 - MATH OPERATIONS
# ================================================================
heading("PAGES 8-9 - MATH OPERATIONS")

# Q1: Find area of a triangle from its three sides.
# Logic: Check triangle inequality and apply Heron's formula.
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:
    half = (a + b + c) / 2
    area = math.sqrt(half * (half - a) * (half - b) * (half - c))
else:
    area = "Invalid triangle"
show("1. Area of triangle (3, 4, 5)", area)

# Q2: Find quotient and remainder of two numbers.
# Logic: // gives integer quotient, % gives remainder.
a, b = 17, 5
show("2. Quotient and remainder", (a // b, a % b) if b != 0 else "Cannot divide by zero")

# Q3: Print an identity matrix of size n.
# Logic: Put 1 on the main diagonal, 0 everywhere else.
n = number("Identity matrix size: ", 3)
identity = [[1 if row == col else 0 for col in range(n)] for row in range(n)] if n >= 0 else []
print("\n3. Identity matrix:")
for row in identity:
    print(*row)

# Q4: Find LCM of two numbers.
# Logic: LCM(a,b) = abs(a*b) // gcd(a,b), except when a or b is zero.
a, b = 12, 18
lcm = abs(a * b) // math.gcd(a, b) if a and b else 0
show("4. LCM of 12 and 18", lcm)

# Q5: Find sum of first n natural numbers.
# Logic: Use n*(n+1)//2.
n = number("Number of natural terms: ", 10)
show("5. Sum of natural numbers", n * (n + 1) // 2 if n >= 0 else "Use a nonnegative number")

# Q6: Determine whether two numbers are amicable.
# Logic: Sum of proper divisors of each must equal the other, and they must differ.
def divisor_sum(value):
    total = 0
    for divisor in range(1, value):
        if value % divisor == 0:
            total += divisor
    return total

a, b = 220, 284
show("6. Are 220 and 284 amicable?", a != b and a > 0 and b > 0 and divisor_sum(a) == b and divisor_sum(b) == a)

# Q7: Perfect squares in a range whose digit sum is less than 10.
# Logic: Examine perfect squares, then add those with digit sum < 10.
start, end = 1, 100
squares = []
for n in range(max(0, start), end + 1):
    root = math.isqrt(n)
    if root * root == n and sum(int(digit) for digit in str(n)) < 10:
        squares.append(n)
show("7. Squares from 1 to 100 with digit sum < 10", squares)

# Q8: Check whether a number is an Armstrong number.
# Logic: Sum each digit raised to the number of digits and compare.
n = number("Number to check as Armstrong: ", 153)
digits = str(n)
is_armstrong = n >= 0 and sum(int(d) ** len(digits) for d in digits) == n
show("8. Armstrong number check", "it is an Armstrong number" if is_armstrong else "it is not an Armstrong number")


# ================================================================
# PAGES 6 - LIST OPERATIONS
# ================================================================
heading("PAGES 9-10 - LIST OPERATIONS")

# Q1: Find the largest number in a list.
# Logic: max() returns the greatest entry.
items = [11, 45, 9, 27, 32]
show("1. Largest number", max(items))

# Q2: Find the second largest number in a list.
# Logic: Remove duplicates, sort descending, choose the second entry.
items = [10, 30, 20, 30, 40]
distinct = sorted(set(items), reverse=True)
show("2. Second largest distinct number", distinct[1] if len(distinct) >= 2 else "Not enough distinct values")

# Q3: Find largest even and largest odd in a list.
# Logic: Separate evens and odds before finding each maximum.
items = [10, 17, 24, 35, 42, 51]
evens = [x for x in items if x % 2 == 0]
odds = [x for x in items if x % 2 != 0]
show("3. Largest even and largest odd", {"even": max(evens) if evens else None, "odd": max(odds) if odds else None})

# Q4: Find average of a list.
# Logic: Sum the numbers, divide by the number of items.
items = [10, 20, 30, 40]
show("4. Average", sum(items) / len(items) if items else None)

# Q5: Count occurrences of a given element.
# Logic: Use list.count().
items, target = [1, 2, 2, 3, 2, 4], 2
show("5. Occurrences of 2", items.count(target))

# Q6: Remove duplicates from a list.
# Logic: Add an item only when it has not already been added.
items = [1, 2, 2, 3, 1, 4]
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
show("6. Remove duplicates", unique)

# Q7: Find the number occurring an odd number of times.
# Logic: Count each number; return those with an odd frequency.
items = [4, 3, 4, 3, 4, 5, 5]
show("7. Number occurring odd times", [x for x, count in Counter(items).items() if count % 2 == 1])

# Q8: Find union of two lists.
# Logic: Combine lists and keep the first appearance of each element.
a, b = [1, 2, 3], [3, 4, 5]
show("8. Union of lists", list(dict.fromkeys(a + b)))

# Q9: Swap first and last element in a list.
# Logic: Assign the first and last elements simultaneously.
items = [10, 20, 30, 40]
if len(items) > 1:
    items[0], items[-1] = items[-1], items[0]
show("9. Swap first and last", items)

# Q10: Find the longest word and its length from a list.
# Logic: Choose the word with maximum character count.
words = ["cat", "elephant", "tiger", "giraffe"]
longest = max(words, key=len) if words else ""
show("10. Longest word and its length", (longest, len(longest)))

# Q11: Generate random numbers from 1 to 20 and append to a list.
# Logic: Call randint(1, 20) once for every requested item.
n = number("How many random numbers? ", 5)
random_numbers = []
for _ in range(max(0, n)):
    random_numbers.append(random.randint(1, 20))
show("11. Random list", random_numbers)


# ================================================================
# PAGE 7 - DICTIONARY OPERATIONS
# ================================================================
heading("PAGE 10 - DICTIONARY OPERATIONS")

# Q1: Check if a key exists in a dictionary.
# Logic: Membership checks dictionary keys.
d = {"name": "Ali", "age": 20}
show("1. Does key 'age' exist?", "age" in d)

# Q2: Add a key-value pair to a dictionary.
# Logic: Assign a value to a new key.
d["city"] = "Lahore"
show("2. Add key-value pair", d)

# Q3: Find the sum of all dictionary items (numeric values).
# Logic: Add the values, not the string keys.
d = {"a": 10, "b": 20, "c": 30}
show("3. Sum of dictionary values", sum(d.values()))

# Q4: Multiply all dictionary items (numeric values).
# Logic: Start at 1 and multiply by each dictionary value.
product = 1
for value in d.values():
    product *= value
show("4. Product of dictionary values", product)

# Q5: Generate a dictionary {x: x*x} for x from 1 to n.
# Logic: Each number is a key and its square is its value.
n = number("Dictionary end number: ", 5)
show("5. Number-to-square dictionary", {x: x * x for x in range(1, n + 1)})

# Q6: Concatenate two dictionaries.
# Logic: update() adds all items from the second dictionary.
a, b = {"a": 1, "b": 2}, {"c": 3, "d": 4}
combined = a.copy()
combined.update(b)
show("6. Concatenated dictionaries", combined)


# ================================================================
# PAGES 8 - TUPLE OPERATIONS
# ================================================================
heading("PAGES 10-11 - TUPLE OPERATIONS")

# Q1: Create a list of (number, square) tuples over a range.
# Logic: For each n, make the pair (n, n*n).
start, end = 1, 5
show("1. Number-square tuples", [(n, n * n) for n in range(start, end + 1)])

# Q2: Remove tuples whose USN (student number) is outside given range.
# Logic: Keep only tuples with numeric roll number between low and high.
# Example USNs use the prefix 'UNI' followed by a roll number.
students = [("UNI001", "Ali"), ("UNI005", "Sara"),
            ("UNI010", "Ahmed"), ("UNI015", "Zara")]
low = number("Lowest roll number: ", 5)
high = number("Highest roll number: ", 12)
filtered = []
for student in students:
    usn = student[0]
    roll = int(usn.replace("UNI", ""))
    if low <= roll <= high:
        filtered.append(student)
show("2. USN tuples within selected range", filtered)

print("\nAll questions completed in this single Python file.")
