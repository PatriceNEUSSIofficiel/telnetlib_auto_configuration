#!/bin/python3
import telnetlib
import getpass

# Set the Telnet server address and port number
host = "localhost"
port = 23

# Set the username
username = input("Enter username : ")

# Get password from the user
print(f"Logging in as '{username}'")
password = getpass.getpass()

# Set the command to execute
command = "ls -l"

# Create a Telnet object
tn = telnetlib.Telnet(host, port)

# Wait for the login prompt
tn.read_until(b"login: ")

# Enter the username and wait for the password prompt
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")

# Enter the password and wait for the shell prompt
tn.write(password.encode('ascii') + b"\n")
tn.read_until(b"$ ")

# Execute the command and wait for the output
tn.write(command.encode('ascii') + b"\n")
output = tn.read_until(b"$ ")

# Print the output
print(output.decode('utf-8'))

# Close the Telnet connection
tn.close()