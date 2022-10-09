import os 
import socket
addres = input("Website Name> ")
websitename = "addres"
ip = socket.gethostbyaddr('ssh.'+addres)
print ("IP Behind Cloudflare - "+ip) 
os.exit()

