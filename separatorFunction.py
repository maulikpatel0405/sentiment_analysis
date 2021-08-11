# This class here separates text files into a sentences in a list

class separatorFunction:

    def __init__(self, readFile):
        self.readFile = readFile

    def separator(self):
        listOfSentences = self.readFile.split(".")
        listOfSentences.pop()
        return listOfSentences

