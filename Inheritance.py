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
        return f"{self.__class__.__name__} ('{self.name}',{self.price},{self.quantity})"
    
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
        

class Phone(Item):
    def __init__(self,name:str,price:float, quantity=0,broken_phones=0):
        
        # Call to super function to have access to all the attributes/ methods in
        # parent class
        
        super().__init__(
            name,price,quantity
        )
        
        # Run validations to the received arguments
        
        assert broken_phones>=0,f"Broken phones {broken_phones} cannot be -ve"
        
        # Assign to self object
        
        self.broken_phones=broken_phones
        
        # Actions to execute
        
    
phone1=Phone("jsc",500,5)


phone2=Phone("asd",700,5)
print(phone1.calculate_total_price())

print(Item.all)
print(Phone.all)
