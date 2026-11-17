from functools import reduce            # reduce lives in a module (Lesson 08)

marks = [35, 72, 48, 90, 66]

# --------------------------------------------------------------------------
# 4. Chaining: total of the passing marks after grace
# --------------------------------------------------------------------------
after_grace = list(map(lambda m: m + 5, marks))               # change
print(after_grace)
passing = list(filter(lambda m: m >= 40, after_grace))        # keep
print(passing)
answer = reduce(lambda a, b: a + b, passing)            # combine
print(answer)                           # 336
####################################################################################################
# What we didn't cover in the class
# map(function, iterable)
# map(function, iterable1, iterable2)
# filter(function, iterable)
# from functools import reduce
# reduce(function, iterable)
# reduce(function, iterable, initial)
####################################################################################################

# Problem statement has an index added in each element of the list.  
# Remove the numbering and space after numbering,
# Remove the words with length of word greater than 10
# Reduce the Vocabulary as a huge sentence

vocabulary = ['1. Hi', '2. How', '3. are', '4. you?', 
              '5. sdfsdfsdsfsdff', '6. Hurray!', '7. What', '8. are', '9. doing?']

#recreate below slowly by understanding
number_map_to_vocab = list(map(lambda word: word.split(" ", 1)[1], vocabulary))
print(number_map_to_vocab)

filtered_to_vocab = list(filter(lambda word: len(word) <= 10, number_map_to_vocab))
print(filtered_to_vocab)

sentence = reduce(lambda word1, word2: word1 + " " + word2, filtered_to_vocab)
print(sentence)

#Clean up a list of student names by removing extra spaces, fixing capitalization, 
# and dropping any empty entries.
names = ["  alice ", "BOB", "", "  charlie  ", "dave"]

#Convert a list of exam scores into letter grades (A through F) based on score ranges.
scores = [92, 67, 85, 45, 78]

#Check a list of passwords and keep only those that are at least 8 characters long 
# and contain at least one digit.
passwords = ["hello", "Secure123", "short1", "NoDigitsHere", "Strong#2024"]

#Convert a list of Celsius temperatures to Fahrenheit, then find which days were hotter than 30°C.
celsius = [12, 25, 31, 38, 18]

#Find the longest word in a list of words.
words = ["python", "is", "wonderful", "for", "learning"]


#Calculate the total price of only the in-stock items in a shopping cart.
cart = [("pen", 1.50, True), ("book", 12.00, False), ("bag", 8.25, True)]
