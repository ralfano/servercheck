import unittest
import requests_mock
from .http import ping_servers

class TestHttp(unittest.TestCase):

    def test_ping_servers(self):
        servers = ('web-node1:80', 'web-node1:8080', 'web-node2:8080')
        with requests_mock.Mocker() as m:
            m.get('http://web-node1:80')
            m.get('http://web-node1:8080')
            m.get('http://web-node2:8080')
            results = ping_servers(servers)
            self.assertEqual(len(results["success"]), 3)



