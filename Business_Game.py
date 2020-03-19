from random import choice, randint

# EXAMPLE PROPERTY, we can then have ten of these (max number) and simply change them when the player buys/sells
property_1 = ["My House", True, False, "0", 10000, "New roof", "New floors"]
# var name, property name, does it have a building on it?, is it rented out?, rental rate (0 if not rented), property value, everything after are different modifications that will impact the value of the house

owned_properties = [property_1]
unowned_properties = []
dream_properties = ["Mansion in the Swiss Alps", "Scandanavian Castle", "Penthouse in New York City", "Mansion on a Hawaiian Beach", "Private Island in the Caribbean", "Giant Residential Yacht", "Private Boeing 747", "Huge Texan Ranch"]
turn_num = 1
player_balance = 100000
marketprice = 100
market_list = [[scenario1, scenario2], [0.75, 1.25]] # list all the scenarios then lists the modifiers
disaster_list = [[doom1, doom2], [0.75, 1.25]] # list all the scenarios then lists the modifiers

# ZIVEN can create more property listings.

# class scenario # I couldn't figure out how to do this without classes so here we are [why do we need this smh] it looks really bad if it's in turnnextturn smh [but turn next turn]
#     scenario_list = [[scenario1,scenario2],[0.75, 1.25]] #list all the scenarios then lists the modifiers
#     scenario = [[],[]]
#     public random_scenario()
#         placeholder = randint(0,n) #where n is the total number of scenarios
#         scenario = scenario_list[[n],[n]]
#         return scenario:
#     execute_scenario(scenario) [k sorry it's throwing errors] bruh lmao


def turn_main():  # TOGETHER
    if turn_num == 1:  # Pylint is adding an error on this line but it's fine, just ignore
        start_screen()
        print("This is a turn, the main structure of the game. In a turn, you can modify, buy, and sell your properties.")
    else:
        turn_next_turn()
    turn_num += 1
    # main turn function

def turn_next_turn():  # DEREK
    if turn_num == 2:  # implement some default starter
        pass
    else:
        placeholder = randint(0, n)  # Derek y'all best remember to add 'n'
        modifier = marketlist[[],placeholder]
        marketprice=marketprice*modifier
        if modifier > 1:
            print("the market went up"+(modifier-1)*100+"percent")
        elif modifier < 1:
            print("the market wend down"+(1-modifier)*100+"percent")
        else:
            print("the market did change")
    
    # implement next turn, when all the background stuff happens (market changes, etc) and tells the user

def turn_modify():  # MIA
    print_properties(owned_properties)

    try:  # gets input from user as to what to do next
        propert = owned_properties.get(input("Which property would you like to work on?").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")

    # general choices, links to the next
    main_choices = {"build", "remodel", "rent", "back"}
    rent_choices = {}  # different rental rate options

    try:  # gets input from user as to what to do next
        func = main_choices.get(input("What would you like to do?").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")

    if func == "back":
        pass
        # link to line in turn_main
    else:
        func()

    pass  # implement modify current property, house flipping, renting out?

def build(property):  # MIA Helper function of turn_modify
    build_choices = {"small house", "medium house", "large house", "giant house", "farm", "hotel", "back"}  # different things that can be on the property
    try:  # gets input from user as to what to do next
        selection = build_choices.get(
            input("What would you like to do?").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
        build()
    # will then change selected property
    pass

def remodel(property):  # MIA   Helper function of turn_modify
    # different chocies for house flipping/improvements
    remodel_choices = {"new floor", "new roof",
                       "repaint", "new windows", "new garden"}

    try:  # gets input from user as to what to do next
        selection = remodel_choices_house.get(
            input("What would you like to do? ").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
        remodel()

    # will then change selected property
    pass


def rent(property):  # MIA   Helper function of turn_modify
    rent_choices = {"1500/month for 5 turns", "3000/month for 2 turns"}
    pass


def print_properties(list_to_print):
    for i, x in enumerate(list_to_print):
        print(f"{i}: {x[0]}")

def turn_buy_new():  # EMILIE
    print("Which property would you like to buy?")
    # enumerates over properties; i will be the number, x the property
    print_properties(unowned_properties)  # prints a list of properties
    num_to_buy = int(input())
    try:
        if num_to_buy > 0 and num_to_buy < 10:
            y = input("Are you sure?").lower()
            if y == "y":
                # this is throwing an error but should work fine
                if player_balance >= unowned_properties[num_to_buy - 1]:
                    # subtracts money from player_balance
                    player_balance -= unowned_properties[num_to_buy - 1][2]
                    # adds property to other list
                    owned_properties.append(unowned_properties[num_to_buy - 1])
                    # removes from unowned list
                    properties.remove(unowned_properties[num_to_buy - 1])
                    print(
                        f"Property bought. Your balance is now {player_balance}")
                else:
                    print(
                        "You don't have enough money for that property. Save up, and maybe you'll be able one day!")
    except:
        print("Error: invalid input.")

def turn_sell():  # EMILIE
    print("Which property would you like to sell?")
    # enumerates over properties; i will be the number, x the property
    print_properties(owned_properties)
    num_to_sell = int(input())
    try:
        if num_to_sell > 0 and num_to_sell < 10:
            y = input("Are you sure?").lower()
            if y == "y":
                player_balance += ownesd_properties[num_to_sell - 1][2]
                unowned_properties.append(owned_properties[num_to_sell - 1])
                properties.remove(owned_properties[num_to_sell - 1])
                print(f"Property sold. Your balance is now {player_balance}")
    except:  # will catch all and any errors
        print("Error: not a valid input.")


def turn_parse_input(input):
    # maps input string to a function that will run. otherwise, print invalid input.
    map_in_to_func = {  # dictionary mapping input -> function that will run
        "next": turn_next_turn(),
        "modify": turn_modify(),
        "buy new": turn_buy_new(),
        "sell": turn_sell()
    }
    func = map_in_to_func.get(input, lambda: print("Invalid input"))
    func()


salary = ["$5000 monthly salary", "$60000 annual salary",
          "$140 daily salary", "$1250 weekly salary"]
relative = ["Great Aunt Hilda", "Uncle Gates", "Uncle Anderson", "Woompus"]
defect = ["not having doors", "not having windows", "being 107 years old"]

# for the start screen print f


def start_screen():  # ZIVEN, JOANNA
    player_name = input("What is your name?")  # When do we ask this?
    # continue beginning story here, inheritance, etc.
    print(f"Dear {player_name}, you have inherited a shack from {choice(relative)}. Despite {choice(defect)}, its location in downtown Vancouver earns a government assessment price of $100000. After a renovation, you can easily sell it for $1000000, taking you indefinitely closer to your dream - $30000000 in a property. With a {choice(salary)}, your journey as a house flipper begins! For help, enter ")


def start_dream_selection():  # ZIVEN
    print("Dream Homes:")
    for home in dream_properties:
        print(str(1) + home)
    prop = int(input(
        "Please enter the number of the dream home you would someday like to own. ")) - 1
    dream_property = dream_properties[prop]
    print(f"Good choice! Who wouldn't want a {dream_property.lower()}.")
    print("The catch is that this is going to cost you $100,000,000.")

# Important -> Do NOT do any sketchy system32 deletion in the Powershell; this will directly affect Ziven's system. :) - Emilie
# Bugfixing, writing -> JOANNA sure?").lower()
    #         if y == "y":
    #             player_balance += ownesd_properties[num_to_sell - 1][2]
    #             unowned_properties.append(owned_properties[num_to_sell - 1])
    #             properties.remove(owned_properties[num_to_sell - 1])
    #             print(f"Property sold. Your balance is now {player_balance}")
    # except:  # will catch all and any errors
    #     print("Error: not a valid input.") Seems like this was randomly copied here, commenting away for now - Emilie


salary = ["$5000 monthly salary", "$60000 annual salary",
          "$140 daily salary", "$1250 weekly salary"]
relative = ["Great Aunt Hilda", "Uncle Gates", "Uncle Anderson", "Woompus"]
defect = ["not having doors", "not having windows", "being 107 years old"]