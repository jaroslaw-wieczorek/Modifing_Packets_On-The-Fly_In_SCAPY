import multiprocessing

from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from evilpostman.iterface import Window
from evilpostman.pyqt_scapy_item import PyQtScapyTableWidgetItem
import queue
import threading
from evilpostman.Packet_handler import Packet_handler


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


class QueuePacketCatcher:
    def __init__(self):
        self.captured_packets = list()
        self.runing = False
        self.nfqueue = NetfilterQueue()
        self.nfqueue.bind(1, self.tamper, mode=COPY_PACKET)
        self.qworker = NFQController(self.nfqueue)
        self.directory = "iptables-backup"
        self.backup = "backup"
        self.handler = Packet_handler()

    def tamper(self, packet):
        pkt: Packet = IP(packet.get_payload())
        # print(pkt.dst)
        pkt: Packet = self.handler.handle_my_packet(pkt)
        packet.set_payload(bytes(pkt))
        packet.accept()

    def start_capture(self):
        if not self.runing:
            self.backupIPTables(self.directory, self.backup)
            os.popen("iptables -A INPUT -j NFQUEUE --queue-num 1")
            self.qworker = NFQController(self.nfqueue)
            self.qworker.daemon = True
            self.runing = True
            self.qworker.start()
        else:
            print("stopping")
            self.restoreIPTables(self.directory, self.backup)
            self.runing = False

    def stop_capture(self):
        print("stopping")
        if self.runing:
            print("restoring")
            self.restoreIPTables(self.directory, self.backup)
            self.runing = False

    def backupIPTables(self, directory, filename):
        if not os.path.exists(directory):
            try:
                os.makedirs(str(directory))
            except Exception as e:
                raise e
        if os.path.exists(directory):
            command = "iptables-save > " + str(directory) + "/" + str(filename)
            os.popen(command)

    def restoreIPTables(self, directory, filename):
        if os.path.exists(directory):
            try:
                command = "iptables-restore < " + str(directory) + "/" + str(filename)
                os.popen(command)

                # os.popen()
            except Exception as err:
                print("iptables error: ", err)
                raise err
        else:
            print("Can't load iptables rules (dir not exist) - clean iptables")
            os.popen("iptables -F")
            
