import random
import sys
import os
from tkinter import N
from resources import ArmorPlate, Axe, DarkWizard, FireEmp, Goblin, Hero, Hire_DeadPool, HolyHandGrenade, LightSaber, MagicMissilelauncher, Medic, Nurse, ProtienShake, RockGolem, Shadow, Slime, SuperTonic, Winchester

def cleanup():
    input("**Press enter to continue...")
    os.system("clear")

def banner(txt):
    print ("*")*(len(txt)+4)
    print ("* " + txt + " *")
    print ("*")*(len(txt)+4)

def pow(txt):
    print ("^")*(len(txt)+4)
    print ("| " + txt + " |")
    print ("^")*(len(txt)+4)

def fight_sequence(enemy, hero, backpack):
    print(" ")
    enemy.description()
    cleanup()

    while enemy.alive() and hero.alive():# fight sequence options
        print("___________________________________________________________________________________")
        hero.print_status()
        enemy.print_status()
        print("___________________________________________________________________________________")
        print(" ")
        print("__________________________")
        print("| What do you want to do? |")
        print("| 1. Fight {}             ").format(enemy.name)
        print("| 2. Use item             |")
        print("| 3. Get status of hero   |")
        print("|_________________________|")
        try:
            

            if input == '':
                print("try again")
                # banner("Please only use integers")
                # fight_sequence(enemy, hero, backpack)
            else:
                pass
        except ValueError:
            banner("Please only use integers")
            # fight_sequence(enemy, hero, backpack)
        print()
        if input == 1:
            os.system("clear")
            hero.attack(enemy)
            if enemy.alive() == False:
                print("You Defeated the Enemy!")
                print("                  \' The {} is dead.".format(enemy.name))
                print("")
                hero.gold += enemy.gold
                print("                  \' You found {} gold!   ".format(enemy.gold))
                print("                  ............................")
        elif input == 2: 
            os.system("clear")
            print(" ______________________________")
            print("| Choose an item number to use |")
            print(" ______________________________")
            backpack.sort()
            for i in range(len(backpack)):
                print(str(i) + ". " + backpack[i].name)
            used = int(input(">>"))
            backpack[used].use(hero, enemy)
            del backpack[used]
        elif input == 3:
            os.system("clear")
            print(hero)
            print(" If your health goes to 0, you die.\nYour max health is the most you can have right now at full streangth.\nYour power is how much damage you deal before armor is involved.\nYour evade is the percentage chance that an attacking enemy will miss you completely.\nEach point of armor will protect you from one point of damage when an enemy attacks you.\noYur fold will be used to buy items in the store.")
        else:
            print("please try again")

        if enemy.alive():
            # Enemy attacks hero
            enemy.attack(hero)
            if hero.alive() == False:
                print("You died :(")
                cleanup()                                                                           
                sys.exit()


def store(a, b, c, d, e, f, g, h, i, j, hero, backpack): # open tbhe store

    def sure(): # function for asking if you want to leave a menu or go back to the store
        os.system("clear")
        print (" __________________________________________")
        print ("| Are you sure you want to leave? (Y or N) |")
        print (" __________________________________________")
        leave = input(" >>")
        if leave.upper() == "Y":
            return
        elif leave.upper() == "N":
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif input == "":
            banner("Invalid input {}, try again: ".format(input))
        else:
            banner("Please enter yes or no. ")
            sure()
        
    def want_to_buy(item, backpack): # function for determining if you want to buy an item you have chosen or not 
        os.system("clear")
        item.pic()
        print(item.description)
        print(" =============================================================================")
        print(" _____________________________________ ")
        print("| Type \'1\' To buy this item.        |")
        print("| Type \'2\' To go back to the store. |")
        print("| Type \'3\' To exit the store.       |")
        print(" _____________________________________ ")
        try:    # options to determine the results from what you pick
            choice = int(input(">>"))
        except ValueError:
            banner("\nPlease only use integers")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        if choice == 1:
            os.system("clear")
            if item.count == 0:
                banner("This item is out of stock.")
                store (a, b, c, d, e, f, g, h, i, j, hero, backpack)
            elif hero.gold < item.price:
                banner("You dont have enough gold.")
                store (a, b, c, d, e, f, g, h, i, j, hero, backpack)
            else: 
                item.pack(hero, backpack)
                print("You bought " + item.name)
                item.count = item.count - 1
                hero.gold -= item.price
                store (a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif choice == 2:
            os.system("clear")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif choice == 3:
            os.system("clear")
            sure()
        elif input == "":
            banner("Invalid input {}, try again: ".format(input))
        else:
            os.system("clear")
            banner("Invalid input, please try again: ")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
    
    cleanup() 
    # shop intro
    print("Select a number for an item in the shop to see what it does or to purchase it. Of course")
    print("this is a buisness so the items arent free. If you dont have enough cash, go kill a")
    print("monster or two. I'll have a portal open between each floor.")
    print("Gold: {}  $".format(hero.gold)) #current hero gold
    print("")# list of items and how many are left
    print ("1. " + str(a) + "\n2. " + str(b) + "\n3. " + str(c) + "\n4. " + str(d) + "\n5. " + str(e) + "\n6. " + str(f) + "\n7. " + str(g) + "\n8. " + str(h) + "\n9. " + str(i) + "\n10. " + str(j) + "\n11. Get Hero Status\n12.  Exit")
    try:
        choice = int(input(">>"))
    except ValueError:
        banner("Please only use integers")
        store(a, b, c, d, e, f, g, h, i, j, hero, backpack) #determines what item the usser wants to look at
    if choice == 1:
        want_to_buy(a, backpack)
    elif choice == 2:
        want_to_buy(b, backpack)
    elif choice == 3:
        want_to_buy(c, backpack)
    elif choice == 4:
        want_to_buy(d, backpack)
    elif choice == 5:
        want_to_buy(e, backpack)
    elif choice == 6:
        want_to_buy(f, backpack)
    elif choice == 7:
        want_to_buy(g, backpack)
    elif choice == 8:
        want_to_buy(h, backpack)
    elif choice == 9:
        want_to_buy(i, backpack)
    elif choice == 10:
        want_to_buy(j, backpack)
    elif choice == 11:
        os.system("clear")
        print(hero)

        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
    elif choice == 12:
        sure()
    elif input == "":
        banner("Invalid input {}, try again: ".format(input))
    else:
        os.system("clear")
        banner("Invalid input, please try again: ")
        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)


def main(): # game intro (Game starts here)
    print("Welcome to Rune Crawler")
    input("press any key to continue...")
    print(" You are a Hero of The great empire Lenuria, and a DARK Wizard has threatened your homeland. The wizard has been sending hoards of monsters")
    print("from its layer at the bottom of the dungeon. Reach him and save your kingdom... For Lenuria!")     
    print("Each floor will have a new, stronger combatant. Between each floor a small fairy store will have a portal open to")
    print("sell you items you might need. Can you make it all of the way to the bottom?")
    start = input("Type \'start\' to start the game and take your first steps into the dungeons first floor!:  ")
    if start.upper() == "START": 
        print("\nYou step into the dungeon and see your first monster!")
        os.system("clear")
    else:
        print("I dont care that you didnt stype start. This is a monster game. *The game maker pushes your hero into the dungeon and a monster appears!")
        os.system("clear")
    backpack = []
    floor_count = 1
    thishero = Hero()
    #items set
    super_tonic = SuperTonic()
    armor_plate = ArmorPlate()
    holy_hand_grande = HolyHandGrenade()
    nurse = Nurse()
    protien_shake = ProtienShake()
    axe = Axe()
    winchester = Winchester()
    magic_missile_launcher = MagicMissilelauncher()
    lightsaber = LightSaber()
    hire_deadpool = Hire_DeadPool()
    #enemies set
    medic = Medic(floor_count)
    shadow = Shadow(floor_count)
    goblin = Goblin(floor_count)
    slime = Slime(floor_count)
    fire_emp = FireEmp(floor_count)
    rock_golem = RockGolem(floor_count)
    dark_wizard = DarkWizard()
    enemy_rotation = [medic, shadow, goblin, slime, fire_emp, rock_golem]


    while floor_count < 25:
        #enemies1   set by level increase
        medic = Medic(floor_count)
        shadow = Shadow(floor_count)
        goblin = Goblin(floor_count)
        slime = Slime(floor_count)
        fire_emp = FireEmp(floor_count)
        rock_golem = RockGolem(floor_count)
        dark_wizard = DarkWizard()
        #
        enemy_rotation = [medic, shadow, goblin, slime, fire_emp, rock_golem]   #array to pick random enemy from
        next_enemy = random.randint(0, 5)
        enemy = enemy_rotation[next_enemy]
        cleanup()
        print("Floor #{} +".format(floor_count))
        print(" ")
        fight_sequence(enemy, thishero, backpack) #calls fight
        store(super_tonic, holy_hand_grande, armor_plate, nurse, protien_shake, axe, winchester, magic_missile_launcher, lightsaber, hire_deadpool, thishero, backpack) #calls store
        floor_count += 1

    cleanup()
    print("Congratulations you beat the final level")   
    input("press any key to continue...")
    print("BUT CAN YOU DEFEAT THE DARK WIZARD?")
    fight_sequence(dark_wizard, thishero, backpack)
    
    print("You Win!!!")
    cleanup()
    


main()