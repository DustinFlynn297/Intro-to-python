# 1. create a function that takes user input for "favorite programming language" and compares it to a list, if the users input matches the list, return and print result to console.
#create function
#create list of programming languages
#create prompt that takes user input
#compare user input to list of programming languages
#if/else statement, if user input matches an item in the list return and print to console.

user_input = input('Enter your favorite programming language: ')
def favorite_programming_language (user_input):
    programming_languages = ["java", "c++", "swift", "javascript", "c#", "c", "swift", "go", "ruby", ]
    for i in range(len(programming_languages)):
        if user_input.lower() == programming_languages[i]:
            confirmed_user_input = user_input
            print (confirmed_user_input + ' is one of our favorite programming languages too!')
        
favorite_programming_language(user_input)