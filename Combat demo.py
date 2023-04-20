#Attack, Defend, Item, Escape

health = 100
items = {}
weapons = {}

def pickUpOption(buttonState, list, listname, listdesc):
    if buttonState == "yes":
        list[listname] = listdesc
        buttonState = None
    else:
        buttonState = None
        pass


class enemy():
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    def Attack():
        print("Hello i attack you for" + enemy.damage)


    
spider = enemy("10","3")
spider.Attack()

class Game:
    print("You find a weapon!")
    
    buttonState = input("Do you pick up the weapon?")
    pickUpOption(buttonState, weapons, "flimsyWeapon", 50)

    print(weapons)
    print("magically you also find stick")

    buttonState = input("Do you pick up the item?")
    pickUpOption(buttonState, items, "stick", "powerfull")
    print(items)
    print("a LARGE \n ENEMY \n SPIDER...\n appears")

    userDesicion = input("what will you do??")
    
