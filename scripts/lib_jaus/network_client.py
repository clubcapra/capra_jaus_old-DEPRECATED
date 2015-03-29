import dpkt, dpkt.udp


class NetworkClient(object):
    def __init__(self):
        pass

    def start(self):
        filename = '../../pcaps/jaus52,5pts.pcap'

        for ts, pkt in dpkt.pcap.Reader(open(filename,'r')):
            eth = dpkt.ethernet.Ethernet(pkt)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                continue
            ip = eth.data
            udp = ip.data
            if type(udp) != dpkt.udp.UDP:
                continue
            if udp.sport != 3794:
                continue

            self._on_message(udp.data)

    def _on_message(self, data):
        print data