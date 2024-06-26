[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588429&assignment_repo_type=AssignmentRepo)

# Andrew Liu's Whack-a-Mole
## CS110 Final Project Spring 2024

## Team Members

Andrew Liu

***

## Project Description

A Whack-A-Mole Game. Players will be timed and within that time they must click on as many moles as they can.

***    

## GUI Design

### Initial Design

![initial gui](assets/Initial_draft.jpg)

### Final Design

![final gui](assets/Final_GUI.PNG)
![final gui](assets/Game_GUI.PNG)
![final gui](assets/End_GUI.PNG)

## Program Design

### Features

1. Starting Menu
2. Click-based game
3. Points system
4. Timer
5. Game end screen

### Classes

-target: Initializes the mole sprite

-timer: Initializes the timer for the game

-sample_controller.py: Is the mainloop for the program

## ATP
### Score
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           | Game starts     |
|  2                   | Score Counter Program  |Score count = 0  |
|  3                   | Hit count button   | hit count increases = 1      |
|  4                   | Hit equation   | Score increases to expected score after hit|
### Mole
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           | Game starts |
|  2                   | Moles start appearing   | Moles pop out of one of nine holes   |
|  3                   | Click on the mole  | Mole is gone and hit counter adds|
|  4                   | Don't click on mole | Mole stays until clicked or until game over |
### Timer
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           | Timer starts    |
|  2                   | Timer goes down by waiting  | Timer decreases per second  |
|  3                   | Wait for time to hit 0 | Game should stop and display final score|
### Menu Navigation
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           | Menu appears    |
|  2                   | Click Start         | Game starts  |
|  3                   | Click quit button       | Game closes|
### Gameover Navigation
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Start game           | Game starts   |
|  2                   | Click Replay        | Game returns to game state |
|  3                   | Click Quit          | Game closes |