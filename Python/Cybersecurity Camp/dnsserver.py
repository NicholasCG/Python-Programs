import socketfuncs
import socket
import sys

s = socket.socket()
s.bind(('0.0.0.0', 10334))

ipdict = {"ngray":"35.237.155.182",
	"aborder":"35.237.248.144",
	"ahenke":"35.237.14.26",
	"dbarata":"35.185.60.223",
	"eboone:":"35.237.60.25",
	"self":"127.0.0.1"}

while True:
	s.listen(10)
	(conn, address) = s.accept()
	socketfuncs.send_message(conn, "DNS Server 1.0")
	domain = socketfuncs.receive_message(conn)
	if domain in ipdict:
		socketfuncs.send_message(conn, ipdict[domain])
	else:
		socketfuncs.send_message(conn, "unknown server")
s.close()
