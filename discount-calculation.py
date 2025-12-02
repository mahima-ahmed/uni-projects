# A store offers a 20% discount to customers whose purchase exceeds 1000€. What amount will the customer pay? Assume that the purchase amount is entered through an input device.
purchase = float(input('Enter the purchase cost: ')) # use float for decimal numbers
if purchase > 1000: # if the purchase price is over 1000€, the discount applies
    print(f'The total purchase price is: {purchase-(purchase*0.2)}€')
else: # if it doesn't exceed that amount, no discount applies
    print(f'The total purchase price is: {purchase}€')
