import os
import socket
import dns.resolver
cfdns = dns.resolver.Resolver()
os.system('clear')
class c:
        orange='\033[33m'
print (c.orange + """
            CFdns - CF Bypass - Realese
                Author - Bluesuma
                      Methods:
                 1] DNS      2] SSH
""")
sitead = input(c.orange + "Wesbite> ")
meth = input(c.orange + "Method> ")
if meth == "1":
    site = "sitead"
    bpip = cfdns.query(sitead, "A")
    for rdata in bpip:
        print (c.orange + "IP Behind CloudFlare")
        print (rdata)

elif meth == "2":
    site = "sitead"
    ip = socket.gethostbyname('ssh.'+sitead)
    print (c.orange + "IP Behind Cloudflare - "+ip)
else:
    print (c.orange + "[!] Error | Please use a listed method")

