from CiscoPy.devices.device import Device
from CiscoPy.devices.interfaces import Interface
import ipaddress
from app import App

class L3Switch(Device):
    def __init__(self, hostname, vtp_domain):
        super().__init__(hostname)  
        self.routing_protocol = 'OSPF'
        self.vtp_domain = vtp_domain
        self.vlans = {'default': []}
        self.vtp_mode = 'server'
        self.networks = []
        self.access_ports = []
        self.trunk_ports = []
        self.lag_interfaces = []

    def add_vlan(self, vlan_name, vlan_id, vtp_domain=None):
        if not vtp_domain:
            vtp_domain = 'default'
        if vtp_domain not in self.vlans:
            self.vlans[vtp_domain] = []
        self.vlans[vtp_domain].append(vlan_id)
        for device in App.devices:
            if isinstance(device, L3Switch) and device.vtp_domain == vtp_domain and device != self:
                device.vlans[vtp_domain] = self.vlans[vtp_domain].copy()

    def add_interface_ip(self, interface_name: str, ip_address: str) -> None:
        for interface in self.interfaces:
            if interface.name == interface_name:
                interface.add_ip(ip_address)
                network, subnet_mask = ip_address.split('/')
                subnet_mask = int(subnet_mask)
                if subnet_mask < 8 or subnet_mask > 30:
                    raise ValueError('Subnet mask should be between 8 and 30')
                network = ipaddress.IPv4Network(network + '/' + str(subnet_mask), strict=False)
                self.networks.append(network)
                for vlan_id in interface.vlan_ids:
                    for device in App.devices:
                        if isinstance(device, L3Switch) and device.vtp_domain == self.vtp_domain and device != self:
                            for dev_interface in device.interfaces:
                                if vlan_id in dev_interface.vlan_ids:
                                    dev_interface.add_ip(str(network.network_address) + '/' + str(subnet_mask))
                                    dev_interface.networks.append(network)
                break
        else:
            raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")
        self.update_networks()

    def update_networks(self) -> None:
        for interface in self.interfaces:
            for vlan_id in interface.vlan_ids:
                for device in App.devices:
                    if isinstance(device, L3Switch) and device.vtp_domain == self.vtp_domain and device != self:
                        for dev_interface in device.interfaces:
                            if vlan_id in dev_interface.vlan_ids:
                                network, subnet_mask = dev_interface.get_ip().split('/')
                                subnet_mask = int(subnet_mask)
                                network = ipaddress.IPv4Network(network + '/' + str(subnet_mask), strict=False)
                                dev_interface.networks.append(network)

    def add_access_port(self, interface_name):
        for interface in self.interfaces:
            if interface.name == interface_name:
                if interface.isLagged:
                    raise ValueError(f"{interface_name} is a lagged interface and cannot be an access port")
                else:
                    self.access_ports.append(interface)
                    break
        else:
            raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")

    def add_trunk_port(self, interface_name, vlan_ids):
        for interface in self.interfaces:
            if interface.name == interface_name:
                if interface.isLagged:
                    raise ValueError(f"{interface_name} is a lagged interface and cannot be a trunk port")
                else:
                    interface.vlan_ids = vlan_ids
                    self.trunk_ports.append(interface)
                    break
        else:
            raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")

    def get_lagged_interfaces(self, interface_dict_list):
        if not isinstance(interface_dict_list, list):
            raise ValueError('interface_dict_list should be a list of dictionaries')
        lag_interfaces = []
        for item in interface_dict_list:
            if not isinstance(item, dict):
                raise ValueError('Each item in the interface_dict_list should be a dictionary')
            if len(item.keys()) != 1:
                raise ValueError('Each dictionary in the interface_dict_list should have only one key-value pair')
            if not isinstance(item[list(item.keys())[0]], list):
                raise ValueError('The value of each dictionary in the interface_dict_list should be a list')
            for interface_name in item[list(item.keys())[0]]:
                if not isinstance(interface_name, str):
                    raise ValueError('The value of each dictionary in the interface_dict_list should be a list of strings')
                if interface_name not in [i.name for i in self.interfaces]:
                    raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")
            lag_interfaces.append(item)
        for item in lag_interfaces:
            for interface_name in item[list(item.keys())[0]]:
                for interface in self.interfaces:
                    if interface.name == interface_name:
                        if interface in self.access_ports or interface in self.trunk_ports:
                            raise ValueError(f"{interface_name} is already configured as an access or trunk port and cannot be a part of a LAG")
                        else:
                            interface.isLagged = True
                            interface.lagGroup = item
                            break
                else:
                    raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")
        self.lag_interfaces = lag_interfaces



from CiscoPy.devices.l3_switch import L3Switch
from CiscoPy.devices.interfaces import Interface

# create two switches
s1 = L3Switch("switch1")
s2 = L3Switch("switch2")

# add interfaces to the switches
s1.add_interface(Interface("GigabitEthernet0/1"))
s1.add_interface(Interface("GigabitEthernet0/2"))
s2.add_interface(Interface("GigabitEthernet0/1"))
s2.add_interface(Interface("GigabitEthernet0/2"))

# configure IPs
s1.add_ip("GigabitEthernet0/1", "192.168.1.1", 24)
s2.add_ip("GigabitEthernet0/1", "192.168.1.2", 24)

# test connectivity
print(s1.ping("192.168.1.2"))

# configure LAG
s1.get_lagged_interfaces([
    {
        "gi0/1": ["GigabitEthernet0/1", "GigabitEthernet0/2"]
    }
])

# configure trunk port
s2.add_trunk_port("GigabitEthernet0/1", [10, 20, 30])

# add access port
s2.add_access_port("GigabitEthernet0/2")
