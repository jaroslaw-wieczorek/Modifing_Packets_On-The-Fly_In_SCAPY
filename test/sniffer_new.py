# usr/env/bin python
# -*- coding:utf-8 -*-
import os
import sys
import uuid
import zlib
import queue

import threading
import multiprocessing

from scapy.all import *
import scapy_http.http as http
from netfilterqueue import NetfilterQueue, COPY_PACKET
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP
import lxml.html as lxhtml
import html

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
        self.nfqueue_request = NetfilterQueue()
        self.nfqueue_response = NetfilterQueue()

        self.nfqueue_request.bind(1, self.other_procesing, mode=COPY_PACKET)
        self.nfqueue_response.bind(2, self.preprocesing_packets, mode=COPY_PACKET)
        self.qworker_request = NFQController(self.nfqueue_request)
        self.qworker_response = NFQController(self.nfqueue_response)

        self.directory = "iptables-backup"
        self.backup = "backup"
        self.http_payload = b''
        self.http_header_exists = False
        self.counter = 0
        self.myhost = b"icons.iconarchive.com"
        self.myreferer = b"http://www.iconarchive.com/show/free-global-security-icons-by-aha-soft/CCTV-Camera-icon.html"
        self.mypath = b"/icons/aha-soft/free-global-security/icons-390.jpg"
        self.dport = 80
        self.dst = "104.25.157.13"

    def extract_payload(self, http_headers, payload, output_path):
        print('extract')
        payload_type = http_headers["Content-Type"].split("/")[1].split(";")[0]
        try:
            if "Content-Encoding" in http_headers.keys():
                if http_headers["Content-Encoding"] == "gzip":
                    file = zlib.decompress(payload, 16 + zlib.MAX_WBITS)
                elif http_headers["Content-Encoding"] == "deflate":
                    file = zlib.decompress(payload)
                else:
                    file = payload
            else:
                file = payload
        except:
            pass

        filename = uuid.uuid4().hex + "." + payload_type
        file_path = output_path + "/" + filename
        fd = open(file_path, "wb")
        fd.write(file)
        fd.close()

    def other_procesing(self, packet):
        pkt: IP = IP(packet.get_payload())
        self.counter += 1
        # print(self.counter, packet)

        image = b''
        content_type = 'Content-Type'

        if pkt.haslayer(TCP) and pkt.haslayer(http.HTTPResponse):  # and (pkt[TCP].sport == 80 or pkt[TCP].dport == 80):
            payload: http.HTTP = pkt[TCP].payload
            self.http_header_exists = False

            if hasattr(payload, 'Headers'):
                http_header = getattr(payload, 'Headers')

                print("[*] Heeader exists \n:", pkt.src, ":", pkt.sport, pkt.dst, ":", pkt.dport, http_header)

                if http_header:
                    self.http_header_exists = True

                    if hasattr(payload, content_type) and b'text/html' in getattr(payload, content_type):
                        print(content_type, ':', getattr(payload, content_type))

                        html_data = str(payload.payload)
                        doc = lxhtml.fromstring(str(html_data))

                        #doc = lxhtml.fromstring(html_page)
                        img = doc.find('.//img')
                        if img is not None:
                            parent = img.getparent()
                            parent.text = img.tail
                        #doc.remove(img)

                        #print("DOC without img:", lxhtml.tostring(doc))

                    if pkt['HTTPResponse'].haslayer(Raw):
                        print(content_type, ':', getattr(payload, content_type))

            else:
                html_data = str(payload.payload)
                doc = lxhtml.fromstring(str(html_data))
                # doc = lxhtml.fromstring(html_page)
                img = doc.find('.//img')
                if img is not None:
                    parent = img.getparent()
                    parent.text = img.tail
                    # doc.remove(img)

                print("DOC without img:", lxhtml.tostring(doc))
                        #print("RAW")
                        #raw = pkt['HTTPResponse'].getlayer(Raw)

                        #print(raw)
                        #print(bytes(raw).split(b'\n\r'))


            if not self.http_header_exists and self.http_payload:
                self.http_payload += payload
                print("add payload")
                print(len(self.http_payload))

            elif self.http_header_exists and self.http_payload:

                http_header_raw = self.http_payload[:self.http_payload.index(b"\r\n\r\n") + 2]
                http_header_parsed = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n",
                                                     http_header_raw.decode("utf8")))

                if "Content-Type" in http_header_parsed.keys():
                    if "image" in http_header_parsed["Content-Type"]:
                        image_payload = self.http_payload[self.http_payload.index(b"\r\n\r\n") + 4:]
                        if image_payload:
                            self.extract_payload(http_header_parsed, image_payload, 'images')
                            self.http_payload = payload

                elif self.http_header_exists and not self.http_payload:
                    self.http_payload = payload

            packet.set_payload(bytes(pkt))
        packet.accept()



    def preprocesing_packets(self, packet):
        pkt: IP = IP(packet.get_payload())
        self.counter += 1
        #print(self.counter, packet)
        if pkt.haslayer(TCP) and (pkt[TCP].dport == 8080 or pkt[TCP].dport == 80 or pkt[TCP].dport == 8000) and pkt[TCP].payload:
            http_request: http.HTTPRequest = pkt[TCP].payload
            http_request.show()
            payload_before = len(pkt[TCP].payload)
            if hasattr(http_request, "Method") and getattr(http_request, "Method") == b"GET":
                #print("MAMY GET")
                #print(http_request)
                if hasattr(http_request, "Accept-Encoding") and getattr(http_request, "Accept-Encoding") and (
                    hasattr(http_request, "Path") and hasattr(http_request, 'Host')) and hasattr(http_request, 'Referer'):
                    if b"gzip" in getattr(http_request, "Accept-Encoding"):
                        host = getattr(http_request, "Host")
                        path = getattr(http_request, "Path")
                        url = host + path
                        if b'.png' in url or b'.jpg' in url or b'.bmp' in url:
                            myurl = self.myhost + self.mypath
                            print(url, '->', myurl)
                            setattr(http_request, "Host", self.myhost)
                            setattr(http_request, "Path", self.mypath)
                            setattr(http_request, 'Referer', self.myreferer)
                            pkt[TCP].dport = self.dport
                            pkt[IP].dst = self.dst
                            # setattr(http_request, "Referer", self.myreferer)
                            payload_after = len(pkt[TCP].payload)
                            payload_dif = payload_after - payload_before
                            del pkt[IP].len
                            #pkt[IP].len = pkt[IP].len + payload_dif
                            del pkt[IP].chksum
                            del pkt[TCP].chksum
                            pkt.show(dump=True)
                            packet.set_payload(bytes(pkt))
        packet.accept()
        # PACKET NFQEUEU TAMPER

        #packet.set_payload(bytes(pkt))
        #packet.accept()

    def start_capture(self):
        if not self.runing:
            self.backupIPTables(self.directory, self.backup)

            os.popen("iptables -A OUTPUT -p tcp --dport 80 -j NFQUEUE --queue-num 1")
            os.popen("iptables -A INPUT -p tcp --sport 80 -j NFQUEUE --queue-num 2")

            self.qworker_request = NFQController(self.nfqueue_request)
            self.qworker_response = NFQController(self.nfqueue_response)

            self.qworker_request.daemon = True
            self.qworker_response.daemon = True
            self.runing = True
            self.qworker_request.start()
            self.qworker_response.start()
        else:
            print("stopping")
            self.restoreIPTables(self.directory, self.backup)
            self.runing = False

    def stop_capture(self):
        self.qworker_request.stop()
        self.qworker_response.stop()
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
        except Exception as err:
            print(err)

