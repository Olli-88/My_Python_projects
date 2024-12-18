from collections import defaultdict
from random import sample

# With this program you can simulate
# how many rounds it takes to get the jackpot on Eurojackpot
# and how many other prizes you won in that time.

compare_result = ""

hits = defaultdict(int)

my_main_nos = set()
my_supp_nos = set()

rounds = 0
round_info = 0

TIERS = {"52": "Tier1", "51": "Tier2", "50": "Tier3", "42": "Tier4", "41": "Tier5", "40": "Tier6", "32": "Tier7", "31": "Tier8", "22": "Tier9", "30": "Tier10", "12": "Tier11", "21": "Tier12", "20": "No win", "11": "No win", "10": "No win", "02": "No win", "01": "No win", "00": "No win"}  

def ask_my_main_nos() -> set[int]:
    while len(my_main_nos) < 5:
        try:
            my_main_no = int(input(f"Give {len(my_main_nos)+1}. main number between 1 - 50: "))
            if my_main_no < 1 or my_main_no > 50:
                print(f"Number {my_main_no} is not between 1 - 50!")
            elif my_main_no in my_main_nos:
                print(f"Number {my_main_no} has been used already!")
            else: 
                my_main_nos.add(my_main_no)
        except ValueError:
            print("Error! Given number is not an integer.")
    return my_main_nos

def ask_my_supp_nos() -> set[int]:  
    while len(my_supp_nos) < 2:
        try:
            my_supp_no = int(input(f"Give {len(my_supp_nos)+1}. Euro number between 1 - 12: "))
            if my_supp_no < 1 or my_supp_no > 12:
                print(f"Number {my_supp_no} is not between 1 - 12!")
            elif my_supp_no in my_supp_nos:
                print(f"Number {my_supp_no} has been used already!")
            else: 
                my_supp_nos.add(my_supp_no)
        except ValueError:
            print("Error! Given number is not an integer.")
    return my_supp_nos

def lottery_draw() -> set[int]:
    main_nos = set(sample(range(1,51),5))
    supp_nos = set(sample(range(1,13),2))
    return main_nos, supp_nos

def count_hits(my_main_nos, my_supp_nos, main_nos, supp_nos) -> None:
    compare_result = str(len(my_main_nos&main_nos))+str(len(my_supp_nos&supp_nos))
    hits[compare_result] += 1  

def rounds_to_jacpot(rounds, round_info) -> None:
    while "52" not in hits:
        main_nos, supp_nos = lottery_draw()
        count_hits(my_main_nos, my_supp_nos, main_nos, supp_nos)
        if rounds == round_info:
            print(round_info)
            round_info += 100000
        rounds += 1
    print(f"It took {rounds:,} rounds to win the jackpot!")

def print_hits() -> None:
    print(f"{"TIERS":<10}{"Numbers"}{"Hits":>15}")
    for tier in TIERS:
        if tier in hits:
            print(f"{TIERS[tier]:.<12}{tier[0]}+{tier[1]}{hits[tier]:.>17,}")

def main():
    ask_my_main_nos()
    ask_my_supp_nos()
    rounds_to_jacpot(rounds,round_info)
    print_hits()

main()