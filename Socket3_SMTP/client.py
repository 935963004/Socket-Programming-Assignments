from socket import *
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.qq.com' #Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'220':
	print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250':
	print('250 reply not received from server.')

login = 'AUTH LOGIN\r\n'
clientSocket.send(login.encode())
recv = clientSocket.recv(1024)
print('login:', recv)
user = base64.b64encode(b'935963004@qq.com').decode() + '\r\n'
clientSocket.send(user.encode())
recv = clientSocket.recv(1024)
print('user:', recv)
password = base64.b64encode(b'cjsmnbloxbhhbfhc').decode() + '\r\n'
clientSocket.send(password.encode())
recv = clientSocket.recv(1024)
print('password:', recv)
# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = 'MAIL FROM: <935963004@qq.com>\r\n'
clientSocket.send(mailFrom.encode())
recv = clientSocket.recv(1024)
print('mail from:', recv)
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
rcptTo = 'RCPT TO: <935963004@sjtu.edu.cn>\r\n'
clientSocket.send(rcptTo.encode())
recv = clientSocket.recv(1024)
print('rcpt to:', recv)
# Fill in end
# Send DATA command and print server response.
# Fill in start
data = b'DATA\r\n'
clientSocket.send(data)
recv = clientSocket.recv(1024)
print('data: ', recv)
# Fill in end
# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024)
print('msg: ', recv)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
quit = 'QUIT\r\n'
clientSocket.send(quit.encode())
recv = clientSocket.recv(1024)
print('quit: ', recv)
clientSocket.close()
# Fill in end