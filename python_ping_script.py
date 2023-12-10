# ping.py

# Stephen Sparks - IFT 487 - Python script that pings IP addresses and search for active hosts 

import subprocess
import os

net_addr = input("Enter the first three octets of an IP address (Example 192.168.0): ") # user input for the start of the IP address range we will be "scanning"

with open(os.devnull, "wb") as bob: #creates a target to prevent any output from ping processes from being displayed (points it to devnull?)
    for n in range(254): # For statement
        ip = net_addr + "." + format(n + 1) # Creating the IP with string concat
        result = subprocess.Popen(["ping", "-n", "1", "-w", "500", ip], stdout=bob , stderr=bob).wait() # subprocess to ping the IP address look at Popen function
        if result: # if statment
            print(ip, "inactive - no ping response") # triggers if result is 0 aka ping unresponsive
        else:
            print(ip, "ACTIVE - ping responded, device detected") #print the ping was successful on any other instance
            
