order_amount = int(input("What is the order amount? "))
state = input("What is the state? ").lower()

if state == "wi" or state == "wisconsin":
    print(f'The subtotal is ${order_amount}.\nThe tax is ${order_amount * 0.055}.\nThe total is ${round(order_amount*1.055, 2)}.')