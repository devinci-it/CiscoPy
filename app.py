from typing import List
from devices.router import Router
from devices.l2_switch import L2Switch
# from devices.l3_switch import L3Switch
from devices.endpoint import Endpoint

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

