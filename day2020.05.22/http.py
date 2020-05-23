from socket import *

sockfd = socket()
sockfd.bind(("0.0.0.0",2003))
sockfd.listen(5)

connfd, addr = sockfd.accept()
print("来自浏览器", addr)
date = connfd.recv(4096)
print(date.decode())

response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
response += "bb"

connfd.send(response.encode())


connfd.close()
sockfd.close()
