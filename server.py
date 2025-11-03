import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("server is listening on port 12345..")

conn, addr = server_socket.accept()
print(f"connected with {addr}")

data = conn.recv(1024).decode()
print("received from client:", data)

conn.send("hello client!".encode())
conn.close()
