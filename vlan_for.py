#Script para configuração automatica de vlan's rodando PYTHON3
import telnetlib
import getpass
import sys

HOST = "10.10.100.2" #IP do seu device (switch e/ou roteador)
user = input("Usuário: ")
password = getpass.getpass() #get password with hide mode


tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n") #senha do seu enable
tn.write(b"conf t\n")
for vlanauto in range (10, 20):
    tn.write(b"Vlan " + str(vlanauto).encode('ascii') + b"\n")
    tn.write(b"name dados_ " + str(vlanauto).encode('ascii') + b"\n")
#tn.write(b"int loop 1\n")
#tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"copy running-config startup-config\n")
tn.write(b"\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))