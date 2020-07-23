from .worker_info import WorkerInfo

class ProbeAck(object):
    """
    System packet that will be encapsulated inside an UDP packet
    and reply back to collector host using information provided
    in probe_init packet
    """
    def __init__(self, packet_id: str, info: 'WorkerInfo'):
        self.id = packet_id
        self.info = info

    def __str__(self):
        return "{} - {}".format(id, str(self.info))

    def __repr__(self):
        return "{}({} - {})".format(self.__class__.__name__,
                                    id,
                                    str(self.info))