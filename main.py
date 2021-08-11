# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from objectIntegrator import objectIntegrator
import nltk
import positiveSentence
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from separatorFunction import separatorFunction
#  nltk.download()
#  aListOfAllTheSamples = ["names", "stopwords", "state_union", "twitter_samples", "movie_reviews",
#  "averaged_perceptron_tagger", "vader_lexicon", "punkt"]
#  nltk.download(aListOfAllTheSamples)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Brandon')

    with open("anArticle.txt", mode="r") as file:
        readFileObject = file.read()
        separator = separatorFunction(readFileObject)
        listOfAllLines = separator.separator()

    aSentimentAnalysis = SentimentIntensityAnalyzer()
    aDictionarySum = objectIntegrator()

    for count, line in enumerate(listOfAllLines,0):
        ASentimentValue = aSentimentAnalysis.polarity_scores(line)
        print(line)
        #  ASentimentValue is a variable that judges the sentence of a line given.
        #  it is a dictionary with four keys and its associated values.
        print(f"first line :{count} and its analysis is ", ASentimentValue)
        aDictionarySum.integrator(ASentimentValue)

# objectIntegrator.aDict is a Dictionary that has average summation and aDictionarySum.count has the
# count value of the lines.


#  help(nltk.corpus.state_union.words())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
