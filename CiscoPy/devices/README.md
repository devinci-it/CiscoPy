## Introduction

The `NetworkDevice` class, `RouterInterface` class, and `Router` class are Python classes that are used for network device management. These classes are designed to simplify the process of managing network devices and their interfaces. They are particularly useful for network administrators who need to manage a large number of devices and interfaces.

In this document, we will describe the functionality and usage of each of these classes. We will also provide a sample code that demonstrates how to use these classes to manage a router.

## NetworkDevice Class

The `NetworkDevice` class represents a network device. It contains the following attributes:

- `hostname` (string): The hostname of the device.
- `management_ip` (string): The management IP address of the device.
- `interfaces` (list): A list of interface objects.

The `NetworkDevice` class contains the following methods:

- `__init__(self, hostname, management_ip=None)`: Initializes a new `NetworkDevice` instance.
- `add_interface(self, interface)`: Adds an interface object to the device.
- `connect(self)`: Connects the device.
- `disconnect(self)`: Disconnects the device.
- `__repr__(self)`: Returns a string representation of the device.
- `__str__(self)`: Returns a string representation of the device.

The `add_interface` method is particularly useful for adding interface objects to the device. An interface object is an instance of the `RouterInterface` class. By adding interface objects to the device, network administrators can keep track of the device's interfaces and their configurations.

The `connect` and `disconnect` methods are used to establish and terminate a connection to the device. If the device is a physical device, the `connect` method may establish a Telnet or SSH connection, for example.

## RouterInterface Class

The `RouterInterface` class represents a router interface. It contains the following attributes:

- `name` (string): The name of the interface.
- `ip_address` (string): The IP address of the interface.
- `subnet` (string): The subnet of the interface.

The `RouterInterface` class contains the following methods:

- `__init__(self, name, ip_address=None, subnet=None)`: Initializes a new `RouterInterface` instance.

The `RouterInterface` class is used to create interface objects that can be added to network devices. These interface objects contain information about the interface's name, IP address, and subnet.

## Router Class

The `Router` class represents a router and inherits from the `NetworkDevice` class. It contains the following additional attributes:

- `routing_protocol` (string): The routing protocol used by the router.
- `routed_interfaces` (dict): A dictionary of routed interface objects.

The `Router` class contains the following additional methods:

- `__init__(self, hostname, routing_protocol=None, **kwargs)`: Initializes a new `Router` instance.
- `add_routed_interface(self, interface=None, name=None, ip_address=None, subnet=None)`: Adds a routed interface object to the router.

The `Router` class is used to create router objects that can be added to a network. These router objects contain information about the router's hostname, management IP address, routing protocol, and routed interfaces.

The `add_routed_interface` method is particularly useful for adding routed interface objects to the router. A routed interface object is an instance of the `RouterInterface` class that has been configured with routing information. By adding routed interface objects to the router, network administrators can keep track of the router's interfaces and their routing configurations.

## Sample and Demo

Here is a sample code that demonstrates how to use the `Router` class:

```
# create a new router instance
router = Router('my_router')

# set the routing protocol
router.routing_protocol = 'OSPF'

# add a new routed interface
router.add_routed_interface(name='GigabitEthernet0/1', ip_address='10.0.0.1', subnet='255.255.255.0')

# print the router's hostname and routed interfaces
print(router.hostname)
print(router.routed_interfaces)

# connect the router
router.connect()

# disconnect the router
router.disconnect()

```

When executed, this code will create a new `Router` instance called `my_router`, set the routing protocol to OSPF, add a new routed interface with the name `GigabitEthernet0/1`, IP address `10.0.0.1`, and subnet `255.255.255.0`, print the router's hostname and routed interfaces, connect the router, and then disconnect the router.

This sample code demonstrates how easy it is to use these classes to manage network devices and their interfaces. By using these classes, network administrators can simplify the process of managing their network infrastructure.

## Conclusion

The `NetworkDevice` class, `RouterInterface` class, and `Router` class are powerful tools for network administrators. These classes can be used to manage network devices and their interfaces, and they can simplify the process of managing a large network infrastructure. By using these classes, network administrators can save time and reduce the risk of errors when managing their networks.