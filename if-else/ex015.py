''' Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [colour], I prefer red”. '''

def color():
    user_color = input('What is your favorite color? ')
    expected_color = 'red'
    
    if user_color.lower() == expected_color.lower():
        print('i like red too!')
    else:
        print(f'I don\'t like {user_color}, i prefer red')
        
color()