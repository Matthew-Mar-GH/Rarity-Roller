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
        self, commons, uncommons, rares, epics, legendaries, mythics, name, lb
    ):
        self.commons = commons
        self.uncommons = uncommons
        self.rares = rares
        self.epics = epics
        self.legendaries = legendaries
        self.mythics = mythics
        self.name = name
        self.lb = lb

    def roll(self):
        roll_val = random.randrange(self.lb, 1001) / 100
        if roll_val <= 5:
            result = random.choices(self.commons, weights=(40, 25, 20, 10, 5), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You recieved {name} and it has a luck boost of {lb}!\n")
        elif roll_val > 5 and roll_val <= 7:
            result = random.choices(self.uncommons, weights=(60, 20, 10, 6, 4), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You recieved {name} and it has a luck boost of {lb}!\n")
        elif roll_val > 7 and roll_val <= 8:
            result = random.choices(self.rares, weights=(70, 20, 6, 3, 1), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You recieved {name} and it has a luck boost of {lb}!\n")
        elif roll_val > 8 and roll_val <= 8.5:
            result = random.choices(self.epics, weights=(75, 15, 5, 4.5, 0.5), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You recieved {name} and it has a luck boost of {lb}!\n")
        elif roll_val > 8.5 and roll_val <= 8.52:
            result = random.choices(self.legendaries, weights=(85, 14.7, 0.3), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You recieved {name} and it has a luck boost of {lb}!\n")
        elif roll_val > 8.52 and roll_val <= 8.53:
            result = random.choices(self.mythics, weights=(95, 4.99, 0.01), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f"You recieved {name} and it has a luck boost of {lb}!\n")
        else:
            print(
                "You did not receive anything! (If you see this message, this program must be in testing!)\n"
            )
            result = None
        return result

    def equip(self, name, lb):
        self.name = name
        self.lb = lb


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
Wand = Item(commons, uncommons, rares, epics, legendaries, mythics, "Placeholder", 0)
while True:
    choice = int(input("What to do?\n"))
    for i in range(choice):
        result = Wand.roll()
        if result:
            name, lb = result
            if Wand.lb < lb:
                Wand.equip(name, lb)
        print(
            f"Current Equipped Item: {Wand.name} | Luck Boost ({Wand.lb}, 1000): {Wand.lb}"
        )
