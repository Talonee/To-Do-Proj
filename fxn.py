cld = []
checked = []
unchecked = []
discarded = []

################### DISPLAY ###################

# display calendar
def display():
    print(cld)

def displayChecked():
    print(checked)

def displayUnchecked():
    print(unchecked)

def displayAll():
    print()
    print("**********************")
    print("Displaying full list")
    display()
    print("Displaying checked list")
    displayChecked()
    print("Displaying unchecked list")
    displayUnchecked()

################### ADD ###################

def add(i):
    if not (isinstance(i, str) or isinstance(i, list) or isinstance(i, tuple)):
        i = str(i)

    if isinstance(i, str) and (i not in cld):
        cld.append(i)
    elif (i in cld):
        print("Item already exist")
    elif isinstance(i, list) or isinstance(i, tuple):
        exist = False
        for item in i:
            if str(item) not in cld:
                cld.append(str(item))
            else:
                exist = True
        if exist:
            print("Few items already exist")

################### REMOVE ###################

# remove single item
def remove(i):
    if isinstance(i, list) or isinstance(i, tuple):
        for item in i:
            if str(item) + "-c" in cld:
                cld.remove(str(item) + "-c")
                checked.remove(str(item) + "-c")
            elif str(item) in cld:
                cld.remove(str(item))
                unchecked.remove(str(item))
            else:
                return "Do not exist"
    else:
        i = str(i)
        if i in cld:
            

    if isinstance(i, str):
        cld.remove(i)
    elif isinstance(i, list):
        for item in i:
            cld.remove(i)

def remCheck():
    pass

def remUncheck():
    pass

################### CHECK + UNCHECK ###################

# update list of checked items
def updateChecked():
    for i in cld:
        if (i not in checked) and i[-2:] == "-c":
            checked.append(i)

# update list of unchecked items
def updateUnchecked():
    for i in cld:
        if (i not in unchecked) and i[-2:] != "-c":
            unchecked.append(i)

def updateAll():
    updateChecked()
    updateUnchecked()

# check specified item
def check(i):
    if isinstance(i, int) and (i >= 0 and i < len(cld)): 
        unchecked.remove(cld[i])
        cld[i] = cld[i] + "-c"
        checked.append(cld[i])
    elif isinstance(i, str) and (i in cld):
        unchecked.remove(i)
        index = cld.index(i)
        cld[index] = cld[index] + "-c"
        checked.append(cld[index])
    else:
        print("Invalid Input")

def uncheck(i):
    if isinstance(i, int) and (i >= 0 and i < len(cld)): 
        checked.remove(cld[i])
        cld[i] = cld[i][:len(cld[i]) - 2]
        unchecked.append(cld[i])
    elif isinstance(i, str) and (i + "-c" in cld):
        checked.remove(i + "-c")
        index = cld.index(i + "-c")
        cld[index] = cld[index][:len(cld[index]) - 2]
        unchecked.append(cld[index])
    else:
        print("Invalid Input")

################### DISCARDED ###################

def clearAll():
    cld.clear()

def clearCheck():
    pass

cld = ["Eat", "Drink", "Sleep"]
updateAll()
displayAll()

add(["Swim", "Cry", "Laugh"])
add("Superhero")
add("♣")
updateAll()
displayAll()

# rem(["Drink, Cry"])
# updateAll()
# displayAll()

# check("Eat")
# check("Drink")
# updateAll()
# displayAll()

# uncheck(1)
# updateAll()
# displayAll()