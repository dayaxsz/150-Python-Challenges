""" Ask for the user’s first name and display the output message
Hello [First Name] """

# Using function

def Person(name):
    print(f"Hello, {name}")

user_name = str(input('Qual o seu nome? '))
Person(user_name)

## using POO

class Person_Poo:
    def __init__(self):
        self.userName = str(input('Como você se chama? '))
        self.userAge = int(input('Qual a sua idade? '))
        print(f'Então você chama {self.userName} e tem {self.userAge} anos!')

UserInput = Person_Poo()