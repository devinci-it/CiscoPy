from devices.device import Device

class Endpoint(Device):
    def __init__(self, hostname):
        super().__init__(hostname)
        self.vlan = 1

    def __str__(self):
        return f"Endpoint {self.hostname} (VLAN {self.vlan})"
