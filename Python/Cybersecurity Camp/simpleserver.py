import socketfuncs
import socket

s = socket.socket()
s.bind(('0.0.0.0', 10333))
while True:
	s.listen(10)

	(conn, address) = s.accept()
	print("Got connection from {}".format(address))


	msg = socketfuncs.receive_message(conn)

	print("Message: {}".format(msg))

s.close()
