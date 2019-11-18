This Programming assignment is based on Python3.7.4
(The test transmission data is encoded in "utf-8")

Operation:
Firstly, store the file which you wanna transmit in the local directory
file name should be "inputfile.txt"

Next, open windows command line and run SftpServer.py:
C:\path\py SftpServer.py 9093

Then, open a new command line window and run SftpClient.py:
C:\path\py SftpClient.py 127.0.0.1

Here is a sample output from Sender end(Server Lost Rate = 30%, Average Delay = 100ms):
Uploading the file inputfile.txt by using sFTP to the target server 127.0.0.1, 9093
sFTP: file sent successfully to 127.0.0.1 in 48.451 secs
Input and output file are same?  True

Here is a sample output from Receiver end(Server Lost Rate = 30%, Average Delay = 100ms)
Reply not sent.
Delay 44
Reply sent.
Reply not sent.
Delay 171
Reply sent.
Delay 100
Reply sent.
Reply not sent.
Reply not sent.
Delay 43
Reply sent.
Reply not sent.
Delay 184
Reply sent.
Delay 18
Reply sent.
Delay 193
Reply sent.
Reply not sent.
Delay 92
Reply sent.
Delay 120
Reply sent.
Delay 129
Reply sent.
Delay 69
Reply sent.
Delay 109
Reply sent.
Delay 47
Reply sent.
Reply not sent.
Delay 43
Reply sent.
Delay 90
Reply sent.
Delay 190
Reply sent.
Delay 2
Reply sent.
Reply not sent.
Delay 31
Reply sent.
Delay 127
Reply sent.
Delay 144
Reply sent.
Delay 38
Reply sent.
Reply not sent.
Reply not sent.
Delay 77
Reply sent.
Delay 79
Reply sent.
Delay 166
Reply sent.
Delay 115
Reply sent.
Delay 46
Reply sent.
Delay 81
Reply sent.
Reply not sent.
Reply not sent.
Delay 35
Reply sent.
Reply not sent.
Delay 0
Reply sent.
Reply not sent.
Delay 62
Reply sent.
Reply not sent.
Reply not sent.
Delay 134
Reply sent.
Reply not sent.
Delay 119
Reply sent.
Delay 133
Reply sent.
Delay 94
Reply sent.
Delay 94
Reply sent.
Delay 4
Reply sent.
Delay 16
Reply sent.
Delay 115
Reply sent.
Delay 168
Reply sent.
Delay 153
Reply sent.
Delay 150
Reply sent.
Reply not sent.
Delay 46
Reply sent.
Delay 28
Reply sent.
Delay 87
Reply sent.
Delay 46
Reply sent.
Reply not sent.
Delay 86
Reply sent.
Delay 173
Reply sent.
Delay 158
Reply sent.
Reply not sent.
Delay 191
Reply sent.
Delay 149
Reply sent.
Delay 168
Reply sent.
Reply not sent.
Delay 14
Reply sent.
Delay 168
Reply sent.
Delay 189
Reply sent.
Delay 94
Reply sent.
Delay 71
Reply sent.
Delay 137
Reply sent.
Delay 88
Reply sent.
Delay 14
Reply sent.
Delay 141
Reply sent.
Delay 67
Reply sent.
Delay 17
Reply sent.
Delay 133
Reply sent.
Delay 163
Reply sent.
Delay 189
Reply sent.
Delay 185
Reply sent.
Delay 82
Reply sent.
Delay 135
Reply sent.
Delay 64
Reply sent.
Delay 99
Reply sent.
Delay 143
Reply sent.
Delay 18
Reply sent.
Reply not sent.
Delay 42
Reply sent.
Delay 28
Reply sent.
Reply not sent.
Reply not sent.
Delay 157
Reply sent.
Delay 85
Reply sent.
Reply not sent.
Reply not sent.
Reply not sent.
Reply not sent.
Delay 57
Reply sent.
Delay 85
Reply sent.
Delay 178
Reply sent.
Delay 34
Reply sent.
Reply not sent.
Delay 161
Reply sent.
Delay 92
Reply sent.
Reply not sent.
Delay 57
Reply sent.
Delay 54
Reply sent.
Reply not sent.
Delay 12
Reply sent.
Delay 153
Reply sent.
Reply not sent.
Delay 159
Reply sent.
Delay 40
Reply sent.
Delay 165
Reply sent.
Delay 192
Reply sent.
Delay 77
Reply sent.
Reply not sent.
Delay 56
Reply sent.
Reply not sent.
Reply not sent.
Delay 142
Reply sent.
Delay 164
Reply sent.
Reply not sent.
Delay 131
Reply sent.
Delay 87
Reply sent.
Delay 200
Reply sent.
Delay 2
Reply sent.
Delay 122
Reply sent.
Delay 77
Reply sent.
Transmission completed