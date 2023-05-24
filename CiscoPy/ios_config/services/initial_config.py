
MOTD = "$ Authorized Access Only! UNAUTHORIZED ACCESS IS STRICLY PROHIBITED! $"
STATIC_PASS='cisco'
PT_L3_SW = [f'G1/0/{num}' for num in range (25)]
ALL=' G1/0/1-24'

def config_initial(hostname,site):
    """
    Generates basic configuration for a network device.

    :param hostname: str
    :param site: str
    :return: str
    """

    return f'''
    interface range {ALL}
    shutdown

    configure terminal
    no ip domain-lookup
    hostname {hostname}
    username admin secret {STATIC_PASS}

    line console 0
    logging synchronous
    exit
    conf t
    ip domain-name {site}.cisco.com
    crypto key generate rsa
    1024


    banner motd {MOTD}
    enable secret {STATIC_PASS}
    line console 0
    password {STATIC_PASS}
    login
    exit

    line vty 0 4
    login local
    transport input ssh
    ip ssh version 2

    service password-encryption

    '''
