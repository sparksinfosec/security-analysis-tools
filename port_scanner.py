# port_scanner.py

# Stephen Sparks - IFT 475 - Python Script that scans ports


import socket # socket module network comms

def scan_ports(target_ip, start_port, end_port): # function called scan port with three parameters
    open_ports = [] # init an empty list

    for port in range(start_port, end_port + 1): # For statment with start port variable going to end point plus 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# creating a socket object and assigning it to sock (look at SOCKET documentation)
        sock.settimeout(1) # sock varable with a method set timeout?

        try:
            sock.connect((target_ip, port)) # tries to connect to the target IP and port
            open_ports.append(port) # adds the open port to the open_port list if successful
            sock.close()
        except(socket.timeout, ConnectionRefusedError): # error handling for connection refused
            pass # pass over it

    return open_ports # returning the list at the end of the function

def main(): # actual exe
    target_ip = input("ENTER the target IP address: ")
    start_port = int(input("Enter the starting port: ")) # makes this input a int
    end_port = int(input("Enter the ending port: "))
    print("Scanning...") # just a print statment

    open_ports = scan_ports(target_ip, start_port, end_port) # calling the functions and passing in the input

    if open_ports:
        print(f"Open ports on {target_ip}: {','.join(map(str, open_ports))}") # prints open ports if found really print out the list of open port after function run
    else:
        print(f"No open ports found on {target_ip}") # if no open ports found print this 
            
if __name__ == "__main__": #running the main program/execution 
    main()
    
# can you make this more interactive, such as showing the scanning of the port and seeing if anything returns instead of just the scanning print line
