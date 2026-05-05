import socket

# Step 1: Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to server
client_socket.connect(("127.0.0.1", 12345))

# Step 3: Send message
client_socket.send("Hello from client".encode())

# Step 4: Receive reply
data = client_socket.recv(1024).decode()
print("Server says:", data)

# Step 5: Close connection
client_socket.close()


#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
import socket

# Step 1: Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind IP and port
server_socket.bind(("localhost", 12345))

# Step 3: Listen for client
server_socket.listen(1)
print("Server is waiting for connection...")

# Step 4: Accept connection
conn, addr = server_socket.accept()
print("Connected to:", addr)

# Step 5: Receive message
data = conn.recv(1024).decode()
print("Client says:", data)

# Step 6: Send reply
conn.send("Hello from server".encode())

# Step 7: Close connection
conn.close()