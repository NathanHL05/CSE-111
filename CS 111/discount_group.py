from datetime import datetime

def get_float_inputs (prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except (ValueError, TypeError):
            print("Please enter a valid value")

def get_subtotal():
    subtotal = 0
    item = 1
    while item !=0:
        item = get_float_inputs("what is the price of the item(if no more, enter 0): ")
        subtotal = subtotal + item
    print(f"your subtotal is ${subtotal:.2f}")
    return subtotal



time = datetime.now()
dayOfWeek = time.weekday()

subtotal = get_subtotal()

if (dayOfWeek == 1 or dayOfWeek == 2):
    if subtotal >= 50:
        percentOff = subtotal * 0.1
        total = subtotal - percentOff 
        tax = total * 0.06
        totalWithTax = total + tax
    elif subtotal < 50:
        req_discount = 50 - subtotal
        print(f"you can qualify for a 10% discount if you spend another ${req_discount}")
        tax_total = subtotal * 1.06
        print(f"today your total is {tax_total:.2f}")
    
else: 
    totalWithTax = subtotal * 1.06
    print(f"sorry no discount today your total is ${totalWithTax}")