from ipaddress import IPv4Address, IPv4Interface
def config_lacp(ports, channel_group_id, speed, native):
    """

`config_lacp` function that generates configuration commands for the LACP channel group

    :param ports: str - range of ports to configure
    :param channel_group_id: int - LACP channel group ID
    :param speed: str - speed of the ports
    :param native: int - native VLAN ID
    :return: str - configuration commands for the LACP channel group

# Define the base interface name and range of ports to be bundled into the port-channel group
ports = "G1/0/"
port_range = "3-4"

# Define the ID of the port-channel group to be created
channel_group_id = 1

# Define the speed to be configured for the bundled interfaces
speed = "1000"

# Define the VLAN ID to be used as the native VLAN for the bundled interfaces
native = 99

# Call the config_lacp function with the specified parameters
config = config_lacp(ports + port_range, channel_group_id, speed, native)

# Print the resulting configuration commands to the console
print(config)


    """
    config = f"""
    interface range {ports}
    no shutdown
    speed {speed}
    switchport mode trunk
    switchport trunk native vlan {native}

    !channel-group {channel_group_id} mode passive
    !channel-group {channel_group_id} mode on
    !channel-group {channel_group_id} mode active

    int port-channel {channel_group_id}
    switchport trunk native vlan {native}
    """
    return config


