properties = [["Dream mansion", 30000000], ["House to Flip", 1000000], ["Starter shack", 1000]]
turn_num = 1
player_balance = 100000 
# Ziven can create more property listings.

def turn_main():  # TOGETHER
    if turn_num == 1:
        start_screen()
        print("This is a turn, the main structure of the game. In a turn, you can modify, buy, and sell your properties.")
    turn_num += 1
    pass  # main turn function

def turn_next_turn():  # DEREK
    pass  # implement next turn, when all the background stuff happens (market changes, etc) and tells the user

def turn_modify():  # MIA
    pass  # implement modify current property, house flipping, renting out?

def turn_buy_new():  # EMILIE
    pass  # implement buying new property

def turn_sell():  # EMILIE
    pass  # implement selling property

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

def start_screen(): # ZIVEN, JOANNA
    print("Dear recipient of a 5,000 monthly salary, you have inherited a starter shack from ")  # continue beginning story here, inheritance, etc.

def start_dream_selection(): # ZIVEN
    print("Which property would you like to buy?")
    # print list
    prop = int(input())
    # map list to input, reference turn_parse_input on how to do this
    print(f"You have chosen {prop}.")

# Important -> Do NOT do any sketchy system32 deletion in the Powershell; this will directly affect Ziven's system. :) - Emilie
# Bugfixing, writing -> JOANNA