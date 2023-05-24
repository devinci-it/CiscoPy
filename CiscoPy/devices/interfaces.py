class Interface:
    def __init__(self, name: str) -> None:
        '''
        Initializes an Interface object.

        Args:
        - name: str, the name of the interface

        Returns:
        - None
        '''
        self.name = name
        self.isLagged = False
        self.vlan_ids = []
        self.ip_addresses = []
        self.networks = []

    def add_vlan(self, vlan_id: int) -> None:
        '''
        Adds a VLAN to the interface.

        Args:
        - vlan_id: int, the ID of the VLAN to add

        Returns:
        - None
        '''
        self.vlan_ids.append(vlan_id)

    def add_ip(self, ip_address: str) -> None:
        '''
        Adds an IP address to the interface.

        Args:
        - ip_address: str, the IP address to add

        Returns:
        - None
        '''
        self.ip_addresses.append(ip_address)

    def get_ip(self) -> str:
        '''
        Returns the first IP address associated with the interface.

        Args:
        - None

        Returns:
        - str, the first IP address associated with the interface
        '''
        return self.ip_addresses[0] if self.ip_addresses else ''
