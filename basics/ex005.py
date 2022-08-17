"""
    Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. 
    Display the answer as The answer is [answer]. 
"""

def conta():
    n1 = int(input('First number: '))
    n2 = int(input('Second number: '))
    n3 = int(input('Third number: '))
    total = (n1 + n2) / n3
    
    print(f'{n1} + {n2} dividido por {n3} dá {total}')
    
conta()