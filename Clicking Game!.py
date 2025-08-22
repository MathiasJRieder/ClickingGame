from ast import With
from cgitb import text
from tkinter import*
from tkinter.messagebox import*
from turtle import *
import random
class MyGUI:
    def __init__(self):
        self.main_Window = Tk()
        self.main_Window.geometry("800x800+100+100")
        self.main_Window.title("SHOWDOWN!")
        self.main_Window.configure(bg='blue')
        self.frame1 = Frame(self.main_Window, width = 800,height = 800, bg='blue')
        self.frame1.place(x=10,y=10)
        self.frame2 = Frame(self.main_Window, width = 50,height = 50, bg='white')
        self.frame2.place(x=300,y=600) #GUI Representation of the physical light to be implemented
        self.scoreone = IntVar()
        self.scoreone.set(0) #Player one score
        self.scoretwo = IntVar()
        self.scoretwo.set(0) #Player two score
        self.scoreevent = IntVar()
        self.scoreevent.set(0) #Determines when the players can score or will be penalized for premptive clicking
        self.gamewon = IntVar()
        self.gamewon.set(0) #Makes buttons stop working (except quit) once the game is won
        self.roundstarted = IntVar()
        self.roundstarted.set(0) #Guards against multiple rounds being started at once and scores can only be affected during a round
        self.label1name = Label(self.frame1, text="Player One", font=('Arial', 24), bg= 'blue')
        self.label1name.place(x=135, y=50)
        self.label1 = Label(self.frame1, textvariable= self.scoreone, font=('Arial', 42), bg= 'blue')
        self.label1.place(x=200, y=100)
        self.label2name = Label(self.frame1, text="Player Two", font=('Arial', 24), bg= 'blue')
        self.label2name.place(x=335, y=50)
        self.label2 = Label(self.frame1, textvariable= self.scoretwo, font=('Arial', 42), bg= 'blue')
        self.label2.place(x=400, y=100)
        self.buttonplayer1 = Button(self.frame1,text = "BUTTON ONE",font = 14,command=self.do_this, bg='purple')
        self.buttonplayer1.place(x=100,y=500)#GUI Representation of the physical button to be implemented
        self.buttonplayer2 = Button(self.frame1,text = "BUTTON TWO",font = 14,command=self.do_this2, bg='purple')
        self.buttonplayer2.place(x=300,y=500)#GUI Representation of the physical button to be implemented
        self.button2 = Button(self.frame1,text = "QUIT GAME",font =14,command = self.main_Window.destroy, bg='purple')
        self.button2.place(x=500,y=500)
        self.choice10 = IntVar()
        self.choice10.set(0)
        self.cb1 = Button(self.frame1, text = "ROUND ONE START!", font= ("Arial", 14), command=self.scorelight, bg='red')
        self.cb1.place(x=20, y=600)
    def scorelight(self):
        if self.gamewon.get() == 0 and self.roundstarted.get() == 0:
            self.roundstarted.set(1)
            rannum = random.randint(1000, 10000) #Light goes off in 1-10 seconds ("after" takes miliseconds as input)
            self.main_Window.after(rannum, self.engage)
            
    def engage(self):
        self.scoreevent.set(1)
        self.frame2.configure(bg='yellow')
        
    def do_this(self):
        if self.gamewon.get() == 0 and self.roundstarted.get() == 1:
            if self.scoreevent.get() == 1:
                scoreone = self.scoreone.get()
                scoreone+= 1
                if scoreone < 3:
                    self.scoreone.set(scoreone)
                    self.cb1.configure(text = "ANOTHER ROUND?", bg='green')
                    self.scoreevent.set(0)
                    self.roundstarted.set(0)
                    self.frame2.configure(bg='white')
                    
                elif scoreone >= 3:
                    self.scoreone.set(3)
                    self.gamewon.set(1)
                    self.cb1.configure(text = "ANOTHER ROUND?", bg='green')
                    self.scoreevent.set(0)
                    self.roundstarted.set(0)
                    self.frame2.configure(bg='white')
                    self.label4 = Label(self.frame1, text= "PLAYER ONE WINS", font=('Arial', 24), bg= 'blue')
                    self.label4.place(x=175, y=200)
                    self.main_Window.after(5000, self.main_Window.destroy)
            elif self.scoreevent.get() == 0:
                scoretwo = self.scoretwo.get()
                scoretwo+= 1
                self.scoretwo.set(scoretwo)
                if scoretwo < 3:
                    self.scoretwo.set(scoretwo)
                elif scoretwo >= 3:
                    self.scoretwo.set(3)
                    self.gamewon.set(1)
                    self.label4 = Label(self.frame1, text= "PLAYER TWO WINS", font=('Arial', 24), bg= 'blue')
                    self.label4.place(x=175, y=200)
                    self.main_Window.after(5000, self.main_Window.destroy)
                    
    def do_this2(self):
        if self.gamewon.get() == 0 and self.roundstarted.get() == 1:
            if self.scoreevent.get() == 1:
                scoretwo = self.scoretwo.get()
                scoretwo+= 1
                if scoretwo < 3:
                    self.scoretwo.set(scoretwo)
                    self.cb1.configure(text = "ANOTHER ROUND?", bg='green')
                    self.scoreevent.set(0)
                    self.roundstarted.set(0)
                    self.frame2.configure(bg='white')
                elif scoretwo >= 3:
                    self.scoretwo.set(3)
                    self.gamewon.set(1)
                    self.cb1.configure(text = "ANOTHER ROUND?", bg='green')
                    self.scoreevent.set(0)
                    self.roundstarted.set(0)
                    self.frame2.configure(bg='white')
                    self.label4 = Label(self.frame1, text= "PLAYER TWO WINS", font=('Arial', 24), bg= 'blue')
                    self.label4.place(x=175, y=200)
                    self.main_Window.after(5000, self.main_Window.destroy)
            elif self.scoreevent.get() == 0:
                scoreone = self.scoreone.get()
                scoreone+= 1
                if scoreone < 3:
                    self.scoreone.set(scoreone)
                elif scoreone >= 3:
                    self.scoreone.set(3)
                    self.gamewon.set(1)
                    self.label4 = Label(self.frame1, text= "PLAYER ONE WINS", font=('Arial', 24), bg= 'blue')
                    self.label4.place(x=175, y=200)
                    self.main_Window.after(5000, self.main_Window.destroy)
     
my_gui = MyGUI()
