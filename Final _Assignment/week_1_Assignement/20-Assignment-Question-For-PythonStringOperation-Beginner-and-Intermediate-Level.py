

print('========== BEGINNER LEVEL ==========')

# Beginner Q1: Length of a string
s = 'hello world'
print('Beginner Q1 - Length:', len(s))

# Beginner Q2: Uppercase and lowercase
s = 'Python3'
print('Beginner Q2 - Uppercase:', s.upper())
print('Beginner Q2 - Lowercase:', s.lower())

# Beginner Q3: Count a character (case-sensitive)
s = 'banana'
ch = 'a'
print('Beginner Q3 - Count:', s.count(ch))

# Beginner Q4: First and last character; handle empty strings
s = 'drawer'
if s:
    print('Beginner Q4 - First:', s[0], 'Last:', s[-1])
else:
    print('Beginner Q4 - The string is empty')

# Beginner Q5: Check for a substring
s = 'data science'
sub = 'science'
print('Beginner Q5 - Substring present:', sub in s)

# Beginner Q6: Slice a string (end index is excluded)
s = 'programming'
start = 3
end = 8
print('Beginner Q6 - Slice:', s[start:end])

# Beginner Q7: Reverse a string
s = 'Python'
print('Beginner Q7 - Reversed:', s[::-1])

# Beginner Q8: Replace a substring (case-sensitive)
s = 'I love apples. Apples are great!'
print('Beginner Q8 - Replaced:', s.replace('apples', 'oranges'))

# Beginner Q9: Split and join a sentence
s = 'split this sentence'
words = s.split()
print('Beginner Q9 - Joined:', '-'.join(words))

# Beginner Q10: Strip whitespace from both ends
s = ' padded text '
print('Beginner Q10 - Stripped:', repr(s.strip()))

print('\n========== INTERMEDIATE LEVEL ==========')

# Intermediate Q1: Count vowels and consonants (ignore nonletters)
s = 'Hello, World! 123'
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print('Intermediate Q1 - Vowels:', vowels, 'Consonants:', consonants)

# Intermediate Q2: Palindrome check, ignoring case and punctuation
s = 'A man, a plan, a canal: Panama!'
cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
print('Intermediate Q2 - Palindrome:', cleaned == cleaned[::-1])

# Intermediate Q3: Manual title case without using .title()
s = 'hELLO wORLD from PYTHON'
words = s.split()
title_words = []
for word in words:
    title_words.append(word[0].upper() + word[1:].lower())
print('Intermediate Q3 - Title case:', ' '.join(title_words))

# Intermediate Q4: Find all substring indices, including overlaps
s = 'aaaa'
sub = 'aa'
indices = []
if sub:  # an empty substring is skipped
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            indices.append(i)
print('Intermediate Q4 - Indices:', indices)

# Intermediate Q5: Character frequency (case-insensitive, skip spaces)
s = 'Baa Baa Black Sheep'
frequency = {}
for ch in s.lower():
    if ch != ' ':
        frequency[ch] = frequency.get(ch, 0) + 1
print('Intermediate Q5 - Frequencies:', frequency)

# Intermediate Q6: Anagrams ignoring case, spaces and punctuation
s1 = 'Listen'
s2 = 'Silent'
clean1 = ''.join(ch.lower() for ch in s1 if ch.isalpha())
clean2 = ''.join(ch.lower() for ch in s2 if ch.isalpha())
print('Intermediate Q6 - Anagrams:', sorted(clean1) == sorted(clean2))

# Intermediate Q7: Compress consecutive runs of characters
s = 'aaabbcaaaa'
compressed = ''
if s:
    current = s[0]
    count = 1
    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            compressed += current + str(count)
            current = ch
            count = 1
    compressed += current + str(count)
print('Intermediate Q7 - Compressed:', compressed)

# Intermediate Q8: Longest alphabetic word (first in case of ties)
# Nonalphabetic characters, including underscores, separate words.
s = 'Find the longest_word here!'
words = []
current_word = ''
for ch in s:
    if ch.isalpha():
        current_word += ch
    elif current_word:
        words.append(current_word)
        current_word = ''
if current_word:
    words.append(current_word)
longest = ''
for word in words:
    if len(word) > len(longest):
        longest = word
print('Intermediate Q8 - Longest word:', longest)

# Intermediate Q9: Remove duplicate characters, preserving order
s = 'banana'
seen = set()
result = ''
for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print('Intermediate Q9 - Unique in order:', result)

# Intermediate Q10: Mask middle characters of email username
email = 'john.doe@example.com'
if '@' in email:
    username, domain = email.split('@', 1)
    if len(username) > 2:
        masked_name = username[0] + '*' * (len(username) - 2) + username[-1]
    elif len(username) == 2:
        masked_name = username[0] + username[-1]
    else:
        masked_name = username
    masked_email = masked_name + '@' + domain
else:
    masked_email = 'Invalid email address'
print('Intermediate Q10 - Masked email:', masked_email)
