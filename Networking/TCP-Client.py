import socket

target_host = "0.0.0.0"
target_port = 9998

# create a socket object
# AF_INET = IPv4
# SOCK_STREAM = TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()