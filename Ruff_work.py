import nltk
import sys
import traceback
from nltk.sentiment import SentimentIntensityAnalyzer

aListOfAllTheSamples = ["names", "stopwords", "state_union", "twitter_samples", "movie_reviews",
"averaged_perceptron_tagger", "vader_lexicon", "punkt"]

# nltk.download(aListOfAllTheSamples)

wordCount = nltk.corpus.stopwords.words("english")
print(wordCount)

aSentimentAnalysis = SentimentIntensityAnalyzer()
ASentimentValue = aSentimentAnalysis.polarity_scores("Amazon is a bad company")
print(ASentimentValue)


"""
except AttributeError as err:
    print(err)
    err = nltk.download("shakespeare")
finally:
    wordCount = nltk.corpus.shakespere.words()
"""
