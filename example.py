from pprint import pprint

from pynso.client import NSOClient
from pynso.datastores import DatastoreType

# Setup a client
client = NSOClient('10.159.91.14', 'admin', 'admin')

# Get information about the API
print('Getting API version number')
pprint(client.info()['version'])

# Get the information about the running datastore
print('Getting the contents of the running datastore')
pprint(client.get_datastore(DatastoreType.RUNNING))

# Get a data path
print('Getting a specific data path: snmp:snmp namespace and the agent data object')
pprint(client.get_data(DatastoreType.RUNNING, ('snmp:snmp', 'agent')))