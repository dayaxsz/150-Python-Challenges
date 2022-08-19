'''Ask for two numbers. If the first one is larger than the second, display the second number first and then the first number, otherwise show the first number first and then the second.'''

def num_comparison():
    n1 = int(input('1st number: '))
    n2 = int(input('2nd number: '))
    
    if n1 > n2:
        print(n2, n1)
    else:
        print(n1, n2)
        
num_comparison()