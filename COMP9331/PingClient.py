import sys
import time
import socket
import math

# input check
if len(sys.argv) != 3:
    print('Invalid Input!')
    sys.exit()

# receive the input(hoost and port num)
host = sys.argv[1]
port = int(sys.argv[2])
add = (host, port)

# create the socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket.')
    sys.exit()
s.settimeout(2)

# start iteration
L_RTT = []
if (port > 1024):
    for i in range(1, 11):
        send_time = time.time()
        msg = 'PING' + str(i) + str(send_time) + '\r\n'
        package_bytes = msg.encode('utf-8')
        s.sendto(package_bytes, (host, port))
        try:
            s.recvfrom(1024)
            receive_time = time.time()  # get the receive time
            delay = int(abs(send_time - receive_time) * 1000)  # time is ms *1000 to make it s
            L_RTT.append(int(delay))
            print('ping to ' + str(host) + ', seq =' + str(i) + ', rtt = ' + str(delay) + ' ms')
        except:
            print('ping to 127.0.0.1' + ', seq =' + str(i) + ', time out')

# output
L_RTT.sort()  # sort the list to make the minimum at the beginning the maximum at the end

min_rtt = L_RTT[0]
avr_rtt = sum(L_RTT) / len(L_RTT)
max_rtt = L_RTT[-1]

print('Maximum RTT is', max_rtt)
print('Minimum RTT is', min_rtt)
print('Average RTT is', avr_rtt)

# for test
# python PingClient.py 127.0.0.1 1025
