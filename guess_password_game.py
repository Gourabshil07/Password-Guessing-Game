import random
def play_round(category,easy_words, medium_words, hard_words):
    difficulty = input("Enter difficulty level(easy, medium, hard): ").strip().lower()

    if difficulty == 'easy':
        secret = random.choice(easy_words)
    elif difficulty == 'medium':
        secret = random.choice(medium_words)
    elif difficulty == 'hard':
        secret = random.choice(hard_words)
    else:
        print("Invalid input! Defaulting to EASY Level.")
        secret = random.choice(easy_words)
    
    attempts = 0
    while True:
        guess = input("\nEnter your guess: ").strip().lower()
        attempts += 1

        if guess == secret:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts")
            break
        else:
            print("\n❌ Wrong guess. Try again!")
        
        hint = ""
        for i in range(len(secret)):
            if i<len(guess) and guess[i] == secret[i]:
                hint += guess[i]
            else:
                hint += '_'
        print("\n🔎 Hint:", " ".join(hint))

    print("\nGame Over. Thanks for playing!\n")

def main():
    while True:
        print("\n==== Welcome to the password guessing game ====")

        print("\nChoose a category of password guessing (FOOD| ANIMAL | PLACE )")

        category = input("Select category: ").strip().lower()

        if category == 'food':
            play_round('food',
                        ['pizza','mango','grape','bread','apple'],
                        ['banana','butter','tomato','noodle','pickle'],
                        ['icecream','sandwich','chocolate','pineapple','biriyani']
                        )
        elif category == 'animal':
            play_round('animals',
                    ['lion','frog','bear','zebra','wolf','deer','tiger'],
                    ['rabbit','monkey','donkey','turkey','pigeon'],
                    ['elephant','crocodile','kangaroo','alligator','porcupine']
                    )
        elif category == 'place':
            play_round('place',
                    ['india','delhi','river','beach','paris'],
                    ['london','sydney','forest','desert'],
                    ['mountains','australia','singapore','indonesia','himalayas'])
                
        else:
            print("⚠ Invalid input! please choose again.")
            continue

        replay = input("Do you want to play again?(Y/N): ").strip().upper()
        if replay != 'Y':
            print("Goodbye!")
            break
        
main()

   
       
