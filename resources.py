# imports
from random import randint, choice

# global variables


# classes
class Weapon:
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage
    
    def get_damage(self):
        return self.damage

# BRYTER MOT STANDARD
GOBLIN_WEAPONS = [Weapon("Rusty Cleaver", 2),
                  Weapon("Rusty Spear", 3),
                  Weapon("Stone Axe", 1)]        

class Character:
    
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
        self.generate_weapon()
        self.attack = self.weapon.get_damage()
        
    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    
    def generate_weapon(self):
        random_weapon = randint(0, 100)
        if random_weapon < 20: self.weapon = Weapon("Shortsword", 3)
        elif random_weapon >= 20 and random_weapon < 40: self.weapon = Weapon("Broadsword", 5)
        elif random_weapon >= 40 and random_weapon < 60: self.weapon = Weapon("Small Knife", 1)
        elif random_weapon >= 60 and random_weapon < 80: self.weapon = Weapon("Spear", 2)
        elif random_weapon >= 80 and random_weapon < 90: self.weapon = Weapon("Halberd", 4) 
        elif random_weapon >= 90 and random_weapon < 95: self.weapon = Weapon("Morning Star", 4)
        elif random_weapon == 96: self.weapon = Weapon("Atiesh", 50)
        elif random_weapon == 97: self.weapon = Weapon("Excalibur", 15)
        elif random_weapon == 98: self.weapon = Weapon("Axe of Dargo", 10)
        elif random_weapon == 99: self.weapon = Weapon("Sword of Khaine", 30)
        elif random_weapon == 100: self.weapon = Weapon("Frostmourne", 20)
        else: self.weapon = Weapon("Fists", 1)
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0
    
    def get_attack(self): # tidigare damage
        return self.attack

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def get_attributes(self):
        return self.name, self.health, self.armor

class Goblin:
    
    def __init__(self, health, armor, id):
        self.health = health
        self.armor = armor
        self.id = id
        self.weapon = choice(GOBLIN_WEAPONS)
        self.attack = self.weapon.get_damage()
        
    def __str__(self) -> str:
        return f"Goblin #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    
    
    def take_damage(self, damage):
        relative_damage = damage - self.armor
        if relative_damage > 0:
            self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def get_name(self):
        return f"Goblin #{self.id}"
    
# functions
def save_character(chars : list()):
    save_list = []
    for character in chars:
        name, health, armor = character.get_attributes()
        save_string = f"{name}/{health}/{armor}\n"
        save_list.append(save_string)
        
    with open("saved_characters.txt", "w", encoding="utf8") as f:
        for line in save_list:
            f.write(line)
        print("Characters has been saved!")

def load_characters():
    characters = []
    with open("saved_characters.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            char = Character(attributes[0],
                             int(attributes[1]),
                             int(attributes[2]))
            
            characters.append(char)
    return characters    

def create_character():
    print("Welcome to the character creator!")
    name = input("What is your character called?: ")
    health = randint(10, 30)
    armor = randint(0, 5)
    
    return_char = Character(name, health, armor)
    
    print()
    print(return_char)
    print("Character has been created")
    return return_char
    