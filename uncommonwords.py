###############################################################################
# Title: uncommonwords.py                                                     #
#                                                                             #
# Description: A script that takes in two files, a list of commons words and  #
# a text file. The goal being to remove all common words from the text file   #
# and then count all words remaining. Some assumptions are made here: words   #
# are case sensitive as in Cat and cat will be treated as two different words.#
# Also, I check for hyphens so that "guinea-pig" is treated as two words      #
# "guinea" and "pig". Beginning and trailing "'"s are removed as well.        #
# Also assuming that the input file common.txt is new line delimited          #
#                                                                             #
# author: Chris Robus                                                         #
# date: 09/05/2019                                                            #
###############################################################################

import sys
import re

PUNCTUATION = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~1234567890 '


def main():
    commonWords = sys.argv[1]
    inputText = sys.argv[2]

    resultList = {}
    commonWordList = []
    unfilteredWords = []
    filteredWords = []

    # Grab our common words strip out new line tags
    # then make everything lower case for easier comparisons.
    commonWordList = [line.rstrip('\n').lower() for line in open(commonWords)]

    with open(inputText, 'r') as f:
        unfilteredWords = f.read().split()

    for item in unfilteredWords:
        # We want to check the special case of hypened words
        for word in item.split("-"):
            insertWord = Filter(word)
            if insertWord != '':
                filteredWords.append(insertWord)

    results = [
        word for word in filteredWords if word.lower() not in commonWordList
    ]

    # Word count
    for item in results:
        if item in resultList.keys():
            resultList[item] = resultList[item] + 1
        else:
            resultList[item] = 1

    # Print out the formated results sorted by Keys
    for key in sorted(resultList.keys(), key=lambda s: s.lower()):
        output = str.ljust(key, 15)
        outputNums = ":" + str.rjust(str(resultList[key]), 5)
        output = output + outputNums
        print(output)


def Filter(word):
    # In order to be version agnostic and still leverage the power of
    # translate() we need to check Python version and run the appropriate code.
    if sys.version_info[0] < 3:
        word = word.translate(None, PUNCTUATION)
    else:
        table = str.maketrans(dict.fromkeys(PUNCTUATION))
        word = word.translate(table)

    # Remove trailing and leading '.
    word = re.sub(r"\'$|^\'", "", word)
    return word


if __name__ == "__main__":
    main()
