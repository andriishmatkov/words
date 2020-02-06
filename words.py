import random


with open(r"D:\Python38\wordsgame\ruwords.txt", "r", encoding="utf-8") as file:
    wordsList = file.read().splitlines()
wordsUsed = []
firstLetterPoints = {"а":4, "б":2, "в":2, "г":2, "д":3, "е":3, "ё":3, "ж":5, "з":4, "и":3, "й":3, "к":1, "л":1, "м":2, "н":1, "о":2, "п":1, "р":1, "с":1, "т":1, "у":4, "ф":3, "х":4, "ц":3, "ч":3, "ш":3, "щ":5, "ъ":15, "ы":15, "ь":15, "э":5, "ю":5, "я":4}
lastLetterPoints = {"а":1, "б":2, "в":2, "г":2, "д":2, "е":3, "ё":3, "ж":5, "з":4, "и":2, "й":3, "к":1, "л":1, "м":2, "н":1, "о":1, "п":1, "р":1, "с":1, "т":1, "у":4, "ф":3, "х":4, "ц":3, "ч":3, "ш":3, "щ":5, "ъ":15, "ы":15, "ь":1, "э":5, "ю":5, "я":2}
alphabet = ["а","б","в","г","д","е","ж","з","и","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","э","ю","я"]
badLetter = ["ъ","ы","ь"]
shift = 0

startingLetter = random.choice(alphabet)
lastLetter = ""
playerOnePoints = 0
playerTwoPoints = 0
earnedPoints = 0	
level = 1
playerOne = ""
playerTwo = ""

def checkLastLetterForBad(playerWord):
	global lastLetter
	shift = -1
	while True:
		lastLetter = playerWord[shift]
		if playerWord[shift] in badLetter:
			shift -= 1
			continue
		if playerWord[shift] == "й":
			lastLetter = "и"
			break
		if playerWord[shift] == "ё":
			lastLetter = "е"
			break
		break
	


def countPoints(playerWord):
	global playerOnePoints
	global playerTwoPoints
	global earnedPoints
	earnedPoints = 0	
	earnedPoints = firstLetterPoints.get(playerWord[0]) + lastLetterPoints.get(playerWord[-1])
	print("Заработано", earnedPoints, end="") 
	if earnedPoints >= 11 and earnedPoints <= 19:
		print(" очков.")
	elif earnedPoints % 10 == 1:
		print(" очко.")
	elif earnedPoints %10 >=2 and earnedPoints % 10 <= 4:
		print(" очка.")
	else:
		print(" очков.")
	#return(earnedPoints)

def checkEnterOne(playerWord):
	global playerOnePoints
	global playerTwoPoints
	global earnedPoints
	global lastLetter
	while True:
		if playerWord in wordsUsed:
			print ( "Слово ","\"", playerWord, "\""," уже было", sep="")
			playerWord = input ( "Введите другое слово: ")
			continue
		if playerWord not in wordsList:
			print ( "Я не знаю такого слова")
			playerWord = input ( "Введите другое слово: ")
			continue
		if playerWord[0] != lastLetter:
			print ( "Cлово начинается не с буквы " + "\"" + lastLetter + "\"", sep="")
			playerWord = input ( "Введите другое слово: ")
			continue
		break

	print ( "Слово ","\"", playerWord,"\""," принято", sep="")
	wordsUsed.append(playerWord)
	checkLastLetterForBad(playerWord)
	countPoints(playerWord)
	playerOnePoints = playerOnePoints + earnedPoints
	

def checkEnterTwo(playerWord):
	global playerOnePoints
	global playerTwoPoints
	global earnedPoints
	global level
	global lastLetter

	while True:
		if playerWord in wordsUsed:
			print ( "Слово ","\"", playerWord, "\""," уже было", sep="")
			playerWord = input ( "Введите другое слово: ")
			continue
		if playerWord not in wordsList:
			print ( "Я не знаю такого слова")
			playerWord = input ( "Введите другое слово: ")
			continue
		if playerWord[0] != lastLetter:
			print ( "Cлово начинается не с буквы " + "\"" + lastLetter + "\"", sep="")
			playerWord = input ( "Введите другое слово: ")
			continue
		break
	

	print ( "Слово ","\"", playerWord,"\""," принято", sep="")
	wordsUsed.append(playerWord)
	countPoints(playerWord)
	checkLastLetterForBad(playerWord)
	playerTwoPoints = playerTwoPoints + earnedPoints
	print("Счет: ", playerOnePoints, ":", playerTwoPoints)
	level += 1


print("Добро пожаловать в игру в слова.")
print("Давайте познакомимся!")
print()
playerOne = input("Игрок №1, введите свое имя: ")
print("Здравствуйте, " + playerOne + "!", sep="")
playerTwo = input("Игрок №2, введите свое имя: ")
print("Здравствуйте, " + playerTwo + "!", sep="")
print()

while playerOnePoints < 10 and playerTwoPoints < 10:
	if level == 1:
		print("НАЧАЛО ИГРЫ. Уровень ", level, ":" , sep="")
		lastLetter = startingLetter
		playerWord = input ( playerOne + ", Введите слово на букву " + "\"" + lastLetter + "\": " )
		checkEnterOne(playerWord)
		playerWord = input ( playerTwo + ", Введите слово на букву " + "\"" + lastLetter + "\": " )
		checkEnterTwo(playerWord)
		print()
	else: 
		print("Уровень ", level, ":", sep="")
		playerWord = input ( playerOne + ", Введите слово на букву " + "\"" + lastLetter + "\": " )
		checkEnterOne(playerWord)
		playerWord = input ( playerTwo + ", Введите слово на букву " + "\"" + lastLetter + "\": " )
		checkEnterTwo(playerWord)
		print()

print("КОНЕЦ ИГРЫ. Счет:", playerOnePoints, ":", playerTwoPoints)
print()
if playerOnePoints > playerTwoPoints:
	print("Победитель игры - " + playerOne)
elif playerOnePoints < playerTwoPoints:
	print("Победитель игры - " + playerTwo)
else:
	print("Ничья!")




input()



