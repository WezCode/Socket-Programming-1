import socket
import pickle

HEADERSIZE = 10

# Usually its on remote machines so cant just use get host name like this
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Receives a stream of data, how big is a chunk of data that you receive
s.connect((socket.gethostname(), 1235))

while True:

	full_msg = b''
	new_msg = True
	while True:
	    msg = s.recv(16)
	    if new_msg:
	    	print(f"new message length: {msg[:HEADERSIZE]}")
	    	# reads in the first 10 characters to extract length of msg
	    	msglen = int(msg[:HEADERSIZE])
	    	new_msg = False

	   	
	    full_msg += msg

	    if len(full_msg) - HEADERSIZE == msglen:
	    	print("full msg received")
	    	print(full_msg[HEADERSIZE:])

	    	d = pickle.loads(full_msg[HEADERSIZE:])
	    	print(d)

	    	new_msg = True
	    	full_msg = b''

	print(full_msg)

