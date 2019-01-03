import socketfuncs
import socket

addr = input("Enter the ip address: ")
s = socket.socket()

s.connect((addr, 10333))
#s.connect(('35.237.10.113', 10333))
#s.connect(('35.237.14.26', 10333))


msg = input("Enter your message: ")
socketfuncs.send_message(s, msg)
s.close()
