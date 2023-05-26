
from  ipaddress import  ip_network
class Interface:
    def __init__(self, name, ip_address=None, subnet_mask=None):
        '''
        Initializes an Interface object.

        Args:
        - name: str, the name of the interface
        - ip_address: str, the IP address of the interface
        - subnet_mask: str, the subnet mask of the interface in CIDR notation

        Returns:
        - None
        '''
        self.name = name
        self.ip_address = ip_address
        self.subnet_mask = subnet_mask
        self.isLagged = False

    def add_ip_address(self, ip_address, subnet_mask):
        '''
        Adds an IP address to the interface.

        Args:
        - ip_address: str, the IP address to add
        - subnet_mask: str, the subnet mask of the IP address in CIDR notation

        Returns:
        - None
        '''
        network = ip_network(f"{ip_address}/{subnet_mask}", strict=False)
        self.ip_address = str(network.network_address)
        self.subnet_mask = str(network.netmask)


    def generate_config(self):
        '''
        Generates the configuration for the interface.

        Returns:
        - str, the configuration for the interface
        '''

        config = f'''
        interface {self.name}
        ip address {self.ip_address} {self.subnet_mask}
        '''
        if self.isLagged:
            config += "channel-group 1 mode active\\n"
        return config


class LAGInterface:
    def __init__(self, interface_dict):
        '''
        Initializes a LAGInterface object.

        Args:
        - interface_dict: dict, a dictionary representing a LAG interface and its constituent interfaces

        Returns:
        - None
        '''
        self.name = list(interface_dict.keys())[0]
        self.interfaces = interface_dict[self.name]

    def generate_config(self):
        '''
        Generates the configuration for the LAG interface.

        Returns:
        - str, the configuration for the LAG interface
        '''
        config = f'''
        interface {self.name}
        no ip address
        '''
        for interface in self.interfaces:
            config += f"channel-group 1 mode active\\n"
        return config


