

class Locale:
    def __init__(self, name, description, itemName):
        self.name = name
        self.description = description
        self.isVisited= False
        self.item = itemName
    def render(self):
        if self.isVisited:
            print("You have returned to " + self.name)
        else:
            print(self.description)
        def removeItem(self):
            self.isVisited = True

class Item:
    def __init__(self, name, description):
        self.name = name
        self. descripton = description
    def render(self):
        print(self.description)

def containsItem(items, target):
    for item in items:
        if item.description == target:
            return True
    return False

beach= Locale("beach", "you are at the beach", "map")
print(beach.name)
print(beach.description)
print(beach.isVisited)
print(beach.item)
print(beach.render())
beach.removeItem()
print(beach.isVisited)
rope = Item("rope", "about 50 feet of braided hemp")
keycard = Item("keycard", "a plastic card with a magnetic strip")
print(rope.name)
print(rope.desrcription)
keycard.render()
items = [rope, keycard]
print(containsItem(items, "keycard"))



