order_amount = int(input("What is the order amount? "))
state = input("What is the state? ").lower()
tax = 0


if state == "wi" or state == "wisconsin":
    tax = 0.055
    print(f'The subtotal is ${order_amount}.\nThe tax is ${order_amount * tax}.')

print(f"The total is ${round(float(order_amount*(tax+1)), 2)}")
