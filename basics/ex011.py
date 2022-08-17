''' Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format. '''

def comparison():
    larger_number = int(input('Tell me a number over 100: '))
    smaller_number = int(input('Now a number under 10: '))
    times = larger_number // smaller_number
    
    print(f'the number {smaller_number} goes {times} times into {larger_number}')
    
comparison()