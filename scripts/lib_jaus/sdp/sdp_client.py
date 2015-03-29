from ..network_client import NetworkClient
from sdp_message import SDPMessage

class SDPClient(NetworkClient):
    on_message = None

    def __init__(self):
        super(SDPClient, self).__init__()

    def _on_message(self, data):
        msg = SDPMessage(data)
        print msg
        print "=========================="
        if self.on_message:
            self.on_message(msg.get_payload())

