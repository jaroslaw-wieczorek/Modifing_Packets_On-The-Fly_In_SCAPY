from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
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

catch = QueuePacketCatcher()
catch.start_capture()