# We will need the following module to generate randomized lost packets
import socket
import sys
import time
import filecmp
from socket import *

if (len(sys.argv) != 2):
    print("Required arguments: Server IP Addr.")
    exit(0)

hostname = sys.argv[1]
port = 9093
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientsocket = socket(AF_INET, SOCK_DGRAM)
clientsocket.settimeout(1)

# default value according to the requirements
retransmission_limit = 5
retransmission_flag = 0
lastpacket_flag = 0
count = 0
seq_num = "0"
# open the input file, "rb" here represents read byte by byte from the file
# default encoding style "utf-8"
f = open("inputfile.txt","rb")
# print the SFTP target server and port number
print("Uploading the file inputfile.txt by using sFTP to the target server %s, %d" % (hostname, port))
start_time = time.time()

while (True):
    # break out after trying limit times of retransmission
    if count > retransmission_limit: 
        print("sFTP: file transfer unsuccessful: packet retransmission limit reached!")
        break
    if retransmission_flag == 0:
        if lastpacket_flag == 1:
            time_taken = time.time() - start_time
            print("sFTP: file sent successfully to %s in %.3f secs" % (hostname, time_taken))
            break
        data = f.read(512)
        # set the lastpacket_flag to 1 if we find that the length of the data is less than 512.
        if len(data) < 512:
            lastpacket_flag = 1
        # insert the sequence number in front of the data
        # convert all string into bytes
        packet = bytes(seq_num, "utf8") + data

    clientsocket.sendto(packet,(hostname, port))

    try:
        ackRecv, address = clientsocket.recvfrom(1024)
        # check the acknowledgement number of the reponse message
        # if receive a wrong ack, start retransmission
        if ackRecv.decode("utf-8") != seq_num:
            retransmission_flag = 1
            count += 1
            # print("Wrong ACK, try retransmission %d" % (count))
            continue
        else:
            # if client receives a good ack, then end the retransmission status and reset the 
            # sequence number
            retransmission_flag = 0
            count = 0
            if seq_num == "0":
                seq_num = "1"
            else:
                seq_num = "0"
            # print ("Fragment delivered!")
    except Exception:
        # detect a timeout, start retransmission
        count += 1
        retransmission_flag = 1
        # print ("Timeout, try retransmission %d" % (count))
f.close()
same = filecmp.cmp("inputfile.txt", "outputfile.txt")
print("Input and output file are same? ", same)



