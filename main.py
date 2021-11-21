from pytracker.TextColor import TextColor
from pytracker.PyTracker import PyTracker


def run():
    # C:\hpswsetup\sp99146\DCHU\src
    tracker = PyTracker(input("Enter absolut path of dir to be tracked: "))
    #tracker = PyTracker("C:\hpswsetup\sp99146\DCHU\src")

    newAddElement = tracker.getNewAddedElement()
    print(TextColor.OKGREEN + "{} file added, {} directory added.".format(len(newAddElement["files"]), len(newAddElement["directories"])))
    for element in newAddElement["directories"] + newAddElement["files"]:
        print(element)

    removedElement = tracker.getRemovedElement()
    print("\n" + TextColor.FAIL + "{} file removed, {} directory removed.".format(len(removedElement["files"]), len(removedElement["directories"])))
    for element in removedElement["directories"] + removedElement["files"]:
        print(element)

    print(TextColor.ENDC)
    if input("you want to save current state ? [y|n] ") == "y":
        tracker.saveCurrentStat()
        print("state saved successfully")


if __name__ == '__main__':
    run()
