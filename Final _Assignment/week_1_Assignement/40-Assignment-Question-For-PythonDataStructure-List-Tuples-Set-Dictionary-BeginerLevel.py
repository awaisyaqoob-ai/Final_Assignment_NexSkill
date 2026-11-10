

print('PART A - LISTS')

# A1. Print the first and last items.
nums = [3, 1, 4, 1, 5]
print('A1:', nums[0], nums[-1])

# A2. Find the length of a list.
colors = ['red', 'blue', 'green']
print('A2:', len(colors))

# A3. Append yellow.
colors = ['red', 'blue']
colors.append('yellow')
print('A3:', colors)

# A4. Insert orange at index 1.
fruits = ['apple', 'banana']
fruits.insert(1, 'orange')
print('A4:', fruits)

# A5. Remove banana.
fruits = ['apple', 'banana', 'grapes']
fruits.remove('banana')
print('A5:', fruits)

# A6. Pop and print the last item.
items = [10, 20, 30]
popped = items.pop()
print('A6:', popped)

# A7. Check whether 3 is in the list.
nums = [1, 2, 3, 4]
print('A7:', 3 in nums)

# A8. Print [2, 3] using slicing.
a = [0, 1, 2, 3, 4]
print('A8:', a[2:4])

# A9. Replace index 1 with 12.
a = [5, 10, 15]
a[1] = 12
print('A9:', a)

# A10. Count appearances of 2.
a = [1, 2, 2, 3, 2]
print('A10:', a.count(2))

print('\nPART B - TUPLES')

# B1. Print the second tuple element.
t = (10, 20, 30)
print('B1:', t[1])

# B2. Find the length of a tuple.
t = ('a', 'b', 'c')
print('B2:', len(t))

# B3. Unpack the tuple into x and y.
x, y = (4, 5)
print('B3:', x, y)

# B4. Check whether 'b' is present.
t = ('a', 'b', 'c')
print('B4:', 'b' in t)

# B5. Create an empty tuple and print its type.
t = ()
print('B5:', type(t))

# B6. Join two tuples.
t1 = (1, 2)
t2 = (3, 4)
print('B6:', t1 + t2)

# B7. Repeat a one-element tuple three times.
t = (7,)
print('B7:', t * 3)

# B8. Find the first index of 2.
t = (1, 2, 3, 2)
print('B8:', t.index(2))

# B9. Count the number of 2s.
t = (1, 2, 3, 2)
print('B9:', t.count(2))

# B10. Create a tuple containing one element.
t = (5,)
print('B10:', t)

print('\nPART C - SETS')

# C1. Convert a list into a set.
numbers = [1, 2, 2, 3]
s = set(numbers)
print('C1:', s)

# C2. Add 4 to a set.
s = {1, 2, 3}
s.add(4)
print('C2:', s)

# C3. Remove 2 from a set.
s = {1, 2, 3}
s.remove(2)
print('C3:', s)

# C4. Check whether 5 is present.
s = {1, 3, 5}
print('C4:', 5 in s)

# C5. Print the size of a set.
s = {10, 20, 30}
print('C5:', len(s))

# C6. Clear a set.
s = {1, 2, 3}
s.clear()
print('C6:', s)

# C7. Add c only if it is missing.
s = {'a', 'b'}
if 'c' not in s:
    s.add('c')
print('C7:', s)

# C8. Remove duplicates by converting to a set.
letters = ['a', 'a', 'b']
s = set(letters)
print('C8:', s)

# C9. Find union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print('C9:', set1 | set2)

# C10. Find intersection of two sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print('C10:', set1 & set2)

print('\nPART D - DICTIONARIES')

# D1. Print the name stored in a dictionary.
d = {'name': 'Ali', 'age': 25}
print('D1:', d['name'])

# D2. Add a city entry.
d = {'name': 'Ali', 'age': 25}
d['city'] = 'Lahore'
print('D2:', d)

# D3. Change age to 30.
d = {'name': 'Ali', 'age': 25}
d['age'] = 30
print('D3:', d)

# D4. Delete the age key.
d = {'name': 'Ali', 'age': 25}
del d['age']
print('D4:', d)

# D5. Check whether the salary key exists.
d = {'name': 'Ali', 'age': 25}
print('D5:', 'salary' in d)

# D6. Print all dictionary keys.
d = {'a': 1, 'b': 2}
print('D6:', d.keys())

# D7. Print all dictionary values.
d = {'a': 1, 'b': 2}
print('D7:', d.values())

# D8. Print key-value pairs with a loop.
d = {'x': 10, 'y': 20}
print('D8:')
for key, value in d.items():
    print(key, value)

# D9. Safely get score from an empty dictionary.
d = {}
print('D9:', d.get('score', 'Not found'))

# D10. Create a dictionary from two lists.
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
print('D10:', d)
