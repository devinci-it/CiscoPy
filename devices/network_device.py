import ipaddress

class NetworkDevice:
    def __init__(self, hostname, management_ip=None):
        self._hostname = hostname
        self._management_ip = management_ip
        self._interfaces = []

    @property
    def hostname(self):
        return self._hostname

    @hostname.setter
    def hostname(self, value):
        self._hostname = value

    @property
    def management_ip(self):
        return self._management_ip

    @management_ip.setter
    def management_ip(self, value):
        self._management_ip = value

    @property
    def interfaces(self):
        return self._interfaces

    def add_interface(self, interface):
        self._interfaces.append(interface)

    def connect(self):
        print(f"{self.__class__.__name__} connected.")

    def disconnect(self):
        print(f"{self.__class__.__name__} disconnected.")

    def __repr__(self):
        return f"{self.__class__.__name__}(hostname='{self._hostname}', management_ip='{self._management_ip}')"

    def __str__(self):
        return f"{self.__class__.__name__} {self._hostname}"


class RouterInterface:
    def __init__(self, name, ip_address=None, subnet=None):
        self._name = name
        self._ip_address = ip_address
        self._subnet = subnet

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @property
    def subnet(self):
        return self._subnet

    @subnet.setter
    def subnet(self, value):
        self._subnet = value


class Router(NetworkDevice):
    def __init__(self, hostname, routing_protocol=None, **kwargs):
        super().__init__(hostname, **kwargs)
        self._routing_protocol = routing_protocol
        self._routed_interfaces = {}

    @property
    def routing_protocol(self):
        return self._routing_protocol

    @routing_protocol.setter
    def routing_protocol(self, value):
        self._routing_protocol = value

    @property
    def routed_interfaces(self):
        return self._routed_interfaces

    def add_routed_interface(self, interface=None, name=None, ip_address=None, subnet=None):
        if not interface:
            interface = RouterInterface(name, ip_address, subnet)

        if not isinstance(interface, RouterInterface):
            raise ValueError('Interface must be an instance of RouterInterface class.')

        if interface.name in self._routed_interfaces:
            raise ValueError('Interface name is already in use.')

        # Validate the network address
        if interface.subnet:
            new_network = ipaddress.IPv4Network(interface.subnet)

            # Check if the network address overlaps with any existing interface networks
            for existing_interface in self._routed_interfaces.values():
                existing_network = existing_interface.subnet
                if existing_network and ipaddress.IPv4Network(existing_network).overlaps(new_network):
                    raise ValueError('Network address overlaps with an existing interface.')

        self._routed_interfaces[interface.name] = interface

# create a new router instance
router = Router('my_router')

# set the routing protocol
router.routing_protocol = 'OSPF'

# add a new routed interface
router.add_routed_interface(name='GigabitEthernet0/1', ip_address='10.0.0.1', subnet='255.255.255.0')

# print the router's hostname and routed interfaces
print(router.hostname)
print(router.routed_interfaces)

# connect the router
router.connect()

# disconnect the router
router.disconnect()
