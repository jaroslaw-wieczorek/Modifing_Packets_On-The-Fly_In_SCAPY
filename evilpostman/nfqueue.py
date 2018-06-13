from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether


def modify(pkt):
    try:
        if pkt.dst == "00:00:00:00:00:00":
            pkt.dst="00:AA:00:AA:00:AA"
        
        
        if pkt.payload:
            if pkt.payload.dst != "0.0.0.0":
                pkt.payload.dst="192.168.1.100"
                print(pkt.payload.dst)
            print(pkt.dst)
    except Exception as err:
        print(err)



class QueuePacketCatcher:
    def __init__(self):
        self.captured_packets = list()

    def getcaptured_packets_by_ref(self):
        return self.captured_packets

    def modify(self, packet):
        pkt = IP(packet.get_payload())
        #self.captured_packets.append(pkt)
        print(pkt.summary())
        print(pkt[IP].ttl, end='')
        pkt[IP].ttl = -2
        print("  ==>  ", end='')
        print(pkt[IP].ttl)
        packet.accept()

    def accept_all(self):
        for pkt in self.captured_packets:
            pkt.accept()
        print("Accepted all packetinos.")

    def start_capture(self):
        nfqueue = NetfilterQueue()
        nfqueue.bind(1, self.modify, mode=COPY_PACKET)
        try:
            print("Begining capture.")
            nfqueue.run()
            #self.accept_all()
        except KeyboardInterrupt:
            pass
        
sniff(prn=modify)

catch = QueuePacketCatcher()
catch.start_capture()