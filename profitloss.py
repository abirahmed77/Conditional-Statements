ap = int(input("Enter the Actual Price of the Product: "))
sp = int(input("Enter the Selling Price of the Product: "))

if sp > ap:
    profit = sp - ap
    print(f"Apnar Profit : {profit}")
    
else:
    loss = ap - sp
    print(f"Apnar Loss : {loss}")