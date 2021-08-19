#!/bin/python3


# This is a python3 portscanner.
# Type  ' python3 portscanner.py [Host or IPv4-Adress] [lower limit for the ports] '



# Import the libraries sys, socket and datetime
import sys
import socket
from datetime import datetime


lower_range_ports = 50
# Setting goal
if len(sys.argv) >= 2:
# Translating Host-Name into IPv4-Adress
     ziel = socket.gethostbyname(sys.argv[1])
else:
     print("Too less arguments!\nType:\npython3 portscanner.py [Host or IPv4-Adress] [lower limit for the ports]")
     sys.exit()
if len(sys.argv) == 3 and int(sys.argv[2])>0 and int(sys.argv[2])<85:
     lower_range_ports = int(sys.argv[2])
else:
     print("Enter a correct lower limit for the ports!\nType:\npython3 portscanner.py [Host or IPv4-Adress] [lower limit for the ports]")
     sys.exit()
     
# Making Banner
print("""\
         ___       _     __                      ____     
        / _ \     | |  _/ _)                    |__ /     
  _ __ | | | |_ __| |_/ \ \  ___ __ _ _ __  _ __ |_ \_ __ 
 | '_ \| | | | '__| __\  \ \/ __/ _` | '_ \| '_ \___/ '__|
 | |_) | |_| | |  | |_ \ \_/ (_| (_| | | | | | | |  | |   
 | .__/ \___/|_|   \__(__/  \___\__,_|_| |_|_| |_|  |_|   
 | |                                                      
 |_|                   
                                                                                                                                                                     
""")
print("by Hxckbxrd (GitHub: https://)\n")
print("-" * 50)
print("Goal gets scanned: ", ziel)
print("Started: ", str(datetime.now()))
print("-" * 50)

# Showing Not-Reachable Ports?     
closed_ports = input("Do you want to see the not-reachable ports? [Y/n]")

# Search for open ports  
try: 
     for port in range(lower_range_ports,85):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          socket.setdefaulttimeout(1)
          result = s.connect_ex((ziel, port))
          if (result == 0):
               print("Port ", str(port), " is open!")
          elif (closed_ports == "Y"):
               print("Port ", str(port), " is not reachable!")
          s.close()     

# Cancel Scanning by pressing Ctrl + C on your keyboard          
except KeyboardInterrupt:
     print("\nProgram stopped.")
     sys.exit()
     
# Handling different socket errors
except socket.gaierror:
     print("Hostname couldn´t get solved.")
     sys.exit()
     
except socket.error:
     print("Couldn´t connect to server.")
     sys.exit()
