import socketfuncs
import socket
import sys

addr = input("IP Address: ")
user = "x"
socketlist = []
#s = socket.socket()
#s.connect((addr,10333))

#msg = socketfuncs.receive_message(s)
#msg = socketfuncs.receive_message(s)

#socketfuncs.send_message(s, user)
while True:
	try:
		s = socket.socket()
		s.connect((addr,10333))
		msg = socketfuncs.receive_message(s)
		socketfuncs.send_message(s, user)
		socketfuncs.send_message(s, "Hammer")
		socketlist.append(s)
#		print(len(socketlist))
	except:
		break
