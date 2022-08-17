''' There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds. '''

def weight():
    kg = int(input('Put some kg value here and i\'ll transform it in pounds: '))
    pound = kg * 2.204
    
    print(f'As promised: {kg} converted to pounds is approximately {pound:.2f} pounds!')
    
weight()