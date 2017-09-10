#!/usr/bin/env python
import argparse
import subprocess

#using this post as a reference:
#http://unix.stackexchange.com/questions/222054/how-can-i-use-linux-as-a-gateway

def set_iptable_rules(internal, external):
    rules = (
        '-t nat -A POSTROUTING -o {external} -j MASQUERADE',
        '-A FORWARD -i {internal} -o {external} -j ACCEPT',
        '-A FORWARD -i {external} -o {internal} -m state --state RELATED,ESTABLISHED -j ACCEPT'
        )
    for rule in rules:
        rule_updated = rule.format(internal=internal, external=external)
        to_run = 'iptables ' + rule_updated
        print('Adding rule: {}'.format(to_run))
        subprocess.run(to_run.split())




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
            "Script to setup pc as a gateway")
    parser.add_argument('-i', nargs=1, default=['wlp3s0'],
            help="The local network facing NIC")
    parser.add_argument('-o', nargs=1, default=['enp0s20u2'],
            help="The NIC facing the internet")

    p = parser.parse_args()

    #add iptable rules
    set_iptable_rules(p.i[0], p.o[0])


    #need to enable IP forwarding
    print("Enabling IP forwarding...")
    subprocess.run('sysctl -w net.ipv4.ip_forward=1'.split())

