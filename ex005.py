def conta():
    n1 = int(input('First number: '))
    n2 = int(input('Second number: '))
    n3 = int(input('Third number: '))
    total = (n1 + n2) // n3
    
    print(f'{n1} + {n2} dividido por {n3} dá {total}')
    
conta()