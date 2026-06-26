## Guess the Number Game

A simple Python console-based game where the computer randomly selects a number between 1 and 100, and the player has to guess it. The program provides hints after each guess by indicating whether the player should choose a higher or lower number. The game continues until the correct number is guessed, and the total number of attempts is displayed at the end.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Important Concepts Learned from the "Guess the Number" Game

* Imported the `random` module to generate a random number for the game.

* Used `random.randint(start, end)` to generate a random integer within a specified range.

  * Example: `random.randint(1, 100)` generates a number between **1 and 100** (both inclusive).

* Used variables to store:

  * The secret random number (`n`)
  * The user's current guess (`user`)
  * The total number of attempts (`guesses`)

* Used a `while` loop to repeatedly ask the user for input until the correct number is guessed.

* Applied the loop condition `while(user != n)`:

  * The loop continues executing as long as the user's guess is different from the secret number.
  * The loop stops automatically when the user guesses the correct number.

* Took user input using `input()` and converted it to an integer using `int()`.

* Used conditional statements (`if`, `elif`, `else`) to handle three possible cases:

  1. If the guessed number is greater than the secret number, ask the user to enter a lower number.
  2. If the guessed number is less than the secret number, ask the user to enter a higher number.
  3. If the guessed number matches the secret number, display a success message.

* Incremented the `guesses` counter after every user attempt to keep track of the total number of guesses.

* Learned how loops, conditions, variables, user input, and random number generation work together to build an interactive console-based game.
