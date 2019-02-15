import uuid

from scapy.all import *
from scapy.config import *

import zlib


from scapy_http.http import *


def extract_payload(http_headers, payload, output_path):
    print('extract')
    payload_type = http_headers["Content-Type"].split("/")[1].split(";")[0]
    try:
        if "Content-Encoding" in http_headers.keys():
            if http_headers["Content-Encoding"] == "gzip":
                file = zlib.decompress(payload, 16+zlib.MAX_WBITS)
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


def stripimg(packet):
        http_payload = b""

        try:
            if packet.haslayer(TCP):
                payload = packet[TCP].payload
                http_header_exists = False
                try:
                    http_header = payload[payload.index(b"HTTP/1.1"):payload.index(b"\r\n\r\n")+2]
                    print("http_header:", http_header)

                    if http_header:
                        http_header_exists = True
                except:
                    pass
                if not http_header_exists and http_payload:
                    http_payload += payload

                elif http_header_exists and http_payload:
                    http_header_raw = http_payload[:http_payload.index(b"\r\n\r\n")+2]
                    http_header_parsed = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", http_header_raw.decode("utf8")))

                    if "Content-Type" in http_header_parsed.keys():

                        if "image" in http_header_parsed["Content-Type"]:
                            image_payload = http_payload[http_payload.index(b"\r\n\r\n")+4:]

                            if image_payload:
                                extract_payload(http_header_parsed, image_payload, output_path)
                    http_payload = payload
                elif http_header_exists and not http_payload:
                    http_payload = payload
        except:
            pass


iface = conf.iface
print(iface)

output_path = './imgages/'


data = b''

def callback(pkt):

    global data
    if pkt.haslayer(HTTP):
        # pkt_http : HTTP = pkt["HTTP"]
        # pkt.show()
        # pkt.show(dump=True)
        print("\tHTTP", True)

        pkt[HTTP].show(dump=False)

        if pkt.haslayer(HTTPRequest):
            print("\t\tHTTPRequest", True)

            if data:
                try:
                    pass
                    #print("Parse in request", data)
                except:
                    pass

            if pkt[HTTPRequest].haslayer(Raw):
                print("New data")
                data = bytes(pkt[HTTPRequest].payload)

            #payload(dump=True)

            """
            http_header_exists = b""
            try:
                http_header = payload[payload.index(b"HTTP/1.1"):payload.index(b"\r\n\r\n") + 2]


                print("Header response:", http_header)
                if http_header:
                    http_header_exists = True
                    print(http_header_exists)
            except ValueError as err:
                print(err)
                pass
            """
        elif pkt.haslayer(HTTPResponse):
            print("\t\tHTTPResponse", True)
            if data:
                try:
                    pass
                    #print("Parse in response", data)
                except:
                    pass

            if pkt[HTTPResponse].haslayer(Raw):
                #print(bytes(pkt[HTTPResponse].payload))
                data = bytes(pkt[HTTPResponse].payload)

        else:
            data += bytes(pkt[HTTP].payload)
            #print('Append raw: ', data)
            # payload(dump=True)
            http_payload = b""



