#Name: Logan Bond
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Store_Item:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def cost_double(self):
        self.cost *= 2

#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
#Shirt = Store_Item(2073, 34, 0.5)
DanAykroydCrystalSkullVodka = Store_Item(1237, 155, 1.2)
AeonianButterfly = Store_Item(5, 1500, 0.7)

#3. Print the stock of all three objects and the cost of the second store item.
#print("Shirt stock:", Shirt.stock)
print("Dan Aykroyd Crystal Skull Vodka stock:", DanAykroydCrystalSkullVodka.stock)
print("Aeonian Butterfly stock:", AeonianButterfly.stock)
print("Dan Aykroyd Crystal Sk ull Vodka cost: $",DanAykroydCrystalSkullVodka.cost)

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
DanAykroydCrystalSkullVodka.cost_double()
print("Dan's new inflation adjustment for his Vodka: $", DanAykroydCrystalSkullVodka.cost)

#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
AeonianButterfly.stock = 1.25
print("I needed Rot arrows, so now the Butterfly stock is:", AeonianButterfly.stock)

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
try:
    print(Shirt.weight)
except:
    print("Can't weigh something that doesn't exist")