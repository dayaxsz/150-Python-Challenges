""" Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days. """

def time():
    days = int(input('Tell me a number of days '))
    hours = int(days * 24)
    minutes = int(hours * 60)
    seconds = int(minutes * 60)
    
    print(f'{days} days together have {hours:,} hours, {minutes:,} minutes and {seconds:,} seconds!')

time()