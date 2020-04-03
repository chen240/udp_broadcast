from socket import *

#１．创建套节字
sockfd=socket(AF_INET,SOCK_STREAM)

#２．绑定地址
sockfd.bind(('192.168.101.13',8888))

#３．设置监听
sockfd.listen(5)

#4.等待接受连接
print("waiting for connect...")
connfd,addr=sockfd.accept()
print("Connect from",addr)
# print(connfd)

while True:
    #5收发消息
    data=connfd.recv(1024).decode()
    if data=="##":
        break
    print(data)
    n=connfd.send(b'Receive your message')
    print("发送了%d字节"%n)

#６．关闭套节字
connfd.close()
sockfd.close()


