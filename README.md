# __CiscoPy__

## __DESCRIPTION__
---
CiscoPY is a Python package that provides a set of tools and utilities for working with Cisco networking devices. It includes modules for interacting with Cisco IOS, parsing and generating Cisco configuration files, and automating common network management tasks. The package is designed to be easy to use and flexible, and is suitable for both novice and experienced network engineers.

**Disclaimer:** Please note that CiscoPY is currently under development and may contain bugs or other issues. Use at your own risk.

---


```txt

/ CiscoPy
|
├── README.md
├── __init__.py
├── ip
│   ├── __init__.py
│   └── vlsm.py
├── main.py
├── routing
├── services
│   ├── __init__.py
│   ├── dhcp.py
│   ├── initial_config.py
│   └── nat.py
└── switching
    ├── __init__.py 
    ├── lacp.py
    └── roas.py

```

---

### MODULE DIRECTORY

---

### SERVICES

---

| Module | Description |
| --- | --- |
| network_config | Contains the config_initial function, which generates basic configuration for a network device. |
| dhcp_config | Contains the config_dhcp function, which can be used to configure DHCP on a network device. |
| pat_config | Contains the config_pat function, which can be used to configure Port Address Translation (PAT) on a network device. |
| ipaddress | A built-in Python module that provides tools for working with IP addresses and networks. |

---

### SWITCHING

---

| Function | Description |
| --- | --- |
| config_ip() | Generates configuration commands for a Cisco router interface. |
| config_initial() | Generates initial configuration commands for a Cisco router. |
| router_on_a_stick() | Generates configuration commands for a Cisco router to implement router-on-a-stick. |
| config_access_ports() | Generates configuration commands for a Cisco switch interface to configure access ports. |
| config_sw_trunkport() | Generates configuration commands for a Cisco switch interface to configure trunk ports. |
| config_vtp() | Generates configuration commands for a Cisco switch to configure VTP. |
| schema_ip() | Generates IP addresses for a given set of VLANs and CIDR blocks. |
| config_lacp() | Generates configuration commands for a Cisco switch to configure LACP. |
| config_ether_lacp() | Generates configuration commands for a Cisco switch to configure EtherChannel with LACP. |