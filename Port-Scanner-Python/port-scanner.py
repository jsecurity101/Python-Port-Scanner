import socket
import subprocess
import sys
from datetime import datetime


name=raw_input("What is the hostname you want to resolve\n")
try:
	host=socket.gethostbyname(name)
	print host
except socket.gaierror, err:
	print "cannot resolve hostname",name,err

#scan

print "=" * 70
print "Please wait while scanning, this will take a while my dood"
print "=" * 70

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)       
 	result = sock.connect_ex((host, port))
        if result == 0:
            print "Port {}: 	 Open".format(port)
	if result != 0:
	    print "Port {}:	Closed".format(port)
        sock.close()

except KeyboardInterrupt:
	sys.exit()
	print '\n'

except socket.gaierror:
    print 'Hostname not resolved'
    sys.exit()

except socket.error:
    print "Connection to server not found"
    sys.exit()
