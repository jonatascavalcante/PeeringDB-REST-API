import sys
import json
import socket

# Receives the input entries
ADDR = sys.argv[1]
SERVER_IP = ADDR.split(':')[0]
PORT = ADDR.split(':')[1]
OPT = sys.argv[2]


def make_request(endpoint):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (SERVER_IP, int(PORT))
	client_socket.connect(server_address)

	request = 'GET ' + endpoint + ' HTTP/1.1\r\nHost: ' + SERVER_IP + ':' + PORT + '\r\nContent-Type: application/json\r\n\r\n'
	client_socket.send(request)
	response = ''
	while True:
		recv = client_socket.recv(1024)
		if not recv:
			break
		response += recv
	
	client_socket.close()
	return response.split("\n\r")[1]


def ixps_by_network():
	all_nets = {}
	ixps_data = make_request('/api/ix')
	ixps = json.loads(ixps_data)

	for ixp in ixps['data']:
		nets_data = make_request('/api/ixnets/' + str(ixp['id']))
		nets = json.loads(nets_data)
		for net in nets['data']:
			if net in all_nets:
				all_nets[net] += 1
			else:
				all_nets[net] = 1

	for key, qtd in all_nets.iteritems():
		netname_data = make_request('/api/netname/' + str(key))
		netname = json.loads(netname_data)
		print str(key) + '\t' + netname['data'] + '\t' + str(qtd) + '\n'


def networks_by_ixp():
	ixps_data = make_request('/api/ix')
	ixps = json.loads(ixps_data)

	for ixp in ixps['data']:
		nets_data = make_request('/api/ixnets/' + str(ixp['id']))
		nets = json.loads(nets_data)
		print str(ixp['id']) + '\t' + ixp['name'] + str(len(nets['data'])) + '\n'


if(int(OPT) == 0):
	ixps_by_network()
elif(int(OPT) == 1):
	networks_by_ixp()
