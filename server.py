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
