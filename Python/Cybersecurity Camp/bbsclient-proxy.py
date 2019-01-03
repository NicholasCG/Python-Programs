import socketfuncs
import socket
import sys
import socks

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

addr = input("Enter the domain: ")

username = input("Username: ")

s = socket.socket()
s.connect((addr, 11333))
msg = socketfuncs.receive_message(s)
if msg != "BBS Server 1.2":
	print("Wrong Protocol!")
	sys.exit()
print(msg)

socketfuncs.send_message(s, username)
while True:
	msg = input("Enter your message: ")
	socketfuncs.send_message(s, msg)
	if msg == "quit":
		break
	elif msg == "dm":
		msgto =  input("To? ")
		msg = input("Message (DM): ")
		socketfuncs.send_message(s, msgto)
		socketfuncs.send_message(s, msg)

	elif msg == "listdm" or msg == "listdms" or msg == "list":
		msgcount = int(socketfuncs.receive_message(s))
		for i in range(msgcount):
			m = socketfuncs.receive_message(s)
			print(m)
s.close()
