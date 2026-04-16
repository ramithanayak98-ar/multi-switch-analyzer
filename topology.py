from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink

class MultiSwitchTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')
        h4 = self.addHost('h4', ip='10.0.0.4/24')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(h3, s3)
        self.addLink(h4, s3)

def run():
    topo = MultiSwitchTopo()
    net = Mininet(topo=topo,
                  controller=lambda name: RemoteController(name, ip='127.0.0.1', port=6633),
                  switch=OVSKernelSwitch,
                  link=TCLink)
    net.start()
    print("\n*** Multi-Switch Topology Started")
    print("*** h1=10.0.0.1, h2=10.0.0.2 connected to s1")
    print("*** h3=10.0.0.3, h4=10.0.0.4 connected to s3")
    print("*** s1 -- s2 -- s3\n")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
