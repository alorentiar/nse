import sys
import os
import nmap

# Get the target host IP from the command line
import nmap

# Define the target and port
target = input("Enter target IP or hostname: ")
port = 443

# Create a new Nmap scanner object
scanner = nmap.PortScanner()

# Define the function to check for web server
def check_webserver(host, port):
    scanner.scan(host, str(port))
    return scanner[host]['tcp'][port]['state'] == 'open'

# Execute the check and print the result
if check_webserver(target, port):
    print("The target is running a web server on port 80")
else:
    print("The target is not running a web server on port 80")
