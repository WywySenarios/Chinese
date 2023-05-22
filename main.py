import random
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# read the file
f = open("C:/Python/Chinese/characters.txt", "rb")
rawData = f.read().decode("UTF-8")
data = rawData.split("\r\n")
while True:  # remove all empty inputs
    try:
        data.remove("")
    except:
        break

# split data into indexes

characters = []
accentedPinyin = []
numberedPinyin = []
translation = []

for index in range(len(data)):
    if data[index][0] == "#":
        continue

    if index % 4 == 0:
        numberedPinyin.append(data[index])
    elif index % 4 == 1:
        translation.append(data[index])
    elif index % 4 == 2:
        characters.append(data[index])
    else:
        accentedPinyin.append(data[index])

'''
print(characters)
print(accentedPinyin)
print(numberedPinyin)
print(translation)
'''

'''
Each item has three information points.
Index 0: Characters in Chinese
Index 1: Pinyin (Accented format)
Index 2: Pinyin (Non accented format)
Index 3: English translation
Tests will be on index 0 and index 2 (Chinese and pinyin).
When pinyin is tested, use the number/letter format instead of the accented format.

Sample character:
你好
nǐ hǎo
ni3 hao3
hello (to you)
'''

running = True
userChoice = ""
userAnswer = ""
exitKeys = ["4", "-1", "exit", "Exit", "EXIT"]
booleanKeys = ["true", "yes", "1", "y", "t"]
nullKeys = ["null", "N/A", "n/a", "none", "NaN", "nan"]
now = "C:/Python/Chinese/tests/" + time.strftime("%Y-%m-%d")
temp = 1
try:
    testResults = open(now + ".txt", "x")
except FileExistsError:
    while True:
        try:
            testResults = open(now + " (" + str(temp) + ").txt", "x")
            testResults.close()
            testResults = open(now + " (" + str(temp) + ").txt", "ab")
            break
        except FileExistsError:
            temp += 1

while running:
    correct = 0

    while running:
        print("There are three tests.")
        print("\t1) Pinyin to character")
        print("\t2) Character to pinyin")
        print("\t3) English to character and pinyin")
        print("\t4) [-1 to exit]")
        userChoice = input("What would you like to test?\n")
        if userChoice == "1" or userChoice == "2" or userChoice == "3":
            break

        for x in exitKeys:  # check if user wants to exit
            if x == userChoice:
                running = False

        if running:
            input("Invalid selection.\nAcknowledged... ")
            clear()

    if not running:
        break

    while True:  # get test length
        try:
            testLength = int(input("How many characters would you like to test?\n"))
            if testLength > 0:
                break
        except:
            pass
        print("You must test a positive integer number of characters.")

    clear()

    questionIndexes = []

    for x in range(testLength):
        temp = True

        while temp:
            questionIndex = random.randint(0, len(characters) - 1)
            temp = False
            for y in questionIndexes:
                if questionIndex == y:
                    temp = True

            if userChoice == "3":

                for y in nullKeys:
                    if y == translation[questionIndex]:
                        temp = True
        questionIndexes.append(questionIndex)

    if userChoice == "1":  # pinyin to character
        for x in range(testLength):  # test each character
            print("Question " + str(x + 1)); testResults.write(("Question " + str(x + 1)).encode("UTF-8"))
            questionIndex = questionIndexes[x]
            print("This character has the following pinyin: " + accentedPinyin[questionIndex] + " (" + numberedPinyin[
                questionIndex] + ")")
            input("Please write the character out.\nAcknowledged...")

            userAnswer = input(
                "This was the character: " + characters[questionIndex] + ".\nWas this your answer?\n").lower()

            for y in booleanKeys:
                if userAnswer == y:
                    userAnswer = "correct"

            if userAnswer == "correct":
                correct += 1
                testResults.write("User wrote correct character.\n\n".encode("UTF-8"))
            else:
                testResults.write("User wrote incorrect character.\n\n".encode("UTF-8"))
            clear()

    elif userChoice == "2":  # character to pinyin
        for x in range(testLength):  # test each character
            print("Question", x + 1)
            testResults.write(("Question " + str(x + 1)).encode("UTF-8"))
            questionIndex = questionIndexes[x]

            userAnswer = input("Write out the pinyin for the following word: " + characters[questionIndex] + "\n")
            testResults.write(("\n\nWrite out the pinyin for the following word: " + characters[questionIndex] + "\n\nUser "
                                                                                                            "answer: "
                                                                                                            "" +
                              userAnswer).encode("UTF-8"))

            if userAnswer == accentedPinyin[questionIndex] or userAnswer == numberedPinyin[questionIndex]:
                correct += 1
                print("Correct!")
                testResults.write(" (correct)".encode("UTF-8"))
            else:
                print("Incorrect. The answer is " + accentedPinyin[questionIndex] + " (" + numberedPinyin[
                    questionIndex] + ")")
                testResults.write(" (incorrect)".encode("UTF-8"))
            testResults.write(("\nAnswer: " + accentedPinyin[questionIndex] + " (" + numberedPinyin[questionIndex] + ")\n\n").encode("UTF-8"))

            input("Acknowledged... ")
            clear()

    else:  # english to chinese
        for x in range(testLength):  # test each character
            print("Question", x + 1)

            print("For the word that translates to " + translation[
                questionIndex] + ", write out the pinyin and the character associated with it.")

            userAnswer = input("Write out the pinyin for this word.\n")

            input("\nPlease write the character out.\nAcknowledged...")

            print("\nThis was the character: " + characters[questionIndex])
            print("This was its pinyin: " + accentedPinyin[questionIndex] + " (" + numberedPinyin[questionIndex] + ")")
            testResults.write(("For the word that translates to " + translation[
                questionIndex] + ", write out the pinyin and the character associated with it.\n\nThis was the "
                                 "character: " + characters[questionIndex] + "\nThis was its pinyin: " + " (" +
                              numberedPinyin[questionIndex] + ")\n\nUser answer: " + userAnswer).encode("UTF-8"))

            if userAnswer == accentedPinyin[questionIndex] or userAnswer == numberedPinyin[questionIndex]:
                correct += 1
                print("Your pinyin was correct.\n")
                testResults.write(" (correct)".encode("UTF-8"))
            else:
                print("Your pinyin was incorrect.\n")
                testResults.write(" (incorrect)".encode("UTF-8"))
            testResults.write(("\nAnswer: " + accentedPinyin[questionIndex] + " (" + numberedPinyin[questionIndex] + ")\n\n").encode("UTF-8"))

            userAnswer = input("Was this your answer?\n").lower()

            for y in booleanKeys:
                if userAnswer == y:
                    userAnswer = "correct"

            if userAnswer == "correct":
                correct += 1
                testResults.write("User wrote correct character.\n\n".encode("UTF-8"))
            else:
                testResults.write("User wrote incorrect character.\n\n".encode("UTF-8"))

            clear()

    # tell user the results
    print("Here are your results:")
    testResults.write("\nHere are your results:\n".encode("UTF-8"))
    print(correct, "questions correct.")
    testResults.write((str(correct) + " questions correct.\n").encode("UTF-8"))

    if userChoice == "3":
        testLength *= 2
    print(str(testLength - correct) + " questions incorrect.\n")
    testResults.write((str(testLength - correct) + " questions incorrect.\n\n").encode("UTF-8"))

    print("\nYou have received a \033[1m", correct / testLength * 100, "%\033[0m final mark.", sep="")
    testResults.write(("\nYou have received a " + str(correct / testLength * 100) + "% final mark.\n\n***\n\n").encode("UTF-8"))
    input("Acknowledged... ")
    clear()

    testResults.close()
    testResults = open(now + " (" + str(temp) + ").txt", "ab")
