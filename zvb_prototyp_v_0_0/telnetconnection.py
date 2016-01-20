import telnetlib
import config
u = config.user
p = config.password
HOST = "localhost"
tn = telnetlib.Telnet(HOST)
tn.read_until("login: ")
tn.write(u + "\r")
tn.read_until("password: ")
tn.write(p + "\r")
tn.read_until(">")
tn.write("vboxmanage list vms\r")
#tn.read_until("C:\Users\admin>")
print tn.read_until(">")
tn.write("exit\r")

print tn.read_all()
print "zamykam"
tn.close()
