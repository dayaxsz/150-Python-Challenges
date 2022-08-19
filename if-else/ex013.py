''' Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, otherwise display “Thank you”. '''

def user_range():
    user_input = int(input('Enter a number under 20: '))
    
    if user_input < 20:
        print('Thank you!')
    else:
        print('Too high')
        
user_range()