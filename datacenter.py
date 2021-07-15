#!/usr/bin/python
# Creates a datacenter topology based on command line parameters and starts the Mininet Command Line Interface.

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import lg, output, setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.cli import CLI
import argparse
import sys
import os

# Parse Command Line Arguments
parser = argparse.ArgumentParser(description="Datacenter Topologies")

parser.add_argument('--fi',
                    type=int,
                    help=("Number of Fan-in Switches to create."
                    "Must be >= 1"),
                    required=True)

parser.add_argument('--n',
                    type=int,
                    help=("Number of hosts to create in each lower level switch."
                    "Must be >= 1"),
                    required=True)

args = parser.parse_args()

lg.setLogLevel('info')

# Topology to be instantiated in Mininet
class DataCenter(Topo):
    "DataCenter Topology"

    def __init__(self, n=1, delay='0ms', fi=1,  cpu=.01, max_queue_size=None, **params):
        """Star Topology with fi fan-in  zones.
           n: number of hosts per low level switch
           cpu: system fraction for each host
           bw: link bandwidth in Mb/s
           delay: link latency (e.g. 10ms)"""
        self.cpu = 1 / ((n * fi * fi) * 1.5)

        # Initialize topo
        Topo.__init__(self, **params)

        hostConfig = {'cpu': cpu}
        swlinkConfig = {'bw': 10, 'delay': '0ms', 'max_queue_size': max_queue_size}
        hostlinkConfig = {'bw': 1, 'delay': '1ms','max_queue_size': max_queue_size}
        tls = self.addSwitch('tls1')
       
        # Add mid level switches and links to top level switch
        for i in range(1, fi+1):
            mls = "mls" + str(i)
            self.addSwitch(mls)
            self.addLink(tls, mls, **swlinkConfig)
            # Add lower level switches and links to mid level switches
            for j in range(1, fi+1):
                lls = "s" + str(i) + "x" + str(j)
                self.addSwitch(lls)
                self.addLink(mls, lls, **swlinkConfig)
                # Add hosts and links to low level switches
                for k in range(1, n+1):
                    host = "h" + str(i) + "x" + str(j) + "x" + str(k)
                    self.addHost(host, **hostConfig)
                    self.addLink(host, lls, **hostlinkConfig)
            
def main():
    "Create specified topology and launch the command line interface"    
    topo = DataCenter(n=args.n, fi=args.fi)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.start()
    CLI(net)
    net.stop()
    
if __name__ == '__main__':
    setLogLevel('info')
    main()