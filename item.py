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
        
    def printItem(self):
        print("   " * self.level, "+" if self.check else "-", self.name)
        for i in self.subItems:
            i.printItem()

    def status(self):
        print("Name:", self.name)
        print("Excitement level:", self.excitement)
        print("Difficulty level:", self.difficulty)
        print("Sub-items (" + len(self.subItems) + "):", [i.name for i in self.subItems])
        print("Level:", self.level)

