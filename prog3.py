import csv

class Item:
    pay_rate=0.8 # class attribute
    all=[]
    def __init__(self,name:str,price:int,quantity:int =0):
        # Self:Item is not valid as as yet Item class is not defined

        # Validating the received arguments

        assert price>=0 , f"Price {price} is not greater than or equal to  zero !!"
        assert quantity>=0 , f"Quantity {quantity} is not greater than zero !!"

        # Assign to self objects {name ,price and quantity are instance variables }
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)

    def calculate_total_price(self)->int:
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        print(f"The price after giving discount is {self.price*Item.pay_rate}")

    def __repr__(self):
        return f"Item ('{self.name}',{self.price},{self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
            for item in items:
                Item(
                    name=item['name'],
                    price=int(item['price']),
                    quantity=int(item['quantity'])
                )
                
    @staticmethod
    def is_integer(num):
        # We will count the floats that are .0
        
        if isinstance(num,float):
            # Considers floats that are .0
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
        
        
    

item1=Item("Phone",100)
item2=Item("Laptop",100,1000)
item2.pay_rate=0.7 # changing pay rate only for item2


print(Item.all)
# The will display objects in not user friendly way . To make this user friendly we use repr
# magic function 
Item.instantiate_from_csv()