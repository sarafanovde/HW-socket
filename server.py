import socket,os

HOST = 'localhost'
PORT = 8000
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
print ('Server started on port %s ...'%(PORT))

while True:
 	connection, address = sock.accept()
 	data = connection.recv(1024).decode()
 	res = data.split('\n')[0].split(' ')[1] 
 	print(res)
 	if res == '/' or res == '/index.html':
 		path = 'index.html'
 	if res == '/about/aboutme.html':
 		path = 'about/aboutme.html'	    
 	file = open(path, 'rb')
 	connection.send("""HTTP/1.1 200 OK\n\n\n""".encode() + file.read())
 	connection.send(file.read())
 	file.close()
 	connection.close()    
sock.close()
	
