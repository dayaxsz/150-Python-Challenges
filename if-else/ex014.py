''' Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank you”, otherwise display the message “Incorrect answer”. '''

def ten_to_twenty():
    user_input = int(input('Enter a number between 10 and 20: '))
    if user_input in range(10, 21):
        print('Thank you!')
    else:
        print('Incorrect answer')
        
ten_to_twenty()