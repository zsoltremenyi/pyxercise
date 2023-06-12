Write a Guess the Number game that has three levels of difficulty.
The first level would be between 1 and 10. The second between 1 and 100.
The third between 1 and 1000.

Prompt for the difficulty level, and then start the game. The computer picks a random number in that range
and prompts the player to guess that number. Each time the player guesses,
the computer should give the player a hint as to whether the number is too high or too low.
Keep track of the number of guesses. Once the player guesses the correct number, the computer should present the
number of guesses and ask if the player would like to play again.

Constraints:
Don't allow non-numeric data entry.
During the game, count non-numeric entries as wrong guesses.

Challenges:
Map the number of guesses taken to comments:
1 guess: "You're a mind reader!"
2-4 guesses: "Most impressive."
5-8 guesses: "You can do better than that."
9 or more: "Better luck next time."

Keep track of previous guesses and issue an alert that the user
has already guessed that number. Count as wrong guess.