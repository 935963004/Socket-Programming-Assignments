import time
from socket import *
serverName = '192.168.1.104'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(0, 10):
	oldTime = time.time()
	sendTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(oldTime))
	message = ('package %d, client_local_time:%s' % (i + 1, sendTime)).encode()
	try:
		clientSocket.sendto(message, (serverName, serverPort))
		modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
		rtt = time.time() - oldTime
		print('报文 %d 收到来自 %s 的应答: %s,往返时延(RTT) = %fs' % (i+1, serverName, modifiedMessage.decode('utf-8'), rtt))
	except Exception as e:
		print('报文 %d: 的请求超时' % (i+1))
