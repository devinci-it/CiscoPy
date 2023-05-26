from ipaddress import ip_network
from CiscoPy.devices.interfaces import Interface
from CiscoPy.devices.routing_protocol import Route
class Device:
    def __init__(self, hostname, is_l2=False):
        '''
        Initializes a Device object.

        Args:
        - hostname: str, the hostname of the device
        - is_l2: bool, whether the device is a layer 2 device (default False)

        Returns:
        - None
        '''
        self.hostname = hostname
        self.interfaces = []
        self.lag_interfaces = []
        self.password = "cisco" # default password
        self.routes = []
        self.is_l2 = is_l2

    # existing methods omitted for brevity

    def add_route(self, destination_network, next_hop, metric=None, admin_distance=None):
        '''
        Adds a route to the device.

        Args:
        - destination_network: str, the destination network for the route
        - next_hop: str, the next hop for the route
        - metric: int, the metric for the route (optional)
        - admin_distance: int, the administrative distance for the route (optional)

        Returns:
        - None
        '''
        # validate inputs
        if not isinstance(destination_network, str):
            raise ValueError('destination_network should be a string')
        if not isinstance(next_hop, str):
            raise ValueError('next_hop should be a string')
        if metric is not None and not isinstance(metric, int):
            raise ValueError('metric should be an integer')
        if admin_distance is not None and not isinstance(admin_distance, int):
            raise ValueError('admin_distance should be an integer')

        if self.is_l2:
            raise ValueError('Cannot add routes to a layer 2 device')

        # add route to routes list
        route = Route(destination_network, next_hop, metric=metric, admin_distance=admin_distance)
        self.routes.append(route)


    def add_interface(self, name, ip_address, subnet_mask):
        '''
        Adds an interface to the device.

        Args:
        - name: str, the name of the interface to add
        - ip_address: str, the IP address of the interface
        - subnet_mask: str, the subnet mask of the interface in CIDR notation

        Returns:
        - None
        '''
        network = ip_network(f"{ip_address}/{subnet_mask}", strict=False)
        interface = Interface(name, str(network.network_address), str(network.netmask))
        self.interfaces.append(interface)

    def add_lag_interface(self, interface_list):
        '''
        Adds a LAG interface to the device.

        Args:
        - interface_list: list of dictionaries, where each dictionary represents a LAG interface and its constituent interfaces

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

    def generate_basic_config(self):
        """
        Generates basic configuration for the device.

        Returns:
        - str: Configuration commands for the device
        """
        ALL = "1-48"
        MOTD = "Authorized access only!"

        config = f'''
        interface range {ALL}
        shutdown

        configure terminal
        no ip domain-lookup
        hostname {self.hostname}
        username admin secret {self.password}

        line console 0
        '''
        config += f"  login local\\n"
        config += f"  logging synchronous\\n"
        config += f"  exec-timeout 10 0\\n"
        config += f"  banner motd {MOTD}\\n"
        config += f"  exit\\n"

        for interface in self.interfaces:
            config += interface.generate_config()

        for lag_interface in self.lag_interfaces:
            config += LAGInterface(lag_interface).generate_config()

        config += self.generate_static_route_config()

        return config

    def generate_static_route_config(self) -> str:
        config = ""
        for route in self.routes:
            config += route.generate_config()
        return config
