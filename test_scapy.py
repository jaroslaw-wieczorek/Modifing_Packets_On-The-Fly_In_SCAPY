from scapy.all import *

TIMEOUT = 2
conf.verb = 0
for ip in range(0, 256):
    packet = IP(dst="192.168.0." + str(ip), ttl=20)/ICMP()
    reply = sr1(packet, timeout=TIMEOUT)
    sendp(Ether(src="FF:FF:FF:FF:FF:55",dst="FF:FF:FF:FF:FF:FF")/IP(dst="192.168.0." + str(ip), ttl=20)/ICMP())
    if not (reply is None):
         print(reply.dst, "is online")
    else:
         print("Timeout waiting for %s" % packet[IP].dst)
    