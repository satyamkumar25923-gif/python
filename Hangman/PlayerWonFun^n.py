import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
display = placeholder

while not game_over:
    guess = input("Guess a letter: ").lower()

    new_display = ""

    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            new_display += letter
        else:
            new_display += display[position]

    display = new_display
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")
