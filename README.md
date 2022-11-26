# TypingTest
An MS-DOS inspired typing test, created with pygame

# STILL A WORK IN PROGRESS
Working on some privlage errors: 

```sh
$ Traceback (most recent call last):
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 418, in <module>
    PlayGame(60)
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 213, in PlayGame
    SpeedRunner(userTyped, file, CountD, TimeLimit)
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 367, in SpeedRunner
    AppendGameStats(Accuracy,WPM)#stores data in repo/GameStats.txt
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 97, in AppendGameStats
    f =open('repo/GameStats.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'repo/GameStats.txt'
```

Also looking for a way to remove the active flikering in the home screen

And planing to enable the WASD keys for navigation

Finally looking for a way to enable the user to reset the game stats without entering repo folder
