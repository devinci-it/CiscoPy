`app.py`

- `CIscoPy/app.py`
    
    ```
    from typing import List
    from router import Router
    from l2_switch import L2Switch
    from l3_switch import L3Switch
    from endpoint import Endpoint
    
    class App:
        devices = []
    
        def __init__(self):
            pass
    
        @classmethod
        def add_device(cls, device_type: str, hostname: str, vtp_domain: str = None) -> None:
            """
            Adds a device to the list of devices.
    
            Args:
            - device_type: str, the type of the device to add (Router, L2 Switch, L3 Switch, or Endpoint)
            - hostname: str, the hostname of the device to add
            - vtp_domain: str, the VTP domain of the device to add (only applicable for switches)
    
            Returns:
            - None
            """
            if device_type == 'Router':
                device = Router(hostname)
            elif device_type == 'L2 Switch':
                device = L2Switch(hostname, vtp_domain=vtp_domain)
            elif device_type == 'L3 Switch':
                device = L3Switch(hostname, vtp_domain=vtp_domain)
            elif device_type == 'Endpoint':
                device = Endpoint(hostname)
            else:
                raise ValueError('Invalid device type')
            cls.devices.append(device)
    
        @classmethod
        def configure(cls):
            """
            Configures all devices in the list of devices.
    
            Returns:
            - None
            """
            for device in cls.devices:
                # implementation goes here
                pass
    
        @classmethod
        def generate(cls):
            """
            Generates configurations for all devices in the list of devices.
    
            Returns:
            - None
            """
            for device in cls.devices:
                if not device.hostname or not device.interfaces:
                    raise ValueError('Hostname and interfaces must be configured for all devices before generating configurations.')
                # generate configuration
                print(f"Configurations for {device.hostname}:")
                if isinstance(device, L2Switch):
                    for vtp_domain, vlan_ids in device.vlans.items():
                        print(f"VLAN database for VTP domain {vtp_domain}:")
                        for vlan_id in vlan_ids:
                            vlan_name = f"vlan_{vlan_id}"
                            print(f"vlan {vlan_id} \\n name {vlan_name}")
                            vlan_interfaces = device.get_vlan_interfaces(vlan_id)
                            print(f"  {len(vlan_interfaces)} interfaces:")
                            for interface_name in vlan_interfaces:
                                print(f"    {interface_name}")
                elif isinstance(device, L3Switch):
                    # implementation for L3Switch goes here
                    pass
                elif isinstance(device, Router):
                    # implementation for Router goes here
                    pass
                elif isinstance(device, Endpoint):
                    # implementation for Endpoint goes here
                    pass
                print("=" * 50)
    
        @classmethod
        def save(cls):
            """
            Saves configurations for all devices in the list of devices.
    
            Returns:
            - None
            """
            # implementation goes here
            pass
    
    ```
    

`main.py`

```
from CiscoPy.devices.router import Router
from CiscoPy.devices.l2_switch import L2Switch
from CiscoPy.devices.l3_switch import L3Switch
from CiscoPy.devices.endpoint import Endpoint
from CiscoPy.config_generator import generate_config

class App:
    devices = []

    def __init__(self):
        pass

    @classmethod
    def add_device(cls, device_type: str, hostname: str, vtp_domain: str = None) -> None:
        """
        Adds a device to the list of devices.

        Args:
        - device_type: str, the type of the device to add (Router, L2 Switch, L3 Switch, or Endpoint)
        - hostname: str, the hostname of the device to add
        - vtp_domain: str, the VTP domain of the device to add (only applicable for switches)

        Returns:
        - None
        """
        if device_type == 'Router':
            device = Router(hostname)
        elif device_type == 'L2 Switch':
            device = L2Switch(hostname, vtp_domain=vtp_domain)
        elif device_type == 'L3 Switch':
            device = L3Switch(hostname, vtp_domain=vtp_domain)
        elif device_type == 'Endpoint':
            device = Endpoint(hostname)
        else:
            raise ValueError('Invalid device type')
        cls.devices.append(device)

    @classmethod
    def generate(cls):
        """
        Generates configurations for all devices in the list of devices.

        Returns:
        - None
        """
        for device in cls.devices:
            if not device.hostname or not device.interfaces:
                raise ValueError('Hostname and interfaces must be configured for all devices before generating configurations.')
            # generate configuration
            print(f"Configurations for {device.hostname}:")
            if isinstance(device, L2Switch):
                for vtp_domain, vlan_ids in device.vlans.items():
                    print(f"VLAN database for VTP domain {vtp_domain}:")
                    for vlan_id in vlan_ids:
                        vlan_name = f"vlan_{vlan_id}"
                        print(f"vlan {vlan_id} \\\\n name {vlan_name}")
                        vlan_interfaces = device.get_vlan_interfaces(vlan_id)
                        print(f"  {len(vlan_interfaces)} interfaces:")
                        for interface_name in vlan_interfaces:
                            print(f"    {interface_name}")
            elif isinstance(device, L3Switch):
                # implementation for L3Switch goes here
                pass
            elif isinstance(device, Router):
                # implementation for Router goes here
                pass
            elif isinstance(device, Endpoint):
                # implementation for Endpoint goes here
                pass
            print("=" * 50)

        generate_config(cls.devices)

    @classmethod
    def save(cls):
        """
        Saves configurations for all devices in the list of devices.

        Returns:
        - None
        """
        # implementation goes here
        pass

```

`config_generator.py`

```
def generate_config(devices):
    """
    Generates configurations for all devices in the list of devices.

    Args:
    - devices: list of device objects.

    Returns:
    - None
    """
    for device in devices:
        if not device.hostname or not device.interfaces:
            raise ValueError('Hostname and interfaces must be configured for all devices before generating configurations.')
        # generate configuration
        print(f"Configurations for {device.hostname}:")
        if isinstance(device, L2Switch):
            for vtp_domain, vlan_ids in device.vlans.items():
                print(f"VLAN database for VTP domain {vtp_domain}:")
                for vlan_id in vlan_ids:
                    vlan_name = f"vlan_{vlan_id}"
                    print(f"vlan {vlan_id} \\\\n name {vlan_name}")
                    vlan_interfaces = device.get_vlan_interfaces(vlan_id)
                    print(f"  {len(vlan_interfaces)} interfaces:")
                    for interface_name in vlan_interfaces:
                        print(f"    {interface_name}")
        elif isinstance(device, L3Switch):
            # implementation for L3Switch goes here
            pass
        elif isinstance(device, Router):
            # implementation for Router goes here
            pass
        elif isinstance(device, Endpoint):
            # implementation for Endpoint goes here
            pass
        print("=" * 50)

```

---

`device.py`

- `CIscoPy/devices/device.py`
    
    ```
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
    
    ```
    

---

`router.py`

- `CIscoPy/devices/router.py`
    
    ```
    from device import Device
    
    class Router(Device):
        def __init__(self, hostname):
            super().__init__(hostname)
            self.routing_protocol = 'OSPF'
    
    ```
    

---

`l2_switch.py`

- `CIscoPy/devices/l2_switch.py`
    
    ```
    from device import Device
    from interface import Interface
    
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
    
    ```
    

---

`l3_switch.py`

---

- `CIscoPy/devices/l3_switch.py`
    
    ```python
    from device import Device
    from interface import Interface
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
    
    ```
    

### DEMO

Here's an example test code for the `l3_switch.py` module:

```
from CiscoPy.devices.l3_switch import L3Switch
from CiscoPy.interface import Interface

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

```

This code creates two switches, adds interfaces to them, configures IPs, and tests connectivity between them using the `ping` method. It then configures a LAG on one switch and a trunk port and an access port on the other switch.

---

`endpoint.py`

- `CIscoPy/devices/endpoint_device.py`
    
    ```
    from device import Device
    
    class Endpoint(Device):
        def __init__(self, hostname):
            super().__init__(hostname)
            self.vlan = 1
    
        def __str__(self):
            return f"Endpoint {self.hostname} (VLAN {self.vlan})"
    
    ```
    

---

`interfaces.py`

- `CIscoPy/devices/interface.py`
    
    ```
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
    
    ```
    

---

```python
.
├── app.py
├── devices
│   ├── device.py
│   ├── endpoint.py
│   ├── __init__.py
│   ├── interfaces.py
│   ├── l2_switch.py
│   ├── l3_switch.py
│   ├── README.md
│   └── router.py
├── __init__.py
├── ip
│   ├── __init__.py
│   └── vlsm.py
├── LICENSE
├── README.md
├── services
│   ├── dhcp.py
│   ├── initial_config.py
│   ├── __init__.py
│   └── nat.py
├── switching
│   ├── __init__.py
│   ├── lacp.py
│   └── roas.py
└── test_app.py
```

Sure! Here's the updated directory structure for the `CiscoPy` package:

```
CiscoPy/
├── CiscoPy/
│   ├── __init__.py
│   ├── app.py
│   ├── ip/
│   │   ├── __init__.py
│   │   └── vlsm.py
│   ├── devices/
│   │   ├── __init__.py
│   │   ├── device.py
│   │   ├── endpoint.py
│   │   ├── interfaces.py
│   │   ├── l2_switch.py
│   │   ├── l3_switch.py
│   │   ├── router.py
│   │   └── README.md
│   └── test/
│       ├── __init__.py
│       └── test_app.py
├── LICENSE
├── README.md
└── setup.py

```

Here's a bash script that will create the directory structure:

```

```

Save the script as a `.sh` file (e.g. `create_directories.sh`) and run it in a terminal to create the directory structure.

To package the project, you can use setuptools. First, make sure that you have setuptools installed by running `pip install setuptools`. Then, create a `setup.py` file in the root directory of the project with the following contents:

There is a syntax error in the `setup()` function call. The `author` parameter is missing a closing quotation mark. Here is the corrected code:

```
from setuptools import setup, find_packages

setup(name='CiscoPy',
      version='0.1',
      description='Python package for configuring Cisco devices',
      author='Github: devinci-it',
      author_email='vince.dev@icloud.com',
      packages=find_packages(),
      install_requires=[
          'netaddr',
      ],
      entry_points={
          'console_scripts': [
              'ciscopy = CiscoPy.app:main'
          ]
      })

```

### OTHER MODULE

- 
    
    
    | Method | Description | Parameters | Example Usage |
    | --- | --- | --- | --- |
    | get_subnets | Calculates subnets based on a given network address and list of required hosts per subnet. | network_address: string representing the network address in CIDR notation (required) required_hosts: list of integers representing the number of required hosts per subnet (optional) subnet_masks: list of subnet masks in CIDR notation (optional) | networks = ['192.168.1.0/24', '10.1.1.0/24', '172.16.0.0/16'] subnets = get_subnets(network_address, required_hosts) |
    | generate_interface_config | Generates a Cisco IOS configuration for assigning an interface address to each network in a given list of IPv4 network addresses. | networks: list of IPv4 network addresses (required) | router = Router() router.add_interface('192.168.1.0/24') router.add_interface('10.1.1.0/24') router.add_interface('172.16.0.0/16') config = router.generate_config() |
    | Router.add_interface | Adds an interface to a Router object with a given network address and optional interface ID. | network_address: string representing the network address in CIDR notation (required) interface_id: string representing the interface ID (optional) | router = Router() router.add_interface('192.168.1.0/24') router.add_interface('10.1.1.0/24', 'gi1') router.add_interface('172.16.0.0/16', 'gi2') |
    
    | Function Name | Description | Parameters | Sample Usage |
    | --- | --- | --- | --- |
    | config_dhcp | Configures DHCP on a network device. | dhcp_pool_name: str, network_address: str, dns_address: str=None, dg: str=None, exclude_ips: tuple=None | config_dhcp(dhcp_pool_name="V10", network_address="10.3.28.0/22", dns_address="10.3.20.100", exclude_ips=("10.3.30.1", "10.3.30.100")) |
    | config_initial | Generates basic configuration for a network device. | hostname: str, site: str | config_initial("router1", "HQ") |
    | config_pat | Configures Port Address Translation (PAT) on a network device. | nat_inside_interface: str, network_addresses: list[str], nat_outside_interface: str, nat_pool_start: str, nat_pool_end: str | config_pat(nat_inside_interface="G0/0", network_addresses=['1.1.1.0/24', '2.2.2.0/25', '3.3.3.0/25'],nat_outside_interface="G0/1", nat_pool_start='200.100.123.1', nat_pool_end='200.100.123.2') |
    
    | Function | Description | Parameters | Sample Usage |
    | --- | --- | --- | --- |
    | config_ip() | Generates configuration commands for a Cisco router interface. | interface_name: str, ip_address: str, subnet_mask: str | config_ip("GigabitEthernet1/0/1", "192.168.1.1", "255.255.255.0") |
    | config_initial() | Generates initial configuration commands for a Cisco router. | hostname: str, domain_name: str | config_initial("MyRouter", "mydomain") |
    | router_on_a_stick() | Generates configuration commands for a Cisco router to implement router-on-a-stick. | router_interface: str, router_ip: str, switch_interface: str, switch_ip: str, vlan_subnet: str | router_on_a_stick("GigabitEthernet0/0", "192.168.1.1", "GigabitEthernet0/1", "192.168.2.1", "10.0.0.0/24") |
    | config_access_ports() | Generates configuration commands for a Cisco switch interface to configure access ports. | interface_name: str, vlan_id: str | config_access_ports("GigabitEthernet1/0/1", "vlan 10") |
    | config_sw_trunkport() | Generates configuration commands for a Cisco switch interface to configure trunk ports. | interface_name: str, mode: str, native_vlan: str, allowed_vlans: str | config_sw_trunkport("GigabitEthernet1/0/1", "switchport mode trunk", "switchport trunk native vlan 10", "switchport trunk allowed vlan 10,20,30") |
    | config_vtp() | Generates configuration commands for a Cisco switch to configure VTP. | hostname: str, password: str, mode: str | config_vtp("MySwitch", "password123", "client") |
    | schema_ip() | Generates IP addresses for a given set of VLANs and CIDR blocks. | cidr_block: str, vlan_list: list[int], subnet_list: list[int] | schema_ip("10.0.0.0/24", [10, 20, 30], [5, 10, 15]) |
    | config_lacp() | Generates configuration commands for a Cisco switch to configure LACP. | interface_name: str, speed: str, mode: str | config_lacp("GigabitEthernet1/0/1", "fast", "active") |
    | config_ether_lacp() | Generates configuration commands for a Cisco switch to configure EtherChannel with LACP. | interface_name1: str, interface_name2: str, speed: str, mode: str | config_ether_lacp("GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "fast", "active") |
    
    | Module | Description | Parameters | Sample Usage |
    | --- | --- | --- | --- |
    | network_config | Contains the config_initial function, which generates basic configuration for a network device. | hostname: str, domain_name: str | network_config.config_initial("MySwitch", "mydomain") |
    | dhcp_config | Contains the config_dhcp function, which can be used to configure DHCP on a network device. | interface_name: str, dhcp_range_start: str, dhcp_range_end: str, subnet_mask: str | dhcp_config.config_dhcp("GigabitEthernet1/0/1", "192.168.1.1", "192.168.1.100", "255.255.255.0") |
    | pat_config | Contains the config_pat function, which can be used to configure Port Address Translation (PAT) on a network device. | interface_name: str, inside_subnet: str, tcp_port: str, udp_port: str | pat_config.config_pat("GigabitEthernet1/0/1", "10.0.0.0/24", "80", "443") |
    | ipaddress | A built-in Python module that provides tools for working with IP addresses and networks. | N/A | import ipaddress |

---

---

Sure! Here's what you need to do to package the project:

1. Make sure that you have setuptools and wheel installed by running `pip install setuptools wheel`.
2. Create a `setup.py` file in the root directory of the project with the following contents:

```
from setuptools import setup, find_packages

setup(name='CiscoPy',
      version='0.1',
      description='Python package for configuring Cisco devices',
      author='Github: devinci-it',
      author_email='vince.dev@icloud.com',
      packages=find_packages(),
      install_requires=[
          'netaddr',
      ],
      entry_points={
          'console_scripts': [
              'ciscopy = CiscoPy.app:main'
          ]
      })

```

This file specifies the package name, version, description, author, packages to include, dependencies to install, and entry point for the package.

1. Create a `README.md` file in the root directory of the project with a brief description of the package and instructions for installation and usage.
2. Create a `LICENSE` file in the root directory of the project with the license you want to use for the package.
3. Run `python setup.py sdist bdist_wheel` to create the source distribution (sdist) and binary distribution (bdist_wheel) of the package.
4. Once the command finishes running, you should see two new directories in your project folder: `dist` and `build`. The `dist` directory contains the distribution files for the package.
5. You can now install the package locally using `pip install dist/CiscoPy-0.1-py3-none-any.whl` (replace `0.1` with the actual version number).
6. Finally, you can upload the package to PyPI using `twine upload dist/*`. You will need to have a PyPI account and be logged in to complete this step.

That's it! Your package is now ready to be installed and used by others.

## CiscoPy Package

The CiscoPy package is a Python package for configuring Cisco network devices. It provides an easy-to-use interface for configuring network devices such as routers and switches, as well as for performing common network tasks such as DHCP configuration and subnetting.

### Installation

To install the CiscoPy package, use `pip`:

```
pip install ciscopy

```

### Usage

### Example 1: Configuring a Router

Here's an example of using the CiscoPy package to configure a router:

```
from ciscopy.devices import Router

router = Router("my_router")

# Add an interface and configure an IP address
router.add_interface("GigabitEthernet0/0", "192.168.1.1", "255.255.255.0")

# Generate the configuration commands
config = router.generate_config()

# Print the configuration commands
print(config)

```

This code creates a new router object, adds an interface to it, and configures an IP address for the interface. It then generates configuration commands for the router and prints them to the console.

### Example 2: Configuring DHCP

Here's an example of using the CiscoPy package to configure DHCP on a network device:

```
from ciscopy.services import dhcp

# Configure DHCP on interface GigabitEthernet1/0/1
dhcp.config_dhcp("GigabitEthernet1/0/1", "192.168.1.1", "192.168.1.100", "255.255.255.0")

```

This code configures DHCP on interface `GigabitEthernet1/0/1` with a DHCP pool range of `192.168.1.1` to `192.168.1.100` and a subnet mask of `255.255.255.0`.

### Testing

The CiscoPy package includes unit tests for each module and function. To run the tests, use `pytest`:

```
pip install pytest
pytest

```

### Example: Testing the `config_dhcp()` Function

Here's an example of a unit test for the `config_dhcp()` function:

```
from ciscopy.services import dhcp

def test_config_dhcp():
    # Configure DHCP on interface GigabitEthernet1/0/1
    dhcp.config_dhcp("GigabitEthernet1/0/1", "192.168.1.1", "192.168.1.100", "255.255.255.0")

    # Check that the configuration was generated correctly
    expected_config = "interface GigabitEthernet1/0/1\\nip address 192.168.1.1 255.255.255.0\\nip dhcp pool 192.168.1.0/24\\ndns-server 8.8.8.8\\ndefault-router 192.168.1.1\\nnetwork 192.168.1.0 255.255.255.0\\nlease 7\\nexclude-address 192.168.1.1 192.168.1.100\\n!\\n"
    assert dhcp.generate_config() == expected_config

```

This test configures DHCP on interface `GigabitEthernet1/0/1` and checks that the generated configuration matches the expected configuration.

### Modules

The CiscoPy package includes the following modules:

- `devices`: Contains classes for representing network devices such as routers and switches.
- `interface`: Contains the `Interface` class, which represents a network interface on a network device.
- `ip`: Contains tools for working with IP addresses and networks.
- `services`: Contains modules for performing common network tasks such as DHCP configuration and NAT configuration.
- `switching`: Contains modules for configuring switch features such as LACP and EtherChannel.

### Functions

The CiscoPy package includes the following functions:

- `config_dhcp()`: Configures DHCP on a network device.
- `config_initial()`: Generates basic configuration for a network device.
- `config_pat()`: Configures Port Address Translation (PAT) on a network device.
- `config_ip()`: Generates configuration commands for a Cisco router interface.
- `router_on_a_stick()`: Generates configuration commands for a Cisco router to implement router-on-a-stick.
- `config_access_ports()`: Generates configuration commands for a Cisco switch interface to configure access ports.
- `config_sw_trunkport()`: Generates configuration commands for a Cisco switch interface to configure trunk ports.
- `config_vtp()`: Generates configuration commands for a Cisco switch to configure VTP.
- `schema_ip()`: Generates IP addresses for a given set of VLANs and CIDR blocks.
- `config_lacp()`: Generates configuration commands for a Cisco switch to configure LACP.
- `config_ether_lacp()`: Generates configuration commands for a Cisco switch to configure EtherChannel with LACP.

### Other Modules

- `network_config`: Contains the `config_initial` function, which generates basic configuration for a network device.
- `dhcp_config`: Contains the `config_dhcp` function, which can be used to configure DHCP on a network device.
- `pat_config`: Contains the `config_pat` function, which can be used to configure Port Address Translation (PAT) on a network device.
- `ipaddress`: A built-in Python module that provides tools for working with IP addresses and networks.

# CiscoPy Package

The CiscoPy package is a Python package that provides an easy-to-use interface for configuring Cisco network devices. It includes various modules and functions that can be used to configure network devices, perform common network tasks, and manage network infrastructure.

## Installation

To install the CiscoPy package, use `pip`:

```
pip install ciscopy

```

Once installed, the package can be imported into a Python script or interactive session using the `import` statement.

## Modules

The CiscoPy package includes the following modules:

- `devices`: Contains classes for representing network devices such as routers and switches.
- `interface`: Contains the `Interface` class, which represents a network interface on a network device.
- `ip`: Contains tools for working with IP addresses and networks.
- `services`: Contains modules for performing common network tasks such as DHCP configuration and NAT configuration.
- `switching`: Contains modules for configuring switch features such as LACP and EtherChannel.

### `devices`

### `Router`

The `Router` class represents a Cisco router.

### `__init__(self, hostname: str)`

Creates a new `Router` object with the specified hostname.

### `add_interface(self, interface_name: str, ip_address: str, subnet_mask: str)`

Adds a new interface to the router with the specified name, IP address, and subnet mask.

### `generate_config(self) -> str`

Generates configuration commands for the router.

### `Switch`

The `Switch` class represents a Cisco switch.

### `__init__(self, hostname: str)`

Creates a new `Switch` object with the specified hostname.

### `add_interface(self, interface_name: str)`

Adds a new interface to the switch with the specified name.

### `generate_config(self) -> str`

Generates configuration commands for the switch.

### `interface`

### `Interface`

The `Interface` class represents a network interface on a network device.

### `__init__(self, name: str)`

Creates a new `Interface` object with the specified name.

### `add_ip_address(self, ip_address: str, subnet_mask: str)`

Adds an IP address to the interface with the specified IP address and subnet mask.

### `generate_config(self) -> str`

Generates configuration commands for the interface.

### `ip`

### `schema_ip(cidr_block: str, vlan_list: List[int], subnet_list: List[int]) -> Dict[int, List[str]]`

Generates IP addresses for a given set of VLANs and CIDR blocks.

### `services`

### `dhcp`

### `config_dhcp(interface_name: str, dhcp_range_start: str, dhcp_range_end: str, subnet_mask: str) -> str`

Configures DHCP on a network device.

### `nat`

### `config_nat(interface_name: str, inside_subnet: str, outside_interface: str) -> str`

Configures NAT on a network device.

### `switching`

### `config_access_ports(interface_name: str) -> str`

Generates configuration commands for a Cisco switch interface to configure access ports.

### `config_sw_trunkport(interface_name: str) -> str`

Generates configuration commands for a Cisco switch interface to configure trunk ports.

### `config_vtp(mode: str, domain: str) -> str`

Generates configuration commands for a Cisco switch to configure VTP.

### `config_lacp(interface_name: str, speed: str, mode: str) -> str`

Generates configuration commands for a Cisco switch to configure LACP.

### `config_ether_lacp(interface_name1: str, interface_name2: str, speed: str, mode: str) -> str`

Generates configuration commands for a Cisco switch to configure EtherChannel with LACP.

## Other Modules

The CiscoPy package also includes the following modules:

- `network_config`: Contains the `config_initial` function, which generates basic configuration for a network device.
- `dhcp_config`: Contains the `config_dhcp` function, which can be used to configure DHCP on a network device.
- `pat_config`: Contains the `config_pat` function, which can be used to configure Port Address Translation (PAT) on a network device.
- `ipaddress`: A built-in Python module that provides tools for working with IP addresses and networks.

## Usage

Here are a few examples of how the CiscoPy package can be used:

### Example 1: Configuring a Router

The `devices` module can be used to create a new router object and add an interface to it. Here's an example:

```
from ciscopy.devices import Router

router = Router("my_router")

# Add an interface and configure an IP address
router.add_interface("GigabitEthernet0/0", "192.168.1.1", "255.255.255.0")

# Generate the configuration commands
config = router.generate_config()

# Print the configuration commands
print(config)

```

This code creates a new router object, adds an interface to it, and configures an IP address for the interface. It then generates configuration commands for the router and prints them to the console.

### Example 2: Configuring DHCP

The `services` module can be used to configure DHCP on a network device. Here's an example:

```
from ciscopy.services import dhcp

# Configure DHCP on interface GigabitEthernet1/0/1
dhcp.config_dhcp("GigabitEthernet1/0/1", "192.168.1.1", "192.168.1.100", "255.255.255.0")

```

This code configures DHCP on interface `GigabitEthernet1/0/1` with a DHCP pool range of `192.168.1.1` to `192.168.1.100` and a subnet mask of `255.255.255.0`.

### Example 3: Generating IP Addresses

The `ip` module can be used to generate IP addresses for a given set of VLANs and CIDR blocks. Here's an example:

```
from ciscopy.ip import schema_ip

cidr_block = "10.0.0.0/24"
vlan_list = [10, 20, 30]
subnet_list = [5, 10, 15]

ip_addresses = schema_ip(cidr_block, vlan_list, subnet_list)

print(ip_addresses)

```

This code generates IP addresses for VLANs 10, 20, and 30 with subnet sizes of 5, 10, and 15, respectively, using the CIDR block `10.0.0.0/24`. The resulting IP addresses are printed to the console.

### Example 4: Configuring Switch Features

The `switching` module can be used to configure various switch features such as LACP and EtherChannel. Here's an example:

```
from ciscopy.switching import config_lacp, config_ether_lacp

# Configure LACP on interface GigabitEthernet1/0/1
config_lacp("GigabitEthernet1/0/1", "fast", "active")

# Configure EtherChannel with LACP on interfaces GigabitEthernet1/0/1 and GigabitEthernet1/0/2
config_ether_lacp("GigabitEthernet1/0/1", "GigabitEthernet1/0/2", "fast", "active")

```

This code configures LACP on interface `GigabitEthernet1/0/1` with a speed of `fast` and a mode of `active`. It then configures EtherChannel with LACP on interfaces `GigabitEthernet1/0/1` and `GigabitEthernet1/0/2` with a speed of `fast` and a mode of `active`.

These are just a few examples of how the CiscoPy package can be used to configure and manage Cisco network devices. The package is designed to simplify the process of configuring and managing network infrastructure, and it can be a valuable tool for network administrators and engineers.

### Directory Structure

The CiscoPy package is organized as follows:

```
ciscopy
├── ciscopy
│   ├── __init__.py
│   ├── devices
│   ├── interface.py
│   ├── ip
│   ├── services
│   └── switching
├── LICENSE
├── README.md
├── setup.py

```

The top-level `ciscopy` directory contains the main package code in the `ciscopy` subdirectory, along with the `LICENSE`, `README.md`, and `setup.py` files. The `ciscopy` subdirectory

Here's the Python code for the revised `l3_switch` module:

write again