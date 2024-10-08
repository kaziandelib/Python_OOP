from items import Item
class Monitor(Item):
    pay_rate = 0.5
    def __init__(self, name : str, price : float, quantity=0):
        # To call to super method to have access to all attribute/methods
        super().__init__(name, price, quantity)