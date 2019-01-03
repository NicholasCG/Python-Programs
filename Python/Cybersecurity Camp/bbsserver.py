import socketfuncs
import socket
import threading

s = socket.socket()
s.bind(('0.0.0.0', 10333))

dms = {}
msghistory = []

def handleUser(conn, address):
	global dms, msghistory

	print("Got connection from {}".format(address))
	#socketfuncs.send_message(conn, "BBS Server 1.2")
	socketfuncs.send_message(conn, "BBS Server 1.2")
	username = socketfuncs.receive_message(conn)
	while True:
		msg = socketfuncs.receive_message(conn)
		print("{} ({}): {}".format(username, address[0], msg))

		if msg == "quit":
			print("<{} ({}) has disconnected>.".format(username, address[0]))
			msghistory.append("<{} ({}) has disconnected.>".format(username, address[0]))
			break
		elif msg == "dm":

			msgto = socketfuncs.receive_message(conn)
			msg = socketfuncs.receive_message(conn)
			print("Got DM from {} to {}: {}".format(username, msgto, msg))
			if msgto in dms:
				dms[msgto].append(msg)
			else:
				dms[msgto] = [msg]
		elif msg == "list":
			socketfuncs.send_message(conn, str(len(msghistory)))
			for msg in msghistory:
				socketfuncs.send_message(conn, msg)

		elif msg == "listdm" or msg == "listdms":
			if username in dms:
				socketfuncs.send_message(conn, str(len(dms[username])))
				for m in dms[username]:
					socketfuncs.send_message(conn, m)
			else:
				socketfuncs.send_message(conn, "0")
		else:
			msghistory.append("{} ({}) {}".format(username, address[0], msg))

while True:
	s.listen(10)
	(conn, address) = s.accept()
	userThread = threading.Thread(target=handleUser, args=(conn, address))
	userThread.start()
s.close()
