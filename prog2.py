class Item:
    pay_rate=0.8 # class attribute

    def __init__(self,name:str,price:int,quantity:int =0):
        # Self:Item is not valid as as yet Item class is not defined

        # Validating the received arguments

        assert price>=0 , f"Price {price} is not greater than or equal to  zero !!"
        assert quantity>=0 , f"Quantity {quantity} is not greater than zero !!"

        # Assign to self objects {name ,price and quantity are instance variables }
        self.name=name
        self.price=price
        self.quantity=quantity


    def calculate_total_price(self)->int:
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        print(f"The price after giving discount is {self.price*Item.pay_rate}")

    

item1=Item("Phone",100)
item2=Item("Laptop",100,1000)
item2.pay_rate=0.7 # changing pay rate only for item2
print(Item.__dict__)# Use to get all the attributes of a class


