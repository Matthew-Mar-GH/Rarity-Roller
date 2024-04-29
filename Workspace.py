# With assistance from:
# https://chat.openai.com/
# w3schools.com
# Stack Overflow
# geeksforgeeks.org
# Title ASCII Art - https://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# docs.python.org
# Treasure Chest ASCII Art - https://ascii.co.uk/art/treasure
import random
import time


class Item:
    def __init__(
        self,
        commons,
        uncommons,
        rares,
        epics,
        legendaries,
        mythics,
        common_lc_weights,
        uncommon_lc_weights,
        rare_lc_weights,
        epic_lc_weights,
        legendary_lc_weights,
        mythic_lc_weights,
        common_odds,
        uncommon_odds,
        rare_odds,
        epic_odds,
        legendary_odds,
        mythic_odds,
        crate_odds,
        name,
        lb,
        roll_counter,
    ):
        self.commons = commons
        self.uncommons = uncommons
        self.rares = rares
        self.epics = epics
        self.legendaries = legendaries
        self.mythics = mythics
        self.common_lc_weights = common_lc_weights
        self.uncommon_lc_weights = uncommon_lc_weights
        self.rare_lc_weights = rare_lc_weights
        self.epic_lc_weights = epic_lc_weights
        self.legendary_lc_weights = legendary_lc_weights
        self.mythic_lc_weights = mythic_lc_weights
        self.common_odds = common_odds
        self.uncommon_odds = uncommon_odds
        self.rare_odds = rare_odds
        self.epic_odds = epic_odds
        self.legendary_odds = legendary_odds
        self.mythic_odds = mythic_odds
        self.crate_odds = crate_odds
        self.name = name
        self.lb = lb
        self.roll_counter = roll_counter

    def roll(self):
        self.roll_counter += 1
        print(f"{line_divider}{ASCII_art_treasure}")
        roll_val = random.randrange(self.lb, 1001) / 100
        if roll_val > self.crate_odds[0][0] and roll_val <= self.crate_odds[0][1]:
            result = random.choices(self.commons, weights=self.common_lc_weights, k=1)[
                0
            ]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > self.crate_odds[1][0] and roll_val <= self.crate_odds[1][1]:
            result = random.choices(
                self.uncommons, weights=self.uncommon_lc_weights, k=1
            )[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > self.crate_odds[2][0] and roll_val <= self.crate_odds[2][1]:
            result = random.choices(self.rares, weights=self.rare_lc_weights, k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > self.crate_odds[3][0] and roll_val <= self.crate_odds[3][1]:
            result = random.choices(self.epics, weights=self.epic_lc_weights, k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > self.crate_odds[4][0] and roll_val <= self.crate_odds[4][1]:
            result = random.choices(
                self.legendaries, weights=self.legendary_lc_weights, k=1
            )[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > self.crate_odds[5][0] and roll_val <= self.crate_odds[5][1]:
            result = random.choices(self.mythics, weights=self.mythic_lc_weights, k=1)[
                0
            ]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        print(f"You have rolled {self.roll_counter} time(s)!\n{line_divider}")
        return result

    def equip(self, name, lb):
        self.name = name
        self.lb = lb

    def return_odds(self):
        self.common_odds = self.crate_odds[0][1] - self.crate_odds[0][0]
        self.uncommon_odds = self.crate_odds[1][1] - self.crate_odds[1][0]
        self.rare_odds = self.crate_odds[2][1] - self.crate_odds[2][0]
        self.epic_odds = self.crate_odds[3][1] - self.crate_odds[3][0]
        self.legendary_odds = self.crate_odds[4][1] - self.crate_odds[4][0]
        self.mythic_odds = self.crate_odds[5][1] - self.crate_odds[5][0]
        print(f"{line_divider}\nItem Equipped: {self.name}\nLuck Boost: {self.lb}")
        if self.lb >= (self.crate_odds[0][1] * 100):
            self.common_odds = 0
        else:
            self.common_odds = ((self.crate_odds[0][1] * 100) - self.lb) / (
                1000 - self.lb
            )
        if self.lb >= (self.crate_odds[1][1] * 100):
            self.uncommon_odds = 0
        elif self.lb >= (self.crate_odds[1][0] * 100):
            self.uncommon_odds = ((self.crate_odds[1][1] * 100) - self.lb) / (
                1000 - self.lb
            )
        else:
            self.uncommon_odds = (
                (self.crate_odds[1][1] - self.crate_odds[1][0]) * 100
            ) / (1000 - self.lb)
        if self.lb >= (self.crate_odds[2][1] * 100):
            self.rare_odds = 0
        elif self.lb >= (self.crate_odds[2][0] * 100):
            self.rare_odds = ((self.crate_odds[2][1] * 100) - self.lb) / (
                1000 - self.lb
            )
        else:
            self.rare_odds = ((self.crate_odds[2][1] - self.crate_odds[2][0]) * 100) / (
                1000 - self.lb
            )
        if self.lb >= (self.crate_odds[3][1] * 100):
            self.epic_odds = 0
        elif self.lb >= (self.crate_odds[3][0] * 100):
            self.epic_odds = ((self.crate_odds[3][1] * 100) - self.lb) / (
                1000 - self.lb
            )
        else:
            self.epic_odds = ((self.crate_odds[3][1] - self.crate_odds[3][0]) * 100) / (
                1000 - self.lb
            )
        if self.lb >= (self.crate_odds[4][1] * 100):
            self.legendary_odds = 0
        elif self.lb >= (self.crate_odds[4][0] * 100):
            self.legendary_odds = ((self.crate_odds[4][1] * 100) - self.lb) / (
                1000 - self.lb
            )
        else:
            self.legendary_odds = (
                (self.crate_odds[4][1] - self.crate_odds[4][0]) * 100
            ) / (1000 - self.lb)
        if self.lb >= (self.crate_odds[5][1] * 100):
            self.mythic_odds = 0
        elif self.lb >= (self.crate_odds[5][0] * 100):
            self.mythic_odds = ((self.crate_odds[5][1] * 100) - self.lb) / (
                1000 - self.lb
            )
        else:
            self.mythic_odds = (
                (self.crate_odds[5][1] - self.crate_odds[5][0]) * 100
            ) / (1000 - self.lb)
        print(ASCII_art_question_mark)
        print(
            f"With {Wand.name}, the odds of rolling a common item is: {round(self.common_odds*100, 5)}%\nWith {Wand.name}, the odds of rolling an uncommon item is: {round(self.uncommon_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling a rare item is: {round(self.rare_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling an epic item is: {round(self.epic_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling a legendary item is: {round(self.legendary_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling a mythic item is: {round(self.mythic_odds*100, 2)}%.\n{line_divider}"
        )


crate_odds = [[0, 6], [6, 8.5], [8.5, 9.5], [9.5, 9.8], [9.8, 9.98], [9.98, 10]]
commons = [
    ["Pencil", 0],
    ["Eraser", 1],
    ["Notebook", 2],
    ["Paperclip", 3],
    ["Binder", 4],
]
common_lc_weights = [40, 25, 20, 10, 5]
uncommons = [
    ["Computer Mouse", 6],
    ["Keyboard", 8],
    ["Monitor", 10],
    ["Laptop", 12],
    ["Phone", 15],
]
uncommon_lc_weights = [60, 20, 10, 6, 4]
rares = [["Water", 20], ["Fire", 25], ["Earth", 30], ["Air", 40], ["Lightning", 50]]
rare_lc_weights = [70, 20, 6, 3, 1]
epics = [
    ["Oak", 75],
    ["Birch", 100],
    ["Acacia", 125],
    ["Jungle", 150],
    ["Dark Oak", 200],
]
epic_lc_weights = [75, 15, 5, 4.5, 0.5]
legendaries = [["Mouse", 300], ["Bird", 400], ["Worm", 500]]
legendary_lc_weights = [85, 14.7, 0.3]
mythics = [["Charred", 550], ["Drowned", 650], ["Befallen", 800]]
mythic_lc_weights = [95, 4.99, 0.01]
common_odds = 0.6
uncommon_odds = 0.25
rare_odds = 0.1
epic_odds = 0.03
legendary_odds = 0.018
mythic_odds = 0.002
Wand = Item(
    commons,
    uncommons,
    rares,
    epics,
    legendaries,
    mythics,
    common_lc_weights,
    uncommon_lc_weights,
    rare_lc_weights,
    epic_lc_weights,
    legendary_lc_weights,
    mythic_lc_weights,
    common_odds,
    uncommon_odds,
    rare_odds,
    epic_odds,
    legendary_odds,
    mythic_odds,
    crate_odds,
    "Pencil",
    0,
    0,
)
all_items_lb = [
    [Wand.commons],
    [Wand.uncommons],
    [Wand.rares],
    [Wand.epics],
    [Wand.legendaries],
    [Wand.mythics],
]
all_weights = [
    [Wand.common_lc_weights],
    [Wand.uncommon_lc_weights],
    [Wand.rare_lc_weights],
    [Wand.epic_lc_weights],
    [Wand.legendary_lc_weights],
    [Wand.mythic_lc_weights],
]
rarity_types = [
    Wand.common_odds,
    Wand.uncommon_odds,
    Wand.rare_odds,
    Wand.epic_odds,
    Wand.legendary_odds,
    Wand.mythic_odds,
]

ASCII_art_treasure = r"""
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'"
                    """
ASCII_art_question_mark = r"""
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

             q###r
              """
line_divider = ">----------------------------------------<"
debugmode = False
print(f"{line_divider}\nHello! Welcome to Rarity Roller v1.0.0!\n")
time.sleep(1)
print("In this game, the goal is to get the item of the highest rarity!\n")
time.sleep(1)
print("To roll for an item, type /roll when prompted on an action!\n")
time.sleep(1)
print(
    "Rolls are determined based on four factors:\n- The number randomly generated (0 to 10)\n- The crate received (each crate has a range of numbers within 0 to 10 that rewards it)\n- The Weights of each item in each crate\n- Your equipped item's luck boost (affects total range of numbers that can be generated)"
)
time.sleep(1)
print("You can also view your odds of each type of crate by entering in /odds\n")
time.sleep(1)
print(f"Good luck!\n{line_divider}")

while True:
    choice = str(
        input("What do you want to do?\n\nType /help for a list of actions.\n")
    )
    if choice == "/roll":
        result = Wand.roll()
        if result != "":
            old_name = Wand.name
            old_lb = Wand.lb
            name, lb = result
            equip_bool = str(input("Equip Item? (Input Y for yes and N for no)\n"))
            if equip_bool == "Y" or equip_bool == "y":
                Wand.equip(name, lb)
        print(
            f"\nCurrent Equipped Item: {Wand.name} | Luck Boost ({Wand.lb}, 1000): {Wand.lb}\n{line_divider}"
        )
    elif choice == "/help":
        print(
            f"{line_divider}\nAvailable Commands:\n/roll - rolls for a random item\n/odds - calculate odds of getting a each item rarity tier based on equipped item's current luck boost\n{line_divider}"
        )
    elif choice == "/odds":
        Wand.return_odds()
