"""
Print the store’s name at the top of the receipt.
Print the list of ordered items.
Sum and print the number of ordered items.
Sum and print the subtotal due.
Compute and print the sales tax amount. Use 6% as the sales tax rate.
Compute and print the total amount due.
Print a thank you message.
Get the current date and time from your computer’s operating system and print the current date and time.
Include a try block and except blocks to handle FileNotFoundError and KeyError.
"""
from datetime import datetime

def print_products(dict):
    print("Available Products:")
    for key, value in dict.items():
        if value == []:
            break
        else:
            print(f"ID: {key} | {value[0]} | Price: ${value[1]}")
    return

def list_to_dict(list):
    dict = {}
    for key in list:
        product_info = []
        for i in range(1, len(key)):
            product_info.append(key[i]) 
        dict[key[0]] = product_info
    return dict

def txt_to_list(txt):
    try:
        with open (txt, 'r') as file:
            content = [line.strip().split(',') for line in file.readlines()]
        return content
    except FileNotFoundError as error:
        print({error})
        print("You are missing the products file, add the products file and try again!.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_purchase_list(products):
    name_list=[]
    price_list=[]
    purchase_list=[]
    for info in products.values():
        try:
            name_list.append(info[0])
            price_list.append(info[1])
        except (IndexError, TypeError, KeyError):
            continue    
    while True:
        product = input("\nEnter product name or ID (To stop enter 0 or checkout): ")
        if product in products:
            item = products[product]
            name = item[0]
            price = item[1]
            quantity = get_int_input(f'\nHow many "{name}" would you like?: ')
            purchase_list.append([name, price, quantity])
        elif product in name_list:
            name = product
            index = name_list.index(product)
            price = price_list[index]
            quantity = get_int_input(f"\nHow many {name} would you like?: ")
            purchase_list.append([name, price, quantity])
        elif product in (0 , "checkout", "Checkout", "check out", "0"):
            break
        else:
            print("\nItem not recognised, please enter valid input.")
    return purchase_list

def make_receipt(purchase_list, subtotal, tax):
    total = subtotal + tax
    quantity = get_total_quantity(purchase_list)
    with open('receipt_history.txt', 'a') as file:
        file.write("\n\n\n")
        file.write(f"\tSmart Mart\n")
        for index in purchase_list:
            cost = float(index[1]) *float(index[2])
            file.write(f"\n{index[0]}\t | \tIndividual price: ${index[1]}\t | \tQuantity: {index[2]} \t\t ${cost :.2f}")
        current_date_and_time = datetime.now()
        file.write(f"\nTotal items: {quantity}")
        file.write(f"\nSubtotal: {subtotal :.2f} \nTax: {tax:.2f}\nTotal: {total:.2f}")
        file.write(f"{current_date_and_time:%B %Y, %A %I:%M %p}")
        file.write(f"\nThank you for shopping at Smart Mart")
        file.write(f"\nCome again!")
    return

def calculate_total_cost(purchase_list):
    subtotal = 0
    for item in purchase_list:
        price = float(item[1])
        quantity = float(item[2])
        subtotal = subtotal + (price * quantity)
    return subtotal

def get_tax(subtotal):
    tax = subtotal * .06
    return tax

def get_total_quantity(order):
    quantity = 0
    for i in range(len(order)):
        item = order[i]
        quantity += int(item[2])
    return quantity

def main():
    product_list = txt_to_list("products.csv")
    products_dict = list_to_dict(product_list)
    print_products(products_dict)
    purchase_list = get_purchase_list(products_dict)
    subtotal = calculate_total_cost(purchase_list)
    print(f"Subtotal: {subtotal}")
    tax = get_tax(subtotal)
    print(f"Tax: {tax:.2f}")
    print(f"Total: {tax+subtotal:.2f}")
    current_date_and_time = datetime.now()
    print(f"\n{current_date_and_time:%B %Y, %A %I:%M %p}")
    print(f"Thank you for shopping and Smart Mart")
    print(f'Make sure to check your receipt in "receipt_history.csv"')
    make_receipt(purchase_list, subtotal, tax)
    return

main()