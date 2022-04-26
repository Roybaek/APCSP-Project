

def encodePigLatin():

    Sentence = input("What is the Sentence: \n")

    wordList = Sentence.split()

    returnList = []

    def pigLatin(word):
        word = word.lower()
        word.split()
        if (word[0] == "a" or word[0] == "e" or word[0] == 'i' or word[0] == 'o' or word[0] == 'u'):
            return(word + 'ay')
        else:
            newWord = word[1:len(word)] + word[0] + "ay"
            return(newWord)

    for i in range(0, len(wordList)):
        returnList.append(pigLatin(wordList[i]))



    return (" ".join(returnList))

print(encodePigLatin())