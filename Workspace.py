'''
   __             _       __       _ _                       ___                      _   _   _                                       
  / /  ___   ___ | |_    /__\ ___ | | | ___ _ __            / __\_   _    /\/\   __ _| |_| |_| |__   _____      __   /\/\   __ _ _ __ 
 / /  / _ \ / _ \| __|  / \/// _ \| | |/ _ \ '__|  _____   /__\// | | |  /    \ / _` | __| __| '_ \ / _ \ \ /\ / /  /    \ / _` | '__|
/ /__| (_) | (_) | |_  / _  \ (_) | | |  __/ |    |_____| / \/  \ |_| | / /\/\ \ (_| | |_| |_| | | |  __/\ V  V /  / /\/\ \ (_| | |   
\____/\___/ \___/ \__| \/ \_/\___/|_|_|\___|_|            \_____/\__, | \/    \/\__,_|\__|\__|_| |_|\___| \_/\_/   \/    \/\__,_|_|   
                                                                 |___/                                                                
'''
# With assistance from:
# https://chat.openai.com/
# w3schools.com
# Stack Overflow
# geeksforgeeks.org
# docs.python.org
import random
class Item:
    def __init__(self, commons, uncommons, rares, name, lb):
        self.commons = commons
        self.uncommons = uncommons
        self.rares = rares
        self.name = name
        self.lb = lb
      
    def roll(self):
        roll_val = (random.randrange(self.lb, 1001)/100)
        if roll_val <= 5:
            result = random.choices(self.commons, weights=(40, 25, 20, 10, 5), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f'You recieved {name} and it has a luck boost of {lb}!\n')
        elif roll_val > 5 and roll_val <= 7:
            result = random.choices(self.uncommons, weights=(60, 20, 10, 6, 4), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f'You recieved {name} and it has a luck boost of {lb}!\n')
        elif roll_val > 7 and roll_val <= 8:
            print("You recieved a hypothetical rare!")
            result = None
        elif roll_val > 8 and roll_val <= 8.5:
            print("You recieved a hypothetical epic!")
            result = None
        elif roll_val > 8.5 and roll_val <= 8.6:
            print("You recieved a hypothetical legendary!")
            result = None
        elif roll_val > 8.6 and roll_val <= 8.65:
            print("You recieved a hypothetical mythic!")
            result = None
        else:
            print("You did not recieve anything! (If you see this message, this program must be in testing!)\n")
            result = None
        return result
    def equip(self, name, lb):
        self.name = name
        self.lb = lb
commons = [["Pencil", 1], ["Eraser", 2], ["Notebook", 3], ["Paperclip", 4], ["Binder", 5]]
uncommons = [["Computer Mouse", 6], ["Keyboard", 8], ["Monitor", 10], ["Laptop", 12], ["Phone", 15]]
rares = []
Wand = Item(commons, uncommons, rares, "Placeholder", 0)
while True:
    choice = str(input("What to do?\n"))
    if choice == "roll":
        result = Wand.roll()
        if result:
            name, lb = result
            if Wand.lb < lb:
                Wand.equip(name, lb)
    print(f'Current Equipped Item: {Wand.name} | Luck Boost (Roll + Luck Boost Value): {Wand.lb}')






