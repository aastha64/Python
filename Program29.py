# SOME IMPORTANT METHODS

# socket(): creates a new socket
# bind(): binds the socket to an address and potrt number
# listen(): enables the server to accept the connections
# accept(): accepts a connection from a client
# recv(): receives data from the client
# send(): sends data to the client


import socket
#  creates a  TCP/IP socket
s =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
print("socket created")

#Socket, AF, INET

#SOCK_STREAM

#listen() : puts the socket into listening mode, allowing it to accepting connection requests.
s.listen()
print("Soket is listening")


