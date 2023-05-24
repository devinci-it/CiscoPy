from devices.device import Device

class Router(Device):
    def __init__(self, hostname):
        super().__init__(hostname)
        self.routing_protocol = 'OSPF'
