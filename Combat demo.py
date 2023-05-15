#Attack, Defend, Item, Escape
import random

pHealth = 100
items = {}
weapons = {} 
equipedWeapon = weapons
defenseFlag = False
turn = 0


#check death status for player
def deathCheck(health):
    if health <= 0: 
        print("Death TRUE") 
    else:
        print("Death FALSE")

#takes health, checks if defended, damages player, sets health
def attack_and_calculate_remaining_health_player(damage, health):
    global pHealth
    if defenseFlag == False :
        remainingHealth = health - damage
    else:
        remainingHealth = health - damage / defenseMod
    print("You have " + str(remainingHealth) + " health remaining... \n")
    pHealth = remainingHealth
    
#if prompted yes, the user will pick up the item
def pickUpOption(buttonState, list, name, description):
    if buttonState == "yes":
        list[name] = description


#enemy class given name, health and its damage
class Enemy:
    def __init__(self,entity, health, damage):
        self.entity = entity
        self.health = health
        self.damage = damage
#states name, states damage cost and remaining health, if death is active
    def attack_to_player(self):
        print(self.entity + " attacks you for " + str(self.damage))
        attack_and_calculate_remaining_health_player(self.damage, pHealth)
        #deathCheck(pHealth)

#
class Menu:
    def __init__(self, equipedWeapon, items, health, enemyHealth=5):
        self.equippedWeapon = equipedWeapon
        self.items = items
        self.health = health
        self.enemyHealth = enemyHealth
    #checks if weapon is set, then inflicts damage based on weapon, if not skips.
    def attack_to_enemy(self):

        if self.equippedWeapon:
            attackDamage = int(list(equipedWeapon.values())[0])
            inflictedDamage = self.enemyHealth - attackDamage
            print(inflictedDamage)
        else:
            print("You have no weapons!")
            
    #raises the global defense flag for next attack against player
    def defend(self):
        global defenseFlag, defenseMod
        print("You brace for the next attack.")
        defenseFlag = True
        defenseMod = 2

    #T O D O
    def item(self):
        print(items)

    #50/50 chance to escape, guaranteed escape on turn 3
    def escape(self):
        escapeOption = False
        if Game.round <= 3:
            escapeOption = True
        else:
            escapeGacha = random.choice[0,1]
            if escapeGacha == 0:
                escapeOption = True

        print(escapeOption)

class Player:
    def __init__(self, name) -> None:
        self.name = name


    def take_turn(self):
        Menu1 = Menu(equipedWeapon,items,pHealth)
        selection = input("1.Attack\n2.Defend\n3.Item\n4.Escape")
        match selection:
            case "Attack":
                Menu1.attack_to_enemy()
                print(equipedWeapon)
            case "Defend":
                Menu1.defend()
            case "Item":
                Menu1.item()
            case "Escape":
                Menu1.escape()
            case _:
                pass



spider = Enemy("Spider", 5, 19)
smallSnake = Enemy("Small Snake", 3,6)


def prematch():
    print("You find a weapon!")
        
    buttonState = input("Do you pick up the weapon?")
    pickUpOption(buttonState, weapons, "flimsyWeapon", 50)

    print(weapons)
    print("Magically, you also find a stick.")

    buttonState = input("Do you pick up the item?")
    pickUpOption(buttonState, items, "stick", "powerful")
    print(items)
    print("A LARGE\nENEMY\nSPIDER...\nappears")

    print("Ah, you took too long to think. The spider attacks!\n")
    spider.attack_to_player()

class Game:
    game_over = False
    enemyParty = {spider, smallSnake}
    
    def __init__(self):
        self.game_over = False
        self.round = 0

    def new_round(self):
        self.round += 1
        print(f"\n***   Round: {self.round}   ***\n")

    prematch()
    while game_over == False:
        jess = Player("Jess")
        jess.take_turn()
        


