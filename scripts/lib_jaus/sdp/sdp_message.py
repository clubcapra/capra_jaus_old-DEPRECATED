import struct
import io


class SDPMessage:

    def __init__(self, data):
        data = io.BytesIO(data)
        type_hc = ord(data.read(1))
        self.message_type = type_hc >> 2
        self.hc_flags = type_hc % 0b11
        self.data_size = struct.unpack(">H", data.read(2))[0]
        self.hc_number = self.hc_length = 0
        if self.hc_flags != 0:
            self.hc_number = ord(data.read(1))
            self.hc_length = ord(data.read(1))

        self.pbad_flags = ord(data.read(1))
        self.destination_id, self.source_id = struct.unpack("<II", data.read(8))
        self.payload = data.read(self.data_size - 15)
        self.sequence_number = struct.unpack("<H", data.read(2))[0]

    def get_message_type(self):
        return self.message_type

    def get_hc_flags(self):
        return self.hc_flags

    def get_data_size(self):
        return self.data_size

    def get_hc_number(self):
        return self.hc_number

    def get_hc_length(self):
        return self.hc_length

    def get_priority(self):
        return (self.pbad_flags & 0b11000000) >> 6

    def get_broadcast_flags(self):
        return (self.pbad_flags & 0b00110000) >> 4

    def get_ack_nack_flags(self):
        return (self.pbad_flags & 0b00001100) >> 2

    def get_data_flags(self):
        return self.pbad_flags & 0b00000011

    def get_destination_id(self):
        return self.destination_id

    def get_source_id(self):
        return self.source_id

    def get_payload(self):
        return self.payload

    def get_sequence_number(self):
        return self.sequence_number

    def __str__(self):
        s = "SDP:\n"
        s += " Message type: %d\n" % self.get_message_type()
        s += " HC flags: %d\n" % self.get_hc_flags()
        s += " Data size: %d\n" % self.get_data_size()
        if self.get_hc_flags() != 0:
            s += " HC Number: %d\n" % self.get_hc_number()
            s += " HC Length: %d\n" % self.get_hc_length()
        s += " Priority: %d\n" % self.get_priority()
        s += " Broadcast flags: %d\n" % self.get_broadcast_flags()
        s += " Ack/Nack flags: %d\n" % self.get_ack_nack_flags()
        s += " Data flags: %d\n" % self.get_data_flags()
        s += " Destination ID: %s\n" % self.get_destination_id()
        s += " Source ID: %s\n" % self.get_source_id()
        s += " Payload: %s\n" % ":".join("{:02x}".format(ord(c)) for c in self.get_payload())
        s += " Sequence number: %d" % self.get_sequence_number()
        return s

