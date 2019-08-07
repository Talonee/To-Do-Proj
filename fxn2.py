from item import Item

class ToDo(Item):

    def __init__(self):
        pass


    lists = {"To-do": [], "Checked": [], "Unchecked": [], "Discarded": set(())}
    err = []  # show all error messages

    ################### DISPLAY ###################


    # display calendar
    def dspTdl(self):
        print("To-do:")
        for i in self.lists["To-do"]:
            i.printItem()


    def dspCkd(self):
        print("Checked:")
        for i in self.lists["Checked"]:
            print("   +", i)


    def dspUck(self):
        print("Unchecked:")
        for i in self.lists["Unchecked"]:
            print("   -", i)


    def dspDsc(self):
        print("Discarded:")
        for i in self.lists["Discarded"]:
            if i[-2:] == "-c":
                print("   +", i)
            else:
                print("   -", i)


    def dspAll(self):
        # updateAll()
        self.dspTdl()
        print()
        self.dspCkd()
        print()
        self.dspUck()
        print()
        self.dspDsc()
        self.dspError()


    def dspError(self):
        print()
        print()
        print()
        print("****************************")
        print("Warning(s):")
        print()
        if len(self.err) == 0:
            print("No errors found.")
        else:
            for i in self.err:
                print(i)


    ################### ADD ###################


    def add(self, *args):
        exist = False
        intReturn = []
        strReturn = []

        if len(args) == 1:
            if isinstance(args[0],
                        (str, int)) and (str(args[0]) not in self.lists["To-do"]):
                self.lists["To-do"].append(Item(str(args[0])))
                self.lists["Unchecked"].append(Item(str(args[0])))
            elif isinstance(args[0],
                            (str, int)) and (str(args[0]) in self.lists["To-do"]):
                self.err.append("Item [" + str(args[0]) + "] already exist")
            elif isinstance(args[0], (list, tuple)):
                for item in args[0]:
                    if item not in self.lists["To-do"]:
                        self.lists["To-do"].append(str(item))
                        self.lists["Unchecked"].append(str(item))
                    else:
                        strReturn.append(str(item))
                        exist = True
                if exist:
                    self.err.append("   Add: Item(s) [" + ", ".join(strReturn) +
                            "] already exist.")

        elif len(args) == 2:  # index + item
            if isinstance(args[0], (str, int)) and isinstance(args[1], (str, int)):
                if isinstance(args[0], str) and isinstance(args[1], int):
                    if not self.lists["To-do"] and args[1] == 0:
                        self.lists["To-do"].append(args[0])
                        self.lists["Unchecked"].append(args[0])
                    elif args[1] >= 0 and args[1] < len(self.lists["To-do"]):
                        self.lists["To-do"].insert(args[1], args[0])
                        self.lists["Unchecked"].append(args[0])
                    else:
                        intReturn.append(str(args[1]))
                        exist = True
                elif isinstance(args[0], int) and isinstance(args[1], str):
                    if not self.lists["To-do"] and args[0] == 0:
                        self.lists["To-do"].append(args[1])
                        self.lists["Unchecked"].append(args[1])
                    elif args[0] >= 0 and args[0] < len(self.lists["To-do"]):
                        self.lists["To-do"].insert(args[0], args[1])
                        self.lists["Unchecked"].append(args[1])
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
                        if i not in self.lists["To-do"]:
                            index = args[0][args[1].index(i)]
                            if not self.lists["To-do"] and index == 0:
                                self.lists["To-do"].append(i)
                                self.lists["Unchecked"].append(i)
                            elif index >= 0 and index < len(self.lists["To-do"]):
                                self.lists["To-do"].insert(index, i)
                                self.lists["Unchecked"].append(i)
                            else:
                                intReturn.append(str(index))
                                exist = True
                        else:
                            strReturn.append(i)
                            exist = True
                elif (all(type(x) is str for x in args[0])
                    and all(type(x) is int for x in args[1])):
                    for i in args[0]:
                        if i not in self.lists["To-do"]:
                            index = args[1][args[0].index(i)]
                            if not self.lists["To-do"] and index == 0:
                                self.lists["To-do"].append(i)
                                self.lists["Unchecked"].append(i)
                            elif index >= 0 and index < len(self.lists["To-do"]):
                                self.lists["To-do"].insert(index, i)
                                self.lists["Unchecked"].append(i)
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
                self.err.append("   Add: Index(ces) [" + ", ".join(intReturn) +
                        "] are out of bound")
            if exist and len(strReturn) > 0:
                self.err.append("   Add: Item(s) [" + ", ".join(strReturn) +
                        "] do not exist")

        else:
            raise IndexError("Invalid number of arguments")


    ################### REMOVE + CLEAR ###################


    def rem(self, i):
        exist = False
        intReturn = []
        strReturn = []

        if isinstance(i, str):
            if (i + "-c" in self.lists["Checked"]):
                self.lists["To-do"].remove(i + "-c")
                self.lists["Checked"].remove(i + "-c")
                self.lists["Discarded"].add(i + "-c")
            elif (i in self.lists["Unchecked"]):
                self.lists["To-do"].remove(i)
                self.lists["Unchecked"].remove(i)
                self.lists["Discarded"].add(i)
            else:
                strReturn.append(i)
                exist = True
        elif isinstance(i, int):
            if i >= 0 and i < len(self.lists["To-do"]):
                remVal = self.lists["To-do"].pop(i)
                if remVal in self.lists["Checked"]:
                    self.lists["Checked"].remove(remVal)
                elif remVal in self.lists["Unchecked"]:
                    self.lists["Unchecked"].remove(remVal)
                self.lists["Discarded"].add(remVal)
            else:
                intReturn.append(str(i))
                exist = True
        elif isinstance(i, (tuple, list)):
            for item in i:
                if isinstance(item, str):
                    if (item + "-c" in self.lists["Checked"]):
                        self.lists["To-do"].remove(item + "-c")
                        self.lists["Checked"].remove(item + "-c")
                        self.lists["Discarded"].add(item + "-c")
                    elif (item in self.lists["Unchecked"]):
                        self.lists["To-do"].remove(item)
                        self.lists["Unchecked"].remove(item)
                        self.lists["Discarded"].add(item)
                    else:
                        strReturn.append(item)
                        exist = True
                elif isinstance(item, int):
                    if item >= 0 and item < len(self.lists["To-do"]):
                        remVal = self.lists["To-do"].pop(item)
                        if remVal in self.lists["Checked"]:
                            self.lists["Checked"].remove(remVal)
                        elif remVal in self.lists["Unchecked"]:
                            self.lists["Unchecked"].remove(remVal)
                        self.lists["Discarded"].add(remVal)
                    else:
                        intReturn.append(str(item))
                        exist = True
                else:
                    raise TypeError("Item wasn't a string or an integer")
        else:
            raise TypeError("Item wasn't a list, tuple, string, or an integer")

        if exist and len(intReturn) > 0:
            self.err.append("Remove: Index(ces) [" + ", ".join(intReturn) +
                    "] are out of bound")
        if exist and len(strReturn) > 0:
            self.err.append("Remove: Item(s) [" + ", ".join(strReturn) +
                    "] do not exist")


    def clearTodo(self):
        [self.lists["Discarded"].add(i) for i in self.lists["To-do"]]
        self.lists["To-do"].clear()
        self.lists["Checked"].clear()
        self.lists["Unchecked"].clear()


    def clearDiscarded(self):
        self.lists["Discarded"].clear()


    def clearError(self):
        self.err.clear()


    def clearAll(self):
        clearTodo()
        clearDiscarded()
        clearError()


    ################### CHECK + UNCHECK ###################


    # def check(i):
    #     if isinstance(i, int) and (i >= 0 and i < len(lists.get("To-do"))):
    #         lists.get("Unchecked").remove(lists.get("To-do")[i])
    #         lists.get("To-do")[i] = lists.get("To-do")[i] + "-c"
    #         lists.get("Checked").append(lists.get("To-do")[i])
    #     elif isinstance(i, str) and (i in lists.get("To-do")):
    #         lists.get("Unchecked").remove(i)
    #         index = lists.get("To-do").index(i)
    #         lists.get("To-do")[index] = lists.get("To-do")[index] + "-c"
    #         lists.get("Checked").append(lists.get("To-do")[index])
    #     else:
    #         print("Invalid Input")


    # def uncheck(i):
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

