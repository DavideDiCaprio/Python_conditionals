'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.'''


def discount():
    quantity = int(input("Enter purchased quantity: "))
    total_price = quantity * 100

    if total_price > 1000:
         discount = discount = total_price*.1 
         final_price = total_price - discount
         print(f"Price is:{final_price}, you saved {discount}")
   
    else :
        print(f"Total price is:{total_price}")
