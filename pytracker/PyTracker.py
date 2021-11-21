import json
import os
import random
import string


class PyTracker:
    def __init__(self, path):
        self.path = path
        self.state = self.loadState()
        self.currentState = self.getCurrentStat(self.path)

    def loadState(self):
        with open('data.json', 'r') as fp:
            try:
                return json.load(fp)
            except ValueError as e:
                return {"files": [], "directories": []}

    def saveCurrentStat(self):
        with open('data.json', 'w') as fp:
            json.dump(self.currentState, fp)

    # get list files and directories in specific path
    def getCurrentStat(self, path=""):
        listFiles = []
        listDirs = []

        for root, dirs, files in os.walk(path, topdown=True):
            print(''.join(random.choice(string.ascii_letters) for i in range(random.randint(0, 120))), end="\n")
            os.system('color {}'.format(random.randint(0, 9)))

            for dir in dirs:
                listDirs.append(dir)
            for file in files:
                listFiles.append(file)

        print("\n" + "-" * 70 + "\n")

        return {"files": listFiles, "directories": listDirs}

    def getNewAddedElement(self):
        newFiles = []
        for file in self.currentState["files"]:
            if file not in self.state["files"]:
                newFiles.append(file)

        newDirectories = []
        for dir in self.currentState["directories"]:
            if dir not in self.state["directories"]:
                newDirectories.append(dir)

        return {"files": newFiles, "directories": newDirectories}

    def getRemovedElement(self):
        removedFiles = []
        for oldElement in self.state["files"]:
            if oldElement not in self.currentState["files"]:
                removedFiles.append(oldElement)

        removedDirectories = []
        for oldElement in self.state["directories"]:
            if oldElement not in self.currentState["directories"]:
                removedDirectories.append(oldElement)

        return {"files": removedFiles, "directories": removedDirectories}
