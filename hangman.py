from os import system
import random
import hangman_art, hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

system('cls')
print(hangman_art.logo)
print(hangman_art.stages[lives])

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guesses = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    system('cls')
    print(hangman_art.logo)
    print(hangman_art.stages[lives])

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        if guess in guesses:
            print(f"You have already guessed {guess}. Try again.")
        else:
            guesses += guess
            print(f"The letter [{guess}] is not in this word.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                system('cls')
                print(hangman_art.logo)
                print(hangman_art.stages[lives])
                print("You lose.")
                print(f'The word was {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
