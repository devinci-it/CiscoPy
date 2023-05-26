import unittest
from CiscoPy.devices.router import Router



class TestRouter(unittest.TestCase):

    def setUp(self):
        self.router = Router('R1')

    def test_add_interface(self):
        self.router.add_interface('GigabitEthernet0/0', '10.0.0.1', '255.255.255.0')
        self.assertEqual(len(self.router.interfaces), 1)

    def test_configure_interface(self):
        self.router.add_interface('GigabitEthernet0/0', '10.0.0.1', '255.255.255.0')
        self.router.configure_interface('GigabitEthernet0/0', ip_address='10.0.0.2',subnet_mask= '255.255.255.0')
        self.assertEqual(self.router.interfaces[0].ip_address, '10.0.0.1')

    def test_generate_config(self):
        self.router.add_interface('GigabitEthernet0/0', '10.0.0.1', '255.255.255.0')
        self.router.add_interface('GigabitEthernet0/1', '10.0.1.1', '255.255.255.0')
        self.router.add_route('192.168.0.0/24', '10.0.0.2', 1, 120)
        expected_output = ' \\n        interface GigabitEthernet0/0 \\n        ip address 10.0.0.1 255.255.255.0 \\n        \\n        interface GigabitEthernet0/1\\n        ip address 10.0.1.1 255.255.255.0\\n        \\n        ip route 192.168.0.0/24 10.0.0.2 1\\n        '
        self.assertEqual(self.router.generate_config(), expected_output)

if __name__ == '__main__':
    unittest.main()
