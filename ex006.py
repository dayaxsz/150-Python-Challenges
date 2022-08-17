""" Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a user-friendly format."""

def pizza():
    begin = int(input('How many slices there are? '))
    eaten = int(input('And how many have you eaten? '))
    slices_left = begin - eaten
    
    print(f'So if you had {begin} slices of pizza and have eaten {eaten}, you have a total of {slices_left} slices left!')
    
pizza()