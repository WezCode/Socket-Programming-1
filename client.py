import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Usually its on remote machines so cant just use get host name like this
s.connect((socket.gethostname(), 1234))

# Receives a stream of data, how big is a chunk of data that you receive


while True:

	full_msg = ''
	new_msg = True
	while True:
	    msg = s.recv(16)

	    if new_msg:
	    	print(f"new message length: {msg[:HEADERSIZE]}")
	    	#Strips whitespace automatically in python and will store the length
	    	# in the int msglen.

	    	# reads in the first 10 characters to extract length of msg
	    	msglen = int(msg[:HEADERSIZE])
	    	new_msg = False

	   	
	    full_msg += msg.decode("utf-8")

	    if len(full_msg) - HEADERSIZE == msglen:
	    	print("full msg received")
	    	print(full_msg[HEADERSIZE:])
	    	new_msg = True
	    	full_msg = ''

	print(full_msg)

