def dinner():
    bill = int(input('What is the total bill? '))
    total_person = int(input('How many people are eating today? '))
    personal_bill = bill / total_person
    
    print(f'If there are {total_person} eating today and the total bill is {bill}, then each person should pay ${personal_bill:.2f}!')
    
dinner()