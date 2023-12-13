# README

This is a repository for my final project where a trivia game has been created.
The trivia game contains Disney themed questions that appear in a true or false
or multiple choice format. 

No dependencies need to be downloaded to run the game; however, you must ensure 
that the true_or_false.csv, multiple_choice.csv, and leaderboard.txt files are 
downloaded and in the same folder as the trivia_game.py file.

To run the game, download all the files and click run without debugging (make 
sure that print(ask_questions()) is uncommented). A screen should pop up prompting 
you to enter a name. Choose a name to enter, and then instructions on how to play 
the game will pop up. Hit enter then type in a or b depending on which question type 
you would like to answer. If you do not type in an expected option, the game will 
prompt you to try again. Continue playing until you have reached 50 points or run 
out of lives (every player starts with 3 lives). At the end, a screen will pop up 
saying wether you won or lost, and then, a leaderboard will appear with the top 3 
highest scorers. 

If you press cancel on the choose a type of question screen, the game will prompt
you to try again. Cancel only exits out of the game if it is pressed while on a 
multiple choice or true or false question. 

## Markdown

This README file supports Markdown syntax and so I can create
section headers using the '#' symbol followed by a title, on its own line.

## Contents

This repository should contain the following folders/files:
- trivia_game.py
- true_or_false.csv
- multiple_choice.csv
- trivia_game_test.py
- leaderboard.txt
The `trivia_game.py` file contains the code to produce questions and compare answers
this file produces a gui for the user to play the trivia game. 
The `true_or_false.csv` file contains all the true or false questions.
The `multiple_choice.csv` file contains all the multiple choice questions.
The `trivia_game_test.py` file contains the unit tests for the trivia_game.py file.
The `leaderboard.txt` file contains the names of past people who have played the game
along with their scores so that a leaderboard can be created.
