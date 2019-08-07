class Item:
    name = ""
    difficulty = "Normal"
    availDiff = ["Trivial", "Easy", "Normal", "Hard", "Extreme"]
    excitement = 0
    availExci = [0, 1, 2]
    subItems = []
    check = False
    level = 0

    def __init__(self, name, dfc="Normal", exc=0, check=False, sub=[], level=0):
        self.name = name
        self.difficulty = dfc
        self.excitement = exc
        self.check = check
        self.sub = sub
        self.level = level
        
    def printItem():
        print("   " * level, "+" if check else "-", name)
        for i in subItems:
            i.printItem()

    def status():
        print("Name:", name)
        print("Excitement level:", excitement)
        print("Difficulty level:", difficulty)
        print("Sub-items (" + len(subItems) + "):", [i.name for i in subItems])
        print("Level:", level)

