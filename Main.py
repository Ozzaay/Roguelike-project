import random
from resources import ArmorPlate, Axe, DarkWizard, FireEmp, Goblin, Hero, Hire_DeadPool, HolyHandGrenade, LightSaber, MagicMissilelauncher, Medic, Nurse, ProteinShake, RockGolem, Shadow, Slime, SuperTonic, Winchester


def cleanup():
    input("**Press enter to continue...")

def banner(txt):
    print ("*")*(len(txt)+4)
    print ("* " + txt + " *")
    print ("*")*(len(txt)+4)

def fight_sequence(enemy, hero, backpack):
    """_The fight sequences and how the battle order works_

    Args:
        enemy (_type_): _The enemies you can encounter during combat_
        hero (_type_): _The player character_
        backpack (_type_): _The items you currently have in your inventory_
    """
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
        print("| 1. Fight                ")
        print("| 3. Get status of hero   |")
        print("|_________________________|")
        choice = input("What would you like to do? ")
        if  choice =="1":
            hero.attack(enemy)
            if enemy.alive() == False:
                print("You Defeated the Enemy!")
                print("                  \' The {} is dead.".format(enemy.name))
                print("")
                hero.gold += enemy.gold
                print("                  \' You found {} gold!   ".format(enemy.gold))
                print("                  ............................")
        elif choice =="åäöåp":
            print(" ______________________________")
            print("| Choose an item number to use |")
            print(" ______________________________")
            backpack.sort()
            for i in range(len(backpack)):
                print(str(i) + ". " + backpack[i].name)
            used = int(choice(">>"))
            backpack[used].use(hero, enemy)
            del backpack[used]
        elif choice =="2":
            print(hero)
            print(" If your health goes to 0, you die.\nYour max health is the most you can have right now at full streangth.\nYour power is how much damage you deal before armor is involved.\nYour evade is the percentage chance that an attacking enemy will miss you completely.\nEach point of armor will protect you from one point of damage when an enemy attacks you.\noYur fold will be used to buy items in the store.")
        else:
            print("Please Try again")

        if enemy.alive():
            # Enemy attacks hero
            enemy.attack(hero)
            if hero.alive() == False:
                print("You died :(")
                cleanup()                                                                           



def store(a, b, c, d, e, f, g, h, i, j, hero, backpack): # open tbhe store
    """_summary_

    Args:
        a (_type_): _Super Tonic: an item that lets you heal back to full hp during combat_
        b (_type_): _Holy Hand Grenade: An item you can use during combat to deal damage to your enemy_
        c (_type_): _Armor: A instant upgrade that decreases the damage you take_
        d (_type_): _NURSE!: An item that instanty heals you back to full hp_
        e (_type_): _Protein shake: An item that increases your max hp_
        f (_type_): _Axe: an item that slightly increases your damage_
        g (_type_): _Winchester: An item the increases your damage_
        h (_type_): _Magic Missile Launcher: An item that greatly increases your damage_
        i (_type_): _Light sabre: An item that increases your damage to the maximum_
        j (_type_): _Wade Wilson: A mercenary that helps you deal more damage_
        hero (_type_): _Your player character: let's you see your characters current status, such as health, damage and armor stats_
        backpack (_type_): _Your item bag that lets you see what items you currently have_
    """

    def sure(): # function for asking if you want to leave a menu or go back to the store 
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
        """_summary_

        Args:
            item (_type_): _The item you are about to buy_
            backpack (_type_): _your item bag where said item will be put_
        """
        print(item.description)
        print(" =============================================================================")
        print(" _____________________________________ ")
        print("| Type \'1\' To buy this item.        |")
        print("| Type \'2\' To go back to the store. |")
        print("| Type \'3\' To exit the store.       |")
        print(" _____________________________________ ")

        # options to determine he results from what you pick
        try:    
            choice = int(input(">>"))
        except ValueError:
            banner("\nPlease only use integers")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        if choice == 1:
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
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif choice == 3:
            sure()
        elif input == "":
            banner("Invalid input {}, try again: ".format(input))
        else:
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
        store(a, b, c, d, e, f, g, h, i, j, hero, backpack) #determines what item the user wants to look at
    if choice == 1: want_to_buy(a, backpack)
    elif choice == 2: want_to_buy(b, backpack)
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
        print(hero)

        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
    elif choice == 12:
        sure()
    elif input == "":
        banner("Invalid input {}, try again: ".format(input))
    else:
        banner("Invalid input, please try again: ")
        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)


def main(): 
    print("Welcome to Rune Crawler")
    input("press any key to continue...")
    print(" You are a Hero of The great empire Lenuria, and a DARK Wizard has threatened your homeland. The wizard has been sending hoards of monsters")
    print("from its layer at the bottom of the dungeon. Reach him and save your kingdom... For Lenuria!")     
    print("Each floor will have a new, stronger combatant. Between each floor a small fairy store will have a portal open to")
    print("sell you items you might need. Can you make it all of the way to the bottom?")
    start = input("Type \'start\' to start the game and take your first steps into the dungeons first floor!:  ")
    if start.upper() == "START": 
        print("\nYou step into the dungeon and see your first monster!")
    else:
        print("I dont care that you didnt type start. This is a dungeoncrawler game. *The game maker pushes your hero into the dungeon and a monster appears!")
    backpack = []
    floor_count = 1
    thishero = Hero()

    #items set
    super_tonic = SuperTonic()
    armor_plate = ArmorPlate()
    holy_hand_grande = HolyHandGrenade()
    nurse = Nurse()
    protein_shake = ProteinShake()
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
        #enemies set by level increase
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
        store(super_tonic, holy_hand_grande, armor_plate, nurse, protein_shake, axe, winchester, magic_missile_launcher, lightsaber, hire_deadpool, thishero, backpack) #calls store
        floor_count += 1

    cleanup()
    print("Congratulations you beat the final level")   
    input("press any key to continue...")
    print("BUT CAN YOU DEFEAT THE DARK WIZARD?")
    fight_sequence(dark_wizard, thishero, backpack)
    
    print("You Win!!!")
    cleanup()


if __name__ == "__main__":
    main()