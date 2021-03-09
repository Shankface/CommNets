# CommNets

to run:
python3 port_checker.py hostname start_port:end_port

if only one port is entered, it will only check status of that port

if no port is specified, it will check all ports between 1-1024

if no hostname is specified, it will check local host from 1-1024

must input hostname (including local host) in order to check specific ports rather than all ports between 1-1024

example: python3 port_checker.py 8.8.8.8 400:450
