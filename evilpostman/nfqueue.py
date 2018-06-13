from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
from evilpostman.iterface import Window
import queue
import threading

class NFQController(threading.Thread):

    def __init__(self,func):
        threading.Thread.__init__(self)
        self._must_stop = False
        self.result = ""
        self.nfqueue = NetfilterQueue()
        self.nfqueue.bind(1, func, mode=COPY_PACKET)

    def stop(self):
        self._must_stop = True

    def run(self):
        try:
            print("Begining capture.")
            self.nfqueue.run()
        except self._must_stop==True:
            pass


class QueuePacketCatcher(Window):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.set_fit_width()
        self.captured_packets = list()
        self.set_button_funct(self.cap_button_sniff, self.start_capture)

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
            a = NFQController(self.modify)
            a.start()



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