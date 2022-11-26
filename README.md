# TypingTest
An MS-DOS inspired typing test, created with pygame

# STILL A WORK IN PROGRESS
working on some compatability errors: 
'''
Traceback (most recent call last):
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 418, in <module>
    PlayGame(60)
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 213, in PlayGame
    SpeedRunner(userTyped, file, CountD, TimeLimit)
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 367, in SpeedRunner
    AppendGameStats(Accuracy,WPM)#stores data in repo/GameStats.txt
  File "/home/BurritoBlankets/TypingTest/SpeedTest.py", line 97, in AppendGameStats
    f =open('repo/GameStats.txt', 'w')
PermissionError: [Errno 13] Permission denied: 'repo/GameStats.txt'
'''
