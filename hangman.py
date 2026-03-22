import random

stages = [
    """
      -----
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """
]

word_list = ["lantern", "velocity", "marble", "compass", "football"]

lives = 6
chosen_word = random.choice(word_list)

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"{lives}/6 LIVES LEFT")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:

        if letter == guess:
            display += letter

            if guess not in correct_letters:
                correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word.")

        if lives == 0:
            game_over = True
            print("YOU LOSE")
            print("The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("YOU WIN")

    print(stages[lives])