##Gavin Murdock
##Oregon Trail
##10/8/21

##imports
import random

from oregonArt import *

#function defs
creator = "Abstract Dev"
tm = "© 2021 by Abstract All rights reserved"
money = 0
oxen = 0
food = 0
clothes = 0
ammo = 0
parts = []
party = []
prof = None
profOptions = ('Banker', 'Carpenter', 'Farmer')

def splash():
    print(LOGO)
    print("\t\t"+creator)
    print("\t"+tm)
    print()
    print()


def trail():
    global money
    global prof
    global profOptions
    profes = input("""
            You may :
            1. Be a banker from Boston
            2. Be a carpenter from Ohio
            3. Be a farmer from Illinois
            4. Find out the differences
                between these choices

            What is your choice?""")
    if profes == "1":
        money = 1300
        prof = profOptions[0]
        print(money)
        lead_name_menu()
    elif profes == "2":
        money = 800
        prof = profOptions[1]
        print(money)
        lead_name_menu()
    elif profes == "3":
        money = 600
        prof = profOptions[2]
        print(money)
        lead_name_menu()

    elif profes == "4":
        print(PROINFO)
        input("Press enter to continue")

def check_name(question):
    while True:
        print("name should be 9 characters or less \n and have no numbers or special characters")
        print()
        name = input(question)
        if name.isalpha():
            if len(name) > 9:
                print("9 characters or less")
                input("Press enter to continue")

            else:
                print(name + " good name")
                return name

        else:
            print("Not a valid name")
            input("Press enter to continue")


def lead_name_menu():
    global leaderName
    global nameOne
    global nameTwo
    global nameThree
    global nameFour
    global party
    partytemp = ["_________","_________","_________","_________"]

    leaderName = check_name("first name of wagon leader?")
    for i in range(4):
        name = check_name("enter the name of party member "+str(i+1))
        partytemp[i]=name
        for person in partytemp:
            print(person)

    nameOne = partytemp[0]
    nameTwo = partytemp[1]
    nameThree = partytemp[2]
    nameFour = partytemp[3]
    partytemp.insert(0,leaderName)
    party = partytemp



def months(startMonth):
    print("""
    
    What mouth  would you like to leave in?
    1. March 
    2. April 
    3. May 
    4. June
    5. July 
    6. Ask For help 
    
    """)
    while True:
        month = input("What is your choice? ")
        if not month.isnumeric():
            print("choose one of the options")
            input()
            continue
        else:
            month = int(month)
            if month == 1:
                startMonth = 1
                return startMonth
            elif month == 2:
                startMonth = 2
                return startMonth
            elif month == 3:
                startMonth = 3

                return startMonth
            elif month == 4:
                startMonth = 4

                return startMonth
            elif month == 5:
                startMonth = 5

                return startMonth
            elif month == 6:
                startMonth = 6

                return startMonth



# def name_menu():
#     global nameOne
#     global nameTwo
#     global nameThree
#     global nameFour
#     nameOne = "_________"
#     nameTwo = "_________"
#     nameThree = "_________"
#     nameFour = "_________"
#
#     namescreen = ("""
#
#     what are the first names of the
#     four other members in your party?
#
#     1.{0:>10}
#     2.{1:>10}
#     3.{2:>10}
#     4.{3:>10}
#     5.{4:>10}   """).format(leaderName, nameOne, nameTwo, nameThree, nameFour)
#     print(namescreen)
#
#     #First name
#     def type_nameOne():
#         global nameOne
#         global nameTwo
#         global nameThree
#         global nameFour
#         nameOne = input("enter names or press enter")
#         if nameOne == "":
#             print("random here")
#         else:
#             if nameOne.isalpha():
#                 if len(nameOne) > 9:
#                     print("9 characters or less")
#                     input("Press enter to continue")
#
#                     name_menu()
#                 else:
#
#                     print(nameOne + " Good Name")
#                     input("Press enter to continue")
#                     namescreen = ("""
#
#                         what are the first names of the
#                         four other members in your party?
#
#                         1.{0:>10}
#                         2.{1:>10}
#                         3.{2:>10}
#                         4.{3:>10}
#                         5.{4:>10}   """).format(leaderName, nameOne, nameTwo, nameThree, nameFour)
#
#                     print(namescreen)
#                     type_nameTwo()
#             else:
#                 print("Not a valid name")
#                 input("Press enter to continue")
#                 name_menu()
#     # second name
#     def type_nameTwo():
#         global nameOne
#         global nameTwo
#         global nameThree
#         global nameFour
#         nameTwo = input("Enter names or press enter")
#         if nameTwo == "":
#             print("random here")
#         else:
#             if nameTwo.isalpha():
#                 if len(nameTwo) > 9:
#                     print("9 characters or less")
#                     input("Press enter to continue")
#                     name_menu()
#                 else:
#
#                     print(nameTwo + " Good Name")
#                     input("Press enter to continue")
#                     namescreen = ("""
#
#                             what are the first names of the
#                             four other members in your party?
#
#                             1.{0:>10}
#                             2.{1:>10}
#                             3.{2:>10}
#                             4.{3:>10}
#                             5.{4:>10}   """).format(leaderName, nameOne, nameTwo, nameThree, nameFour)
#                     print(namescreen)
#                     type_nameThree()
#             else:
#                 print("Not a valid name")
#                 input("Press enter to continue")
#                 name_menu()
# #third name
#     def type_nameThree():
#         global nameOne
#         global nameTwo
#         global nameThree
#         global nameFour
#         nameThree = input("Enter names or press enter")
#         if nameThree == "":
#             print("random here")
#         else:
#             if nameThree.isalpha():
#                 if len(nameThree) > 9:
#
#                     print("9 characters or less")
#                     input("Press enter to continue")
#                     name_menu()
#                 else:
#
#                     print(nameThree + " Good Name")
#                     input("Press enter to continue")
#                     namescreen = ("""
#
#                         what are the first names of the
#                         four other members in your party?
#
#                         1.{0:>10}
#                         2.{1:>10}
#                         3.{2:>10}
#                         4.{3:>10}
#                         5.{4:>10}   """).format(leaderName, nameOne, nameTwo, nameThree, nameFour)
#                     print(namescreen)
#                     type_nameFour()
#
#
#             else:
#                 print("Not a valid name")
#                 input("Press enter to continue")
#                 name_menu()
#         # fourth name
# #fourth name
#     def type_nameFour():
#         global nameOne
#         global nameTwo
#         global nameThree
#         global nameFour
#         global money
#         global oxen
#         global food
#         global clothes
#         global ammo
#         global parts
#         global party
#
#         nameFour = input("Enter names or press enter")
#         if nameFour == "":
#             print("random here")
#         else:
#             if nameFour.isalpha():
#                 if len(nameFour) > 9:
#
#                     print("9 characters or less")
#                     input("Press enter to continue")
#                     name_menu()
#                 else:
#
#                     print(nameFour + " Good Name")
#                     input("Press enter to continue")
#                     namescreen = ("""
#
#                               what are the first names of the
#                               four other members in your party?
#
#                               1.{0:>10}
#                               2.{1:>10}
#                               3.{2:>10}
#                               4.{3:>10}
#                               5.{4:>10}   """).format(leaderName, nameOne, nameTwo, nameThree, nameFour)
#                     print(namescreen)
#                     party = [leaderName, nameOne,nameTwo,nameThree,nameFour]
#                     print(party)
#                     shop(money, oxen, food, clothes, ammo, parts)
#             else:
#                 print("Not a valid name")
#                 input("Press enter to continue")
#                 name_menu()
#     type_nameOne()
# #first name


def game_menu():

    menulp = True
    def game_info():
        print(GMINFO)
    while menulp:
        print(TITLE)
        choiceMenu = int(input("""
            You may:
            1. Travel the trail
            2. Learn about the trail
            3. Wossey out

            What is your choice? """))
        if choiceMenu == 1:
            trail()
            menulp = False



        if choiceMenu == 2:
            game_info()
            input("press enter to continue")

        if choiceMenu == 3:

            def quitmn():
                woose = input("are you sure you want to woose out? y/n")
                if "y" in woose or "Y" in woose or "n" in woose or "N" in woose:
                    if "y" in woose or "Y" in woose:
                        quit()
                    if "n" in woose or "N" in woose:
                        main()
                    else:
                        print("not a valid option")
                    quitmn()
                else:
                    print("plz type yes or no")
                    quitmn()
            quitmn()

        else:
            print("Thats not a vaild option")



def shop(money,oxen,food,clothes,ammo,parts,partsInventory):
    input("Press any key to continue")
    bill = 0
    partsInventory = []
    choices = ["Oxen", "Food", "Clothes", "Ammunition", "Waggon parts", "Check Out"]
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]

    print("Before leaving Independence you should buy Equipment and Supplies.")
    print(str.format("you have ${:.2f} in cash to make this trip", money))
    print("remember you can buy supplies along the way so you dont have to spend it all now")
    input("Press any Key to Continue")

    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        print("welcome to the General Store")
        print("Here is a list of things you can buy")
        print("______________________________________")
        print()
        for i in range(len(choices)):
            print(str.format("\t{:<2}: {:<20} ${:<.2f}",i+1,choices[i],spent_on_items[i]))
        print(str.format("Total Bill so far     ${:<.2f}",bill))
        print(str.format("Total funds available: ${:<.2f}",money - bill))


#Alex worked on this and bugs in this on the 18th for most of class

        choice = int(input("What is your choice"))
        if choice == 1:
            bill-=spent_on_items[0]
            oxen = 0
            spent_on_items[0] = 0.00
            print("""There are 2 oxen in a yoke. 
            I recommend at least 3 yokes.
            I charge $40 a yoke""")
            print(str.format("Total Bill do far ${:<.2f}", bill))
            answer = int(input("How many Yoke do you want"))
            answer = int(answer)
            cost = answer * 40.00
            oxen = answer * 2
            bill += cost
            spent_on_items[0] = cost

        elif choice == 2:
            bill -= spent_on_items[0]
            food = 0
            spent_on_items[1] = 0.00
            print("""You are going to need thousands of pounds of food""")
            print(str.format("Total Bill do far ${:<.2f}", bill))
            answer = int(input("How many pounds of food do you want"))
            cost = answer * 0.25
            food = answer
            bill += cost
            spent_on_items[1] = cost
        elif choice == 3:
            bill -= spent_on_items[0]
            clothes = 0
            spent_on_items[2] = 0.00
            print("""""")
            print(str.format("Total Bill do far ${:<.2f}", bill))
            answer = int(input("How many sets of clothing do you want"))
            cost = answer * 10.00
            clothes = answer
            bill += cost
            spent_on_items[2] = cost

        elif choice == 4:
            bill -= spent_on_items[0]
            ammo = 0
            spent_on_items[3] = 0.00
            print("""""")
            print(str.format("Total Bill do far ${:<.2f}", bill))
            answer = int(input(""))
            cost = answer * 2.00
            ammo = answer
            bill += cost
            spent_on_items[3] = cost

        elif choice == 5:
            global parts_bill
            print("""""")
            partsInventory = []
            parts_bill = 0.00
            parts = ["Wagon Wheel", "Wagon axle", "Wagon Tonue", "Back to main"]
            parts_cost = [10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost)-1]= parts_bill
                # display your menu
                spent_on_items[len(spent_on_items) - 1] = bill
                print("Your going to want some replacement parts for the road")
                print("I recommend buying at least 2 of each")
                print("______________________________________")
                print()
                for i in range(len(parts)):
                    print(str.format("\t{:<2}: {:<20}", i + 1, parts[i]))
                print(str.format("Total Bill so far     ${:<.2f}", bill))
                print(str.format("Total funds available: ${:<.2f}", money - bill))
                parts_choice = int(input("what is your choice"))
                if parts_choice == 1:
                    answer = int(input("How many wagon wheels do you want?"))
                    for i in range(answer):

                        partsInventory.append("Wagon wheel")
                    parts_bill += parts_cost[0] * answer
                elif parts_choice == 2:
                    answer = int(input("How many wagon axle do you want?"))
                    for i in range(answer):
                        partsInventory.append("Wagon axle")
                    parts_bill += parts_cost[0] * answer
                elif parts_choice == 3:
                    answer = int(input("How many wagon tonue do you want?"))
                    for i in range(answer):
                        partsInventory.append("Wagon tonue")
                    parts_bill += parts_cost[0] * answer
                elif parts_choice == 4:
                    bill += parts_bill
                    spent_on_items[4] = parts_bill
                    break
                else:
                    print("Something went wrong")




        elif choice == 6:
            if bill <= money:
                money -= bill

                return oxen, parts, money, food, clothes, ammo, partsInventory

            else:
                print("you don't have that much money alter your shopping list")

        else:
            print("something went wrong")


def travel(oxen, pace, party_condition, weather, total_length, parts, money, food, clothes, ammo, miles_traveled, party, health, rations):
    #ox x pace x w x c
    while oxen > 1:
        foodPer = (1,2,3,4,5)
        oxenEat = ((oxen / 2) * 10)

        print(type(pace), type(party_condition),type(weather))
        traveledToday = (((oxen * pace) * weather) * int(party_condition))
        print(traveledToday)
        total_length -= traveledToday
        miles_traveled += traveledToday
        print(total_length)
        foodToday = ((((random.choice(foodPer) * len(party)) * oxenEat) * pace) * rations)
        food -= foodToday
        if food < -10:
            dead = random.choice(party)
            party.remove(dead)
            print(dead, "Has died of starvation")
            print("You harvest", dead, "for food")
            food = food + random.randrange(10, 180)
            health -= 20
            input()
            return party, food, total_length, miles_traveled
        return health, party, food, total_length, miles_traveled
    else:
        print("""
        
        You have no oxen you can't move
        You need to trade for them. Good luck!
        
        """)


def display_supplies(oxen, parts, money, food, clothes, ammo, partsInventory, party):
    supplies = [oxen, money, food, clothes, ammo]
    supDesc = ["Oxen", "money", "food", "clothes", "ammo"]

    for i in range(len(supplies)):
        print(str.format("{:>2}: {:>20}", supDesc[i], supplies[i]))
    for x in range(len(partsInventory)):
        print(str.format("{:>2}", partsInventory[x]))
    for p in range(len(party)):
        print(str.format("{:>2}", party[p]))
    input("press enter to continue")

def change_pace(pace):
    print("This will change how fast you travel")
    print("""
    
    1:This is the slowest you can travel 
    2:This is the avrage you travel
    3:This is the fastest you can travel 
    
    """)
    while True:
        change_pace = input("What is your choice? ")
        change_pace = int(change_pace)
        print(pace)
        if change_pace == 1:
            pace = 1
        elif change_pace == 2:
            pace = 2
        elif change_pace == 3:
            pace = 3
        elif change_pace == 4:
            break
        else:
            print("choose one of the options")
            input()
    return pace


def change_rations(rations):
    print("This will change how fast you travel")
    print("""

    1:Filling 
    2:Meager
    3:Barebones 

    """)
    while True:
        change_rations = input("What is your choice? ")
        change_rations = int(change_rations)
        if change_rations == 1:
            rations = 3
        elif change_rations == 2:
            rations = 2
        elif change_rations == 3:
            rations = 3
        elif change_rations == 4:
            break
        else:
            print("choose one of the options")
            input()
    return rations


def main():
    global money
    global oxen
    global food
    global clothes
    global ammo
    global parts
    global party
    global prof
    global profOptions
    #define game variables
    playing = True
    #display splash screen
    splash()
    input("Press enter to continue")
    while playing:

        #define all variables needed to play the game
        player_name = None
        diff = None

        diffDesc = (1, 2, 3)
        startMonth = "March"
        health = 100
        day = 1
        date = startMonth +"/"+ str(day)
        weather = 1
        party_condition = int(1)
        pace = 1
        partsInventory = []
        rations = 1
        travel_options = ["Continue on Trail", "Check supplies", "Change pace", "Change Ration", "Rest", "Trade", "Hunt"]
        total_length = int(2200)
        miles_traveled = 0
        broke_down = None
        playing = game_menu()
        player_name = leaderName
        difIndex = profOptions.index(prof)
        diff = diffDesc[difIndex]
        startMonth = months(startMonth)
        print(prof, money, diff, player_name, party, startMonth)
        oxen, parts, money, food, clothes, ammo, partsInventory = shop(money, oxen, food, clothes, ammo, parts, partsInventory)

        while total_length > 0 and len(party) >= 1 and health > 0:
            trail_options = ["Continue on Trail", "check supplies", "change pace", "change Rations", "Rest", "Trade","hunt"]
            print(oxen, parts, money, food, clothes, ammo, partsInventory)
            #sick = pick_illness()
            #display_travle_screen()
            #choice = display_menu(trail_options)
            print("day:", day)
            for i in range(len(trail_options)):
                print(str.format("\t{0:<2}: {1:<20}", i + 1, travel_options[i]))
            choice = input("What do you want to do")
            if not choice.isnumeric():
                print("please enter a number")
                input()
            else:
                choice = int(choice)
                if choice >7:
                    print("Please choose the available options")
                    input()
                else:
                    if choice == 1:
                        print(type(oxen))
                        if oxen >= 1 and not broke_down:
                            day +=1
                            health, party, food, total_length, miles_traveled = travel(oxen, pace, party_condition, weather, total_length, parts, money, food, clothes, ammo, miles_traveled, party, health, rations)
                        else:
                            print("cant travel at this time")
                            if oxen < 1:
                                print("you have no oxen")
                            else:
                                print("you are broke down you need a" + broke_down)
                                continue
                    elif choice == 2:
                        display_supplies(oxen, parts, money, food, clothes, ammo, partsInventory, party)
                        continue
                    elif choice == 3:
                        pace = change_pace(pace)
                    elif choice == 4:
                        rations = change_rations()
                    elif choice == 5:
                        day += 1
                        health += rest()
                    elif choice == 6:
                        trade()
                    elif choice == 7:
                        food = hunt()




        if total_length <= 0:
            print("Good job you made it to Oregon")
        else:
            while True:
                print(GRAVESTONE)
                print()
                print()
                print("You died lmao")
                will = input("Do you want to right a will?")
                if will == "y" or "yes" or "Yes" or "Y":
                   print("TO BAD YOU DONT HAVE A FAMILY LMAOOOOOO")
                   break
                   input()
                elif will == "n" or "no" or "No" or "N":
                    print("good choice you don't have a family anyways")
                    break
                    input()
                else:
                    print("try again")
                    input()

    print("Game Over")
main()





#Notes: Oxen won't return to main after shop but everything else does