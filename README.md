# PyNSO


[![Build](https://travis-ci.org/DimensionDataCBUSydney/pynso.svg?branch=master)](https://travis-ci.org/DimensionDataCBUSydney/pynso)
[![PyPI](https://img.shields.io/pypi/v/pynso.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/l/pynso.svg?maxAge=2592000)]()
[![PyPI](https://img.shields.io/pypi/pyversions/pynso.svg?maxAge=2592000)]()

Overview
--------

A Python client library for Cisco NSO (previously tail-f)

Installation
------------

To install use pip:

    $ pip install pynso


Or clone the repo:

    $ git clone https://github.com/DimensionDataCBUSydney/pynso.git
    $ python setup.py install
    
Usage
-----

```python
from pprint import pprint

from pynso.client import NSOClient
from pynso.datastores import DatastoreType

# Setup a client
client = NSOClient('10.123.92.12', 'admin', 'admin')

# Get information about the API
print('Getting API version number')
pprint(client.info()['version'])

# Get the information about the running datastore
print('Getting the contents of the running datastore')
pprint(client.get_datastore(DatastoreType.RUNNING))
```