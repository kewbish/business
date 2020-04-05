from ast import literal_eval
from configparser import ConfigParser
from random import choice, randint, random, sample
from colorama import init, Fore, Style
import os.path as p

# Property list attributes:
# property name, property size on a scale of 1-5, does it have a building on it?, what type of building does it have on it? (may be blank), is it rented out?, rental rate (0 if not rented), property value, number of turns rent will be payed, everything after are different modifications that will impact the value of the house

tiny_house = ["Tiny house", 0, 25000, 0]

property_1 = ["Village Square", 1, True, tiny_house, False, 0, 125000, 0]
property_2 = ["Water Tower Row", 4, True, tiny_house, False, 0, 225000, 0]
property_3 = ["Mountainview Valley", 3, True, tiny_house, False, 0, 525000, 0]
property_4 = ["Tropical Paradise", 5, True, tiny_house, False, 0, 15025000, 0]
property_5 = ["Far Fields", 5, True, tiny_house, False, 0, 225000, 0]
property_6 = ["Urban Alleyway", 3, True, tiny_house, False, 0, 625000, 0]
property_7 = ["City Corner", 1, True, tiny_house, False, 0, 825000, 0]
property_8 = ["Main Street", 3, True, tiny_house, False, 0, 1025000, 0]
property_9 = ["Urban Waterfront", 2, True, tiny_house, False, 0, 2025000, 0]
property_10 = ["Suburban Sprawl", 4, True, tiny_house, False, 0, 1525000, 0]
property_11 = ["Desert Oasis", 5, True, tiny_house, False, 0, 325000, 0]
property_12 = ["Beach Boulevard", 2, True, tiny_house, False, 0, 2025000, 0]
property_13 = ["Sodden Swamp", 1, True, tiny_house, False, 0, 100000, 0]
property_14 = ["Fairway Greens", 3, True, tiny_house, False, 0, 775000, 0]
property_15 = ["Erst Isle", 5, True, tiny_house, False, 0, 10025000, 0]

owned_properties = []
unowned_properties = [property_1, property_2, property_3, property_4, property_5, property_6, property_7,
                      property_8, property_9, property_10, property_11, property_12, property_13, property_14, property_15]
all_properties = [property_1, property_2, property_3, property_4, property_5, property_6, property_7,
                  property_8, property_9, property_10, property_11, property_12, property_13, property_14, property_15]
# might want to make all_properties owned_properties + unowned_properties so prices can be affected by multipliers iirc
dream_properties = ["Mansion in the Swiss Alps", "Scandanavian Castle", "Condominium Building in Vancouver", "Mansion on a Hawaiian Beach",
                    "Private Island in the Caribbean", "Giant Residential Yacht", "Private Boeing 747", "Huge Texan Ranch", "AMS Student Nest"]
dream_property = ""
rent = 0
turn_num = 1
player_balance = 500000
naturaldisaster = 0
market_price = 1
market_list = [1.01, 1.01, 1.01, 0.99, 0.99, 0.99, 0.85, 1.15, 0.9, 1.1, 0.95, 1.05, 0.98, 1.02, 1.00, 1.00, 1.00, 1.00, 1.02, 1.02, 1.02, 0.98, 0.98, 0.98]  # list all the scenarios then lists the modifiers
disaster_list = ["Typhoon", "Tornado", "Flood", "Earthquake"]
disaster_result = [0.75, 0.8, 0.9, 0.65]
turn_stage = 0
relative = ["Great Aunt Hilda", "Uncle Gates", "Uncle Anderson", "Granny Smith", "Woompus"]
rent_rate_list = []

# structure: Has the player taken out a loan, what is the loan amount, what is the /turn payment, how many turns left are there for it to be repaid.
loan = [False, 0, 0, 0]

# structure: type of building, price, value added to property, value returned per turn
small_house = ["Small house", 100000, 200000, 0]
medium_house = ["Medium house", 300000, 500000, 0]
large_house = ["Large house", 400000, 750000, 0]
giant_house = ["Giant house", 750000, 1000000, 0]
farm = ["Farm", 750000, 750000, 100000]
hotel = ["Hotel", 2000000, 3000000, 125000]
casino_resort = ["Casino Resort", 5000000, 10000000, 750000]

build_choices = [small_house, medium_house, large_house, giant_house, farm, hotel, casino_resort]  # different things that can be on the property


class Game():
    def __init__(self):
        print(""" 
 /$$$$$$$            /$$                             /$$     /$$                       /$$$$$$$                       /$$$$$$ 
| $$__  $$          |__/                            | $$    | $$                      | $$__  $$                     /$$__  $$
| $$  \ $$  /$$$$$$  /$$  /$$$$$$$  /$$$$$$        /$$$$$$  | $$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$   /$$$$$$ | $$  \__/
| $$$$$$$/ |____  $$| $$ /$$_____/ /$$__  $$      |_  $$_/  | $$__  $$ /$$__  $$      | $$$$$$$/ /$$__  $$ /$$__  $$| $$$$    
| $$__  $$  /$$$$$$$| $$|  $$$$$$ | $$$$$$$$        | $$    | $$  \ $$| $$$$$$$$      | $$__  $$| $$  \ $$| $$  \ $$| $$_/    
| $$  \ $$ /$$__  $$| $$ \____  $$| $$_____/        | $$ /$$| $$  | $$| $$_____/      | $$  \ $$| $$  | $$| $$  | $$| $$      
| $$  | $$|  $$$$$$$| $$ /$$$$$$$/|  $$$$$$$        |  $$$$/| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$/|  $$$$$$/| $$      
|__/  |__/ \_______/|__/|_______/  \_______/         \___/  |__/  |__/ \_______/      |__/  |__/ \______/  \______/ |__/      \n""")
        print("Elevating your business knowledge - a game by Ziven, Derek, Mia, Emilie, and Joanna / Clen")
        self.clear_terminal()
        print("----------")
        self.clear_terminal()
        path = p.dirname(__file__)
        path = p.join(path, "config.game")
        if not p.isfile(path):
            with open(path, "w+") as x:
                x.write("""[Player Information]
PlayerBalance = 500000
TurnNum = 1
Rent = 0
DreamProperty =
Loan = [False, 0, 0, 0]

[Owned Properties]

[Unowned Properties]
property_1 = ["Village Square", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 125000, 0]
property_2 = ["Water Tower Row", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_3 = ["Mountainview Valley", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 525000, 0]
property_4 = ["Tropical Paradise", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 15025000, 0]
property_5 = ["Far Fields", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_6 = ["Urban Alleyway", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 625000, 0]
property_7 = ["City Corner", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 825000, 0]
property_8 = ["Main Street", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 1025000, 0]
property_9 = ["Urban Waterfront", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_10 = ["Suburban Sprawl", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 1525000, 0]
property_11 = ["Desert Oasis", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 325000, 0]
property_12 = ["Beach Boulevard", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_13 = ["Sodden Swamp", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 100000, 0]
property_14 = ["Fairway Greens", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 775000, 0]
property_15 = ["Erst Isle", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 10025000, 0]
                """)
        path = p.dirname(__file__)
        path = p.join(path, "basis_config.game")
        if not p.isfile(path):
            with open(path, "w+") as x:
                x.write("""[Player Information]
PlayerBalance = 500000
TurnNum = 1
Rent = 0
DreamProperty =
Loan = [False, 0, 0, 0]

[Owned Properties]

[Unowned Properties]
property_1 = ["Village Square", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 125000, 0]
property_2 = ["Water Tower Row", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_3 = ["Mountainview Valley", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 525000, 0]
property_4 = ["Tropical Paradise", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 15025000, 0]
property_5 = ["Far Fields", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_6 = ["Urban Alleyway", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 625000, 0]
property_7 = ["City Corner", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 825000, 0]
property_8 = ["Main Street", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 1025000, 0]
property_9 = ["Urban Waterfront", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_10 = ["Suburban Sprawl", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 1525000, 0]
property_11 = ["Desert Oasis", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 325000, 0]
property_12 = ["Beach Boulevard", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_13 = ["Sodden Swamp", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 100000, 0]
property_14 = ["Fairway Greens", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 775000, 0]
property_15 = ["Erst Isle", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 10025000, 0]
                """)
        init(convert=True)
        config = ConfigParser()
        y = input("Would you like to load a past save? y/n ")
        if "y" in y:
            path = p.dirname(__file__)
            path = p.join(path, "config.game")
        else:
            path = p.dirname(__file__)
            path = p.join(path, "basis_config.game")
        config.read(path)
        self.player_balance = int(
            config["Player Information"]["PlayerBalance"])
        self.turn_num = int(config["Player Information"]["TurnNum"])
        self.rent = int(config["Player Information"]["Rent"])
        dp = config["Player Information"]["DreamProperty"]
        if dp:
            self.dream_property = dp
        else:
            self.dream_property = ""
        del dp
        self.owned_properties = []
        self.unowned_properties = []
        for x in config.items("Owned Properties"):
            self.owned_properties.append(list(literal_eval(f'{x[1]}')))
            # literal_eval converts a string of lists of lists into a list of lists of lists
        for x in config.items("Unowned Properties"):
            self.unowned_properties.append(list(literal_eval(f'{x[1]}')))
            # literal_eval converts a string of lists of lists into a list of lists of lists
        self.loan = list(literal_eval(config["Player Information"]["Loan"]))

    def clear_terminal(self):  # ZIVEN
        # This is some strange code I found on Stack Overflow that seems to clear the terminal.
        # system('cls' if name == 'nt' else 'echo -e \\\\033c')
        print("")

    def start_screen(self):  # ZIVEN, JOANNA
        try:
            player_name = input("What is your name? ")
            if player_name.lower().strip() == "transitionite":
                self.clear_terminal()
                print(f"{Fore.CYAN}Haha - very funny. If you enjoy our game, please consider donating to the University Transition Program.\nHere's a link: https://support.ubc.ca/projects/university-transition-program/ {Style.RESET_ALL}")
            self.clear_terminal()
            print(f"Dear {player_name}, your {choice(relative)} has recently unfortunately died.\nIn the will, they left their remaining savings of $500000 to you. But there's a catch. They want you to become the housing market tycoon they never were.\nYou are to use this money and your regular salary of $10000 to become a housing millionare.\nLearn how to follow the market, flip homes, and save money until you can afford to buy your dream property and retire in style.\nOne last thing before you get started: watch your spending because if you fail to pay your taxes for three turns in a row, you lose.")
            self.clear_terminal()
            print("The following are the selection of available dream homes:")
            loopcounter = 1
            for home in dream_properties:
                print(str(loopcounter) + ": " + home)
                loopcounter += 1
            prop = int(input(
                "Please enter the number of the dream home you would like to save up for. ")) - 1
            self.clear_terminal()
            if prop >= 0 and prop <= 8:
                self.dream_property = dream_properties[prop]
                print(
                    f"Good choice! Who wouldn't want a {self.dream_property.lower()}?")
                print(
                    "The thing is, that's going to cost you $50000000. So you had better get to work! Enjoy the game.")
            else:
                print("Invalid input.")
                self.start_screen()
        except:
            print("Invalid input.")
            self.start_screen()

    def turn_main(self):  # ZIVEN
        global naturaldisaster
        
        if self.turn_num == 1:
            self.start_screen()
            self.clear_terminal()
            input("This is a turn, the main structure of the game. \nIn a turn, you can modify, buy, and sell your properties.\nBut beware; you can only do each thing once per turn, and you can only ever own ten properties. \nMany events also take place during the intervals between turns, including the payment of rent and delivery of your salary. \nYour goal is to earn $50000000 and cash out before the market crashes so you can buy your dream home and win the game!")
            self.random_fact()
            self.turn_next_turn()
            self.turn_choose()
        else:
            self.random_fact()
            self.turn_next_turn()
            self.turn_choose()
        naturaldisaster += 1

    def turn_choose(self):  # ZIVEN
        # This function can be used to navigate through the turn structure. It provides the structure calling the functions for each component of the turns.
        global turn_stage

        if turn_stage == 0 and self.loan[0] == False:
            self.clear_terminal()
            turn_choice = input("Would you like to take out a loan this turn? y/n ").lower()
            if "y" in turn_choice:
                self.turn_loan()

        elif turn_stage == 0 and (self.loan[2] * self.loan[3]) <= self.player_balance and self.loan[0] == True:
            self.clear_terminal()
            turn_choice = input("Would you like to prepay the remainder of your loan payments this turn? This will free you of your remaining debt. y/n ").lower()
            if "y" in turn_choice:
                self.turn_prepay()

        turn_stage += 1
        if len(self.owned_properties) > 0:
            if turn_stage == 1:
                self.clear_terminal()
                turn_choice = input(
                    "Would you like to modify an existing property this turn? y/n ").lower()
                if "y" in turn_choice:
                    self.turn_modify()
                turn_stage += 1

            if turn_stage == 2:
                self.clear_terminal()
                turn_choice = input(
                    "Would you like to sell an existing property this turn? y/n ").lower()
                if "y" in turn_choice:
                    self.turn_sell()
                turn_stage += 1

        if len(self.owned_properties) == 0:
            turn_stage = 3
        if turn_stage == 3 and len(self.owned_properties) <= 10:
            self.clear_terminal()
            turn_choice = input(
                "Would you like to buy a new property this turn? y/n ").lower()
            if "y" in turn_choice:
                self.turn_buy()
        turn_stage = 0
        self.turn_num += 1

        self.clear_terminal()
        y = input("Would you like to save your progress? y/n ")
        if "y" in y:
            self.save()
        self.turn_main()

    def turn_next_turn(self):  # DEREK, ZIVEN
        global market_price
        global naturaldisaster
        global player_balance
        modifier = 1
        self.player_balance += 10000
        naturaldisaster += 1
        # Display the turn number.
        self.clear_terminal()
        print(
            f"{Style.BRIGHT}{Fore.CYAN}Turn number: {str(self.turn_num)}{Style.RESET_ALL}")
        if self.turn_num > 1:  # Market does not need to change on first turn because nothing is owned yet. # Here, the market is varied in the variable modifier which comes from market_list.
            placeholder = randint(0, len(market_list) - 1)
            modifier = market_list[placeholder]
            market_price *= modifier
            if modifier > 1:
                print(
                    f"{Fore.GREEN}The housing market went up {round((modifier - 1) * 100)} percent. {Style.RESET_ALL}")
            elif modifier < 1:
                print(
                    f"{Style.BRIGHT}{Fore.RED}The housing market went down {round((1 - modifier) * 100)} percent.{Style.RESET_ALL}")
            else:
                print("The housing market did not change.")
            # random number to choose which disaster happens.
            n = randint(0, 4)
            chance = random()
            # gradually increases the chance of natural disastors, try to have it happen once every 100 turns
            if (chance < naturaldisaster * 0.002):
                # ! TypeError: list indices must be integers or slices, not tuple
                market_price = disaster_result[abs(n - 1)] * market_price
                print("Oh no! A " + (disaster_list[n-1].lower()) + " occurred, and the market went down " + str(
                    round((1 - disaster_result[n-1]) * 100)) + " percent")
                naturaldisaster = 0  # after a disastor happens, reset the chance for disaster to occur
        print(f"{Fore.GREEN}You earned 10000 dollars from your salary.{Style.RESET_ALL}")

        rent = 0
        # The total rent owed to the player is determined.
        for home in self.owned_properties:
            if home[7] > 0:
                rent += home[5]
                home[7] -= 1
            elif home[7] == 0:
                home[5] = 0
                home[4] = False
                print(
                    f"{Fore.YELLOW}You are not renting {home[0]}.{Style.RESET_ALL}")
        if rent > 0:  # If there is any rent from this process, it is paid.
            self.player_balance += rent
            # Player is given information about their financial status.
            print(f"{Fore.GREEN}You earned {rent} dollars in rent.{Style.RESET_ALL}")

        propPay = 0
        for home in self.owned_properties:
            if home[3] != "" and int(home[3][3]) != 0:
                propPay += home[3][3]
        if propPay > 0:   # If there is any payment from properties, it is paid.
            self.player_balance += propPay
            print(f"{Fore.GREEN}Your buildings have earned you {str(propPay)} dollars.{Style.RESET_ALL}")

        propTax = 0
        propValue = 0
        for home in self.owned_properties:
            propValue += home[6]
        propTax = propValue * 0.001
        self.player_balance -= propTax
        if propTax > 0:
            print(f"{Style.BRIGHT}{Fore.RED}You paid {round(propTax, 2)} dollars in property tax.{Style.RESET_ALL}")

        if self.loan[0] == True:
            self.player_balance -= self.loan[2]
            print(
                f"{Style.BRIGHT}{Fore.RED}You paid {int(round(self.loan[2]))} dollars for your loan payment.{Style.RESET_ALL}")
            self.loan[3] -= 1
            print(f"You have {self.loan[3]} loan payments remaining.")
            if self.loan[3] <= 0:
                self.loan[0] = False
                self.loan[1] = 0
                self.loan[2] = 0

        if self.player_balance >= 0:
            print(
                f"{Fore.YELLOW}Your balance is now {int(self.player_balance)} dollars.{Style.RESET_ALL}")
            # print("That means you are " + str(round(((player_balance/50000000)*100), 3)) + " percent of the way to being able to afford your dream home!")
            print(
                f"That means you are {round(((self.player_balance/50000000)*100), 3)} percent of the way to being able to afford your dream home!")
            # The price of all of the properties will be changed based on the market variation.
            for home in self.unowned_properties:
                home[6] = int(round(home[6]*modifier))
            for home in self.owned_properties:
                home[6] = int(round(home[6]*modifier))
            # If the player owns any properties, they will be printed with their new, market-based prices.
            if len(self.owned_properties) > 0:
                self.clear_terminal()
                print("The properties you currently own and their values: ")
                self.print_properties(self.owned_properties)

        else:
            print(f"{Style.BRIGHT}{Fore.RED}You have been irresponsible with your spending and gone bankrupt. You lose the game.{Style.RESET_ALL}")
            path = p.dirname(__file__)
            path = p.join(path, "config.game")
            with open(path, "w+") as x:
                x.write("""[Player Information]
PlayerBalance = 500000
TurnNum = 1
Rent = 0
DreamProperty =
Loan = [False, 0, 0, 0]

[Owned Properties]

[Unowned Properties]
property_1 = ["Village Square", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 125000, 0]
property_2 = ["Water Tower Row", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_3 = ["Mountainview Valley", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 525000, 0]
property_4 = ["Tropical Paradise", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 15025000, 0]
property_5 = ["Far Fields", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_6 = ["Urban Alleyway", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 625000, 0]
property_7 = ["City Corner", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 825000, 0]
property_8 = ["Main Street", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 1025000, 0]
property_9 = ["Urban Waterfront", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_10 = ["Suburban Sprawl", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 1525000, 0]
property_11 = ["Desert Oasis", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 325000, 0]
property_12 = ["Beach Boulevard", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_13 = ["Sodden Swamp", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 100000, 0]
property_14 = ["Fairway Greens", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 775000, 0]
property_15 = ["Erst Isle", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 10025000, 0]
                """)
            exit(0)
        if self.player_balance >= 50000000 and self.loan[0] == False:
            self.clear_terminal()
            path = p.dirname(__file__)
            path = p.join(path, "config.game")
            with open(path, "w+") as x:
                x.write("""[Player Information]
PlayerBalance = 500000
TurnNum = 1
Rent = 0
DreamProperty =
Loan = [False, 0, 0, 0]

[Owned Properties]

[Unowned Properties]
property_1 = ["Village Square", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 125000, 0]
property_2 = ["Water Tower Row", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_3 = ["Mountainview Valley", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 525000, 0]
property_4 = ["Tropical Paradise", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 15025000, 0]
property_5 = ["Far Fields", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 225000, 0]
property_6 = ["Urban Alleyway", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 625000, 0]
property_7 = ["City Corner", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 825000, 0]
property_8 = ["Main Street", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 1025000, 0]
property_9 = ["Urban Waterfront", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_10 = ["Suburban Sprawl", 4, True, ["Tiny house", 0, 25000, 0], False, 0, 1525000, 0]
property_11 = ["Desert Oasis", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 325000, 0]
property_12 = ["Beach Boulevard", 2, True, ["Tiny house", 0, 25000, 0], False, 0, 2025000, 0]
property_13 = ["Sodden Swamp", 1, True, ["Tiny house", 0, 25000, 0], False, 0, 100000, 0]
property_14 = ["Fairway Greens", 3, True, ["Tiny house", 0, 25000, 0], False, 0, 775000, 0]
property_15 = ["Erst Isle", 5, True, ["Tiny house", 0, 25000, 0], False, 0, 10025000, 0]
                """)
            print(f"{Fore.GREEN}Congratulations! You have successfully become a housing millionare and earned enough to retire in style by buying a {self.dream_property.lower()}. You've just won the game in {str(self.turn_num)} turns!{Style.RESET_ALL}")
            y = input(
                "You can now buy your dream home. Would you like to continue? y/n ").lower()
            if "y" in y:
                print(f"{self.dream_property} bought. Again, congrats!\n")
            else:
                print(
                    "Well, that's too bad - your agent has already bought it! Congrats!\n")
            print(f"{Fore.CYAN}We hope you've learned about the real estate market, and had fun playing!\n- Ziven, Derek, Mia, Emilie & Joanna / Clen{Style.RESET_ALL}")
            self.clear_terminal()
            print(f"{Fore.YELLOW}Save file reset.{Style.RESET_ALL}")
            exit(0)
    def turn_loan(self):  # ZIVEN, MIA
        self.clear_terminal()
        amount_choices = {"1": r"$100000", "2": r"$500000", "3": r"$1000000", "4": r"$10000000"}
        self.print_properties_dictionary(amount_choices)
        try:
            selection = amount_choices.get(input("What amount would you like to borrow? "))
        except:
            y = input("Invalid input. Would you like to exit? ")
            if "y" in y:
                return
            self.turn_loan()

        self.clear_terminal()
        rate_and_term_choices = {"1": r"5% interest over 10 turns", "2": r"12% interest over 20 turns", "3": r"13% interest over 25 turns", "4": r"14% interest over 30 turns", "5": r"25% interest over 50 turns"}
        self.print_properties_dictionary(rate_and_term_choices)
        try:
            rselection = rate_and_term_choices.get(
                input("Which interest rate and duration would you like? "))
        except:
            y = input("Invalid input. Would you like to exit? ")
            if "y" in y:
                return
            self.turn_loan()
        self.clear_terminal()
        y = input("Are you sure you want to take out this loan?\nRemember, you will need to make payments each turn and you will lose the game if you default. \nYou cannot win the game until you pay off all your loans. y/n ").lower()
        if "y" in y:
            if selection == r"$100000":
                self.loan[1] = 100000
            elif selection == r"$500000":
                self.loan[1] = 500000
            elif selection == r"$1000000":
                self.loan[1] = 1000000
            elif selection == r"$10000000":
                self.loan[1] = 10000000
            self.loan[0] = True
            self.player_balance += self.loan[1]
            loan_amount = self.loan[1]
            if rselection == r"5% interest over 10 turns":
                # We'll just do simple interest to keep it simple. Simple interest to keep it simple, gotcha. yep
                self.loan[1] *= 1.05
                self.loan[3] = 10
                self.loan[2] = self.loan[1]/self.loan[3]
            elif rselection == r"12% interest over 20 turns":
                self.loan[1] *= 1.12
                self.loan[3] = 20
                self.loan[2] = self.loan[1]/self.loan[3]
            elif rselection == r"13% interest over 25 turns":
                self.loan[1] *= 1.13
                self.loan[3] = 25
                self.loan[2] = self.loan[1]/self.loan[3]
            elif rselection == r"14% interest over 30 turns":
                self.loan[1] *= 1.14
                self.loan[3] = 30
                self.loan[2] = self.loan[1]/self.loan[3]
            elif rselection == r"25% interest over 50 turns":
                self.loan[1] *= 1.25
                self.loan[3] = 50
                self.loan[2] = self.loan[1]/self.loan[3]

            self.clear_terminal()
            input(f"You have successfully taken a loan of {loan_amount} dollars. You will be making payments of {self.loan[2]} dollars for the next {self.loan[3]} turns.")
        else:
            return
    # structure: Has the player taken out a loan, what is the loan amount, what is the /turn payment, how many turns left are there for it to be repaid.
    def turn_prepay(self):  # ZIVEN

        try:
            print(f"Your balance is currently {self.player_balance} dollars. The total value of your remaining loan payments is {self.loan[2]*self.loan[3]} dollars.")
            y = input(f"Would you like to pay {self.loan[2]*self.loan[3]} dollars to end your loan now? y/n ").lower()
            if "y" in y:
                y = input(f"Are you sure? (Your balance is ${self.player_balance}.) y/n ")
                if "y" in y:
                    self.player_balance -= (self.loan[2]*self.loan[3])
                    self.loan[0] = False
                    self.loan[1] = 0
                    self.loan[2] = 0
                    self.loan[3] = 0

                    input("Success! You have paid off your loan, and you are now debt free!")
        except:  # if input does not match, break
            y = input("Invalid input. Would you like to exit?")
            if "y" in y:
                return
            self.turn_prepay()

    def turn_modify(self):  # MIA
        self.clear_terminal()
        for i, x in enumerate(self.owned_properties):
            if x[3] != "" and x[4] == False:
                print(f"{i + 1}: {x[0]} - {x[3][0]} - ${x[6]} total value")
            elif x[3] != "" and x[4] == True:
                print(
                    f"{i + 1}: {x[0]} - {x[3][0]} - ${x[6]} total value - ${x[5]} rent per turn for {x[7]} more turns.")
            else:
                print(f"{i + 1}: {x[0]} - ${x[6]} total value")
                
        try:  # gets input from user as to what to do next
            prop = self.owned_properties[int(input("Which property would you like to work on? ")) - 1]
        except:  # if input does not match, break
            y = input("Invalid input. Would you like to exit?")
            if "y" in y:
                return
            self.turn_modify()
        # general choices, links to the next
        main_choices = {"1": "Build", "2": "Demolish", "3": "Remodel", "4": "Rent"}

        self.clear_terminal()
        try:  # gets input from user as to what to do next
            self.print_properties_dictionary(main_choices)
            selection = main_choices.get(input("What would you like to do? "))
        except:  # if input does not match
            print("Invalid input.")
            self.turn_modify()

        if selection == "Remodel":
            self.turn_remodel(prop)
        elif selection == "Rent":
            self.turn_rent(prop)
        elif selection == "Build":
            self.turn_build(prop)
        elif selection == "Demolish":
            self.turn_demolish()

    def turn_build(self, prop):  # MIA, EMILIE, ZIVEN   Helper function of turn_modify
        self.clear_terminal()
        for i, x in enumerate(build_choices):
            print(
                f"{i + 1}: A {x[0].lower()} costs {x[1]} dollars, will add {x[2]} dollars to the property value, and will pay {x[3]} dollars per turn.")

        try:  # gets input from user as to what to do next
            # not case sensitive
            selection = int(input("What would you like to build? "))
            index = selection - 1
            y = input(f"Are you sure you'd like to build a {build_choices[index][0].lower()}? (Your balance is ${int(self.player_balance)}.) y/n ").lower()
            if prop[2] == False and build_choices[index][1] <= self.player_balance and "y" in y:
                prop[2] = True
                prop[3] = build_choices[index]
                prop[6] += build_choices[index][2]
                self.clear_terminal()
                print(f"You have successfully built a {build_choices[index][0].lower()} on {prop[0]}. Your balance is now {self.player_balance} dollars.")
                input(f"The property value is now {int(prop[6])} dollars.")
            elif prop[2] == True:
                self.clear_terminal()
                input("There's already a building on this property. You will need to demolish it before building something else.")

                self.turn_modify()
            elif build_choices[index][1] > self.player_balance:
                print("You don't have enough money to build this. Save up - another day!")
                self.turn_modify()
            elif y != "y":
                return
        except:  # if input does not match, restart function
            y = input("Invalid input. Would you like to exit? y/n")
            if "y" in y:
                return
            else:
                self.turn_build(prop)

    # I am aware that this function essentially asks them what they want to work on after they have already specified it in turn_modify, but I don't know of a better way to do it. - Ziven # I think that's alright - Emilie
    def turn_demolish(self):  # ZIVEN, EMILIE
        props_with_buildings = []
        for prop in self.owned_properties:
            if prop[2] == True:
                props_with_buildings.append(prop)
        if len(props_with_buildings) > 0:
            self.clear_terminal()
            for i, x in enumerate(props_with_buildings):
                print(f"{str(i + 1)}: {x[0]} - {x[3][0]}")
            try:
                selection = int(input("What would you like to demolish? "))
                index = self.owned_properties.index(
                    props_with_buildings[selection - 1])
                self.clear_terminal()
                y = input(f"You are about to demolish the {self.owned_properties[index][3][0].lower()} on {self.owned_properties[index][0]}. Are you sure? (Your balance is ${self.player_balance}.) Demolition will cost 10000 dollars. y/n ")
                if "y" in y and self.player_balance >= 10000:
                    self.player_balance -= 10000  # Deducts cost
                    # Subtracts building value from property
                    self.owned_properties[index][6] -= self.owned_properties[index][3][2]
                    # Ensures value is never less than zero (say if you took a casino resort off of sodden swamp.)
                    if self.owned_properties[index][6] < 0:
                        self.owned_properties[index][6] = 0
                    # Sets building existence to false
                    self.owned_properties[index][2] = False
                    # Removes all modifications made to the property.
                    for item in self.owned_properties[index]:
                        if self.owned_properties[index].index(item) > 7:
                            del item
                    self.owned_properties[index][3] = ""  # Removes building
                    # Eliminates all rent from property.
                    self.owned_properties[index][4] = False
                    self.owned_properties[index][5] = 0
                    self.owned_properties[index][7] = 0
                    self.clear_terminal()
                    print(f"Demolition complete. Your balance is now {int(self.player_balance)} dollars.")
                    input(f"The property value is now {self.owned_properties[index][6]} dollars.")

                elif self.player_balance < 10000:
                    self.clear_terminal()
                    input("You don't have enough money to demolish this. Save up for another day!")

            except:
                y = input("Invalid input. Would you like to exit? y/n ").lower()
                if "y" in y:
                    return

                self.turn_demolish()
        else:
            print("You have not built anything on any of your properties.")
            input("You must first construct something in order to demolish it.")

    # Perhaps, instead of adding a set value upon completing certain renovations, the property value should be changed by a certain percentage. Because on some properties, a few thousand bucks means nothing. The same would apply to the cost of the renovation. - Ziven

    def turn_remodel(self, prop):  # MIA   Helper function of turn_modify
        if prop[2] == True:
            self.clear_terminal()
            print("Remodeling a part of your property will increase its value, but be careful! Remodels cost a lot of money.")
            # A dictionary with different choices for house flipping/improvements as well as costs

            remodel_choices = {"1": ["Repaint", "10000"], "2": ["New floor", "15000"], "3": ["New roof", "20000"], "4": ["New windows", "20000"], "5": ["New garden", "30000"]}

            for key, value in remodel_choices.items():
                print(str(key) + ': ' + str(value[0]) + ' - ' + str(value[1]))

            try:  # gets input from user as to what to do next
                selection = remodel_choices.get(input("What would you like to do? "))
            except:  # if input does not match, restart function
                print("Invalid input.")
                self.turn_remodel(prop)

            cost = selection[1]

            if self.player_balance >= 10000 and selection not in prop:
                try:
                    ans = input(f"Are you sure? Your balance is ${self.player_balance}. y/n ").lower()
                    if ans == "y":
                        self.clear_terminal()
                        print("Modification made! What a wonderful addition to the property!")
                        # appends modification to end of property list
                        prop.append(selection[0])
                        # removes the cost of the renovation
                        self.player_balance -= int(cost)
                        # increases the value of the property
                        prop[6] += int(cost)*3
                        self.clear_terminal()
                        input(f"Your balance is now {self.player_balance} dollars and the property value is {prop[6]} dollars.")

                except:
                    print("Invalid input.")
                    self.turn_remodel(prop)
            elif self.player_balance < 10000:
                input("You don't have enough money for that!")

            elif selection in prop:
                input("This property already has that modification!")
        else:
            input("You do not have a building on this property to modify.")
            self.turn_modify()

    # MIA   Helper function of turn_modify, generates three different rent options
    def turn_rent(self, prop):
        global rent_rate_list
        global rate
        global duration
        rate = 0
        duration = 0
        x = 1
        # checks if it is rented
        if prop[4] == True:
            input("You've already rented this property out. Please wait for the rental period to expire before re-renting.")
            #
            self.turn_modify()
        if prop[2] == False:
            input("You don't have a building on this property. Build something on it to rent it out!")
            self.turn_modify()

        rent_rate_list = []
        rent_choices_list = []  # A list to hold all the possibilities
        for i in range(3):
            # tiny house, small house, medium house, large house, giant house, farm, hotel, casino resort
            rent_choices_list.append(self.rentGen(prop))
            del i

        if prop[3][0] == "Small house":
            x = 1.5
        elif prop[3][0] == "Medium house":
            x = 2
        elif prop[3][0] == "Large house" or prop[3][0] == "Farm":
            x = 3
        elif prop[3][0] == "Giant house" or prop[3][0] == "Hotel":
            x = 4
        elif prop[3][0] == "Casino Resort":
            x = 5

        rent_choices_list[0][0] *= x
        rent_choices_list[1][2] *= x
        rent_choices_list[2][4] *= x

        rent_choices = {   # A dictionary to help with input
            "1": f"{rent_choices_list[0][0]} dollars/turn for {rent_choices_list[0][1]} turns",
            "2": f"{rent_choices_list[1][2]} dollars/turn for {rent_choices_list[1][3]} turns",
            "3": f"{rent_choices_list[2][4]} dollars/turn for {rent_choices_list[2][5]} turns"
        }

        self.clear_terminal()
        self.print_properties_dictionary(rent_choices)  # Prints rent_choices
        selection = input("Which rental rate would you like? ")

        if "1" in selection:
            rate = rent_choices_list[0][0]
            duration = rent_choices_list[0][1]
        elif "2" in selection:
            rate = rent_choices_list[1][2]
            duration = rent_choices_list[1][3]
        elif "3" in selection:
            rate = rent_choices_list[2][4]
            duration = rent_choices_list[2][5]
        else:
            print("Invalid input.")
            self.turn_rent(prop)

        # modifies the property list, communicates with the player
        prop[4] = True
        prop[5] = int(rate)
        prop[7] = int(duration)
        self.clear_terminal()
        input(f"Great! Now you will be receiving an income of {rate} from this property for the next {duration} turns.")

    def rentGen(self, prop):  # MIA   Helper function of rent, creates random rental rate based on property value
        global rent_rate_list
        rent_rate = int(prop[6] / (randint(50, 100)))
        rent_rate_list.append(rent_rate)
        rent_duration = randint(10, 20)
        rent_rate_list.append(rent_duration)
        return rent_rate_list

    def print_properties(self, list_to_print):
        for i, x in enumerate(list_to_print):
            print(f"{i + 1}: {str(x[0])} - ${int(x[6])}")

    def print_properties_dictionary(self, dictionary_to_print):
        for key, value in dictionary_to_print.items():
            # I believe the ,'s would indicate a list and would come out with funny formatting - Emilie
            print(str(key) + ': ' + str(value))

    def turn_buy(self):  # EMILIE
        # enumerates over properties; i will be the number, x the property name / description / first el. in array
        # prints a list of property names
        try:
            self.clear_terminal()
            self.print_properties(self.unowned_properties)
            num_to_buy = int(input("Which property would you like to buy? "))
            # ! invalid literal for int() with base 10: '', problem if no input is given
            if num_to_buy >= 0 and num_to_buy <= 15:
                y = input(f"Are you sure? Your balance is ${int(self.player_balance)} y/n ")
                if "y" in y:
                    if self.player_balance >= self.unowned_properties[num_to_buy - 1][6]:
                        # subtracts money from player_balance
                        self.player_balance -= self.unowned_properties[num_to_buy - 1][6]
                        # adds property to other list
                        self.owned_properties.append(
                            self.unowned_properties[num_to_buy - 1])
                        # removes from unowned list
                        del self.unowned_properties[num_to_buy - 1]
                        self.clear_terminal()
                        input(f"Property bought. Your balance is now {round(self.player_balance)} dollars.")
                    else:
                        print("You don't have enough money for that. Save up - maybe one day!")
                        self.clear_terminal()
                        y = input("Would you like to exit?").lower()
                        if not y == "y":
                            self.turn_buy()
        except:
            print("Invalid input.")
            self.turn_buy()

    def turn_sell(self):  # EMILIE
        try:
            self.clear_terminal()
            self.print_properties(self.owned_properties)
            num_to_sell = int(input("Which property would you like to sell? "))
            if num_to_sell >= 0 and num_to_sell <= len(self.owned_properties):
                y = input(
                    f"Are you sure? Your balance is ${int(self.player_balance)} y/n ").lower()
                if "y" in y:
                    self.player_balance += (
                        self.owned_properties[num_to_sell - 1][6])
                    self.owned_properties[num_to_sell - 1][5] = 0
                    self.owned_properties[num_to_sell - 1][7] = 0
                    self.unowned_properties.append(
                        self.owned_properties[num_to_sell - 1])
                    del self.owned_properties[num_to_sell - 1]
                    self.clear_terminal()
                    input(f"Property sold. Your balance is now {int(self.player_balance)} dollars.")
               
        except:
            print("Invalid input.")
            self.turn_sell()

    def random_fact(self):  # EMILIE
        all_facts = ["Define wholesaling = buying a property from a seller while securing another buyer willing to buy the property at a higher price.", "Define real estate development = everything from the purchase of raw land to sale of developed land. Real estate developers scout land, manage renovation or construction, fund projects, and obtain permits and public approval.", "Define type 1 house flipping = Purchase property in a rapidly rising economy + sell after a period of time at a much higher price.", "Define type 2 house flipping = Purchase a property at low price that has potential to be renovated and sell it after renovations at a much higher price.", "Historically, house flipping has created economic bubbles, such as in the Florida land boom of the 1920s and the real estate bubble in the 2000s caused by relaxed federal borrowing standards. ", "An effect of house flipping is gentrification, the controversial process of changing tha character of a neighbourhood by an influl of affluent businesses and residents.", "Private Mortgage Insurange (PMI) costs 0.5 - 5 perlent of the loan per month.", "Loans for house flipping have higher intresa rates than the conventional home loan, at 12 - 14 percent vs. 4 percent.", "At an auction, you may not have the chance to inspect a property before placing the down payment.", "Invest in a property only if it is in an area with employment growth, a good school system, and rising real estate sales.", "Avoid investing in an area with high crime rate or too many properties on sale.", "Invest in a property only if its price is below its market value.", "Define rubric for 'structurally sound' ≥ does not need (roof replacement U rewiring) U uninhabited by fungi", "Avoid investing in a property that is inaccessible from your primary residence.", "To estimate the cost of a renovation, add 20% to the final total.", "Do not over-value a home by investing too much in renovation. Instead, improve it 'just enough to make a healthy profit and keep it on par with what’s selling in the neighborhood'.", "Define mill = unit of property tax rate. 1 mill = 0.1%. \n + 'mill levy' = 'property tax'", "Tax rates are calculated separately for each tax jurisdiction, like school district, city, and country. \n The property tax (mill levy) is determined by adding all the levies", "Property values are assessed every 1 - 5 years.", "Add swings to the attic.", "Define thermostat = a component which senses the temperature of a physical system and performs actions so that the system's temperature is maintained near a desired setpoint. Install a programmable thermostat.", "Define Property value evaluation type 1 of 3 = Sales evaluation. \n Criteria : Comparable sales in the area, Location, Condition of the property, Market", "Define Property value evaluation type 2 of 3 = Cost. (for developed properties) \n Criteria : Cost to replace the building, deducting depreciation", "Always pair spiral stairs with a slide.", "Define Property value evaluation type 3 of 3 = Income. (for owners renting out properties)\n Criteria : Income from rent, deducting maintenance/management costs and taxes.", r"Define the 70% Rule = Investors should pay no more than 70 percent of the after repair value (ARV) of a property minus the cost of the repairs needed when house flipping.", r"Define the Canadian Property Bubble = From 2003 to present, property prices in Canada have increased up to 337%.", "In response to the Canadian Property Bubble, a foreign buyer tax and speculation tax were levied.", r"In the Canadian Property Bubble, mortgage consumed over 50% of an average family’s monthly budget.", r"Canada is heavily dependent on the real estate industry, which accounts for around 12 percent of its GDP.", "Define wholesaling = buying a property from a seller while securing another buyer willing to buy the property at a higher price.", "Define real estate development = everything from the purchase of raw land to sale of developed land. Real estate developers scout land, manage renovation or construction, fund projects, and obtain permits and public approval.", "Define type 1 house flipping = Purchase property in a rapidly rising economy + sell after a period of time at a much higher price.", "Define type 2 house flipping = Purchase a property at low price that has potential to be renovated and sell it after renovations at a much higher price.", "Historically, house flipping has created economic bubbles, such as in the Florida land boom of the 1920s and the real estate bubble in the 2000s caused by relaxed federal borrowing standards. ", "An effect of house flipping is gentrification, the controversial process of changing the character of a neighbourhood by an influx of affluent businesses and residents.", "Private Mortgage Insurange (PMI) costs 0.5 - 5 percent of the loan per month.", "Loans for house flipping have higher intrest rates than the conventional home loan, at 12 - 14 percent vs. 4 percent.", "At an auction, you may not have the chance to inspect a property before placing the down payment.", "Invest in a property only if it is in an area with employment growth, a good school system, and rising real estate sales.", "Avoid investing in an area with high crime rate or too many properties on sale.", "Invest in a property only if its price is below its market value.", "Define rubric for 'structurally sound' ≥ does not need (roof replacement U rewiring) U uninhabited by fungi", "Avoid investing in a property that is inaccessible from your primary residence.", "To estimate the cost of a renovation, add 20% to the final total.", "Do not over-value a home by investing too much in renovation. Instead, improve it 'just enough to make a healthy profit and keep it on par with what’s selling in the neighborhood'.", "Define mill = unit of property tax rate. 1 mill = 0.1%. \n + 'mill levy' = 'property tax'", "Tax rates are calculated separately for each tax jurisdiction, like school district, city, and country. The property tax (mill levy) is determined by adding all the levies", "Property values are assessed every 1 - 5 years.", "Add swings to the attic.", "Define thermostat = a component which senses the temperature of a physical system and performs actions so that the system's temperature is maintained near a desired setpoint. Install a programmable thermostat.", "Define Property value evaluation type 1 of 3 = Sales evaluation. \n Criteria : Comparable sales in the area, Location, Condition of the property, Market", "Define Property value evaluation type 2 of 3 = Cost. (for developed properties) \n Criteria : Cost to replace the building, deducting depreciation", "Always pair spiral stairs with a slide.", "Define Property value evaluation type 3 of 3 = Income. (for owners renting out properties)/n Criteria : Income from rent, deducting maintenance/management costs and taxes.", r"Define the 70% Rule = Investors should pay no more than 70 percent of the after repair value (ARV) of a property minus the cost of the repairs needed when house flipping.", r"Define the Canadian Property Bubble = From 2003 to present, property prices in Canada have increased up to 337%.", "In response to the Canadian Property Bubble, a foreign buyer tax and speculation tax were levied.", r"In the Canadian Property Bubble, mortgage consumed over 50% of an average family’s monthly budget.", "Canada is heavily dependent on the real estate industry, which accounts for around 12 percent of its GDP."]

        if self.turn_num == 1:
            self.clear_terminal()
            print(f"{Fore.YELLOW}We wanted to share some housing market information with you.{Style.RESET_ALL}")
        if self.turn_num <= 31:
            self.clear_terminal()
            fact_choice = sample(all_facts, 1)[0]
            input(f"Housing fact: {fact_choice}")
        else:
            self.clear_terminal()
            fact_repeat = choice(all_facts)
            input(f"Housing fact: {fact_repeat}")

    def save(self):
        config = ConfigParser()
        config.add_section("Player Information")
        config["Player Information"]["PlayerBalance"] = str(
            int(self.player_balance))
        config["Player Information"]["TurnNum"] = str(self.turn_num)
        config["Player Information"]["Rent"] = str(int(self.rent))
        config["Player Information"]["DreamProperty"] = str(
            self.dream_property)
        config["Player Information"]["Loan"] = str(self.loan)
        config.add_section("Owned Properties")
        for i, x in enumerate(self.owned_properties):
            config["Owned Properties"][f"property{i}"] = str(
                x).replace("(", "").replace(")", "")
        config.add_section("Unowned Properties")
        for i, x in enumerate(self.unowned_properties):
            config["Unowned Properties"][f"property{i}"] = str(
                x).replace("(", "").replace(")", "")
        path = p.dirname(__file__)
        path = p.join(path, "config.game")
        with open(path, "w") as x:
            config.write(x)

if __name__ == "__main__":
    game = Game()
    while True:
        game.turn_main()
