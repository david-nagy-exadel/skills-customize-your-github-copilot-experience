# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Word Bank and Game State

#### Description
Create a predefined list of words and write the logic to randomly select one at the start of each game. Initialize the game state by tracking guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Define a list of at least 10 words for the game to draw from.
- Randomly select one word at the start using the `random` module.
- Initialize a variable to track the number of incorrect guesses remaining (e.g., 6).
- Initialize a set or list to store letters the player has already guessed.

### 🛠️ Handle Player Input and Display Progress

#### Description
Implement the main game loop that accepts letter guesses from the player and updates the display to show correctly guessed letters and remaining blanks.

#### Requirements
Completed program should:

- Prompt the player to enter a letter guess each turn.
- Validate that the input is a single alphabetical character.
- Display the current progress in `_ _ _` format, revealing correctly guessed letters.
- Inform the player if a guessed letter is correct or incorrect.
- Show the number of incorrect guesses remaining after each turn.
- Example output after a correct guess:
  ```
  Word: _ p p _ e
  Incorrect guesses left: 5
  ```

### 🛠️ Implement Win and Lose Conditions

#### Description
Add logic to detect when the game ends — either the player guesses the full word or runs out of attempts — and display an appropriate message.

#### Requirements
Completed program should:

- End the game and display a congratulations message when all letters are correctly guessed.
- End the game and display a losing message (revealing the hidden word) when incorrect guesses reach zero.
- Example win message: `Congratulations! You guessed the word: apple`
- Example lose message: `Game over! The word was: apple`

