import socket
import sys

# if port is hanging for 0.3 seconds set it to error code
socket.setdefaulttimeout(0.3)

#set default host and range
ip = '127.0.0.1'
rang = [1, 1024]

# if user inputs host, set default host to inputted host
if len(sys.argv) > 1:
    ip = sys.argv[1]

# if user inputs range, set default range to inputted range
if len(sys.argv) > 2:
    if len(sys.argv[2].split(':')) == 1:
        rang = [sys.argv[2], sys.argv[2]]
    else: rang = sys.argv[2].split(':')

# display name of host and range of ports being scanned
print("Scanning host: " + ip + ", Ports: " + str(rang[0]) + "-" + str(rang[1]))

for x in range(int(rang[0]), int(rang[1])+1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, x))
    
    if result == 0: 
        print("Port " + str(x) + " is open")
    elif result == 11:
        print("Port " + str(x) + " is filtered")

sock.close()