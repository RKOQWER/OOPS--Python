class Item:

    def __init__(self,name:str):
        print(f"An instance created for {name} successfully")
    def calculate_total_price(self,x:int,y:int)->int:
        return x*y

item1=Item("Phone")
item1.name="Phone"
item1.price=100
item1.quantity=5
print(item1.calculate_total_price(item1.price,item1.quantity))

item2=Item("Laptop")
item2.name="Phone"
item2.price=100
item2.quantity=5
print(item2.calculate_total_price(item1.price,item1.quantity))