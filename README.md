# SSH Password Brute Force Script

This script is a basic SSH password brute-force tool that attempts to gain access to an SSH server by trying passwords from a specified list. The script utilizes the `pwn` library for SSH connections and handles exceptions using `paramiko`.
____
## Dependencies

- Python 3.x
- `pwn` library
- `paramiko` library

## Prerequisites
- Install the required libraries if not already installed:
  
   ```bash
   pip install paramiko pwn
   pip install pwn

## Usage

1. Configure the Script
   
   ```bash
     hostname = ''  # Insert the target hostname or IP address here
     username = ''  # Insert the SSH username here
   
2. Prepare Password List
  -  Create a file named ssh-passwords.txt in the same directory as the script.
  -  Add each password you want to test on a new line in this file.

3. Run the script
   
   ```bash
     python ssh-bruteforce.py
   
