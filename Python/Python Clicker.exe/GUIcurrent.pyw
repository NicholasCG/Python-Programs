from tkinter import *
import random
import time

snakes = 10
countamount = 0
size = 0
cash = 50
xo = 0
yo = 200
nxo = 0
nyo = 200
xt = 0
yt = 200
nxt = 0
nyt = 200
statet = 0
state = 0
# auto-countup functions
def counter_label(label):
  def count():
    global snakes
    snakes += countamount
    label.config(text=str("%.1f" % snakes) + " Pythons")
    label3.config(text=str(countamount) + " PpS")
    label.after(1000, count)

  count()
                  
def countamountplus():
   global countamount
   countamount += 1

def snakesplus():
  global snakes
  snakes += 1
  label.config(text=str("%.1f" % snakes) + " Pythons")
root = Tk(className = " Python Clicker! - Nick Gray ")

root.geometry("1366x746")
root.lift()
root.resizable(0,0)
root.configure(background = "white")


# The snake button, the couter labels, and the two large frames
label2 = Label(root, font = ("Comic Sans MS", 16), text = "Dollars: $" + str(cash))
label2.place(relx=.5 ,rely = .05, anchor = CENTER)
label2.configure(background = "white")

label = Label(root,font = ("Comic Sans MS", 16))
label.place(relx = .5, rely = .1, anchor = CENTER)
label.configure(background = "white")

label3 = Label(root, font = ("Comic Sans MS", 14))
label3.place(relx = .5, rely = .15, anchor =  CENTER)
label3.configure(background = "white")

button = Button(root,command = snakesplus)
mi = PhotoImage(file = "snake.gif")
button.configure(image = mi)
button.place(relx=.5, rely = .5 ,anchor = CENTER)

frame1 = Frame(bg = "white", height = root.winfo_height() * .4835 , width = (root.winfo_width() / 3) * .859, bd = 5, relief = SUNKEN).place(x = 975, y = 0)#x=1200,y=0
frame2 = Frame(bg = "white", height = root.winfo_height() * .4835 , width = (root.winfo_width() / 3) * .859, bd = 5, relief = SUNKEN).place(x = 975, y = 370)#x=1200,y=0

# Line grpah

lg = Canvas(root,width = 379, height = 200,bg = "ivory3",relief = SUNKEN)

def graph():
    def grapher():
            global xo
            global yo
            global nxo
            global nyo
            global xt
            global yt
            global nxt
            global nyt
            global statet
            global state
            nxo += 5
            nxt += 5
            chancet = random.randint(0,50)
            chance = random.randint(0,100)
    
            if chance == 1:
                state = 1 - state
                    
            if state == 0:
                nyo = random.randint(nyo-1,nyo)
            elif state == 1:
                nyo = random.randint(nyo,nyo+1)
            if nyo <= 5:
                nyo = 6
                state = 1 - state
            elif nyo > 200:
                nyo = 200
                state = 1 - state
    
            if chancet == 1:
                statet = 1 - statet
                    
            if statet == 1:
                nyt = random.randint(nyt-1,nyt-0)
            elif statet == 0:
                nyt = random.randint(nyt,nyt+1)
            if nyt <= 5:
                nyt = 6
                statet = 1 - statet
            elif nyt > 200:
                nyt = 200
                statet = 1 - statet
            lg.create_line(xo,yo,nxo,nyo,fill = "red")
            lg.create_line(xt,yt,nxt,nyt,fill = "blue")
            xo = nxo
            yo = nyo
            xt = nxt
            yt = nyt

            if xo > 380:
                lg.delete(ALL)
                xo = 0
                nxo = 0
                xt = 0
                nxt = 0
           
            lg.after(10, grapher)
    grapher()


stockFrame = Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
stockFrame.place(x = 1000, y = 600)

costFrame = Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
costFrame.place(x=1075, y = 600)

numberOwnedFrame = Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
numberOwnedFrame.place(x = 1150, y = 600)

stockFrameNameOne = Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
stockFrameNameOne.place(x = 1000, y = 630)

costFrameStockOne = Frame(frame2,  bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
costFrameStockOne.place(x = 1075, y = 630)

numberOwnedStockOne =  Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
numberOwnedStockOne.place(x = 1150, y = 630)

stockFrameNameTwo =  Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
stockFrameNameTwo.place(x = 1000, y = 660)

costFrameStockTwo =  Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
costFrameStockTwo.place(x = 1075, y = 660)

numberOwnedStockTwo =  Frame(frame2, bg = "gray76", height = 30, width = 75, bd = 2, relief = SUNKEN)
numberOwnedStockTwo.place(x = 1150, y = 660)

# Shop button functions

def ibutcom():
    global snakes
    global countamount
    if snakes >= 15:
      snakes -= 15
      countamount += .1
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")
def gbutcom():
    global snakes
    global countamount
    if snakes >= 100:
      snakes -= 100
      countamount += 1
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")
def hbutcom():
    global snakes
    global countamount
    if snakes >= 1100:
      snakes -= 1100
      countamount += 8
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")
def mbutcom():
    global snakes
    global countamount
    if snakes >= 12000:
      snakes -= 12000
      countamount += 47
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")
def abutcom():
    global snakes
    global countamount
    if snakes >= 130000:
      snakes -= 130000
      countamount += 260
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")
def dlbutcom():
    global snakes
    global countamount
    if snakes >= 1400000:
      snakes -= 1400000
      countamount += 1400
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")
def pbutcom():
    global snakes
    global countamount
    if snakes >= 20000000:
      snakes -= 20000000
      countamount += 7800
      label.config(text=str("%.1f" % snakes) + " Pythons")
      label3.config(text=str(countamount) + " PpS")

def bcheck(label):
  def checktime():
    if snakes  > 14:
      ibutton.configure(state=ACTIVE)
    else:
      ibutton.configure(state= DISABLED)
      
    if snakes > 99:
      gbutton.configure(state = ACTIVE)
    else:
      gbutton.configure(state = DISABLED)

    if snakes > 1099:
      hbutton.configure(state = ACTIVE)
    else:
      hbutton.configure(state = DISABLED)
      
    if snakes > 11999:
      mbutton.configure(state = ACTIVE)
    else:
      mbutton.configure(state = DISABLED)

    if snakes > 129999:
      abutton.configure(state = ACTIVE)
    else:
      abutton.configure(state = DISABLED)

    if snakes > 1399999:
      dlbutton.configure(state = ACTIVE)
    else:
      dlbutton.configure(state = DISABLED)

    if snakes > 19999999:
      pbutton.configure(state = ACTIVE)
    else:
      pbutton.configure(state = DISABLED)
      
    label.after(100, checktime)
  checktime()

ibutton = Button(root, text = "  Incubator",font = ("bold"), bg = "white", anchor = W, height = 5,width = 45,command = ibutcom)
ibutton.place( y = 0)

gbutton = Button(root, text = " Grandma",font = ("bold"),bg = "white", anchor = W,height = 5, width = 45,command = gbutcom)
gbutton.place(y = 107)
hbutton = Button(root, text = " Henchmen",font = ("bold"),bg = "white", anchor = W,height = 5, width = 45, command = hbutcom)
hbutton.place(y=214)
mbutton = Button(root, text = " Mayor",font = ("bold"),bg = "white", anchor = W,height = 5,width = 45, command = mbutcom)
mbutton.place(y=321)
abutton = Button(root, text = " Actor",font = ("bold"),bg = "white", anchor = W,height = 5,width = 45, command = abutcom)
abutton.place(y = 428)
dlbutton = Button(root, text = " Drug lord",font = ("bold"),bg = "white", anchor = W,height = 5,width = 45, command = dlbutcom)
dlbutton.place(y=535)
pbutton = Button(root, text = " Pirates",font = ("bold"),bg = "white", anchor = W,height = 5,width = 45, command = pbutcom)
pbutton.place(y=642)


counter_label(label)
lg.place(x=980, y = 375)
graph()
bcheck(label)
root.mainloop()
