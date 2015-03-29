from sdp.sdp_client import SDPClient


class Jaus:
    def __init__(self):
        self.client = SDPClient()
        self.client.on_message = self.on_message

    def start(self):
        self.client.start()

    def on_message(self, msg):
        print msg
        print msg.encode("hex")