lists = {"To-do": [], "Checked": [], "Unchecked": [], "Discarded": []}
# lists.get("To-do") = lists.get("To-do") # to do list
# lists.get("Checked") = lists.get("Checked")  # checked item
# lists.get("Unchecked") = lists.get("Unchecked")  # unchecked item
# dsc = lists.get("Discarded") # discarded item
err = []  # show all error messages

################### DISPLAY ###################


# display calendar
def dspTdl():
    print(lists["To-do"])


def dspCkd():
    print(lists["Checked"])


def dspUck():
    print(lists["Unchecked"])


def dspDsc():
    print(lists["Discarded"])


def dspAll():
    # updateAll()
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
        if isinstance(args[0],
                      (str, int)) and (str(args[0]) not in lists["To-do"]):
            lists["To-do"].append(str(args[0]))
            lists["Unchecked"].append(str(args[0]))
        elif isinstance(args[0],
                        (str, int)) and (str(args[0]) in lists["To-do"]):
            err.append("Item [" + str(args[0]) + "] already exist")
        elif isinstance(args[0], (list, tuple)):
            exist = False
            strReturn = []
            for item in args[0]:
                if item not in lists["To-do"]:
                    lists["To-do"].append(str(item))
                    lists["Unchecked"].append(str(item))
                else:
                    strReturn.append(str(item))
                    exist = True
            if exist:
                err.append("Item(s) [" + ", ".join(strReturn) +
                           "] already exist.")

    elif len(args) == 2:
        # single args
        if isinstance(args[0], (str, int)) and isinstance(args[1], (str, int)):
            if isinstance(args[0], str) and isinstance(args[1], int):
                lists["To-do"].insert(args[1], args[0])
                lists["Unchecked"].append(args[0])
            elif isinstance(args[0], int) and isinstance(args[1], str):
                lists["To-do"].insert(args[0], str(args[1]))
                lists["Unchecked"].append(str(args[1]))
            else:
                raise TypeError("Cannot have two Strings")

        # list and tuple args
        elif isinstance(args[0],
                        (list, tuple)) and isinstance(args[1], (list, tuple)):
            if len(args[0]) != len(args[1]):
                raise TypeError("Invalid list lengths")

            exist = False
            strReturn = []

            if all(type(x) is int
                   for x in args[0]) and all(type(x) is str for x in args[1]):
                for i in args[1]:
                    if i not in lists["To-do"]:
                        lists["To-do"].insert(args[0][args[1].index(i)], i)
                        lists["Unchecked"].append(i)
                    else:
                        strReturn.append(i)
                        exist = True
            elif (all(type(x) is str for x in args[0])
                  and all(type(x) is int for x in args[1])):
                for i in args[0]:
                    if i not in lists["To-do"]:
                        lists["To-do"].insert(args[1][args[0].index(i)], i)
                        lists["Unchecked"].append(i)
                    else:
                        strReturn.append(i)
                        exist = True
            else:
                raise TypeError(
                    "One parameter must contain strictly numbers, another must contain strictly strings"
                )

            if exist:
                err.append("Item(s) [" + ", ".join(strReturn) +
                           "] already exist.")

        else:
            raise TypeError("Invalid parameters")
    else:
        raise IndexError("Invalid number of arguments")


################### REMOVE ###################
'''
lists.get("Checked").remove(remVal) if (remVal in lists.get("Checked")) else lists.get("Unchecked").remove(remVal)

'''


# remove item(s) from specified fxn
def rem(item, fxn):
    # name = fxn
    # if fxn in lists.keys():
    #     fxn = lists.get(fxn)  # dynamic var name
    # lists.update({name: fxn})

    if fxn not in lists.keys():
        raise NameError("Incorrect list name")

    if isinstance(item, (list, tuple)):
        exist = False
        intReturn = []
        strReturn = []

        for i in item:
            if isinstance(i, int):  ########## E R R O R
                if i >= 0 and i < len(lists[fxn]):
                    remVal = lists[fxn].pop(i)
                    if fxn == "Checked" or fxn == "Unchecked":
                        lists["To-do"].remove(remVal)
                    else:
                        lists["Checked"].remove(remVal) if (
                            remVal in lists["Checked"]
                        ) else lists["Unchecked"].remove(remVal)

            elif isinstance(i, str):
                if (i + "-c" in fxn):
                    lists["To-do"].remove(i + "-c")
                    lists["Checked"].remove(i + "-c")
                elif (i in fxn):
                    lists["To-do"].remove(i)
                    lists["Unchecked"].remove(i)
                else:
                    strReturn.append(i)
                    exist = True
            else:
                raise TypeError("Item wasn't a string or an integer")

        if exist and len(intReturn) > 0:
            err.append("Index(ces) [" + ", ".join(intReturn) +
                       "] are out of bound")
        if exist and len(strReturn) > 0:
            err.append("Item(s) [" + ", ".join(strReturn) + "] do not exist")
    elif isinstance(item, (str, int)):
        if isinstance(item, int):
            if item >= 0 and item < len(lists[fxn]):
                remVal = lists[fxn].pop(item)
                if fxn == "Checked" or fxn == "Unchecked":
                    lists["To-do"].remove(remVal)
                else:
                    lists["Checked"].remove(remVal) if (
                        remVal in lists["Checked"]
                    ) else lists["Unchecked"].remove(remVal)
            else:
                intReturn.append(str(item))
                exist = True
        else:
            if (item + "-c" in fxn):
                lists["To-do"].remove(item + "-c")
                lists["Checked"].remove(item + "-c")
            elif (item in fxn):
                lists["To-do"].remove(item)
                lists["Unchecked"].remove(item)
            else:
                strReturn.append(item)
                exist = True
    else:
        raise TypeError("Item wasn't a list, tuple, string, or an integer")


def remAll():
    pass


################### UPDATE ###################

# # update list of checked items
# def updateChecked():
#     for i in lists.get("To-do"):
#         if (i not in lists.get("Checked")) and i[-2:] == "-c":
#             lists.get("Checked").append(i)
#     lists.update({"To-do": lists.get("To-do"),
#                   "Checked": lists.get("Checked"),
#                   "Unchecked": lists.get("Unchecked")})

# # update list of unchecked items
# def updateUnchecked():
#     for i in lists.get("To-do"):
#         if (i not in lists.get("Unchecked")) and i[-2:] != "-c":
#             lists.get("Unchecked").append(i)
#     lists.update({"To-do": lists.get("To-do"), "Checked": lists.get("Checked"), "Unchecked": lists.get("Unchecked")})

# def updateAll():
#     lists.update({"To-do": lists.get("To-do"), "Checked": lists.get("Checked"), "Unchecked": lists.get("Unchecked")})
#     print(lists)
#     updateChecked()
#     updateUnchecked()

################### CHECK + UNCHECK ###################


# check specified item
def check(i):
    if isinstance(i, int) and (i >= 0 and i < len(lists.get("To-do"))):
        lists.get("Unchecked").remove(lists.get("To-do")[i])
        lists.get("To-do")[i] = lists.get("To-do")[i] + "-c"
        lists.get("Checked").append(lists.get("To-do")[i])
    elif isinstance(i, str) and (i in lists.get("To-do")):
        lists.get("Unchecked").remove(i)
        index = lists.get("To-do").index(i)
        lists.get("To-do")[index] = lists.get("To-do")[index] + "-c"
        lists.get("Checked").append(lists.get("To-do")[index])
    else:
        print("Invalid Input")


def uncheck(i):
    if isinstance(i, int) and (i >= 0 and i < len(lists.get("To-do"))):
        lists.get("Checked").remove(lists.get("To-do")[i])
        lists.get("To-do")[i] = lists.get(
            "To-do")[i][:len(lists.get("To-do")[i]) - 2]
        lists.get("Unchecked").append(lists.get("To-do")[i])
    elif isinstance(i, str) and (i + "-c" in lists.get("To-do")):
        lists.get("Checked").remove(i + "-c")
        index = lists.get("To-do").index(i + "-c")
        lists.get("To-do")[index] = lists.get(
            "To-do")[index][:len(lists.get("To-do")[index]) - 2]
        lists.get("Unchecked").append(lists.get("To-do")[index])
    else:
        print("Invalid Input")


################### DISCARDED ###################


def clearAll():
    # clear lists.get("To-do")
    # clear check
    # clear uncheck
    # add to discarded
    pass


def clearCheck():
    pass


# add(1, ["Swim", "Laugh", "Superhero", "♣"])
add(["Eat", "Drink", "Sleep"])
add([0,0,10,0], ["Swim", "Laugh", "Superhero", "♣"])


# print(lists.get("To-do"))
# add(6, "Run")
# add("Dance", 3)
add([1024, "Fruit", "Life", 1738, "Drink"])
# add("Swim")
# # case 1
# add([1, 2, 2, 2], ["Watermelon", "Grass", "Apple", "Beans"])
# # case 2
# add([1, 2, 4, 0], [1, "Fish", 2, 6])
# add(["Woopers"], [1])
# case 3
# add(["Watermelon", "Grass", "Apple", "Beans"], ["Watermelon", "Grass", "Apple", "Beans"])

# rem([1, 1, 6, 12, 5], "To-do")
rem(["Laugh", "Superhero", "Laugh", "Swim", "sWim", "Drink"], "Unchecked")

# rem([0, 2, 5, 3], "To-do")
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