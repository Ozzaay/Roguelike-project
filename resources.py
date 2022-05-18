from pprint import pprint
import random

################## Items #########################
class Item: ### Sets Item super class
    def __init__(self, name, price, count, description):
        self.name = self
        self.price = price
        self.count = count
        self.description = description
    def __str__(self): #description
        return (str(self.name) + ": " + str(self.price) + "-Gold, " + str(self.count) + "-left")
    def pack(self, user, backpack):
       backpack.append(self)

class SuperTonic(Item):
    def __init__(self):
        self.name = "Super Tonic" #name
        self.count = 5 #how many are in the store
        self.price = 20*((self.count-6) * (-1)) #price incrimented by how many are left
        self.description = "Brings your character back to max health.(Usable in battle)" #description of useage
    def use(self, user, enemy): 
        user.health = user.max

class HolyHandGrenade(Item):
    def __init__(self):
        self.name = "Holy Hand Grenade"
        self.count = 25
        self.price = 20
        self.description = "Thous shalt count to three, no more, no less. (Never misses and does 15 damage, for use in a battle)"
    def use(self, user, enemy):
        enemy.health = enemy.health - 15
        
class ArmorPlate(Item):
    def __init__(self):
        self.name = "Armor"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Instant: Adds two armor to your character. (each point of armor negates one damage per attack)"
    def pack(self, user, backpack):
        user.armor = user.armor + 2

class Nurse(Item):
    def __init__(self):
        self.name = "NURSE!"
        self.count = 9999
        self.price = 10
        self.description = "Instant: Our realm famous fairy medical staff will heal you up here and now. No refunds. (brings health back to max)"
    def pack(self, user, backpack):
        user.health = user.max

class ProtienShake(Item):
    def __init__(self):
        self.name = "Protien shake"
        self.count = 15
        self.price = 20 + ((self.count-15)*5) 
        self.description = "Instant: Adds 5 to your max health and 5 to your current health."
    def pack(self, user, backpack):
        user.max = user.max + 5
        user.health = user.health +5


class Axe(Item):
    def __init__(self):
        self.name = "Axe"
        self.count = 1
        self.price = 10
        self.description = "Instant: AND MY AXE... for +1 power."
    def pack(self, user, backpack):
        user.power = user.power + 1

class Winchester(Item):
    def __init__(self):
        self.name = "Winchester"
        self.count = 1
        self.price = 25
        self.description = "Instant: Good ol' Winchester rifle, for those long shots... and +2 power."
    def pack(self, user, backpack):
        user.power = user.power + 2

class MagicMissilelauncher(Item):
    def __init__(self):
        self.name = "Magic Missile Launcher"
        self.count = 1
        self.price = 40
        self.description = "Instant: All the magic missiles you could ever want! Dont let it get dispelled! (+3 to power)"
    def pack(self, user, backpack):
        user.power = user.power + 3

class LightSaber(Item):
    def __init__(self):
        self.name = "Light Saber"
        self.count = 1
        self.price = 55
        self.description = "Instant: Batteries and force crystal sold seperately. (+4 power)"
    def pack(self, user, backpack):
        user.power = user.power + 4

class Hire_DeadPool(Item):
    def __init__(self):
        self.name = "Wade Wilson"
        self.count = 1
        self.price = 150
        self.description = "Instant: Otherwise known as Deadpool.. He will fight with you.. for a price. (+10 power)"
    def pack(self, user, backpack):
        user.power = user.power + 10
#################################################


################# charachters ###################
class Character:
    def __init__(self, name, health, power, level): # charachter stats
        self.name = name
        self.health = health
        self.max = health
        self.power = power
        self.level = 1

    def __str__(self):
        print(self.name + ": " + self.health + "hp, " + self.power + "pw, " + self.evade + "ev, " + self.armor + "ar") # shows char stats

    def print_status(self):
        print ("The {} has {} health and {} power.".format(self.name, self.health, self.power)) # shows char stats
 
    def alive(self): # determines if char is alive after an attack
        if self.health > 0:
            return True
        else:
            return False
    
    def attack(self, enemy):    # determines damage a char does on any given attack
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            print("The enemy missed!")
        else:
            if enemy.armor > self.power:
                    print("The attack doesnt go through your armor!")
            else:
                damage = (self.power- enemy.armor)
                enemy.health = enemy.health - damage
                print ("The {} does {} dammage to the {}. The {} has {} health left.".format(self.name, damage, enemy.name, enemy.name, enemy.health))

class Hero(Character):
    def __init__(self):
        self.name = "hero"
        self.max = 20
        self.health = 20
        self.power = 5
        self.evade = 1
        self.armor = 0
        self.gold = 20
        self.level = 1
    def attack(self, enemy):
        crit = random.randint(1, 10)
        miss = random.randint(1, 100)
        reflect = random.randint(1,8)
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            if crit < 3:
                if (enemy.armor > (self.power*2)):
                    print("It doesnt go through the enemies armor!")
                else:
                    damage = (self.power*2 -enemy.armor)
                    print("Critical Strike!")
                    enemy.health = enemy.health - damage
            else:
                if enemy.armor > self.power:
                    print("It doesnt go through the enemies armor!")
                else:
                    damage = (self.power- enemy.armor)
                    enemy.health = enemy.health - damage
                    print ("The hero does {} damage to the {}. The {} has {} health left.".format(damage, enemy.name, enemy.name, enemy.health))
            if isinstance(enemy, FireEmp):
                self.health = self.health - 1
                print("The hero is hurt by the flames. He takes one damage.")
            if isinstance(enemy, RockGolem) and reflect == 1:
                self.health = self.health - (self.power/2)
                print("The rock golem's hard skin makes your sword bounce back doing half your power as damage top you!")
    def __str__(self):
        evdpct = self.evade*5
        return ("| Health: {}\n| Max-Health: {}\n| Power: {}\n| Evade: {}({}%)\n| Armor: {}\n| Gold: {}".format(self.health, self.max, self.power, self.evade, evdpct, self.armor, self.gold ))

class Medic(Character):
    def __init__(self, level):
        self.name = "Witch Doctor"
        self.health = 10 + (10*.1*level)
        self.max = 10 + (10*.1*level)
        self.power = 2 + (2*.1*level)
        self.evade = 0 + (2*.1*level)
        self.armor = 0 + (0*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def attack(self, enemy):
        miss = random.randint(1, 100)
        recover = random.randint(1, 10)
        if recover < 3 and self.health < 9:
            self.health = self.health + 2
            print("The witch doctor cures his Wounds! (+2 hp)")
        if 1 < miss < (enemy.evade * 5):
            print("The Wich Doctor missed!")
        else:
            if enemy.armor > self.power:
                print("It doesnt go throught the your armor!")
            else:
                damage = (self.power - enemy.armor)
                enemy.health = enemy.health - damage
                print ("The Medic does {} damage to the {}. The {} has {} health left.".format(damage, enemy.name, enemy.name, enemy.health))
    def description(self):
        print("You hear a witch doctor's cackle coming from a dark corner of the cave. Prepare for a fight.")

class Shadow(Character):  
    def __init__(self, level):
        self.name = "shadow"
        self.health = 1 + (1*.1*level)
        self.max = 1 + (1*.1*level)
        self.power = 1 + (2*.1*level)
        self.evade = 3 
        self.armor = 0 + (1*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def description(self):
        print("You dont hear anything, but the shadow on the wall you see moving definately isn't yours. Without warning it lunges forward.")

class Goblin(Character):
    def __init__(self, level):
        self.name = 'Goblin'
        self.health = 6 + (12*.1*level)
        self.max = 6 + (12*.1*level)
        self.power = 2 + (2*.1*level)
        self.evade = 3 + (3*.1*level)
        self.armor = 0 + (3*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def description(self):
        print("You see a simple goblin waddle forth.")

class Zombie(Character):
    def __init__(self, level):
        self.name = 'zombie'
        self.health = 10 + (10*.1*level)
        self.max = 10 + (10*.1*level)
        self.power = 1 + (1*.1*level)
        self.evade = 2 + (2*.1*level)
        self.armor = -1 + (-1*.1*level)
        self.level = 1 + (1*.1*level)
    def alive():
        return True
    def description(self):
        print(" ")

class Slime(Character):
    def __init__(self, level):
        self.name = 'Slime'
        self.health = 10 + (15*.1*level)
        self.max = 10 + (15*.1*level)
        self.power = 1 + (2*.1*level)
        self.evade = 2 + (3*.1*level)
        self.armor = -1 + (1*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1 
    def description(self):
        print("An amorpheous blop drops from the ceiling of the cave and lands at your feet. I wouldn't step in that if I were you...")

class FireEmp(Character):
    def __init__(self, level):
        self.name = "Fire Imp"
        self.health = 6 + (10*.1*level)
        self.max = 6 + (10*.1*level)
        self.power = 3 + (6*.1*level)
        self.evade = 4 + (4*.1*level)
        self.armor = 0 + (0*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def attack(self, enemy):
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            print("The Fire Imp missed!")
        else:
            if enemy.armor > self.power:
                print("It doesnt go throught the your armor!")
            else:
                preburn = self.power - enemy.armor
                damage = self.power + 1 - enemy.armor   
                enemy.health = enemy.health - damage
    def description(self):
        print ("An Imp leaps fromt he fire of a torch lit on the wall, it looks like it wont be letting you pass by freely.")   
    
class RockGolem(Character):
    def __init__(self, level):
        self.name = "Rock Golem"
        self.health = 15 + (12*.1*level)
        self.max = 15 + (12.1*level)
        self.power = 1 + (3*.1*level)
        self.evade = 0 
        self.armor = 2 + (2*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def description(self):
        print("A place in the cave wall begins to move. Great, they have a cave troll.... wait it's just a rock golem. Prepare yourself!")


class DarkWizard(Character):
    def __init__(self):
        self.name = "Dark Wizard"
        self.health = 50
        self.max = 50
        self.power = 3
        self.evade = 0
        self.armor = 10
        self.level = 1
    def description(self):
        print("The man you have been searching for, who started all of this madness. you charge forward and scream, FOR DEMACIA!!!!   .. oh wait, is that you gandalf?")
