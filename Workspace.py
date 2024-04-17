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
name = ""
lb = 0
class Item:
    def __init__(self, commons, uncommons, rares, name, lb):
        self.commons = commons
        self.uncommons = uncommons
        self.rares = rares
        self.name = name
        self.lb = lb
      
    def roll(self):
        roll_val = random.randint(1, 101) + self.lb
        if roll_val <= 30:
            result = random.choices(self.commons, weights=(40, 25, 20, 10, 5), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f'You recieved {name} and it has a luck boost of {lb}!\n')
        elif roll_val > 30 and roll_val <= 50:
            result = random.choices(self.uncommons, weights=(60, 20, 10, 6, 4), k=1)[0]
            name = result[0]
            lb = result[1]
            print(f'You recieved {name} and it has a luck boost of {lb}!\n')
        else:
            print("You did not recieve anything LMAO\n")
            pass
    def equip(self, name, lb):
        self.name = name
        self.lb = lb
commons = [["Pencil", 0.5], ["Eraser", 1], ["Notebook", 2], ["Paperclip", 2.5], ["Binder", 5]]
uncommons = [["Computer Mouse", 6], ["Keyboard", 8], ["Monitor", 10], ["Laptop", 12], ["Phone", 15]]
rares = []
Wand = Item(commons, uncommons, rares, "Placeholder", 0)
for i in range(100):
    Wand.roll()
    Wand.equip(name, lb)
    print(Wand.name, Wand.lb)






