import string

alphabetE = []

for i in range(0, len(string.ascii_lowercase)):
    alphabetE.append(string.ascii_lowercase[i])

def returnIndex(list, value):
    for i in range(0,len(list)):
        if list[i] == value:
            return i

def encodeCeaser(message, shift):
    shift = int(shift)
    letterList = []
    message = message.lower()
    for i in range (0, len(message)):
        letterList.append(message[i])
    
    for i in range(0, len(letterList)):
        if not letterList[i] in alphabetE:
            continue
        index = returnIndex(alphabetE, letterList[i])
        letterList[i] = alphabetE[index + shift]
    return "".join(letterList)

def decodeCeaser(message, shift):
    if int(shift) == 0:
        return message
    elif int(shift) <= 0:
        return "Not possible to shift negative"
    else:
        shift = int(shift)
        letterList = []
        message = message.lower()
        for i in range (0, len(message)):
            letterList.append(message[i])
        for i in range(0, len(letterList)):
            if not letterList[i] in alphabetE:
                continue
            index = returnIndex(alphabetE, letterList[i])
            letterList[i] = alphabetE[index - shift]
        return "".join(letterList)

var = int(input('''What encoding method would you like to use?:
      1. Pig Latin
      2. Ceaser Ciper'''))

if var == 1:
    import PigLatin
    
elif var == 2:
    var2 = int(input("""What would you like to do?:
                     1. Encode
                     2. Decode"""))
    if var2 == 1:
        msgInput = str(input("What do you want to encode?: "))
        shiftInput = int(input("What is your shift?: "))
        print("Your message is: " + encodeCeaser(msgInput, shiftInput))

    if var2 == 2:
        msgInput = str(input("What do you want to decode: "))
        shiftInput = int(input("What is your shift?: "))
        print("Your message is: " + decodeCeaser(msgInput, shiftInput))