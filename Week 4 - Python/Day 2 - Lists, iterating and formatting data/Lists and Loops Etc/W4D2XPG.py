# Exercise 2
# total = 0
customer = input("Customer name: ")
staff = input("Staff name: ")
items = []
prices = []
quantities = []
totals = []
space = " "

item = None
while item != "quit":
    item = input("Item name: ")
    if item == "quit":
        break
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    items.append(item)
    prices.append(price)
    quantities.append(quantity)

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

print("**************************************")
print()
print("Customer:      " + customer )
print("Staff:         " + staff)
print()
print("Items" + (space*10) + "Num" + (space*2) + "Price" + (space*3) + "Total")
print()
x=0
for x in range(len(items)):
    gap1 = 15 - len(items[x])
    gap2 = 5 - len(str(quantities[x]))
    gap3 = 8 - len(str(prices[x]))
    total = quantities[x] * prices [x]
    totals.append(total)
    print(items[x] + (space*gap1) + str(quantities[x]) + (space*gap2) + str(prices[x]) + (space*gap3) + str(truncate(total, 2)))
net = sum(totals)
vat = net*0.2
gross = net + vat

print()
print("Net Total:      " + str(truncate(net, 2)))
print("20% VAT:        " + str(truncate(vat, 2)))
print("Gross Total:    " + str(truncate(gross, 2)))
print()
print("**************************************")
