1. **Importing Libraries**: The code starts by importing the `random` module, which is used for generating random numbers during the game.

2. **Choices Dictionary**: A dictionary named `choices` is defined to map numeric choices (0, 1, 2) to their corresponding words (Snake, Water, Gun).

3. **Check Function**: The `check` function takes two arguments (`comp` for computer's choice and `user` for user's choice) and determines the outcome of the game based on the choices made. It returns `0` for a draw, `-1` if the user loses, and `1` if the user wins.

4. **Main Game Loop**: The program enters an infinite loop using `while True`. Inside the loop:
    - The computer's choice (`comp`) is generated using `random.randint(0, 2)`.
    - The user is prompted to enter their choice (0 for Snake, 1 for Water, 2 for Gun) using `input`.
    - The user's input is checked to ensure it's a valid choice. If not, a message is printed, and the loop continues.
    - The choices made by both the user and the computer are displayed.
    - The `check` function is called to determine the winner, and the result is printed.
    - The user is asked if they want to play again. If they enter anything other than 'Y', the loop breaks, and the game ends.

This code implements a simple Snake-Water-Gun game where the user plays against the computer. It continuously prompts the user to play again until they choose not to.
