# usr/env/bin python
# -*- coding:utf-8 -*-
import os
import sys
import queue
import threading
import multiprocessing

from scapy.all import *
import scapy_http.http as http
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP


GLOBAL_pkts = []


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
        self.nfqueue.bind(1, self.preprocesing_packets, mode=COPY_PACKET)
        self.qworker = NFQController(self.nfqueue)
        self.directory = "iptables-backup"
        self.backup = "backup"
        self.http_sessions = {}

    def get_whole_http(self, packet):
        # this is our callback on nfqueue when http session is gather
        pass

    def preprocesing_packets(self, packet):
        pkt = IP(packet.get_payload())
        http_payload = b""
        http_header_exists = False
        image = b""
        if pkt.haslayer(TCP) and pkt[TCP].haslayer(http.HTTP):
            GLOBAL_pkts.append(pkt)

        """ PACKET NFQEUEU TAMPER """

        packet.set_payload(bytes(pkt))
        packet.accept()

    def start_capture(self):
        if not self.runing:
            self.backupIPTables(self.directory, self.backup)
            os.popen("iptables -A INPUT -p tcp -j NFQUEUE --queue-num 1")
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


def scapy_callback(pkt):
    pass

if __name__ == '__main__':
    nfqueue = QueuePacketCatcher()
    nfqueue.start_capture()

    while True:
        try:
            pass
        except KeyboardInterrupt as err:
            break

        except Exception as err:
            print(err)

wrpcap('test.pcap', GLOBAL_pkts)
print("done")