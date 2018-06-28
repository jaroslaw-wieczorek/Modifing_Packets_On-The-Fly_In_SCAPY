from scapy.all import *
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
from evilpostman.iterface import Window
from evilpostman.pyqt_scapy_item import PyQtScapyTableWidgetItem
import queue
import threading


class Packet_handler(Window):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.magic_filter = None

    def pkt_hasLayer(self, pkt, layer):
        if pkt.haslayer(layer):
            self.add_row_to_mod_list_packets(pkt)

    def filter(self, packet):
        #checks if packet applies to filter
        #packet_copy=packet
        #current_dic = self.filter_dic

        self.magic_filter = self.magical()
        #print(self.magic_filter)
        for name, protocols in self.magic_filter.items():
            if self.protocol_verify(packet, protocols):
                return [True, name]
        return [False, False]

    def protocol_verify(self,packet, protocols):
        for protocol in protocols:
            try:
                protocol_curr = packet[protocol[0]]
                if protocol_curr:
                    for value in protocol[1:]:
                        if str(getattr(protocol_curr, value[0])) != str(value[1]):
                            return False
            except:
                return False
        return True
    def modify(self, packet, filter_name):
        #modifies packet
        for protocol in self.modify_dic[filter_name].items():
            if packet[protocol[0]]:
                 for value in protocol[1:]:
                     #getattr(protocol_curr, value[0]) != value[1]:
                     setattr(packet[protocol[0]], value[0], value[1])
        return packet

    def handle_my_packet(self, packet):
        packetino = packet
        self.add_row_to_cap_list_of_packets(packetino)
        filter_result = self.filter(packetino)
        #self.add_row_to_mod_list_packets(packetino)
        #print(filter_result[0])
        if filter_result[0]:
            print("CAUGHT ONE")
            #packetino = self.modify(packetino, filter_result[1])
            #modifies the packet adds to modified list
            self.add_row_to_modified_list_of_packets(packetino)
        return packetino