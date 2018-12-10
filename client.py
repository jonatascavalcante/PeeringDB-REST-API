import sys
import json
import socket

# Receives the input entries
IP = sys.argv[1]
PORT = sys.argv[2]
OPT = sys.argv[3]

BIND = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(BIND)


def ixps_by_network():
	ixps = localhost:8080/api/ix
	# pegar o 'data' da requisicao
	for ixp in ixps:
		nets = localhost:8080/api/ixnets/ixp['id']
		# pegar o 'data' da requisicao
		for net in nets:
			if net in all_nets:
				all_nets[net] += 1
			else
				all_nets[net] = 1

	for key, qtd in all_nets.iteritems():
		netname = localhost:8080/api/netname/key
		print key + '\t' + netname + '\t' + qtd + '\n'


def networks_by_ixp():
	ixps = localhost:8080/api/ix

	for ixp in ixps:
		nets = localhost:8080/api/ixnets/ixp['id']
		print ixp['id'] + '\t' + ixp['name'] + len(nets) + '\n'


if(OPT == 0):
	ixps_by_network()
else if(OPT == 1):
	networks_by_ixp()
