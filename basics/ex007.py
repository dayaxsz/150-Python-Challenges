""" Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you will be [new age]. """

def birthday():
    name = str(input('What is your name? '))
    age = int(input('And what is your age today? '))
    next_birthday = age + 1
    
    print(f'{name}, in your next b-day you\'ll have {next_birthday}!')
    
birthday()