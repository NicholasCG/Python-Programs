# Auto line graph. Good for generating a fake stock chart.
from tkinter import *
import time
import random


root = Tk(className = "Performance")
root.attributes("-topmost", True)
linex=0
liney = 0
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

lg = Canvas(root,width = 381, height = 200,bg = "ivory2")

def graph():
    def grapher():
            global xo
            global yo
            global nxo
            global nyo
            global xt

            global linex
            global liney
            nxo += 5
            nxt += 5
            
                
            while linex < 385:
                lg.create_line(linex,0,linex,200,fill = "ivory4")
                linex += 5

            while liney < 205:
                lg.create_line(0,liney,381,liney,fill="ivory4")
                liney += 5
                
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
