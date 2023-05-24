import ipaddress

def vlsm(network: str, new_prefixes: list) -> list:
    """
    Performs VLSM (Variable Length Subnet Masking) on an IPv4 network

    Args:
    network (str): the IPv4 network in the format "x.x.x.x/y"
    new_prefixes (list): the list of new prefix lengths for each subnet in the network

    Returns:
    list: the list of subnets created by the VLSM process
    """

    subnets = []
    new_prefixes.sort()

    network = ipaddress.IPv4Network(network)
    subnet_list = network.subnets(new_prefix=new_prefixes[0])
    subnets.append(subnet_list.__next__())
    new_prefixes.pop(0)

    for prefix in new_prefixes:
        next_subnet = subnet_list.__next__()
        to_add = next_subnet.subnets(new_prefix=prefix)
        subnets.append(to_add.__next__())

    return subnets

def subnet(network: str, subnet_count: int) -> list:
    """
    Performs subnetting on an IPv4 network

    Args:
    network (str): the IPv4 network in the format "x.x.x.x/y"
    subnet_count (int): the number of subnets to create

    Returns:
    list: the list of subnets created by the subnetting process
    """
    subnets = []
    network = ipaddress.IPv4Network(network)
    pref_diff = subnet_count.bit_length()
    nextworks = network.subnets(prefixlen_diff=pref_diff)
    return [net for net in nextworks]
