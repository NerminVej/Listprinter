spam = ['apples', 'bananas', 'tofu', 'cats']


def listprinter(listInput):
    if listInput == "":
        return
    else:
        for i, item in enumerate(listInput):
            if len(listInput) - i == 1:
                print("and " + item + ".")
            else:
                print(item + ", ")


listprinter(spam)
