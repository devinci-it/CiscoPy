from CiscoPy.devices.device import Device
from ipaddress import ip_network
from CiscoPy.devices.interfaces import Interface

class Router(Device):
    def __init__(self, hostname):
        '''
        Initializes a Router object.

        Args:
        - hostname: str, the hostname of the router

        Returns:
        - None
        '''
        super().__init__(hostname)
        self.connection = None

    def connect(self):
        '''
        Connects to the router.

        Returns:
        - None
        '''
        # implementation of connection logic
        self.connection = "connected"

    def disconnect(self):
        '''
        Disconnects from the router.

        Returns:
        - None
        '''
        # implementation of disconnection logic
        self.connection = None

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
        interface = Interface(name, ip_address, str(network.netmask))
        self.interfaces.append(interface)


    def configure_interface(self, interface_name, ip_address=None, subnet_mask=None):
        '''
        Configures an interface on the router with the given IP address and subnet mask.

        Args:
        - interface_name: str, the name of the interface to configure
        - ip_address: str, the IP address to assign to the interface
        - subnet_mask: str, the subnet mask to assign to the interface

        Returns:
        - None
        '''

        # implementation of interface configuration logic
        interface = Interface(interface_name)
        interface.add_ip_address(ip_address, subnet_mask)
        self.interfaces.append(interface)

    def generate_config(self):
        '''
        Generates the configuration for the router.

        Returns:
        - None
        '''
        # implementation of configuration generation logic
        config = ""
        for interface in self.interfaces:
            config += interface.generate_config() + "\\n"
        return config


    def add_subinterface(self, interface_name, vlan_id, ip_address, subnet_mask):
        '''
        Adds a subinterface to the router for router-on-a-stick configuration.

        Args:
        - interface_name: str, the name of the physical interface to add the subinterface to
        - vlan_id: int, the VLAN ID to configure on the subinterface
        - ip_address: str, the IP address to assign to the subinterface
        - subnet_mask: str, the subnet mask to assign to the subinterface

        Returns:
        - None
        '''
        subinterface_name = f"{interface_name}.{vlan_id}"
        subinterface = Interface(subinterface_name, ip_address, subnet_mask)
        self.interfaces.append(subinterface)


    def generate_ospfv2_single_area(self, area_id, router_id=None, networks=None, passive_interface=None):
        """
        Generates OSPFv2 single area configuration for the router.

        Args:
        - area_id: str, the ID of the OSPF area
        - router_id: str (optional), the router ID for the OSPF process
        - networks: list of IPNetwork objects or strings, the networks to advertise in the OSPF domain (default is self.networks)
        - passive_interface: str (optional), the name of a passive interface to configure

        Returns:
        - list of strings, the generated configuration
        """
        if router_id is None:

            print("Reminder: It is recommended to set a router ID for the OSPF process by either configuring a loopback interface or using the assign_router_id() method.")

        config = []
        config.append(f"router ospf {area_id}")
        if router_id is not None:
            config.append(f" router-id {router_id}")
        if passive_interface is not None:
            config.append(f" passive-interface {passive_interface}")
        if networks is not None:
            config.append(f" network {networks}")
        config.append(" no auto-summary")
        return config


