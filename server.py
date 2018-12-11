import sys
import json
from flask import Flask
from flask import jsonify

# Receives the input entries
PORT = sys.argv[1]
NETFILE = sys.argv[2]
IXFILE = sys.argv[3]
NETIXLANFILE = sys.argv[4]
app = Flask(__name__)

# Loads the data from the files
with open(NETFILE) as f:
	netfile_data = json.load(f)
with open(IXFILE) as f:
	ixfile_data = json.load(f)
with open(NETIXLANFILE) as f:
	netixlanfile_data = json.load(f)

# Creates the endpoints
@app.route("/api/ix")
def get_all_IXPs_objects():
	return jsonify(data = ixfile_data['data'])


@app.route("/api/ixnets/<ix_id>")
def get_IXP_networks_ids(ix_id):
	ids = []
	
	for network in netixlanfile_data['data']:
		if network['ix_id'] == int(ix_id):
			ids.append(network['net_id'])
	
	return jsonify(data = ids)


@app.route("/api/netname/<net_id>")
def get_network_name(net_id):
	for network in netfile_data['data']:
		if network['id'] == int(net_id):
			return jsonify(data = network['name'])


if __name__ == '__main__':
	app.run(port=PORT)
