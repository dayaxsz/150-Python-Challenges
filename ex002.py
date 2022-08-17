"""Ask for the user’s first name and then ask for their surname and display the output message
Hello [First Name] [Surname]. """

## using function

def User_Data():
    user_name = input('Qual o seu nome? ')
    user_surname = input('Qual o seu sobrenome? ')
    print(f'Então seu nome  é {user_name} e seu sobrenome é {user_surname}')
    
User_Data()

## using POO

class User_Data_Poo:
    def __init__(self):
        self.name = input('Qual o seu nome? ')
        self.surname = input('Qual o seu sobrenome? ')
        print(f'Então seu nome é {self.name} e seu sobrenome é {self.surname}!')
        
User_Data = User_Data_Poo()