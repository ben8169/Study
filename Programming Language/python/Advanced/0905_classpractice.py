class Item:
    def __init__(self, name:str, price:int, weight:float, isdropable:bool):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self):
        None
    
    def discard(self):
        None

class WearableItem(Item):
    def __init__(self, name:str, price:int, weight:float, isdropable:bool, effect:str):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def wear(self):
        None

# class UsableItem(WearableItem):
#     def __init__(self, name, price, weight, isdropable,effect):
#         super().__init__()
    
#     def use(self):
#         None

class UsableItem(Item):
    def __init__(self, name:str, price:int, weight:float, isdropable:bool, effect:str):
        super().__init__(name, price, weight, isdropable) #생성자 오버라이딩
        self.effect = effect
    
    def use(self):
        None