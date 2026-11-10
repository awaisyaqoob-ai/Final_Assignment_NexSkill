



print("========== PART A: LISTS ==========")

# A1: Squares of even numbers from 0 to 20.
even_squares = [x ** 2 for x in range(21) if x % 2 == 0]
print("QA1:", even_squares)

# A2: Sort without changing the original list.
nums = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(nums)
print("QA2:", f"sorted={sorted_nums}, original={nums}")

# A3: Remove duplicates, preserving first appearance.
items = [3, 1, 3, 2, 1, 4, 2]
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print("QA3:", unique_items)

# A4: Flatten a nested list with a comprehension.
nested = [[1, 2], [3, 4], [5]]
flat = [item for group in nested for item in group]
print("QA4:", flat)

# A5: Case-insensitive alphabetical sort.
names = ["alice", "Bob", "charlie", "DAVID"]
print("QA5:", sorted(names, key=str.lower))

# A6: Replace indices 2, 3 and 4 with two values.
a = [10, 20, 30, 40, 50, 60]
a[2:5] = [100, 200]
print("QA6:", a)

# A7: All indices where the target appears.
values = [7, 2, 7, 4, 7, 5]
indices = [i for i, value in enumerate(values) if value == 7]
print("QA7:", indices)

# A8: Items occurring exactly once.
values = [1, 2, 2, 3, 4, 4, 5]
only_once = [value for value in values if values.count(value) == 1]
print("QA8:", only_once)

# A9: Rotate list right by one position.
values = [1, 2, 3, 4]
rotated = values[-1:] + values[:-1]
print("QA9:", rotated)

# A10: Separate even and odd numbers.
values = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [x for x in values if x % 2 == 0]
odds = [x for x in values if x % 2 != 0]
print("QA10:", f"even={evens}, odd={odds}")


print("\n========== PART B: TUPLES ==========")

# B1: Convert list to tuple and unpack.
values = [1, 2, 3, 4]
t = tuple(values)
a, b, c, d = t
print("QB1:", f"tuple={t}, unpacked={(a, b, c, d)}")

# B2: Take the second item from each inner tuple.
t = (("a", 1), ("b", 2), ("c", 3))
seconds = [pair[1] for pair in t]
print("QB2:", seconds)

# B3: Return sum, minimum, and maximum as a tuple.
def get_stats(numbers):
    return sum(numbers), min(numbers), max(numbers)


total, smallest, largest = get_stats((5, 2, 9, 1))
print("QB3:", f"sum={total}, min={smallest}, max={largest}")

# B4: Concatenate tuples, then convert to list.
t1 = (1, 2, 3)
t2 = (4, 5)
print("QB4:", list(t1 + t2))

# B5: Most frequent tuple item (first occurrence breaks ties).
t = (3, 1, 2, 3, 2, 3, 4)
most_frequent = max(t, key=t.count)
print("QB5:", most_frequent)

# B6: Same elements with same counts, independent of order.
t1 = (1, 2, 2, 3)
t2 = (3, 2, 1, 2)
print("QB6:", sorted(t1) == sorted(t2))

# B7: Last three elements.
t = (10, 20, 30, 40, 50)
print("QB7:", t[-3:])

# B8: Repeat a tuple three times.
t = (1, 2)
print("QB8:", t * 3)

# B9: Flatten a nested tuple.
t = ((1, 2), (3, 4))
flattened = tuple(item for group in t for item in group)
print("QB9:", flattened)

# B10: Manhattan distance between two 2D points.
point1 = (2, 3)
point2 = (7, 9)
distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
print("QB10:", distance)


print("\n========== PART C: SETS ==========")

# C1: Set difference (first minus second).
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
print("QC1:", sorted(set1 - set2))

# C2: Intersection of three sets.
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
set3 = {0, 2, 3, 6}
print("QC2:", sorted(set1 & set2 & set3))

# C3: Unique lowercase words in a sentence.
sentence = "Python is Fun and python is Useful"
unique_words = set(sentence.lower().split())
print("QC3:", sorted(unique_words))

# C4: Remove duplicates and sort values.
values = [4, 2, 4, 1, 3, 2]
print("QC4:", sorted(set(values)))

# C5: Strict subset (subset but not equal).
small = {1, 2}
large = {1, 2, 3}
print("QC5:", small < large)

# C6: Squares of multiples of three between 1 and 15.
squares = {x * x for x in range(1, 16) if x % 3 == 0}
print("QC6:", sorted(squares))

# C7: Count repeated occurrences after the first occurrence.
values = [1, 2, 2, 3, 3, 3, 4]
duplicate_count = len(values) - len(set(values))
print("QC7:", duplicate_count)

# C8: Remove vowels using a vowel set.
message = "Hello Python World"
vowels = set("aeiouAEIOU")
without_vowels = "".join(char for char in message if char not in vowels)
print("QC8:", without_vowels)

# C9: Symmetric difference (in exactly one of the sets).
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("QC9:", sorted(set1 ^ set2))

# C10: Compare UNIQUE characters only (as specified in the question).
# Note: Equal sets alone do not prove two words are true anagrams.
word1 = "listen"
word2 = "silent"
same_unique_characters = set(word1) == set(word2)
print("QC10:", same_unique_characters)


print("\n========== PART D: DICTIONARIES ==========")

# D1: Count word frequencies using get().
sentence = "apple banana apple orange banana apple"
frequencies = {}
for word in sentence.split():
    frequencies[word] = frequencies.get(word, 0) + 1
print("QD1:", frequencies)

# D2: Invert a dictionary with unique values.
original = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in original.items():
    inverted[value] = key
print("QD2:", inverted)

# D3: Merge dictionaries; the second overrides common keys.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}
merged = {**dict1, **dict2}
print("QD3:", merged)

# D4: Group words by the first letter.
words = ["apple", "ant", "banana", "ball", "cat"]
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
print("QD4:", groups)

# D5: Keep dictionary entries whose values are greater than 50.
scores = {"Ali": 65, "Sara": 45, "Ahmed": 82, "Zara": 50}
above_50 = {name: score for name, score in scores.items() if score > 50}
print("QD5:", above_50)

# D6: Safely access a nested key even if a level is missing.
student = {"details": {"address": {"city": "Lahore"}}}
city = student.get("details", {}).get("address", {}).get("city", "Unknown")
print("QD6:", city)

# D7: Dictionary mapping numbers 1 through 10 to cubes.
cubes = {x: x ** 3 for x in range(1, 11)}
print("QD7:", cubes)

# D8: Find the key with the highest corresponding value.
scores = {"Ali": 85, "Sara": 92, "Ahmed": 79}
highest_key = max(scores, key=scores.get)
print("QD8:", highest_key)

# D9: Build a dictionary from parallel lists.
keys = ["name", "age", "city"]
values = ["Ali", 22, "Lahore"]
combined = dict(zip(keys, values))
print("QD9:", combined)

# D10: Remove keys that have a None value.
record = {"name": "Ali", "age": None, "city": "Lahore", "phone": None}
clean_record = {key: value for key, value in record.items() if value is not None}
print("QD10:", clean_record)
