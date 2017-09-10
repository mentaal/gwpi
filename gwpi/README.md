GWPI
====

Handy script to pass on internet access to another machine on a local network.

Host machine that runs script sets up iptables to allow masquerading to allow a
client machine to access the host machine's second network interface which
presumably is connected to the internet. 

I use this to provide internet access to my raspberry PI. 

Usage
-----

Run gwpi using -i and reference the network interface facting the local network
and -o, referencing the network facing the internet.

On the Raspberry PI, I run this alias

alias gw='sudo iptables -t nat -A OUTPUT -p udp --dport 53 -j DNAT --to
8.8.8.8:53'

