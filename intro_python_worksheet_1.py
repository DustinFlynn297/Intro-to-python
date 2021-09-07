import random

# 1. create a function that takes user input for "favorite programming language" and compares it to a list, if the users input matches the list, return and print result to console.
#create function
#create list of programming languages
#create prompt that takes user input
#compare user input to list of programming languages
#if/else statement, if user input matches an item in the list return and print to console.


# def favorite_programming_language (user_input):
#     user_input = input('Enter your favorite programming language: ')
#     programming_languages = ["java", "c++", "swift", "javascript", "c#", "c", "swift", "go", "ruby", ]
#     for i in range(len(programming_languages)):
#         if user_input.lower() == programming_languages[i]:
#             return (user_input + ' is one of our favorite programming languages too!')          
        
# print(favorite_programming_language('input'))

# 2. create a function that takes in a minimum number and maximum number, and return a random number between the min and max range.
#create a function with two parameters, 
#create variable to hold randomly generated number
#return variable/random number

# def random_number_given_min_max (min_number, max_number):
#     random_number = random.randint(min_number, max_number)
#     return random_number

# print(random_number_given_min_max(2, 25))

# 3. create a function that takes ina  word and returns the reversal of the word.
# create function that takes one parameter
# create a variable to hold the user input
# iterate over the word in reverse

def string_reversal (original_string):
    original_string = input('Enter any word and we will display it spelled backwards. ')
    input_length = len(original_string)
    sliced_input =original_string[input_length::-1]
    print (sliced_input)

string_reversal('any')