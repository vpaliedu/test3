import game_data
import random

score = 0
inGame = True
guessedNum = 0

def checker(guess, numA, numB):
    global inGame
    global score

    if guess == "a":
        guessedNum = game_data.data[numA]['follower_count']
        if guessedNum > game_data.data[numB]['follower_count']:
            score +=1
            return "You right! {score}"
        else:
            inGame = False
            return f"You loose, final score {score}"
    else:
        guessedNum = game_data.data[numB]['follower_count']
        if guessedNum > game_data.data[numA]['follower_count']:
            score +=1
            return f"You right! {score}"
        else:
            inGame = False
            return f"You loose, final score {score}"

while inGame == True:
    numA = random.randint(0,49)
    numB = random.randint(0,49)

    while numA==numB:
        numB = random.randint(0,49)
    print(f"A: {game_data.data[numA]['name']},{game_data.data[numA]['description']}, {game_data.data[numA]['country']}")
    print("VS")
    print(f"B: {game_data.data[numB]['name']},{game_data.data[numB]['description']}, {game_data.data[numB]['country']}")
    guess = input("Which is higher? a/b?")
    print(checker(guess, numA, numB))