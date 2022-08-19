''' Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”. '''

def numbers():
    user_input = int(input('Choose a number: '))
    
    if user_input < 10:
        print('Too low')
    elif user_input in range(10, 21):
        print('Correct')
    else:
        print('Too high')
        
numbers()