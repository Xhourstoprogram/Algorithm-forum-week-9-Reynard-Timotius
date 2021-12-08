from shopclassRTP import ShopListRTP

def itemsRTP():
    items = []
    num = int(input("How many items will you order today?"))
    while num < 1:
        print("Number of items must be at least 1")
        num = int(input("How many items will you order today?"))
    
    for i in range (num):
        foodname = str(input("Enter food name: "))
        pounds = float(input("Enter amount of pounds: "))
        while pounds <= 0:
            print("Amount of pounds must be greater than 0")
            pounds = float(input("Enter amount of pounds: "))
        print()
        item = ShopListRTP(foodname, pounds)
        items.append(item)
    return items

def ItemsSumarry(items):
    print("This is a sumarry of the purchased items")
    print("========================================")
    for i in items:
        print(f"Item : {i.getname()}")
        print(f"Amount : {i.getamount()}")
        print("Price per one pound : ${:.2f}".format(i.getnormalprice()))
        print("Price of total order : ${:.2f}".format(i.getcalculateprice()))
        print()

def TotalPriceRTP(items):
    price = 0
    for i in items:
        price += i.getcalculateprice
        print("The total of all the orders is: ${:.2f}".format(price))

def main():
    items = itemsRTP()
    ItemsSumarry(items)
    TotalPriceRTP(items)

main()