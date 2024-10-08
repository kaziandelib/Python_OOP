from items import Item
from phones import Phone
from monitors import  Monitor


item1  = Item("MyItem", 50, 8)
item1.name = "NotMyItem"
print(item1.name)

item2 = Phone("iNoSung123", 100, 4)
item2.apply_discount()
print(item2.price)

item3 = Monitor("Pressy", 750, 8)
item3.apply_discount()
print(item3.price)