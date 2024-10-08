from items import Item
class Phone(Item):
    def __init__(self, name : str, price : float, quantity=0, reserved_phones=0):
        # To call to super method to have access to all attribute/methods
        super().__init__(name, price, quantity)

        # Run validation to received arguments
        assert reserved_phones >= 0, f'Reserved Phones {reserved_phones} is not greater than or equal to zero!'

        # Assign to self object
        self.reserved_phones = reserved_phones

phone1 =  Phone("iNoSung123", 500, 5, 1)
phone2 = Phone("Motolazy3i7", 570, 8, 1)
