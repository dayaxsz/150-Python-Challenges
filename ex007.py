def birthday():
    name = str(input('What is your name? '))
    age = int(input('And what is your age today? '))
    next_birthday = age + 1
    
    print(f'{name}, in your next b-day you\'ll have {next_birthday}!')
    
birthday()