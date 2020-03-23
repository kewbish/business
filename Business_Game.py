from random import choice, randint, sample

# Property list attributes:
# property name, property size on a scale of 1-5, does it have a building on it?, what type of building does it have on it? (may be blank), is it rented out?, rental rate (0 if not rented), property value, everything after are different modifications that will impact the value of the house

property_1 = ["Village Square", 1, False, "", False, 0, 100000]
property_2 = ["Water Tower Row", 4, False, "", False, 0, 200000]
property_3 = ["Mountainview Valley", 3, False, "", False, 0, 500000]
property_4 = ["Tropical Paradise", 5, False, "", False, 0, 15000000]
property_5 = ["Far Fields", 5, False, "", False, 0, 200000]
property_6 = ["Urban Alleyway", 3, False, "", False, 0, 600000]
property_7 = ["City Corner", 1, False, "", False, 0, 800000]
property_8 = ["Main Street", 3, False, "", False, 0, 1000000]
property_9 = ["Urban Waterfront", 2, False, "", False, 0, 2000000]
property_10 = ["Suburban Sprawl", 4, False, "", False, 0, 1500000]
property_11 = ["Desert Space", 5, False, "", False, 0, 300000]
property_12 = ["Beach Boulevard", 2, False, "", False, 0, 2000000]
property_13 = ["Sodden Swamp", 1, False, "", False, 0, 75000]
property_14 = ["Fairway Greens", 3, False, "", False, 0, 750000]
property_15 = ["Erst Isle", 5, False, "", False, 0, 0, 10000000]


owned_properties = []
unowned_properties = [property_1, property_2, property_3, property_4, property_5, property_6, property_7,
                      property_8, property_9, property_10, property_11, property_12, property_13, property_14, property_15]
dream_properties = ["Mansion in the Swiss Alps", "Scandanavian Castle", "Condominium Building in Vancouver",
                    "Mansion on a Hawaiian Beach", "Private Island in the Caribbean", "Giant Residential Yacht", "Private Boeing 747", "Huge Texan Ranch"]
turn_num = 1
player_balance = 100000
marketprice = 1
naturaldisaster = 1
market_list = [0.9, 1.1]  # list all the scenarios then lists the modifiers
# list all the scenarios then lists the modifiers
disaster_list = [["doom1", "doom2"], [0.75, 1.25]]
turn_stage = 0
relative = ["Great Aunt Hilda", "Uncle Gates",
            "Uncle Anderson", "Granny Smith"]


# Note: pass at the end of functions SHOULD BE DELETED, and ONLY USED AS PLACEHOLDER WHILE THERE IS NO OTHER CODE
# Note: A lot of unused variable errors, perhaps you want to return some of them?
# Note: A lot of used before assignment errors, these can be ignored and work fine AFAIK


def turn_main():  # ZIVEN
    if player_balance == 100000000:
        dream_property = choice(dream_properties)
        print(
            f"Congratulations! You have successfully become a housing millionare and earned enough to retire in style by buying a {dream_property}. You've just won the game!")  # removed .lower(), cannot use methods in f-string afaik
    if turn_num == 1:
        start_screen()
        print("This is a turn, the main structure of the game. \n In a turn, you can modify, buy, and sell your properties.\n But beware; you can only do each thing once per turn, and you can only ever own ten properties. \n Many events also take place during the intervals between turns. \n Your goal is to earn $100000000 and cash out before the market crashes so you can buy your dream home and win the game.")
        random_fact()
    else:
        turn_next_turn()
        turn_choose()
    turn_num += 1
    naturaldisaster += 1
    # main turn function


def turn_choose():  # ZIVEN This function can be used to navigate through the turn structure. It provides the structure calling the functions for each component of the turns.
    if turn_stage == 0:
        turn_choice = input(
            "Would you like to modify an existing property this turn? y/n ").lower()
        if turn_choice == "y":
            turn_modify()
        turn_stage += 1
    if turn_stage == 1:
        turn_choice = input(
            "Would you like to sell an existing property this turn? y/n ").lower()
        if turn_choice == "y":
            turn_sell()
        turn_stage += 1
    if turn_stage == 2:
        turn_choice = input(
            "Would you like to buy a new property this turn? y/n ").lower()
        if turn_choice == "y":
            turn_buy_new()
        turn_stage = 0


# I believe the turn_next_turn function should also add the player's salary ($5000/turn) and later handle paying rent and other things like that. - Ziven
def turn_next_turn():  # DEREK
    if turn_num == 2:  # implement some default starter
        pass
    else:
        placeholder = randint(0, len(market_list))
        modifier = market_list[placeholder]
        marketprice = marketprice * modifier
        if modifier > 1:
            print("The market went up " + (modifier - 1) * 100 + " percent.")
        elif modifier < 1:
            print("The market went down " + (1 - modifier) * 100 + " percent.")
        else:
            print("The market did not change.")
        if (randint < naturaldisaster * 0.01):
            marketprice = marketlist[[], placeholder] * marketprice  # ! marketlist does not exist.
            print("Oh no! A " + marketlist[[placeholder], []] + " occurred, and the market went down "+(
                1 - marketlist[[], [placeholder]]) * 100 + " percent")
            n = 0  # ! where is n used?
        random_fact()
    player_balance = player_balance + 5000

def turn_modify():  # MIA
    print_properties(owned_properties)

    try:  # gets input from user as to what to do next
        prop = owned_properties.get(input(
            "Which property would you like to work on? ").lower())  # not case sensitive
    except:  # if input does not match, break
        print("Invalid input")

    # general choices, links to the next
    main_choices = ["build", "remodel", "rent"]

    try:  # gets input from user as to what to do next
        func = main_choices.get(
            input("What would you like to do?").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
    func(prop)


def build(prop):  # MIA Helper function of turn_modify, leave it for now
    selected = prop
    answer = False
    build_choices = {"small house", "medium house", "large house", "giant house",
                     "farm", "hotel", "back"}  # different things that can be on the property
    try:  # gets input from user as to what to do next
        selection = build_choices.get(
            input("What would you like to do?").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
        build(prop)
    if prop[2] == False:
        prop[2] = True
        prop[3] = selection


def remodel(prop):  # MIA   Helper function of turn_modify
    # different choices for house flipping/improvements
    remodel_choices = {"new floor", "new roof",
                       "repaint", "new windows", "new garden"}
    print_properties(remodel_choices)  # prints possibilities
    try:  # gets input from user as to what to do next
        selection = remodel_choices.get(
            input("What would you like to do? ").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
        remodel(selected)  # ! selected does not exist
    prop.append(selection)  # appends modification to end of property list


def rent(prop):  # MIA   Helper function of turn_modify, generates three different rent options
    rent_choices = []  # where is this populated?
    for i in rent_choices:  # adds each possibility to the list, max of three
        if len(rent_choices) == 3:
            break
        rent_choices[i] = rentGen(prop)

    print_properties(rent_choices)

    try:  # gets input from user as to what to do next
        selection = rent_choices.get(
            input("What would you like to do? ").lower())  # not case sensitive
    except:  # if input does not match, restart function
        print("Invalid input")
        remodel(selected)

    # modifies the property list
    prop[4] = True
    prop[5] = selection


def rentGen(prop):  # MIA   Helper function of rent, creates random rental rate based on property
    rent_rate = prop[6] / (randint(500, 2000))
    rent_duration = randint(1, 10)

    rent_string = "{}/month for {} turns".format(rent_rate, rent_duration)

    return rent_string


def print_properties(list_to_print):
    for i, x in enumerate(list_to_print):
        print(f"{i}: {x[0]}")


def turn_buy_new():  # EMILIE
    print("Which property would you like to buy?")
    # enumerates over properties; i will be the number, x the property name / description / first el. in array
    # prints a list of property names
    print_properties(unowned_properties)
    num_to_buy = int(input())
    try:
        if num_to_buy > 0 and num_to_buy < 10:
            y = input("Are you sure?").lower()
            if y == "y":
                # this is throwing an error but should work fine
                if player_balance >= unowned_properties[num_to_buy - 1]:
                    # subtracts money from player_balance
                    player_balance -= unowned_properties[num_to_buy - 1][6]
                    # adds property to other list
                    owned_properties.append(unowned_properties[num_to_buy - 1])
                    # removes from unowned list
                    properties.remove(unowned_properties[num_to_buy - 1])
                    print(
                        f"Property bought. Your balance is now {player_balance}.")
                else:
                    print(
                        "You don't have enough money for that property. Save up - one day!")
    except:
        print("Invalid input.")


def turn_sell():  # EMILIE
    print("Which property would you like to sell?")
    print_properties(owned_properties)
    num_to_sell = int(input())
    try:
        if num_to_sell > 0 and num_to_sell < len(owned_properties):
            y = input("Are you sure? ").lower()
            if y == "y":
                player_balance += owned_properties[num_to_sell - 1][6]
                unowned_properties.append(owned_properties[num_to_sell - 1])
                properties.remove(owned_properties[num_to_sell - 1])
                print(f"Property sold. Your balance is now {player_balance}.")
    except:  # will catch all and any errors
        print("Invalid input.")


def turn_parse_input(input):
    # maps input string to a function that will run. otherwise, print invalid input.
    map_in_to_func = {  # dictionary mapping input -> function that will run
        "next": turn_next_turn(),
        "modify": turn_modify(),
        "buy new": turn_buy_new(),
        "sell": turn_sell()
    }
    func = map_in_to_func.get(input, lambda: print("Invalid input."))
    func()


def start_screen():  # ZIVEN, JOANNA
    player_name = input("What is your name? ")
    print(f"Dear {player_name}, your {choice(relative)} has recently unfortunately died.\n In the will, they left their remaining savings of $100000 to you. But there's a catch. They want you to become the housing market tycoon they never were.\n You are to use this money and your regular salary of $5000 to become a housing millionare.\n Learn how to follow the market, flip homes, and save money until you can afford to buy your dream property and retire in style.\n One last thing before you get started: watch your spending because if you go bankrupt, you lose.")
    start_dream_selection()


def start_dream_selection():  # ZIVEN
    print("The following are the selection of available dream homes:")
    loopcounter = 1
    for home in dream_properties:
        print(str(loopcounter) + ". " + home)
        loopcounter += 1
    try:
        prop = int(input(
            "Please enter the number of the dream home you would like to save up for. ")) - 1
        dream_property = dream_properties[prop]
    except:
        print("Invalid input.")
        start_dream_selection()
    print(f"Good choice! Who wouldn't want a {dream_property.lower()}?")
    print("The thing is, this is going to cost you $100000000. So you had better get to work! Enjoy the game.")


if __name__ == "__main__":
    print("Hello, this should work-")


def random_fact():  # EMILIE
    all_facts = ["Define wholesaling = buying a property from a seller while securing another buyer willing to buy the property at a higher price.", "Define real estate development = everything from the purchase of raw land to sale of developed land. Real estate developers scout land, manage renovation or construction, fund projects, and obtain permits and public approval.", "Define type 1 house flipping = Purchase property in a rapidly rising economy + sell after a period of time at a much higher price.", "Define type 2 house flipping = Purchase a property at low price that has potential to be renovated and sell it after renovations at a much higher price." ,"Historically, house flipping had created economic bubbles, such as in the Florida land boom of the 1920s and the real estate bubble in the 2000s caused by relaxed federal borrowing standards. ", "An effect of house flipping is gentrification, the controversial process of changing the character of a neighbourhood by an influx of affluent businesses and residents.", "Private Mortgage Insurange (PMI) costs 0.5 - 5 percent of the loan per month." ,"Loans for house flipping have higher intrest rates than the conventional home loan, at 12 - 14 percent vs. 4 percent.", "At an auction, you may not have the chance to inspect a property before paying down payment.", "Invest in a property only if it is in an area with employment growth, a good school system, and rising real estate sales.", "Avoid investing in an area with high crime rate or too many properties on sale.", "Invest in a property only if its price is below its market value.", "Define rubric for 'structurally sound' ≥ does not need (roof replacement U rewiring) U uninhabited by fungi", "Avoid investing in a property that is inaccessible from your primary residence.", "To estimate the cost of a renovation, add 20% to the final total.", "Do not over-value a home by investing too much in renovation. Instead, improve it 'just enough to make a healthy profit and keep it on par with what’s selling in the neighborhood'.", "Add heat insulation to the attic for $200.", "Install energy - efficient windows for $7500 - 10,000.", "Install a high efficiency water heater.", "Add swings to the attic.", "Define thermostat = a component which senses the temperature of a physical system and performs actions so that the system's temperature is maintained near a desired setpoint. Install a programmable thermostat.", "Add a bathroom.", "Remodel the basement for $640000.", "Always pair spiral stairs with a slide.", "For more information regarding the benefits of bryophytes on a rooftop, see ", r"Define the 70% Rule = Investors should pay no more than 70% of the after repair value (ARV) of a property minus the cost of the repairs needed. \n Follow the 70% rule.", "Define the Canadian Property Bubble = From 2003 to present, property prices in Canada have increased up to 337%.", "In response to the Canadian Property Bubble, a foreign buyer tax and speculation tax were levied.", r"In the Canadian Property Bubble, mortage consumed over 50% of an avergage family’s monthly budget.", r"Canada is heavily dependent on the real estate industry, accounting for around 12% of GDP."]
    # r-strings just escape the %'s - they were causing a couple of linting errors.
    if turn_num == 1:
        print("We wanted to share some housing market information with you, in the following categories: Definitions, Tips, Current market trends")  # throwing an incorrect linting error, but everything is fine!
    elif turn_num % 2 == 0:
        fact_choice = choice(all_facts)
        print(f"{fact_choice}")