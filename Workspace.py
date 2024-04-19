"""
   __             _       __       _ _                       ___                      _   _   _                                       
  / /  ___   ___ | |_    /__\ ___ | | | ___ _ __            / __\_   _    /\/\   __ _| |_| |_| |__   _____      __   /\/\   __ _ _ __ 
 / /  / _ \ / _ \| __|  / \/// _ \| | |/ _ \ '__|  _____   /__\// | | |  /    \ / _` | __| __| '_ \ / _ \ \ /\ / /  /    \ / _` | '__|
/ /__| (_) | (_) | |_  / _  \ (_) | | |  __/ |    |_____| / \/  \ |_| | / /\/\ \ (_| | |_| |_| | | |  __/\ V  V /  / /\/\ \ (_| | |   
\____/\___/ \___/ \__| \/ \_/\___/|_|_|\___|_|            \_____/\__, | \/    \/\__,_|\__|\__|_| |_|\___| \_/\_/   \/    \/\__,_|_|   
                                                                 |___/                                                                
"""

# With assistance from:
# https://chat.openai.com/
# w3schools.com
# Stack Overflow
# geeksforgeeks.org
# docs.python.org
import random


class Item:
    def __init__(
        self,
        commons,
        uncommons,
        rares,
        epics,
        legendaries,
        mythics,
        crate_odds,
        name,
        lb,
    ):
        self.commons = commons
        self.uncommons = uncommons
        self.rares = rares
        self.epics = epics
        self.legendaries = legendaries
        self.mythics = mythics
        self.crate_odds = crate_odds
        self.name = name
        self.lb = lb

    def roll(self):
        roll_val = random.randrange(self.lb, 1001) / 100
        if roll_val > crate_odds[0][0] and roll_val <= crate_odds[0][1]:
            result = random.choices(self.commons, weights=(40, 25, 20, 10, 5), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > crate_odds[1][0] and roll_val <= crate_odds[1][1]:
            result = random.choices(self.uncommons, weights=(60, 20, 10, 6, 4), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > crate_odds[2][0] and roll_val <= crate_odds[2][1]:
            result = random.choices(self.rares, weights=(70, 20, 6, 3, 1), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > crate_odds[3][0] and roll_val <= crate_odds[3][1]:
            result = random.choices(self.epics, weights=(75, 15, 5, 4.5, 0.5), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > crate_odds[4][0] and roll_val <= crate_odds[4][1]:
            result = random.choices(self.legendaries, weights=(85, 14.7, 0.3), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        elif roll_val > crate_odds[5][0] and roll_val <= crate_odds[5][1]:
            result = random.choices(self.mythics, weights=(95, 4.99, 0.01), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You received {name} and it has a luck boost of {lb}!\n")
        else:
            print(
                "You did not receive anything! (If you see this message, this program must be in testing!)\n"
            )
            result = None
        return result

    def equip(self, name, lb):
        self.name = name
        self.lb = lb

    def return_odds(self):
        odds_output = []
        common_odds = crate_odds[0][1] - crate_odds[0][0]
        uncommon_odds = crate_odds[1][1] - crate_odds[1][0]
        rare_odds = crate_odds[2][1] - crate_odds[2][0]
        epic_odds = crate_odds[3][1] - crate_odds[3][0]
        legendary_odds = crate_odds[4][1] - crate_odds[4][0]
        mythic_odds = crate_odds[5][1] - crate_odds[5][0]
        print(f"Item Equipped: {self.name}\nLuck Boost: {self.lb}")
        if self.lb >= (crate_odds[0][1] * 100):
            common_odds = 0
        else:
            common_odds = ((crate_odds[0][1] * 100) - self.lb) / (1000 - self.lb)
        if self.lb >= (crate_odds[1][1] * 100):
            uncommon_odds = 0
        elif self.lb >= (crate_odds[1][0] * 100):
            uncommon_odds = ((crate_odds[1][1] * 100) - self.lb) / (1000 - self.lb)
        else:
            uncommon_odds = ((crate_odds[1][1] - crate_odds[1][0]) * 100) / (
                1000 - self.lb
            )
        if self.lb >= (crate_odds[2][1] * 100):
            rare_odds = 0
        elif self.lb >= (crate_odds[2][0] * 100):
            rare_odds = ((crate_odds[2][1] * 100) - self.lb) / (1000 - self.lb)
        else:
            rare_odds = ((crate_odds[2][1] - crate_odds[2][0]) * 100) / (1000 - self.lb)
        if self.lb >= (crate_odds[3][1] * 100):
            epic_odds = 0
        elif self.lb >= (crate_odds[3][0] * 100):
            epic_odds = ((crate_odds[3][1] * 100) - self.lb) / (1000 - self.lb)
        else:
            epic_odds = ((crate_odds[3][1] - crate_odds[3][0]) * 100) / (1000 - self.lb)
        if self.lb >= (crate_odds[4][1] * 100):
            legendary_odds = 0
        elif self.lb >= (crate_odds[4][0] * 100):
            legendary_odds = ((crate_odds[4][1] * 100) - self.lb) / (1000 - self.lb)
        else:
            legendary_odds = ((crate_odds[4][1] - crate_odds[4][0]) * 100) / (
                1000 - self.lb
            )
        if self.lb >= (crate_odds[5][1] * 100):
            mythic_odds = 0
        elif self.lb >= (crate_odds[5][0] * 100):
            mythic_odds = ((crate_odds[5][1] * 100) - self.lb) / (1000 - self.lb)
        else:
            mythic_odds = ((crate_odds[5][1] - crate_odds[5][0]) * 100) / (
                1000 - self.lb
            )
        print(
            f"With {Wand.name}, the odds of rolling a common item is: {round(common_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling an uncommon item is: {round(uncommon_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling a rare item is: {round(rare_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling an epic item is: {round(epic_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling a legendary item is: {round(legendary_odds*100, 2)}%\nWith {Wand.name}, the odds of rolling a mythic item is: {round(mythic_odds*100, 2)}%."
        )


crate_odds = [[0, 5], [5, 7], [7, 8], [8, 8.5], [8.5, 8.6], [8.6, 8.65]]
commons = [
    ["Pencil", 1],
    ["Eraser", 2],
    ["Notebook", 3],
    ["Paperclip", 4],
    ["Binder", 5],
]
uncommons = [
    ["Computer Mouse", 6],
    ["Keyboard", 8],
    ["Monitor", 10],
    ["Laptop", 12],
    ["Phone", 15],
]
rares = [["Water", 20], ["Fire", 25], ["Earth", 30], ["Air", 40], ["Lightning", 50]]
epics = [
    ["Oak", 75],
    ["Birch", 100],
    ["Acacia", 125],
    ["Jungle", 150],
    ["Dark Oak", 200],
]
legendaries = [["Mouse", 300], ["Bird", 400], ["Worm", 500]]
mythics = [["Charred", 550], ["Drowned", 650], ["Befallen", 800]]
Wand = Item(
    commons,
    uncommons,
    rares,
    epics,
    legendaries,
    mythics,
    crate_odds,
    "Placeholder",
    0,
)
while True:
    choice = str(input("What do you want to do?\nType /help for a list of actions.\n"))
    if choice == "/roll":
        result = Wand.roll()
        if result:
            name, lb = result
            equip_bool = str(input("Equip Item? (Input Y for yes and N for no)\n"))
            if equip_bool == "Y" or equip_bool == "y":
                Wand.equip(name, lb)
        print(
            f"Current Equipped Item: {Wand.name} | Luck Boost ({Wand.lb}, 1000): {Wand.lb}"
        )
    elif choice == "/help":
        print(
            "Available Commands:\n/roll - rolls for a random item\n/odds - calculate odds of getting a each item rarity tier based on equipped item's current luck boost"
        )
    elif choice == "/odds":
        Wand.return_odds()
