from datetime import datetime

subtotal = float(input('What is the subtotal?'))
currentDay = datetime.now()
salesTax = subtotal*0.06
discount = 0
differenceForDiscount = 50-subtotal



if (subtotal >= 50 and (currentDay.weekday() == 1 or currentDay.weekday() == 2)):
    discount = subtotal*0.1
    subtotal = subtotal - discount

subtotal = subtotal+salesTax

if(discount>0):
    print(f'Discount: {discount}')
    print(f'Sales Tax: {salesTax}')
    print(f'Total amount: {subtotal}')
else:
    print(f'You need {differenceForDiscount} for obtain 10%')
    print(f'Sales Tax: {salesTax}')
    print(f'Total amount: {subtotal}')