#Attack, Defend, Item, Escape

pHealth = 100
remainingHealth = None
items = {}
weapons = {}

def deathCheck(pHealth):
    if pHealth < 0: 
        print("Death TRUE") 
    else:
        print("Death FALSE")

def avp(damageDone, health):
    global pHealth
    remainingHealth = health - damageDone
    print("You have " + str(remainingHealth) + " health remaining...")
    pHealth = remainingHealth
    remainingHealth = None

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

    def attack(abc):
        print("Hello i attack you for " + str(abc.damage))
        avp(abc.damage, pHealth)
        deathCheck(pHealth)


spider = enemy(5,19)    

class Game:
    gamestate = True
    if gamestate == True:
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
        print("ah you took too long to think, spider attacks!")
        spider.attack()
        spider.attack()
        spider.attack()
        spider.attack()


          