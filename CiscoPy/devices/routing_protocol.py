
class Route:
    def __init__(self, destination_network: str, next_hop: str, metric: int = None, admin_distance: int = None):
        '''
        Initializes a Route object.

        Args:
        - destination_network: str, the destination network for the route
        - next_hop: str, the next hop for the route
        - metric: int, the metric for the route (optional)
        - admin_distance: int, the administrative distance for the route (optional)

        Returns:
        - None
        '''
        self.destination_network = destination_network
        self.next_hop = next_hop
        self.metric = metric
        self.admin_distance = admin_distance

    def generate_config(self) -> str:
        '''
        Generates the configuration for the route.

        Returns:
        - str, the configuration for the route
        '''
        config = ""
        protocol = self.get_protocol()
        admin_distance = self.get_admin_distance()
        config += f"ip route {self.destination_network} {self.next_hop} {admin_distance} {protocol} {self.metric}\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n"
        return config

    def get_protocol(self) -> str:
        '''
        Returns the routing protocol for the route based on the admin distance.

        Returns:
        - str, the routing protocol for the route
        '''
        if self.admin_distance == 120:
            return "RIP"
        elif self.admin_distance == 90:
            return "EIGRP"
        elif self.admin_distance == 110:
            return "OSPF"
        elif self.admin_distance == 1:
            return "CONNECTED"
        elif self.admin_distance == 0:
            return "STATIC"

    def get_admin_distance(self) -> int:
        '''
        Returns the administrative distance for the route.

        Returns:
        - int, the administrative distance for the route
        '''
        if self.admin_distance is None:
            protocol = self.get_protocol()
            if protocol == "RIP":
                return 120
            elif protocol == "EIGRP":
                return 90
            elif protocol == "OSPF":
                return 110
            elif protocol == "CONNECTED":
                return 1
            elif protocol == "STATIC":
                return 0
        else:
            return self.admin_distance


class RIPRoute(Route):
    '''
    A subclass of the Route class for RIP routes.
    '''
    def __init__(self, destination_network: str, next_hop: str, metric: int = None):
        super().__init__(destination_network, next_hop, metric=metric, admin_distance=120)


class EIGRPRoute(Route):
    '''
    A subclass of the Route class for EIGRP routes.
    '''
    def __init__(self, destination_network: str, next_hop: str, metric: int = None):
        super().__init__(destination_network, next_hop, metric=metric, admin_distance=90)


class OSPFRoute(Route):
    '''
    A subclass of the Route class for OSPF routes.
    '''
    def __init__(self, destination_network: str, next_hop: str, metric: int = None):
        super().__init__(destination_network, next_hop, metric=metric, admin_distance=110)


class ConnectedRoute(Route):
    '''
    A subclass of the Route class for connected routes.
    '''
    def __init__(self, destination_network: str, next_hop: str):
        super().__init__(destination_network, next_hop, admin_distance=1)


class StaticRoute(Route):
    '''
    A subclass of the Route class for static routes.
    '''
    def __init__(self, destination_network: str, next_hop: str):
        super().__init__(destination_network, next_hop, admin_distance=0)