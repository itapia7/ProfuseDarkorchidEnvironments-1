# String Practice:

sentence = input("Can you write a sentence?")
print(sentence)
print(sentence[0])
print(sentence[-1])
print(sentence.upper())
print(sentence.find("is"))
print(sentence[14:16])
print(sentence.replace("Israel","Izzy"))
# Create a Python program that asks the user to input a sentence.
# Print the first and last letter of the sentence.
# Convert the entire sentence to uppercase and print the result.
# Find and print a substring from the inputted sentence.
# Replace a word in the sentence and print the updated sentence.


# Input Practice:

name = input("What is your name?")
age = input("How old are you?")
fmovie = input("What is your favorite movie?")

print(f'Your name is {name} and your are {age} years old. Your favorite movie is {fmovie}.')

# Create a Python program that asks the user for their name, age, and favorite movie.
# Print a message back to the user with this information.
# Note: Make sure to convert the age to an integer.


# F-String Practice:

item1 = input("Can you name 1 item in your room?")
item2 = input("Can you name a 2nd item in your room?")
item3 = input("Can you name a 3rd item in your room?")

print(f'Your are in a room with a {item1}, a {item2}, and a {item3}.')

# Create a Python program that asks the user for three objects in the room.
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.

# Advanced String Practice:

sentence2 = input("Can you write a sentence?")
print(sentence2[::-1])

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python".

# Advanced Input Practice:

book = input("What is your favorite book?")
movie = input("What is your favorite movie?")
song = input("What is your favorite song?")
print(f"Your favorite book is {book}, your favorite movie is {movie}, and your favorite song is {song}.")

# Create a Python program that asks the user for the name of their favorite book, movie, and song.
# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."


# Advanced F-String Practice:

name = input("What is your name?")
age = input("How old are you?")
cyear = input("What is the current year?")
print(f'Hello {name} your are {age} and the current year is {cyear}.')

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

num1 = float(input("Can you select a number?"))
num2 = float(input("Can you select a 2nd number?"))

difference = num1 - num2
print(difference)
sum = num1 + num2
product = num1 * num2
quotient = num1/num2
print(sum)
print(product)
print(quotient)

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.

movie_summary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."

print(movie_summary)
print(len(blue_b_summary))
print(blue_beetle_summary.upper())
print(blue_beetle_summary.lower())
print(blue_beetle_summary.replace("Blue", "Red"))
print(blue_beetle_summary.find("beetle"))
beetle = blue_beetle_summary[-7:-1]
print(beetle)
print(blue_beetle_summary[::-1])

# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."