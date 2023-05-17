from ipaddress import IPv4Address, IPv4Interface
def router_on_a_stick(base_port, vlans=None, site_ids=None, sites=None):
    """
    The router_on_a_stick function generates router configuration commands for VLAN trunking on a Cisco router. Specifically, it generates configuration commands for subinterfaces with dot1Q encapsulation and IP addresses defined based on the site ID, native VLAN ID, and VLAN ID associated with each VLAN. The resulting commands can be manually copied and pasted into the router's configuration.

    :param base_port: str - The router's interface that will be used for trunking.
    :param vlans: list - A list of tuples containing a dictionary of VLAN name and description, subnet mask, and port to associate the VLAN to.
    :param site_ids: list - A list of integers representing unique site IDs.
    :param sites: list - A list of strings representing site locations.
    :return: str - The configuration commands for VLAN trunking.
    
    """

    to_return = ""
    for (site, site_id) in zip(sites, site_ids):
        site = (site, site_id)
        vlan_list = []
        vtp_domain = site[0]
        native = 99
        for each in vlans:
            native_conf = f"""
            interface {base_port}.{native}
            no shutdown
            encapsulation dot1Q {native} native
            ip address {f'10.{site[1]}.{native}.1'} 255.255.255.0
            no shutdown
            """
            vlan_interface = list(each[0].keys())[0]
            inter_vlan_gateway = IPv4Interface(
                f'10.{site[1]}.{vlan_interface[5:7]}.1{each[1]}')
            roas_router_config = f"""
                interface {base_port}.{str(vlan_interface[5:7])}
                encapsulation dot1Q {str(vlan_interface[5:7])}
                no shutdown
                ip address {inter_vlan_gateway.ip} {inter_vlan_gateway.netmask}
                no shutdown
            """
            to_return += roas_router_config
        to_return += native_conf
    return to_return


    print(f"""
enable
configure terminal
!
interface {base_port}
no shutdown
!
""")

base_port = 'G0/0'
vlans = [
    ({"VLAN 10": "MANAGEMENT"}, "/25", "GigabitEthernet0/1"),
    ({"VLAN 20": "SERVERS"}, "/23", "GigabitEthernet0/2"),
    ({"VLAN 30": "CL-STUDENT"}, "/23", "GigabitEthernet0/3"),
    ({"VLAN 40": "CL-FACULTY"}, "/22", "GigabitEthernet1/1"),
    ({"VLAN 50": "CL-802.11"}, "/22", "GigabitEthernet1/2")
]
site_ids = [3]
sites = ['SF']

print(router_on_a_stick(base_port, vlans, site_ids, sites))
