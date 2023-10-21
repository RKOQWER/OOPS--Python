class Item:
    
    def __init__(self,name,price,quantity=0):
        
        self.name=name
        self.price=price
        self.qunatity=quantity
        
    def calculate_total_price(self):
        # self will be passed by python itself we don't have to pass it explicitly
        # However in method definition we should receive it implicitly
        return self.price*self.qunatity
    
item1=Item("Phone",100)
item2=Item("Laptop",1000)

item2.has_numpad=False
print(Item.__dir__)# All the attributes for class level

print(item1.__dir__)# All the attributes for instance level

