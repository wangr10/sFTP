#Use PingServer.py as a template

# We will need the following module to generate randomized lost packets
import random
import time
import sys
from socket import *

# Checking command line arguement
if (len(sys.argv) != 2):
    print("Required arguments: port number(Please set it to 9093 according to the requirements of the project)")
    exit(0)
	
port = int(sys.argv[1]) 

exp_num = "0"

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', port))
# Assign Loss and Delay parameters,(Delay = 100 means 100 milliseconds)
LOSS_RATE = 0.1
AVERAGE_DELAY = 400
f = open("outputfile.txt", "wb")
	
while True:
	# Generate random number in the range of 0 to 1
	rand = random.uniform(0, 1)

	# Receive the client packet along with the address it is coming from
	RawData, address = serverSocket.recvfrom(1024)
	# RawData is in byte style, therefore we need to convert it into string to do the comparison
	dataRec = RawData.decode("utf-8") 
	# Print the received data.
	# print(dataRec)
	# print(len(dataRec))

	# Decide whether to reply, or simulate packet loss. If rand is less than LOSS_RATE, we consider the packet lost and do not respond
	if rand < LOSS_RATE:
	   print("Reply not sent.")
	   continue
   	# Otherwise, the server responds
	seq_num = dataRec[0]
	if exp_num == seq_num:
		if exp_num == "0":
			exp_num = "1"
		else:
			exp_num = "0"
		f.write(RawData[1:])

	# Simulate network delay.
	delay = random.randint(0.0, 2 * AVERAGE_DELAY)
	print("Delay %d" % (delay))
	time.sleep(delay / 1000);
	serverSocket.sendto(bytes(seq_num, "utf8"), address)
	print("Reply sent.")
	if len(dataRec) < 513:
		break
f.close()
print("Transmission completed")