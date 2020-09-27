def word_map(texts):
    """
    Inputs a list of string texts
    Returns a dictionary of unique words and their occurrences over texts
    """
    # Write your code here
    
    wordmapDic = {}
    # pre-porcess the list
    wordList = []
    for text in texts:
        oneList = text.split(" ")
        wordList.extend(oneList)
    # add to the dictionary
    for word in wordList:
        word = word.lower()
        if word in wordmapDic:
            wordmapDic[word] += 1
        elif word != "":
            wordmapDic[word] = 1 
    
    return wordmapDic
    
    
def uncommon_word_map(texts):
    """
    Inputs a list of string texts
    Returns a dictionary of unique uncommon words and their occurrences over texts
    """
    # Write your code here
    
    commonwordsLines = []
    file1 = open('commonwords.txt', 'r')

    commonwordsLines = file1.read().splitlines() 
    wordmapDic = {}
    # pre-porcess the list
    wordList = []
    for text in texts:
        oneList = text.split(" ")
        wordList.extend(oneList)
    # add to the dictionary 
    for word in wordList:
        word = word.lower()
        if word not in commonwordsLines:
            if word in wordmapDic:
                wordmapDic[word] += 1
            elif word != "":
                wordmapDic[word] = 1 

    return wordmapDic
    


def check_word_map():
    texts = ["",
        "Life is like Machine Learning  ",
        "We are learning from experience"]
    result = word_map(texts)
    for key in sorted(result.keys()):
        print(key, ":", result[key])

def check_word_map2():
    texts = [""]
    result = word_map(texts)
    for key in sorted(result.keys()):
        print(key, ":", result[key])


def check_uncommon_word_map():
    texts = [
        "Life is like Machine Learning",
        "We are learning from experience"]
    result = uncommon_word_map(texts)
    for key in sorted(result.keys()):
        print(key, ":", result[key])

import os

def main():
    # check_word_map()
    cwd = os.getcwd()
    print(cwd)
    check_uncommon_word_map()


if __name__ == "__main__":
    main()
