from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom
																			
# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    "Mininet Complex Topology"

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        # Host and link configuration
        hostConfig = {'cpu': cpu}
        linkConfigEth = {'bw': 25, 'delay': '2ms', 'loss': 0, 'max_queue_size': max_queue_size}
        linkConfigWiFi = {'bw': 10, 'delay': '6ms', 'loss': 3, 'max_queue_size': max_queue_size}
        linkConfig3G = {'bw': 3, 'delay': '10ms', 'loss': 8, 'max_queue_size': max_queue_size}

        # Hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        h1 = self.addHost('h1', **hostConfig)
        h2 = self.addHost('h2', **hostConfig)
        h3 = self.addHost('h3', **hostConfig)

        # Link h1-s1
        self.addLink(h1, s1, **linkConfigEth)

        # Link s1-s2
        self.addLink(s1, s2, **linkConfigEth)
        
        # Link s2-s3
        self.addLink(s2, s3, **linkConfigEth)
        
        # Link h2-s3
        self.addLink(h2, s3, **linkConfigWiFi)

        # Link s2-s4
        self.addLink(s2, s4, **linkConfigEth)

        # Link h3-s4
        self.addLink(h3, s4, **linkConfig3G)