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
