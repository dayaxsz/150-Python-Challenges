""" Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay. """

def dinner():
    bill = int(input('What is the total bill? '))
    total_person = int(input('How many people are eating today? '))
    personal_bill = bill / total_person
    
    print(f'If there are {total_person} eating today and the total bill is {bill}, then each person should pay ${personal_bill:.2f}!')
    
dinner()