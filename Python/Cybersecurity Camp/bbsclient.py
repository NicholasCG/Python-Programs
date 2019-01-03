import socketfuncs
import socket
import sys

s2 = socket.socket()
addr = input("Enter the domain: ")

s2.connect(('35.185.60.223', 10334))
protocol = socketfuncs.receive_message(s2)
print(protocol)

if protocol != "DNS Server 1.0":
	print("Wrong Protocol!")
	sys.exit()

socketfuncs.send_message(s2, addr)
ip = socketfuncs.receive_message(s2)

if ip == "unknown server":
	print("No IP associated with domain!")
	sys.exit()

#print(ip)
username = input("Username: ")
s2.close()

s = socket.socket()
s.connect((ip, 10333))
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
