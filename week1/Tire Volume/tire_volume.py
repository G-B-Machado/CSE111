from datetime import datetime
import math

today = datetime.now()
print("Hello, welcome to Machado's store. Please answer these questions to continue.")
customerName = input('What´s your name?')
customerPhone = input('What´s your phone number?')
print('Now, let´s search your tire')

w = int(input('Enter the width of the tire in mm: '))
a = int(input('Enter the aspect ratio of the tire: '))
d = int(input('Enter the diameter of the wheel in inches: '))

v = round((math.pi*(w**2)*a*((w*a)+(2540*d)))/10000000000,2)
print(f'The approximate volume is {v} liters')
with open("volumes.txt", "at") as volumes_file:
    print(f'{today}, {w}, {a}, {d}, {v}', file=volumes_file)

sale = input('Do you want to buy a tire with these parameters?')
if (sale == 'yes'):
    with open("customers.txt", "at") as customers_file:
        print(f'{customerName}, {customerPhone}', file=customers_file)
    print('Thank you for buying!')
else:
    print('Thank you and come back often')