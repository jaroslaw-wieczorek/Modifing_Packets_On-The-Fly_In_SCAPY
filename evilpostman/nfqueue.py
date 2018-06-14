from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
from evilpostman.iterface import Window


def modify(pkt):
    try:
        if pkt.dst != "0.0.0.0":
           pkt.dst="192.168.1.100"
        print(pkt.dst)
    except Exception as err:
        print(err)



class QueuePacketCatcher(Window):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.set_fit_width()
        self.captured_packets = list()
        self.set_sniff_tab_button_sniff(self.start_capture)
        self.runing = False

    def getcaptured_packets_by_ref(self):
        return self.captured_packets

    def modify(self, packet):
        pkt = IP(packet.get_payload())
        #print(pkt.dst)
        self.add_row_to_sniff_tab_list_of_packets(pkt)
        packet.set_payload(bytes(pkt))
        packet.accept()

    def accept_all(self):
        for pkt in self.captured_packets:
            pkt.accept()
        print("Accepted all packetinos.")

    def start_capture(self):
        if self.runing != True:
            self.runing = True
            nfqueue = NetfilterQueue()
            nfqueue.bind(1, self.modify, mode=COPY_PACKET)
            print("Begining capture.")
            nfqueue.run()
            #self.accept_all()


    def backupIPTables(directory, filename):
        if not os.path.exists(directory):
            try:
                os.makedirs(str(directory))
                os.popen("iptables-save > " + str(directory) + "/" + str(filename))
            except Exception as e:
                raise e

    def restoreIPTables(directory, filename):
        if not os.path.exists(directory):
            try:
                os.makedirs(str(directory))
                os.popen("iptables-restore " + str(directory) + "/" + str(filename))
            except Exception as e:
                raise e