# Network Topologies and Simulations using Mininet

The goal of this project is to represent network topologies and simulating basic network commands in <a href="http://mininet.org">Mininet</a>, a network simulator that runs multiple Linux containers for individual hosts and uses <a href="openvswitch.org">Open vSwitch</a> for network device emulation.

## Defining Network Topologies

`mntopo.py` defines a simple network topology consisting of 2 hosts, 3 switches, and 4 links, as illustrated in the following figure:

<p align="center">
  <img src="https://user-images.githubusercontent.com/87489775/125826918-bc79ba05-e099-46f4-a83b-96cabef27e85.png">
</p>

`topology.sh` is a script that produces some raw data for the TCP congestion window and bandwidth in Mbps and some figures. Here's an example of the bandwidth results:

<p align="center">
  <img src="https://user-images.githubusercontent.com/87489775/125826843-3fb08c8b-def8-44bf-b470-46c081c327b2.png">
</p>

`complextopo.py` defines a more complex network topology consisting of 3 hosts, 4 switches, and a mix of Ethernet, WiFi, and 3G links, as illustrated in the following figure:

<p align="center">
  <img src="https://user-images.githubusercontent.com/87489775/125828903-f772f337-36f6-441a-aa45-2303c18d345a.png">
</p>

## Network Simulation

Mininet's CLI is used to simulate basic network commands over our topology. `cli.py` loads our complex topoloy from earlier. After Mininet loads the topology, the Mininet command prompt is available: `mininet>`

To execute a command on one host, type the host name followed by the command. For example, to test the connection between `h1` and `h2`, we can command `h1` to ping `h2` with 10 packets of data and print out the results:

`mininet> h1 ping h2 -c 10`

There may be some packet loss during the ping command execution due to the loss rates on WiFi link between `s3` and `h2`.

You can issue ping commands between all hosts on the topology to verify that the topology is connected using the `pingall` command. A failed ping (either due to loss rates or misconfiguration) between a pair of hosts is marked by an `X`.

## Data Centre Topology

`datacenter.py` can be used to emulate a custom, fan-in type data centre topology, where there will be a top-level switch (tls) connected to a number of mid-level switches (mls), which are in turn connected to rack switches with a number of hosts connected to them. The custom topology is defined by 2 parameters, which are accepted as arguments to `datacenter.py`:

- `fi`: The fan-in rate, i.e. the number of mls' connected to the tls.
- `n`: The number of hosts connected to each rack switch.

Here's an example of a data centre topology with `fi = 2` and `n = 5`:

<p align="center">
  <img src="https://user-images.githubusercontent.com/87489775/125832199-3fcf9a6c-b097-4c82-9c68-b87bf3900136.png">
</p>
