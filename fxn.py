lists = {"To-do": [], "Checked": [], "Unchecked": [], "Discarded": set(())}
err = []  # show all error messages

################### DISPLAY ###################


# display calendar
def dspTdl():
    print("To-do:")
    for i in lists["To-do"]:
        if i[-2:] == "-c":
            print("   +", i)
        else:
            print("   -", i)


def dspCkd():
    print("Checked:")
    for i in lists["Checked"]:
        print("   +", i)


def dspUck():
    print("Unchecked:")
    for i in lists["Unchecked"]:
        print("   -", i)


def dspDsc():
    print("Discarded:")
    for i in lists["Discarded"]:
        if i[-2:] == "-c":
            print("   +", i)
        else:
            print("   -", i)


def dspAll():
    # updateAll()
    dspTdl()
    print()
    dspCkd()
    print()
    dspUck()
    print()
    dspDsc()
    dspError()


def dspError():
    print()
    print()
    print()
    print("****************************")
    print("Warning(s):")
    print()
    if len(err) == 0:
        print("No errors found.")
    else:
        for i in err:
            print(i)


################### ADD ###################


def add(*args):
    exist = False
    intReturn = []
    strReturn = []

    if len(args) == 1:
        if isinstance(args[0],
                      (str, int)) and (str(args[0]) not in lists["To-do"]):
            lists["To-do"].append(str(args[0]))
            lists["Unchecked"].append(str(args[0]))
        elif isinstance(args[0],
                        (str, int)) and (str(args[0]) in lists["To-do"]):
            err.append("Item [" + str(args[0]) + "] already exist")
        elif isinstance(args[0], (list, tuple)):
            for item in args[0]:
                if item not in lists["To-do"]:
                    lists["To-do"].append(str(item))
                    lists["Unchecked"].append(str(item))
                else:
                    strReturn.append(str(item))
                    exist = True
            if exist:
                err.append("   Add: Item(s) [" + ", ".join(strReturn) +
                           "] already exist.")

    elif len(args) == 2:  # index + item
        if isinstance(args[0], (str, int)) and isinstance(args[1], (str, int)):
            if isinstance(args[0], str) and isinstance(args[1], int):
                if not lists["To-do"] and args[1] == 0:
                    lists["To-do"].append(args[0])
                    lists["Unchecked"].append(args[0])
                elif args[1] >= 0 and args[1] < len(lists["To-do"]):
                    lists["To-do"].insert(args[1], args[0])
                    lists["Unchecked"].append(args[0])
                else:
                    intReturn.append(str(args[1]))
                    exist = True
            elif isinstance(args[0], int) and isinstance(args[1], str):
                if not lists["To-do"] and args[0] == 0:
                    lists["To-do"].append(args[1])
                    lists["Unchecked"].append(args[1])
                elif args[0] >= 0 and args[0] < len(lists["To-do"]):
                    lists["To-do"].insert(args[0], args[1])
                    lists["Unchecked"].append(args[1])
                else:
                    intReturn.append(str(args[0]))
                    exist = True
            else:
                raise TypeError("Cannot have two Strings")

        # list and tuple args
        elif isinstance(args[0],
                        (list, tuple)) and isinstance(args[1], (list, tuple)):
            if len(args[0]) != len(args[1]):
                raise TypeError("Invalid list lengths")

            if (all(type(x) is int for x in args[0])
                    and all(type(x) is str for x in args[1])):
                for i in args[1]:
                    if i not in lists["To-do"]:
                        index = args[0][args[1].index(i)]
                        if not lists["To-do"] and index == 0:
                            lists["To-do"].append(i)
                            lists["Unchecked"].append(i)
                        elif index >= 0 and index < len(lists["To-do"]):
                            lists["To-do"].insert(index, i)
                            lists["Unchecked"].append(i)
                        else:
                            intReturn.append(str(index))
                            exist = True
                    else:
                        strReturn.append(i)
                        exist = True
            elif (all(type(x) is str for x in args[0])
                  and all(type(x) is int for x in args[1])):
                for i in args[0]:
                    if i not in lists["To-do"]:
                        index = args[1][args[0].index(i)]
                        if not lists["To-do"] and index == 0:
                            lists["To-do"].append(i)
                            lists["Unchecked"].append(i)
                        elif index >= 0 and index < len(lists["To-do"]):
                            lists["To-do"].insert(index, i)
                            lists["Unchecked"].append(i)
                        else:
                            intReturn.append(str(index))
                            exist = True
                    else:
                        strReturn.append(i)
                        exist = True
            else:
                raise TypeError(
                    "One parameter must contain strictly numbers, another must contain strictly strings"
                )
        else:
            raise TypeError("Invalid parameters")

        if exist and len(intReturn) > 0:
            err.append("   Add: Index(ces) [" + ", ".join(intReturn) +
                       "] are out of bound")
        if exist and len(strReturn) > 0:
            err.append("   Add: Item(s) [" + ", ".join(strReturn) +
                       "] do not exist")

    else:
        raise IndexError("Invalid number of arguments")


################### REMOVE + CLEAR ###################


def rem(i):
    exist = False
    intReturn = []
    strReturn = []

    if isinstance(i, str):
        if (i + "-c" in lists["Checked"]):
            lists["To-do"].remove(i + "-c")
            lists["Checked"].remove(i + "-c")
            lists["Discarded"].add(i + "-c")
        elif (i in lists["Unchecked"]):
            lists["To-do"].remove(i)
            lists["Unchecked"].remove(i)
            lists["Discarded"].add(i)
        else:
            strReturn.append(i)
            exist = True
    elif isinstance(i, int):
        if i >= 0 and i < len(lists["To-do"]):
            remVal = lists["To-do"].pop(i)
            if remVal in lists["Checked"]:
                lists["Checked"].remove(remVal)
            elif remVal in lists["Unchecked"]:
                lists["Unchecked"].remove(remVal)
            lists["Discarded"].add(remVal)
        else:
            intReturn.append(str(i))
            exist = True
    elif isinstance(i, (tuple, list)):
        for item in i:
            if isinstance(item, str):
                if (item + "-c" in lists["Checked"]):
                    lists["To-do"].remove(item + "-c")
                    lists["Checked"].remove(item + "-c")
                    lists["Discarded"].add(item + "-c")
                elif (item in lists["Unchecked"]):
                    lists["To-do"].remove(item)
                    lists["Unchecked"].remove(item)
                    lists["Discarded"].add(item)
                else:
                    strReturn.append(item)
                    exist = True
            elif isinstance(item, int):
                if item >= 0 and item < len(lists["To-do"]):
                    remVal = lists["To-do"].pop(item)
                    if remVal in lists["Checked"]:
                        lists["Checked"].remove(remVal)
                    elif remVal in lists["Unchecked"]:
                        lists["Unchecked"].remove(remVal)
                    lists["Discarded"].add(remVal)
                else:
                    intReturn.append(str(item))
                    exist = True
            else:
                raise TypeError("Item wasn't a string or an integer")
    else:
        raise TypeError("Item wasn't a list, tuple, string, or an integer")

    if exist and len(intReturn) > 0:
        err.append("Remove: Index(ces) [" + ", ".join(intReturn) +
                   "] are out of bound")
    if exist and len(strReturn) > 0:
        err.append("Remove: Item(s) [" + ", ".join(strReturn) +
                   "] do not exist")


def clearTodo():
    [lists["Discarded"].add(i) for i in lists["To-do"]]
    lists["To-do"].clear()
    lists["Checked"].clear()
    lists["Unchecked"].clear()


def clearDiscarded():
    lists["Discarded"].clear()


def clearError():
    err.clear()


def clearAll():
    clearTodo()
    clearDiscarded()
    clearError()


################### CHECK + UNCHECK ###################


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


'''
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
'''

### Add
add(["Eat", "Drink", "Sleep"])
add(["Swim", "Laugh", "Superhero", "♣"], [0,0,10,0])
add([1024, "Fruit", "Life", 1738, "Drink"])
add("Run", 8)
add("Alligator")
add("Doink", 6)
# add([1, 2, 2, 2], ["Watermelon", "Grass", "Apple", "Beans"])
# add([1, 2, 4, 0], [1, "Fish", 2, 6])
# add(["Watermelon", "Grass", "Apple", "Beans"], ["Watermelon", "Grass", "Apple", "Beans"])

### Remove
rem(["Laugh", "Laugh", "Swim", "sWim", "Drink"])
rem([0,16,0,222,0])
# clearAll()

dspAll()