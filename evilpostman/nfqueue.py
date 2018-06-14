import multiprocessing

from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether
from evilpostman.iterface import Window
from evilpostman.pyqt_scapy_item import PyQtScapyTableWidgetItem
import queue
import threading


class NFQController(threading.Thread):
    def __init__(self, nfq):
        threading.Thread.__init__(self)
        self._must_stop = False
        self.other = nfq

    def stop(self):
        self._must_stop = True
        sys.exit()

    def run(self):
        print("Begining capture.")
        self.other.run()


class QueuePacketCatcher(Window):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        self.captured_packets = list()
        self.runing = False
        self.nfqueue = NetfilterQueue()
        self.nfqueue.bind(1, self.modify, mode=COPY_PACKET)
        self.qworker = NFQController(self.nfqueue)





    def getcaptured_packets_by_ref(self):
        return self.captured_packets


    def modify(self, packet):
        pkt = IP(packet.get_payload())
        # print(pkt.dst)
        self.add_row_to_cap_list_packets(pkt)
        packet.set_payload(bytes(pkt))
        packet.accept()

    def get_packet(self, packet):
        pkt = IP(packet.get_payload())
        # print(pkt.dst)
        self.add_row_to_cap_list_packets(pkt)
        packet.set_payload(bytes(pkt))
        packet.accept()

    def accept_all(self):
        for pkt in self.captured_packets:
            pkt.accept()
        print("Accepted all packetinos.")

    def start_capture(self):
        self.add_row_to_cap_list_packets(IP(dst="192.168.100.123"))
        if self.runing != True:
            self.qworker = NFQController(self.nfqueue)
            self.qworker.daemon = True
            self.runing = True
            self.qworker.start()
        else:
            print("stopping")
            self.runing = False
            try:
                self.qworker._stop()
            except Exception as err:
                print(err)

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
