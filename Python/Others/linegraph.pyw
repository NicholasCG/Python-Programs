# Auto line graph. Good for generating a fake stock chart.
from tkinter import *
import time
import random

root = Tk(className = "Graph Function")
root.attributes("-topmost", True)
linex=0
liney = 0
xo = 0
yo = 200
nxo = 0
nyo = 200

statet = 0
state = 0

lg = Canvas(root,width = 381, height = 200,bg = "ivory2")

def graph():
    def grapher():
            global xo
            global yo
            global nxo
            global nyo

            global statet
            global state

            global linex
            global liney
            nxo += 1
            nxt += 1
            chancet = random.randint(0,50)
            chance = random.randint(0,100)
                
            while linex < 385:
                lg.create_line(linex,0,linex,200,fill = "ivory4")
                linex += 5

            while liney < 205:
                lg.create_line(0,liney,381,liney,fill="ivory4")
                liney += 5
                
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
                linex = 0
                liney = 0
                
            lg.after(50, grapher)
    grapher()

def main():
	lg.pack()
	graph()
	root.mainloop()
	
if __name__ == "__main__":
	main()
