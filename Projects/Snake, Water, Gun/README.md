## Snake, Water & Gun Game

A simple Python console-based game inspired by the classic Rock, Paper, Scissors game. The player competes against the computer by choosing **Snake**, **Water**, or **Gun**. The computer randomly selects its choice, and the winner is determined based on predefined game rules.

## Game Rules

```python

* **Snake drinks Water** → Snake wins 🐍
* **Water damages Gun** → Water wins 💧
* **Gun kills Snake** → Gun wins 🔫

## Important Concepts Learned from this Project

* Imported the `random` module to generate random choices for the computer.

* Used `random.choice()` to randomly select an item from a list.

  * Example: `random.choice([-1, 0, 1])`

* Learned how to represent game choices using integers:

  * `Snake = -1`
  * `Water = 0`
  * `Gun = 1`

* Used dictionaries to map user input to numerical values.

  * Example:

    {"s": -1, "w": 0, "g": 1}
    ```

* Used a reverse dictionary to convert numerical values back into readable text for displaying results.

  * Example:

    {-1: "Snake", 0: "Water", 1: "Gun"}
    ```

* Took user input using the `input()` function and used dictionary lookup to retrieve the corresponding numerical value.

* Used conditional statements (`if`, `elif`, `else`) to compare the choices of the player and the computer.

* Learned how nested conditional statements can be used to implement game logic.

* Used formatted strings (`f-strings`) to display the choices made by both the player and the computer.

* Improved understanding of:

  * Variables
  * Dictionaries
  * Conditional statements
  * Random number generation
  * User input
  * Game logic implementation

