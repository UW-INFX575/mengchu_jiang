__author__ = 'sara'


import string
from stemming.porter2 import stem
import nltk
from nltk.util import ngrams
from nltk import bigrams
from nltk import trigrams

# stop words list reference
# http://www.ranks.nl/stopwords
stopWordsList = open("//Users//sara//Github//mengchu_jiang//Assignment2//longStopWordsList.txt").read().splitlines()

# remove punctuation from the file
def removePunctuation(fileStr):
    table = string.maketrans("","")
    return fileStr.translate(table, string.punctuation)

# remove numbers
def removeNumbers(fileStr):
    return ''.join([i for i in fileStr if not i.isdigit()])

# strip stop words from the file
def removeStopWords(bagOfWords):
    words = []
    for word in bagOfWords:
        if word not in stopWordsList:
            words.append(word)
    return words

# stemming
# library stemming 1.0.1
def stem(bagOfWords):
    words = []
    for word in bagOfWords:
        words.append(word)
    return words


# main code
if __name__ == '__main__':
    # open and read file
    index = 6334220
    for i in range(10):
        index = index + i
        aFile = open("//Users//sara//Documents//MSIM课程//INFX_575//Assignments//2//%s.txt" % index)
        lines = aFile.readlines()

        # remove punctuation from the file
        newLines = removePunctuation(lines[0])
        # remove numbers
        newLines = removeNumbers(newLines)
        # switch to lowercase
        newLines = newLines.lower()
        # and split sentences into a list of words
        words = newLines.split()

        # strip stop words from the file
        cleanedWords = removeStopWords(words)

        # stemming
        cleanedWords = stem(cleanedWords)

        # count number of unique words in the list
        uniqueWords = []
        count = []
        for word in cleanedWords:
            if word not in uniqueWords:
                uniqueWords.append(word)
                count.append(0)

        # count frequency for each unique word
        for word in cleanedWords:
            for i in range(len(uniqueWords)):
                if word == uniqueWords[i]:
                    count[i] = count[i]+1

        # write result into file
        # unigrams
        output1 = open("//Users//sara//Github//mengchu_jiang//Assignment2//unigram%s.txt" % index,"wr")

        for i in range(len(uniqueWords)):
            output1.write("%s,%s\n" % (uniqueWords[i],count[i]))
        output1.close()

        # get bigrams, trigrams
        # and frequency of each n grams
        bigramsWords = bigrams(cleanedWords)
        trigramsWords = trigrams(cleanedWords)
        frequencyBi = nltk.FreqDist(bigramsWords)
        frequencyTri = nltk.FreqDist(trigramsWords)

        # write to file
        # bigrams
        output2 = open("//Users//sara//Github//mengchu_jiang//Assignment2//bigram%s.txt" % index,"wr")
        for key in frequencyBi.keys():
            output2.write("%s %s,%s\n" % (key[0], key[1],frequencyBi[key]))
        output2.close()

        # trigrams
        output3 = open("//Users//sara//Github//mengchu_jiang//Assignment2//trigram%s.txt" % index,"wr")
        for key in frequencyTri.keys():
            output3.write("%s %s,%s\n" % (key[0], key[1],frequencyTri[key]))
        output3.close()