def turn_next_turn():
    pass  # implement next turn

def turn_modify():
    pass  # implement modify current property

def turn_buy_new():
    pass  # implement buying new property

def turn_sell():
    pass

def turn_parse_input(input):
    # maps input string to a function that will run. otherwise, print invalid input.
    map_in_to_func = {
        "next": turn_next_turn(),
        "modify": turn_modify(),
        "buy new": turn_buy_new(),
        "sell": turn_sell()
    }
    func = map_in_to_func.get(input, lambda: print("Invalid input"))
    func()


# Important -> Do NOT do any sketchy system32 deletion in the Powershell, as I believe this will directly affect Ziven's system. Don't kill his computer :) - Emilie