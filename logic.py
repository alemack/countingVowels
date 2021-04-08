it_works = True

def countvowels(string):
    countA = 0
    countE = 0
    countI = 0
    countO = 0
    countU = 0
    countY = 0

    string = string.lower()

    for i in range(len(string)):
        if (string[i] == "a"):
            countA += 1
        elif (string[i] == "e"):
            countE += 1
        elif (string[i] == "i"):
            countI += 1
        elif (string[i] == "o"):
            countO += 1
        elif (string[i] == "u"):
            countU += 1
        elif (string[i] == "y"):
            countY += 1
        else:
            i = i + 1

    print(f"a {countA}, o {countO}, u {countU}, i {countI}, e {countE}, y {countY}")


while it_works:
    string = input()
    countvowels(string)