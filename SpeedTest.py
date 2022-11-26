#TYPING TEST PROJECT; BY Pillo & John

#To Change Timelimt enter value in sconds on line 152 & 255 as a PlayGame() argument


#Import modules
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as p
import sys
import tkinter
from time import time, sleep
import math
import textwrap
import random
print("\nPlease report any bugs to JGDL2003@gmail.com\nHappy Typing  (‘∇^d)")
############ARGUMENTATIVE FUNCTIONS############
#(Makes Syntax Easier)

#Prints Text in Pygame GUI
def PrintText(NameTxt, TxtSize, Color, TxtCor):
	Font=p.font.Font('repo/DOS_VGA.ttf',TxtSize)
	Name= Font.render (NameTxt, True, Color)
	screen.blit (Name, TxtCor)

#Inverse GUI Buttons Colors
def Button(NameTxt, Color1, Color2, TxtCor, Rect, TxtSize):
	font=p.font.Font('repo/DOS_VGA.ttf',TxtSize)
	p.draw.rect(screen, Color1, Rect)
	Name=font.render (NameTxt, True, Color2)
	screen.blit (Name, TxtCor)
	p.display.update()

#Wraps Text in Pygame GUI (stolen from https://www.pygame.org/wiki/TextWrap)
def WrapText(surface, text, color, rect, font, aa=False, bkg=None):
	rect = p.Rect(rect)
	y = rect.top
	lineSpacing = -2

#Get the height of the font
	fontHeight = font.size("Tg")[1]
	while text:
		i = 1

#determine if the row of text will be outside our area
		if y + fontHeight > rect.bottom:
			break

# determine maximum width of line
		while font.size(text[:i])[0] < rect.width and i < len(text):
			i += 1

# if we've wrapped the text, then adjust the wrap to the last word
		if i < len(text):
			i = text.rfind(" ", 0, i) + 1

# render the line and blit it to the surface
		if bkg:
			image = font.render(text[:i], 1, color, bkg)
			image.set_colorkey(bkg)
		else:
			image = font.render(text[:i], aa, color)

		surface.blit(image, (rect.left, y))
		y += fontHeight + lineSpacing

		# remove the text we just blitted
		text = text[i:]
	return text

def AppendGameStats(Var1,Var2):
#Append New Attempt Number:

	f =open('repo/GameStats.txt', 'r')#	gets text from file
	line = f.readlines()
	f.close

	LineBeingChanged = (line[4])
	NoSlashN = LineBeingChanged[:-1]#removes invisbile "\n"
	NewNum=(len(LineBeingChanged.split(",")))+1#gets attempt number
	line[4] = "{}, {}\n".format(NoSlashN, NewNum)#appends attempt number


#Append New Accuracy Score:
	LineBeingChanged = (line[5])
	NoSlashN = LineBeingChanged[:-1]
	NewNum= str(Var1)
	line[5] = "{}, {}\n".format(NoSlashN, NewNum)


#Append New Accuracy Score:
	LineBeingChanged = (line[6])
	NoSlashN = LineBeingChanged[:-1]
	NewNum= str(Var2)
	line[6] = "{}, {}\n".format(NoSlashN, NewNum)

	f =open('repo/GameStats.txt', 'w')
	f.writelines(line)
	f.close

def Graph(Accuracy,WPM):
	ScreenBackground()
	Stats = p.image.load("repo/GameStats.png").convert_alpha()
	screen.blit(Stats, (0, 50))
	PrintText("Game Stats", 50, White, (30,65))
	PrintText("Attempt", 40, Black, (415,720))

#	Just blits Score label but with a 90 deg angle
	Font=p.font.Font('repo/DOS_VGA.ttf',40)
	sc0re = Font.render ("Score", True, Black)
	sc0re = p.transform.rotate(sc0re, 90)
	screen.blit (sc0re, (40,360))

# Blits graph legened
	Button(" -o- Words per Minute", White, Red, (255,120), [250,120,600,30], 30)
	PrintText("-o- Accuracy", 30, Black, (630,120))

#	Button(" -o- Accuracy", White, Black, (400,110), [495,500,380,30], 30)

	p.display.flip()

	Play = True
	while Play:
		for event in p.event.get():
			if event.type == p.KEYDOWN:#enable keyboard
				Play = False
	TimeUp(Accuracy,WPM)

############GAME SCREENS############

def ScreenBackground():
	screen.fill(Blue)#makes screen blue

#	Screen Borders
	p.draw.rect(screen, Grey, [0, 0, 900, 30])#Text Bg
	p.draw.line(screen, Grey, (10,45),(890,45),2)#TopHorizontal Line
	p.draw.line(screen, Grey, (10,880),(890,880),2)#BottomHorizontal Line
	p.draw.line(screen, Grey, (10,45),(10,880),2)#LeftVertical Line
	p.draw.line(screen, Grey, (890,45),(890,880),2)#RightVertical Line

#	Text
	PrintText("File  Edit  Search  Options", 25, Black, (20,5)) #Prints Menu option

def PopUpBackground1():
	p.draw.rect(screen, Grey, [100, 250, 700, 300])#Text Bg
	p.draw.line(screen, Black, (110,265),(790,265),2)#TopHorizontal
	p.draw.line(screen, Black, (110,535),(790,535),2)#BottomHorizontal
	p.draw.line(screen, Black, (110,535),(110,265),2)#LeftVertical
	p.draw.line(screen, Black, (790,535),(790,265),2)#RightVertical
	p.draw.line(screen, Black, (129,564),(829,564),30)#BoldHorizontal
	p.draw.line(screen, Black, (814,279),(814,579),30) #BoldVertical

def PopUpBackground2():
	p.draw.rect(screen, Grey, [100, 250, 700, 300])#Bg
	p.draw.rect(screen, White, [100, 250, 700, 40])#WhiteTitleTab
	p.draw.line(screen, Black, (100,250),(800,250),1)#TopHorizontal
	p.draw.line(screen, Black, (100,550),(800,550),1)#BottomHorizontal
	p.draw.line(screen, Black, (100,250),(100,550),1)#LeftVertical
	p.draw.line(screen, Black, (800,250),(800,550),1)#RightVertical
	p.draw.line(screen, Black, (129,564),(829,564),30)#BoldHorizontal
	p.draw.line(screen, Black, (814,279),(814,579),30) #BoldVertical

def MenuScreen():
	PopUpBackground1()
	PrintText('Welcome to the Typing Test Game', 25, Black, (230,300))
	PrintText('Created by Jose Duenas-Lopez', 25, Black, (250,350))
	PrintText('Open script', 25, Black, (375,380))
	Button("<  Press Enter to Play  >", Grey, Black, (264,450), [264,450,373,25], 26)
	Button("<  Press ESC to close game  >", Grey, Black, (247,475), [247,475,405,25], 25)

def PlayGame(TimeLimit):
	rNum = random.randrange(2,16,3)#genarates random number to pick prompt

#Typing Prompt
	with open('repo/Prompts.txt') as f:
		line = f.readlines()
		LineBeingRead = (line[rNum])
		NoSlashN = LineBeingRead[:-1]#removes invisbile "\n"
		file = NoSlashN
		f.close

#	Prints Screen:
	ScreenBackground()
	Colons=": : : : : : : : : : : : : : : : : : : : : : : : : : : : "
	WrapText(screen, Colons, Grey, [20, 100,20, 800],font, aa=False, bkg=Grey)#Prints Side Colons
	WrapText(screen, file, Grey, [50, 100,800, 800],font, aa=False, bkg=Grey)#Prints prompt

	userTyped=""#Stores users input

#	Timer Variables
	TimeLimit=int(TimeLimit)
	StartEpoch=int(time())
	end=int(StartEpoch+TimeLimit)
	clock=p.time.Clock()
	timeUP= False

#	Gameloop
	run = True
	while run==True:
		for event in p.event.get():
			if event.type == p.QUIT:
				run=False

#			Prints User Input in Pygame GUI
			if event.type==p.KEYDOWN:
				user_key = event.unicode

				if event.key == p.K_ESCAPE:#if you hit esc, goto menuscreen
					run = False
					MenuScreen()

				if event.key == p.K_RETURN:#if player finishes early and they hit enter
					SpeedRunner(userTyped, file, CountD, TimeLimit)


				if event.key == p.K_BACKSPACE:

					if len(userTyped) > 0:
						userTyped = userTyped[:-1]
						ScreenBackground()
						WrapText(screen, Colons, Grey, [20, 100,20, 800],font, aa=False, bkg=Grey)#Prints Side Colons
						WrapText(screen, file, Grey, [50, 100,800, 800], font, aa=False, bkg=Grey)#Prints Prompt
						WrapText(screen, userTyped, Black, [50, 100,800, 800], font, aa=False, bkg=Black)#Prints User Text

				else:
					userTyped=userTyped+user_key
					ScreenBackground()
					WrapText(screen, Colons, Grey, [20, 100,20, 800],font, aa=False, bkg=Grey)#Prints Side Colons
					WrapText(screen, file, Grey, [50, 100,800, 800], font, aa=False, bkg=Grey)#Prints Prompt
					WrapText(screen, userTyped, Black, [50, 100,800, 800], font, aa=False, bkg=Black)#Prints User Text


#		Timer:
		CountD=int(end-time())
		if CountD >= 0:
			p.draw.rect(screen, Grey, [417, 30,60, 43])#Timer Bg
			PrintText(format(CountD), 50, Blue, (420,30))
			clock.tick(60)
			p.display.flip()

		else:
			if timeUP == False:
#				Finds Accuracy:
				userTypeLen=len(userTyped)
				Accuracy=0

				for num in range(0,userTypeLen, 1):
					if userTyped[num]==file[num]:
						Accuracy=int(Accuracy)+1

				if Accuracy != 0:
					Accuracy=round(((Accuracy/userTypeLen)*100),2)
					Accuracy=round(Accuracy)


				WPM=round(len(userTyped.split(" ")))#finds words per minute
				WPM=WPM * (60//TimeLimit)

				timeUP = True#ends timer

				AppendGameStats(Accuracy,WPM)#stores data in repo/GameStats.txt
				from repo import MatPlot#Updates data
				TimeUp(Accuracy,WPM,img)#opens time-Up window

def TimeUp(Accuracy,WPM):
	#	Time is Up Screen:
	PopUpBackground2()
	PrintText("Time is Up", 40, Red, (335,255))
	PrintText(("Accuracy:.............{}%".format(Accuracy)), 35, Black, (190,350))
	PrintText(("Words per minute:.....{}".format(WPM)), 35, Black, (190,390))

	Button("< Retry >", White, Black, (125,460), [125,460,180,35], 35)
	Button("< Graph >", White, Black, (360,460), [360,460,180,35], 35)
	Button("  Quit  ", White, Black , (605,460), [595,460,180,35], 35)
	PrintText('<       >', 35, Black, (595,460))# since quit is only 4 letters...formating purposes
	p.display.flip()

	pos = 0
	Option = 0
	Play = True

	while Play:

		for event in p.event.get():
			if event.type == p.KEYDOWN:#enable keyboard

				if event.key == p.K_LEFT:#if you hit Left Arrow Key:
					pos = pos - 1
					if pos == -2:
						pos = -1

				elif event.key == p.K_RIGHT:#if you hit Right Arrow Key:
					pos = pos + 1
					if pos == 2:
						pos = 1


				if pos <= -1:
					Button("> Retry <", Black, White, (125,460), [125,460,180,35], 35)
					Option = 1
				else:
					Button("< Retry >", White, Black, (125,460), [125,460,180,35], 35)


				if pos == 0:
					Button("> Graph <", Black, White, (360,460), [360,460,180,35], 35)
					Option = 2
				else:
					Button("< Graph >", White, Black, (360,460), [360,460,180,35], 35)


				if pos >= 1:
					font=p.font.Font('repo/DOS_VGA.ttf',35)
					p.draw.rect(screen, Black, [595,460,180,35])
					Name=font.render ("  Quit  ", True, White)
					Name2=font.render ('>       <', True, White)
					screen.blit (Name, (605,460))
					screen.blit (Name2, (595,460))
					p.display.update()

					Option = 3
				else:
					font=p.font.Font('repo/DOS_VGA.ttf',35)
					p.draw.rect(screen, White, [595,460,180,35])
					Name=font.render ("  Quit  ", True, Black)
					Name2=font.render ('<       >', True, Black)
					screen.blit (Name, (605,460))
					screen.blit (Name2, (595,460))
					p.display.update()


				if event.key == p.K_RETURN:
					if Option == 1:
						sleep(0.1)
						PlayGame(60)

					elif Option == 2:
						sleep(0.1)
						Graph(Accuracy,WPM)

					elif Option == 3:
						sleep(0.1)
						p.quit()
						sys.exit()
					else:
						break

def SpeedRunner(userTyped,file, CountD, TimeLimit):

	timeUP = True#ends timer
	userTypeLen=len(userTyped)
	Accuracy=0

	for num in range(0,userTypeLen, 1):
		if userTyped[num]==file[num]:
			Accuracy=int(Accuracy)+1

	if Accuracy != 0:
		Accuracy=round(((Accuracy/userTypeLen)*100),2)
		Accuracy=round(Accuracy)


	WPM=round(len(userTyped.split(" ")))#finds words per minute
	WPM=WPM * (60//(TimeLimit-CountD))


	AppendGameStats(Accuracy,WPM)#stores data in repo/GameStats.txt
	from repo import MatPlot#Upadtes GameStats graph
	TimeUp(Accuracy,WPM)#opens time-Up window






#MAIN GAME LOOP:
p.init()
screen = p.display.set_mode([900,900])
p.display.set_caption('Typing Test')

Play = True
while Play:

	if p.mouse.get_visible():#Disables mouse
		p.mouse.set_visible(False)


#Colors: https://www.schemecolor.com/ms-dos-logo.php
	Black= (int(0), int(0), int(0))
	Grey= (int(192), int(192), int(192))
	Red= (int(255), int(0), int(0))
	Pink= (int(255), int(0), int(255))
	Blue= (int(0), int(0), int(255))
	Yellow= (int(255), int(255), int(0))
	White = (int(255),int(255),int(255))

#Text Variables:
	font=p.font.Font('repo/DOS_VGA.ttf',30)

	for event in p.event.get():
		if event.type == p.QUIT:#if you click the x, you quit game
			p.quit()
			sys.exit()

		if event.type == p.KEYDOWN:#enable keyboard
			if event.key == p.K_ESCAPE:#if you hit esc, you quit game
				Button(">  Press ESC to close game  <", Black, Grey, (247,475), [247,475,405,25], 25)
				sleep(0.1)
				p.quit()
				sys.exit()
			else:
				Button("<  Press ESC to close game  >", Grey, Black, (247,475), [247,475,405,25], 25)


			if event.key == p.K_RETURN:#if you hit enter, you will play game
				Button(">  Press Enter to Play  <", Black, Grey, (264,450), [264,450,373,25], 26)
				sleep(0.1)
				PlayGame(60)
			else:
				Button("<  Press Enter to Play  >", Grey, Black, (264,450), [264,450,373,25], 26)


		else:
			Play= True


#		GameLook:
			ScreenBackground()


			MenuScreen()
