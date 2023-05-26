from CiscoPy.devices.interfaces import Interface
class Device:
    def __init__(self, hostname):
        '''
        Initializes a Device object.

        Args:
        - hostname: str, the hostname of the device

        Returns:
        - None
        '''
        self.hostname = hostname
        self.interfaces = []
        self.lag_interfaces = []

    def add_interface(self, name):
        '''
        Adds an interface to the device.

        Args:
        - name: str, the name of the interface to add

        Returns:
        - None
        '''
        interface = Interface(name)
        self.interfaces.append(interface)

    def add_lag_interface(self, interface_list):
        '''
        Adds a LAG interface to the device.

        Args:
        - interface_list: a list of dictionaries, where each dictionary represents a LAG interface and its constituent interfaces

        Returns:
        - None
        '''
        if not isinstance(interface_list, list):
            raise ValueError('interface_list should be a list of dictionaries')
        for item in interface_list:
            if not isinstance(item, dict):
                raise ValueError('Each item in the interface_list should be a dictionary')
            if len(item.keys()) != 1:
                raise ValueError('Each dictionary in the interface_list should have only one key-value pair')
            if not isinstance(item[list(item.keys())[0]], list):
                raise ValueError('The value of each dictionary in the interface_list should be a list')
            for interface in item[list(item.keys())[0]]:
                if not isinstance(interface, str):
                    raise ValueError('The value of each dictionary in the interface_list should be a list of strings')
                if interface not in [i.name for i in self.interfaces]:
                    raise ValueError(f"{interface} is not a valid interface for {self.hostname}")
                for i in self.interfaces:
                    if i.name == interface:
                        i.isLagged = True
            self.lag_interfaces.append(item)

