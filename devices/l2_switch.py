from devices.device import Device
from devices.interfaces import Interface


class L2Switch(Device):
    def __init__(self, hostname, vtp_domain):
        '''
        Initializes an L2Switch object.

        Args:
        - hostname: str, the hostname of the L2 switch
        - vtp_domain: str, the VTP domain of the L2 switch

        Returns:
        - None
        '''
        super().__init__(hostname)
        self.stp_enabled = True
        self.vtp_domain = vtp_domain
        self.vlans = {'default': []}
        self.vtp_mode = 'server'
        self.access_ports = []
        self.trunk_ports = []

    def add_vlan(self, vlan_name, vlan_id, vtp_domain=None):
        '''
        Adds a VLAN to the L2 switch.

        Args:
        - vlan_name: str, the name of the VLAN to add
        - vlan_id: int, the ID of the VLAN to add
        - vtp_domain: str (optional), the VTP domain of the VLAN to add (default = None)

        Returns:
        - None
        '''
        if not vtp_domain:
            vtp_domain = 'default'
        if vtp_domain not in self.vlans:
            self.vlans[vtp_domain] = []
        self.vlans[vtp_domain].append(vlan_id)
        for device in App.devices:
            if isinstance(device, L2Switch) and device.vtp_domain == vtp_domain and device != self:
                device.vlans[vtp_domain] = self.vlans[vtp_domain].copy()

    def get_vlan_interfaces(self, vlan_id):
        '''
        Gets the interfaces associated with a VLAN.

        Args:
        - vlan_id: int, the ID of the VLAN to get interfaces for

        Returns:
        - vlan_interfaces: list, a list of interface names associated with the VLAN
        '''
        vlan_interfaces = []
        for interface in self.interfaces:
            if vlan_id in interface.vlan_ids:
                vlan_interfaces.append(interface.name)
        return vlan_interfaces

    def add_access_port(self, interface_name):
        '''
        Configures an access port on the L2 switch.

        Args:
        - interface_name: str, the name of the interface to configure as an access port

        Returns:
        - None
        '''
        for interface in self.interfaces:
            if interface.name == interface_name:
                if interface in self.trunk_ports:
                    raise ValueError(f"{interface_name} is already configured as a trunk port and cannot be an access port")
                else:
                    self.access_ports.append(interface)
                    break
        else:
            raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")

    def add_trunk_port(self, interface_name, vlan_ids):
        '''
        Configures a trunk port on the L2 switch.

        Args:
        - interface_name: str, the name of the interface to configure as a trunk port
        - vlan_ids: list, a list of VLAN IDs to allow on the trunk port

        Returns:
        - None
        '''
        for interface in self.interfaces:
            if interface.name == interface_name:
                if interface in self.access_ports:
                    raise ValueError(f"{interface_name} is already configured as an access port and cannot be a trunk port")
                else:
                    interface.vlan_ids = vlan_ids
                    self.trunk_ports.append(interface)
                    break
        else:
            raise ValueError(f"{interface_name} is not a valid interface for {self.hostname}")
