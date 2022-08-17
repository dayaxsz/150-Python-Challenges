'''

Write code that will display the joke “What do you call a bear with no
teeth?” and on the next line display the answer “A gummy bear!” 
Try to create it using only one line of code. 

'''

# Using print()

print('What do you call a bear with no teeth? \nA gummy bear! ')

# Using function

def Joke():
    print('What do you call a bear with no teeth? \nA gummy bear! ')

Joke()

# Using POO

class Joke_POO:
    start = 'What do you call a bear with no teeth?'
    end = 'A gummy bear!'
    print(f'{start} \n{end}')

Joke_POO()