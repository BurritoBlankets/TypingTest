import matplotlib.pyplot as plt


#GET DATA:
#The code below takes Data from the repo/GameStats.txt and converts it from a string
#to integers then stores them in local list.
with open('repo/GameStats.txt') as file:
    lines = file.readlines()
    Attempts = (lines[4])
    AttemptsStringList = (Attempts.split(","))
    AttemptsIntList = list(map(int, AttemptsStringList))

with open('repo/GameStats.txt') as file:
    lines = file.readlines()
    Accuracy = (lines[5])
    AccuracyStringList = (Accuracy.split(","))
    AccuracyIntList = list(map(int, AccuracyStringList))

with open('repo/GameStats.txt') as file:
    lines = file.readlines()
    WPM = (lines[6])
    WPMStringList = (WPM.split(","))
    WPMIntList = list(map(int, WPMStringList))
file.close()



#GRAPHING:

#graph set-up:
#plt.style.use("Solarize_Light2")#Graph style
fig, ax = plt.subplots()
MSfont = {'fontname':'monospace'}#Font

#data:
Attempts = AttemptsIntList
Accuracy = AccuracyIntList
WPM = WPMIntList

#graphing data:
ax.plot(Attempts, WPM, 'ro--', label="Words per Minute")#Graphs WPM in red w/ dashed line
ax.plot(Attempts, Accuracy, 'ko-.', label="Accuracy (%)")#Graphs Accuracy in blk w/ dashed-dotted line

#final touches
ax.grid(True)#enables grid
plt.savefig("repo/GameStats.png", dpi=150, transparent=True)#saved in repo file because this scipt will be opened outside of repo folder
ax.legend(loc='best', ncol=2, shadow=False, facecolor="white")#Legened: location automatic, 2 columns, w/ box shadow
