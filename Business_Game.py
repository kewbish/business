from random import choice, randint, random, sample
from os import system, name

# Property list attributes:
# property name, property size on a scale of 1-5, does it have a building on it?, what type of building does it have on it? (may be blank), is it rented out?, rental rate (0 if not rented), property value, everything after are different modifications that will impact the value of the house

property_1 = ["Village Square", 1, False, "", False, 0, 100000, 0]
property_2 = ["Water Tower Row", 4, False, "", False, 0, 200000, 0]
property_3 = ["Mountainview Valley", 3, False, "", False, 0, 500000, 0]
property_4 = ["Tropical Paradise", 5, False, "", False, 0, 15000000, 0]
property_5 = ["Far Fields", 5, False, "", False, 0, 200000, 0]
property_6 = ["Urban Alleyway", 3, False, "", False, 0, 600000, 0]
property_7 = ["City Corner", 1, False, "", False, 0, 800000, 0]
property_8 = ["Main Street", 3, False, "", False, 0, 1000000, 0]
property_9 = ["Urban Waterfront", 2, False, "", False, 0, 2000000, 0]
property_10 = ["Suburban Sprawl", 4, False, "", False, 0, 1500000, 0]
property_11 = ["Desert Space", 5, False, "", False, 0, 300000, 0]
property_12 = ["Beach Boulevard", 2, False, "", False, 0, 2000000, 0]
property_13 = ["Sodden Swamp", 1, False, "", False, 0, 75000, 0]
property_14 = ["Fairway Greens", 3, False, "", False, 0, 750000, 0]
property_15 = ["Erst Isle", 5, False, "", False, 0, 10000000, 0]

owned_properties = []
unowned_properties = [property_1, property_2, property_3, property_4, property_5, property_6, property_7,
                      property_8, property_9, property_10, property_11, property_12, property_13, property_14, property_15]
all_properties = [property_1, property_2, property_3, property_4, property_5, property_6, property_7,
                      property_8, property_9, property_10, property_11, property_12, property_13, property_14, property_15]                      
dream_properties = ["Mansion in the Swiss Alps", "Scandanavian Castle", "Condominium Building in Vancouver",
                    "Mansion on a Hawaiian Beach", "Private Island in the Caribbean", "Giant Residential Yacht", "Private Boeing 747", "Huge Texan Ranch"]
dream_property = ""
rent = 0
turn_num = 1
player_balance = 100000
naturaldisaster = 0
market_price = 1
market_list = [1.01, 1.01, 1.01, 0.99, 0.99, 0.99, 0.85, 1.15, 0.9, 1.1, 0.95, 1.05, 0.98, 1.02, 1.00, 1.00, 1.00, 1.00, 1.02, 1.02, 1.02, 0.98, 0.98, 0.98]  # list all the scenarios then lists the modifiers
# list all the scenarios then lists the modifiers
disaster_list = ["Typhoon", "Tornado", "Flood", "Earthquake"]
disaster_result = [0.75,0.8,0.9,0.65]
turn_stage = 0
relative = ["Great Aunt Hilda", "Uncle Gates",
            "Uncle Anderson", "Granny Smith"]
rent_rate_list = []
# structure: type of building, price, value returned per turn
build_choices = [["Small house", 50000, 500], ["Medium house", 75000, 800], ["Large house", 100000, 1000], ["Giant house", 250000, 2500], ["Farm", 200000, 1800], ["Hotel", 400000, 5000]]  # different things that can be on the property

def clear_terminal(): # ZIVEN
    # This is some strange code I found on Stack Overflow that seems to clear the terminal. 
    # system('cls' if name == 'nt' else 'echo -e \\\\033c')
    print("\n")

def turn_main():  # ZIVEN
    global turn_num
    global naturaldisaster
    global dream_property
    if player_balance == 100000000:
        print(f"Congratulations! You have successfully become a housing millionare and earned enough to retire in style by buying a {dream_property}. You've just won the game in {str(turn_num)} turns!")
    if turn_num == 1:
        start_screen()
        input("This is a turn, the main structure of the game. \nIn a turn, you can modify, buy, and sell your properties.\nBut beware; you can only do each thing once per turn, and you can only ever own ten properties. \nMany events also take place during the intervals between turns, including the payment of rent and delivery of your salary. \nYour goal is to earn $100000000 and cash out before the market crashes so you can buy your dream home and win the game!")
        random_fact()
        turn_next_turn()
        turn_choose()
    else:
        random_fact()
        turn_next_turn()
        turn_choose()
    naturaldisaster += 1


def turn_choose():  # ZIVEN
    # This function can be used to navigate through the turn structure. It provides the structure calling the functions for each component of the turns.
    global turn_stage
    global turn_num
    clear_terminal()
    if len(owned_properties) > 0:
        if turn_stage == 0:
            turn_choice = input(
                "Would you like to modify an existing property this turn? y/n ").lower()
            if turn_choice == "y":
                turn_modify()
            turn_stage += 1
        clear_terminal()
        if turn_stage == 1:
            turn_choice = input(
                "Would you like to sell an existing property this turn? y/n ").lower()
            if turn_choice == "y":
                turn_sell()
            turn_stage += 1
    clear_terminal()
    if len(owned_properties) == 0:
        print("You don't currently own any properties.")
        turn_stage = 2   
    if turn_stage == 2 and len(owned_properties) <= 10:
        turn_choice = input(
            "Would you like to buy a new property this turn? y/n ").lower()
        if turn_choice == "y":
            turn_buy()
        else:
            turn_num += 1
            turn_main()
    turn_stage = 0
    turn_num += 1



# Perhaps also have it include updating the value of each property in accordance with any modifications made to it - Mia # Should that not just be handled directly after doing the modification? - Ziven
def turn_next_turn():  # DEREK, ZIVEN
    clear_terminal()
    global player_balance
    global market_price
    global rent
    global naturaldisaster
    modifier = 1
    player_balance += 5000
    naturaldisaster += 1
    print("Turn number: " + str(turn_num))     # Display the turn number.
    if turn_num > 1: # Market does not need to change on first turn because nothing is owned yet. # Here, the market is varied in the variable modifier which comes from market_list.
        placeholder = randint(0, len(market_list) - 1)
        modifier = market_list[placeholder]
        market_price *= modifier
        if modifier > 1:
            print("The housing market went up " + str(round((modifier - 1) * 100)) + " percent.")
        elif modifier < 1:
            print("The housing market went down " +
                  str(round((1 - modifier) * 100)) + " percent.")
        else:
            print("The housing market did not change.")
        n = randint(0,4) #random number to choose which disaster happens.
        chance = random()
        if (chance < naturaldisaster * 0.005): #gradually increases the chance of natural disastors, try to have it happen once every 100 turns
            market_price = disaster_result[n] * market_price # ! TypeError: list indices must be integers or slices, not tuple
            print("Oh no! A " + (disaster_list[n].lower()) + " occurred, and the market went down "+ str((
                1 - disaster_result[n]) * 100) + " percent")
            naturaldisaster = 0  # after a disastor happens, reset the chance for disaster to occur
    print("You earned 5000 dollars from your salary.")      
    rent = 0
    for home in owned_properties: #The total rent owed to the player is determined.
        if home[7] > 0:
            rent += home[5] 
            home[7] -= 1  
    if rent > 0: #If there is any rent, it is paid.
        player_balance += rent
        print(f"You have also earned {str(rent)} dollars in rent.") # Player is given information about their financial status.
    print(f"Your balance is now {str(player_balance)} dollars.")
    print("That means you are " + str(round(((player_balance/100000000)*100), 3)) + " percent of the way to being able to afford your dream home!")
    for home in all_properties: # The price of all of the properties will be changed based on the market variation.
        home[6] *= modifier
    if len(owned_properties) > 0: # If the player owns any properties, they will be printed with their new, market-based prices.
        print("These are the properties you currently own and their current values:")
        print_properties(owned_properties)
    input("")

# TO Do: Implement property tax based on total value of owned properties - ZIVEN

def turn_modify():  # MIA
    clear_terminal()
    print_properties(owned_properties)
    try:  # gets input from user as to what to do next
        prop = owned_properties[int(input(
            "Which property would you like to work on? ")) - 1]
    except:  # if input does not match, break
        print("Invalid input")
        turn_modify()
    # general choices, links to the next
    clear_terminal()
    main_choices = {"1": "Remodel", "2": "Rent"}
    print_properties_dictionary(main_choices)

    try:  # gets input from user as to what to do next
        selection = main_choices.get(input("What would you like to do? "))
    except:  # if input does not match, restart function
        print("Invalid input")
    clear_terminal()
    if selection == "Remodel":
        turn_remodel(prop)
    elif selection == "Rent":
        turn_rent(prop)

# Should it not cost money to build/remodel houses? - Ziven
# ^^ Yes yes yes we need to decide that - Mia
# One moment - I'm just blowing things up - Ziven

def turn_build(prop):  # MIA, EMILIE, ZIVEN   Helper function of turn_modify
    for i, x in enumerate(build_choices):
        print(f"{i}. {x[0]}")

    try:  # gets input from user as to what to do next
        selection = int(input("What would you like to build?"))  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
        turn_build(prop)  # prop never gets used anywhere, we can simply have this function have no arguments
    if not prop[2] and selection[1] <= player_balance:
        prop[2] = True
        prop[3] = selection[0]
        prop[5] += selection[2]
    elif prop[2]:
        print("There's already a building on this property.")
    elif selection[1] >= player_balance:
        print("You don't have enough money to build here. Save up - another day!")


def turn_demolish():
    props_with_buildings = []
    for prop in owned_properties:
        if prop[2]:
            props_with_buildings += prop
    print_properties(props_with_buildings)

    try:
        selection = int(input("Which property's building would you like to demolish?"))
        index = owned_properties.index(props_with_buildings[selection - 1])
        y = input(f"You're about to demolish {props_with_buildings[selection - 1][0]}'s building'. Are you sure? y/n ")
        if y == "y":
            player_balance += props_with_buildings[selection - 1][1] - 5000 # 5000 represents demolition cost
            owned_properties[index][3] = ""
            owned_properties[index][5] -= 0 # subtract rent
        else:
            pass
    except:
        print("Invalid input.")
        turn_demolish()


def turn_remodel(prop):  # MIA   Helper function of turn_modify
    global player_balance
    print ("Remodeling a part of your property will increase its value, but be careful! Remodels cost $10000 apiece.")
    remodel_choices = {  # A dictionary with different choices for house flipping/improvements
        "1": "New floor",
        "2": "New roof",
        "3": "Repaint",
        "4": "New windows",
        "5": "New garden"
    }

    print_properties_dictionary(remodel_choices)

    try:  # gets input from user as to what to do next
        selection = remodel_choices.get(input("What would you like to do? "))
    except:  # if input does not match, restart function
        print("Invalid input.")
        turn_remodel(prop)

    if player_balance >= 10000 and selection not in prop:
        print("Modification made! What a wonderful addition to the property!")
        prop.append(selection)  # appends modification to end of property list
        player_balance -= 10000   # removes the cost of the renovation
        prop[6] += 15000
        input(f"Your balance is now {player_balance}.")
        clear_terminal()
    elif player_balance < 10000:
        input("You don't have enough money for that!")
        clear_terminal()
    elif selection in prop:
        input("This property already has that modification!")
        clear_terminal()


def turn_rent(prop):  # MIA   Helper function of turn_modify, generates three different rent options
    global rent_rate_list
    rent_rate_list = []
    rent_choices_list = []  # A list to hold all the possibilities
    for i in range(3):
        rent_choices_list.append(rentGen(prop))
    rent_choices = {   # A dictionary to help with input
        "1": f"{rent_choices_list[0][0]}/turn for {rent_choices_list[0][1]} turns",
        "2": f"{rent_choices_list[1][2]}/turn for {rent_choices_list[0][3]} turns",
        "3": f"{rent_choices_list[2][4]}/turn for {rent_choices_list[0][5]} turns"
    }
    print_properties_dictionary(rent_choices)  # Prints rent_choices

    try:  # gets input from user as to what to do next
        selection = rent_choices.get(input("Which rental rate would you like? "))
    except:  # if input does not match, restart function
        print("Invalid input.")
        turn_rent(prop)

    # modifies the property list
    if prop[4] == False:
        prop[4] = True
        prop[5] = selection[0]
        prop[7] = selection[1]
        input("Great! Now you will be receiving an income from this property for the next few turns.")
        

def rentGen(prop):  # MIA   Helper function of rent, creates random rental rate based on property
    global rent_rate_list
    rent_rate = int(prop[6] / (randint(50, 200)))
    rent_rate_list.append(rent_rate)
    rent_duration = randint(3, 10)
    rent_rate_list.append(rent_duration)
    return rent_rate_list


def print_properties(list_to_print):
    for i, x in enumerate(list_to_print):
        print(f"{i + 1}: {x[0]} - ${int(x[6])}")


def print_properties_dictionary(dictionary_to_print):
    for key, value in dictionary_to_print.items():
        print(str(key) + ': ' + str(value))  # I believe the ,'s would indicate a list and would come out with funny formatting - Emilie


def turn_buy(): # EMILIE
    global player_balance
    # enumerates over properties; i will be the number, x the property name / description / first el. in array
    # prints a list of property names
    clear_terminal()
    print_properties(unowned_properties)
    num_to_buy = int(input("Which property would you like to buy? "))
    try:
        if num_to_buy >= 0 and num_to_buy <= 15: # ! invalid literal for int() with base 10: '', problem if no input is given
            y = input("Are you sure? y/n ").lower()
            if y == "y":
                if player_balance >= unowned_properties[num_to_buy - 1][6]:
                    # subtracts money from player_balance
                    player_balance -= unowned_properties[num_to_buy - 1][6]
                    # adds property to other list
                    owned_properties.append(unowned_properties[num_to_buy - 1])
                    # removes from unowned list
                    del unowned_properties[num_to_buy - 1]
                    input(f"Property bought. Your balance is now {player_balance} dollars.")
                else:
                    input(
                        "You don't have enough money for that property. Save up - one day!")
                    turn_buy()
            else:
                pass # They don't want to buy it, so we'll take them out of the function.
    except:
        print("Invalid input.")
        turn_buy()


def turn_sell():  # EMILIE
    global player_balance
    clear_terminal()
    print_properties(owned_properties)
    num_to_sell = int(input("Which property would you like to sell? ")) # ! Invalid literal for int90 with base 10 It's not working right now it's working but we have a loop
    try:
        if num_to_sell >= 0 and num_to_sell <= len(owned_properties):
            y = input("Are you sure? y/n ").lower()
            if y == "y":
                player_balance += (owned_properties[num_to_sell - 1][6])
                owned_properties[num_to_sell - 1][5] = 0
                owned_properties[num_to_sell - 1][7] = 0
                unowned_properties.append(owned_properties[num_to_sell - 1])
                del owned_properties[num_to_sell - 1]
                input(f"Property sold. Your balance is now {player_balance} dollars.")
            else:
                pass
    except:
        print("Invalid input.")
        turn_sell()


def start_screen():  # ZIVEN, JOANNA
    player_name = input("What is your name? ")
    clear_terminal()
    print(f"Dear {player_name}, your {choice(relative)} has recently unfortunately died.\nIn the will, they left their remaining savings of $100000 to you. But there's a catch. They want you to become the housing market tycoon they never were.\nYou are to use this money and your regular salary of $5000 to become a housing millionare.\nLearn how to follow the market, flip homes, and save money until you can afford to buy your dream property and retire in style.\nOne last thing before you get started: watch your spending because if you go bankrupt, you lose.")
    clear_terminal()
    print("The following are the selection of available dream homes:")
    loopcounter = 1
    for home in dream_properties:
        print(str(loopcounter) + ": " + home)
        loopcounter += 1
    try:
        prop = int(input(
            "Please enter the number of the dream home you would like to save up for. ")) - 1
        if prop >= 0 and prop <= 7:
            dream_property = dream_properties[prop]
        else:
            print("Invalid input.")
            start_screen()
    except:
        input("Invalid input.")
        start_screen()
    clear_terminal()
    print(f"Good choice! Who wouldn't want a {dream_property.lower()}?")
    input("The thing is, that's going to cost you $100000000. So you had better get to work! Enjoy the game.")
    clear_terminal()


def random_fact():  # EMILIE
    global turn_num
    all_facts = ["Define wholesaling = buying a property from a seller while securing another buyer willing to buy the property at a higher price.", "Define real estate development = everything from the purchase of raw land to sale of developed land. Real estate developers scout land, manage renovation or construction, fund projects, and obtain permits and public approval.", "Define type 1 house flipping = Purchase property in a rapidly rising economy + sell after a period of time at a much higher price.", "Define type 2 house flipping = Purchase a property at low price that has potential to be renovated and sell it after renovations at a much higher price.", "Historically, house flipping has created economic bubbles, such as in the Florida land boom of the 1920s and the real estate bubble in the 2000s caused by relaxed federal borrowing standards. ", "An effect of house flipping is gentrification, the controversial process of changing the character of a neighbourhood by an influx of affluent businesses and residents.", "Private Mortgage Insurange (PMI) costs 0.5 - 5 percent of the loan per month.", "Loans for house flipping have higher intrest rates than the conventional home loan, at 12 - 14 percent vs. 4 percent.", "At an auction, you may not have the chance to inspect a property before placing the down payment.", "Invest in a property only if it is in an area with employment growth, a good school system, and rising real estate sales.", "Avoid investing in an area with high crime rate or too many properties on sale.", "Invest in a property only if its price is below its market value.", "Define rubric for 'structurally sound' ≥ does not need (roof replacement U rewiring) U uninhabited by fungi", "Avoid investing in a property that is inaccessible from your primary residence.", "To estimate the cost of a renovation, add 20% to the final total.", "Do not over-value a home by investing too much in renovation. Instead, improve it 'just enough to make a healthy profit and keep it on par with what’s selling in the neighborhood'.", "Define mill = unit of property tax rate. 1 mill = 0.1%. /n + 'mill levy' = 'property tax'", "Tax rates are calculated separately for each tax jurisdiction, like school district, city, and country. The property tax (mill levy) is determined by adding all the levies", "Property values are assessed every 1 - 5 years.", "Add swings to the attic.", "Define thermostat = a component which senses the temperature of a physical system and performs actions so that the system's temperature is maintained near a desired setpoint. Install a programmable thermostat.", "Define Property value evaluation type 1 of 3 = Sales evaluation. /n Criteria : Comparable sales in the area, Location, Condition of the property, Market", "Define Property value evaluation type 2 of 3 = Cost. (for developed properties) /n Criteria : Cost to replace the building, deducting depreciation", "Always pair spiral stairs with a slide.", "Define Property value evaluation type 3 of 3 = Income. (for owners renting out properties)/n Criteria : Income from rent, deducting maintenance/management costs and taxes.", r"Define the 70% Rule = Investors should pay no more than 70 percent of the after repair value (ARV) of a property minus the cost of the repairs needed when house flipping.", r"Define the Canadian Property Bubble = From 2003 to present, property prices in Canada have increased up to 337%.", "In response to the Canadian Property Bubble, a foreign buyer tax and speculation tax were levied.", r"In the Canadian Property Bubble, mortgage consumed over 50% of an average family’s monthly budget.", r"Canada is heavily dependent on the real estate industry, which accounts for around 12 percent of its GDP."]
    clear_terminal()
    clear_terminal()
    clear_terminal()
    clear_terminal()
    if turn_num == 1:
        print("We wanted to share some housing market information with you, in the following categories: Definitions, Tips, Current market trends.")
    # to avoid crash when turn_num > number of elements # good idea, thanks!
    if turn_num <= 30:
        fact_choice = sample(all_facts, 1)[0]
        input(f"Housing fact: {fact_choice}")
    else:
        fact_repeat = choice(all_facts)
        input(f"Housing fact: {fact_repeat}")
    clear_terminal()

if __name__ == "__main__":
    while player_balance < 100000000:  # fix number
        turn_main()
        # system("clear")