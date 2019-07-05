tdl = []  # to do list
ckd = []  # checked item
uck = []  # unchecked item
dsc = []  # discarded item
err = []  # show all error messages

################### DISPLAY ###################


# display calendar
def dspTdl():
    print(tdl)


def dspCkd():
    updateChecked()
    print(ckd)


def dspUck():
    updateUnchecked()
    print(uck)

def dspDsc():
    print(dsc)

def dspAll():
    updateAll()
    print("To-do:")
    dspTdl()
    print()
    print("Checked:")
    dspCkd()
    print()
    print("Unchecked:")
    dspUck()
    print()
    print("Discarded:")
    dspDsc()
    dspError()


def dspError():
    print()
    print()
    print()
    print("****************************")
    print("Warning(s):")
    if len(err) == 0:
        print("No errors found.")
    else:
        for i in err:
            print(i)


################### ADD ###################


def add(*args):
    if len(args) == 1:
        if isinstance(args[0], (str, int)) and (args[0] not in tdl):
            tdl.append(str(args[0]))
            uck.append(str(args[0]))
        elif isinstance(args[0], (str, int)) and (args[0] in tdl):
            err.append("Item [" + args[0] + "] already exist")
        elif isinstance(args[0], list) or isinstance(args[0], tuple):
            exist = False
            strReturn = "Item(s) ["
            for item in args[0]:
                if item not in tdl:
                    tdl.append(item)
                    uck.append(item)
                else:
                    if not exist:
                        strReturn += item
                    else:
                        strReturn += ", " + item

                    exist = True

            if exist: err.append(strReturn + "] already exist.")

    elif len(args) == 2:
        # single args
        if isinstance(args[0], (str, int)) and isinstance(args[1], (str, int)):
            if isinstance(args[0], str) and isinstance(args[1], int):
                tdl.insert(args[1], args[0])
                uck.append(args[0])
            elif isinstance(args[0], int) and isinstance(args[1], (str, int)):
                tdl.insert(args[0], str(args[1]))
                uck.append(str(args[1]))
            else:
                raise TypeError("Cannot have two Strings")

        # list and tuple args
        elif isinstance(args[0],
                        (list, tuple)) and isinstance(args[1], (list, tuple)):
            if len(args[0]) != len(args[1]):
                raise TypeError("Invalid list lengths")

            exist = False
            strReturn = "Item(s) ["

            if all(type(x) is int for x in args[0]):
                for i in args[1]:
                    if str(i) not in tdl:
                        tdl.insert(args[0][args[1].index(i)], str(i))
                        uck.append(str(i))
                    else:
                        if not exist:
                            strReturn += str(i)
                        else:
                            strReturn += ", " + str(i)
                        exist = True

            elif (all(type(x) is str for x in args[0])
                  and all(type(x) is int for x in args[1])):
                for i in args[0]:
                    if i not in tdl:
                        tdl.insert(args[1][args[0].index(i)], i)
                        uck.append(i)
                    else:
                        if not exist:
                            strReturn += i
                        else:
                            strReturn += ", " + i
                        exist = True
            else:
                raise TypeError("One parameter must contain strictly numbers")

            if exist: err.append(strReturn + "] already exist.")

        else:
            raise TypeError("Invalid parameters")
    else:
        raise IndexError("Invalid number of arguments")


################### REMOVE ###################


# remove single item
def rem(i):
    if isinstance(i, list) or isinstance(i, tuple):
        for item in i:
            if str(item) + "-c" in tdl:
                tdl.remove(str(item) + "-c")
                ckd.remove(str(item) + "-c")
            elif str(item) in tdl:
                tdl.remove(str(item))
                uck.remove(str(item))
            else:
                return "Do not exist"
    # else:
    #     i = str(i)
    #     if i in tdl:

    # if isinstance(i, str):
    #     tdl.remove(i)
    # elif isinstance(i, list):
    #     for item in i:
    #         tdl.remove(i)


def remCheck():
    pass


def remUncheck():
    pass


################### UPDATE ###################


# update list of checked items
def updateChecked():
    for i in tdl:
        if (i not in ckd) and i[-2:] == "-c":
            ckd.append(i)


# update list of unchecked items
def updateUnchecked():
    for i in tdl:
        if (i not in uck) and i[-2:] != "-c":
            uck.append(i)


def updateAll():
    updateChecked()
    updateUnchecked()


################### CHECK + UNCHECK ###################


# check specified item
def check(i):
    if isinstance(i, int) and (i >= 0 and i < len(tdl)):
        uck.remove(tdl[i])
        tdl[i] = tdl[i] + "-c"
        ckd.append(tdl[i])
    elif isinstance(i, str) and (i in tdl):
        uck.remove(i)
        index = tdl.index(i)
        tdl[index] = tdl[index] + "-c"
        ckd.append(tdl[index])
    else:
        print("Invalid Input")


def uncheck(i):
    if isinstance(i, int) and (i >= 0 and i < len(tdl)):
        ckd.remove(tdl[i])
        tdl[i] = tdl[i][:len(tdl[i]) - 2]
        uck.append(tdl[i])
    elif isinstance(i, str) and (i + "-c" in tdl):
        ckd.remove(i + "-c")
        index = tdl.index(i + "-c")
        tdl[index] = tdl[index][:len(tdl[index]) - 2]
        uck.append(tdl[index])
    else:
        print("Invalid Input")


################### DISCARDED ###################


def clearAll():
    # clear tdl
    # clear check
    # clear uncheck
    # add to discarded
    pass


def clearCheck():
    pass


tdl = ["Eat", "Drink", "Sleep"]
# add(["Swim", "Laugh", "Superhero", "♣"])
# add(6, "Run")
# add("Dance", 3)
# add(["Swim", "Fruit", "Life", "♣", "Drink"])
# add("Swim")

# # case 1
# add([1, 2, 2, 2], ["Watermelon", "Grass", "Apple", "Beans"])
# # case 2
# add([1, 2, 4, 0], [1, "Fish", 2, 6])
# add(["Woopers"], [1])
# case 3
# add(["Watermelon", "Grass", "Apple", "Beans"], ["Watermelon", "Grass", "Apple", "Beans"])


dspAll()

# lst2 = ["Watermelon", "Grass", "Apple", "Beans"]
# lst1 = [1,2,-1,2]
# lst3 = ["!", 2222, "asdasd"]
# print(all(isinstance(x, (str, int)) for x in lst3))
# woop = []

# for i in lst2:
#     woop.insert(lst1[lst2.index(i)], i)
# print(woop)

# rem(["Drink, Cry"])
# updateAll()
# displayAll()

# check("Eat")
# check("Drink")
# updateAll()
# displayAll()

# uncheck(1)
# updateAll()
# displayAll()"