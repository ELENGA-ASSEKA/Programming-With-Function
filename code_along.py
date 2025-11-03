from datetime import datetime
#Discount rate and sale tax rate
discount_rate = 0.10
sale_tax_rate = 0.06
subtotal = 0

#compute the price
print('Enter the price and quantity for heach item.')
price = 1
while price != 0:

#Get the price
    price = float(input(("Please enter the price: ")))
    if price != 0:

        quantity = int(input('Please enter the quantity:'))

        subtotal += price * quantity

print()
print()

#round the subtotal
subtotal = round(subtotal, 2)
print(f'Subtotal: {subtotal:.2f}')

#Call the now() methode to get the current datetime
current_datetime = datetime.now()
day_of_week = current_datetime.weekday()

#Use the condition
if day_of_week ==1 or day_of_week ==2:
    if subtoatal < 50:
        lacking = 50 - subtotal
        print("To receive the discount, add" f"{lacking:.2f} to your order.")
    else:
        discount = round(subtotal * discount_rate, 2)
        print(f"Discount amount: {discount:.2f}")
        subtotal -= discount

sale_tax = round(subtotal * sale_tax_rate, 2)
print(f"Salt tax amount: {sale_tax:.2f}")

total = subtotal + sale_tax
print(f'Total: {total:.2f}')