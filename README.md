# Typing Test
An MS-DOS-inspired typing test, created with pygame!



## Requirements

#### Root Privileges:
* This is required because GitHub, by default, adds root privileges to the repo folder, which prevents the game from saving your scores to the GameStats.txt

#### Pygame:
* The entirety of the game is initialized in the pygame module. [You can find instructions on installation here.](https://www.pygame.org/wiki/GettingStarted)

#### Matplotlib:
* This game includes a graphing feature that creates a graph with data from GameStats.txt. [Here is a link to its installation.](https://matplotlib.org/stable/users/installing/index.html)



## Installation
```
$ git clone https://github.com/BurritoBlankets/TypingTest.git
```



## Screenshots
#### Home Screen
![Home](https://user-images.githubusercontent.com/110593817/204119736-e7c3290a-e263-4813-b842-2c9cb71a983b.png)

The game is initialized with the return key. And can be exited at any time with the use of the return key. You will see that the mouse does not work with the game; I did this intentionally to simulate the lack of mouse accommodation on the original MS-DOS software.


#### Prompts
![Test](https://user-images.githubusercontent.com/110593817/204119740-0b0e73e9-ad6e-4aa9-b615-d35983931bf7.png)

Each session, the game generates a random number between one and five to pick one of any of the five Aesops fables from the prompts.txt to utilize in the PlayGame function. The user's input will word wrap in real-time, making the enter button unnecessary. Unless the user wishes to terminate the program early and see their score or the user finishes the prompt before the time runs out.


#### Time Is Up Window
![TimeIsUp](https://user-images.githubusercontent.com/110593817/204119744-5c1ff727-abe0-41b7-8eb5-584db1bb49ee.png)

Once time runs out, the Time Is Up window pops up, prompting the user to retry, quit, or see a graph. You can navigate this window by utilizing the left and right arrow keys.


#### Graph
![Graph](https://user-images.githubusercontent.com/110593817/204119745-5516c3dd-2e9f-4fe0-832a-e325e318e6f2.png)

After each game, the Code stores the user's Words per Minute and their Accuracy score in the GameStats.txt. Afterward, the  Code runs a separate script, MatPlot.py, which utilizes the matplotlib module to create an image of a graph (GameStats.png). When the "Graph" option is selected in the Time Is Up window, the GameStats.png is Blit-ed on the screen. This screen can be exited by the use of any button
