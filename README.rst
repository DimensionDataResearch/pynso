PyNSO
=====

|Build| |PyPI1| |PyPI2| |PyPI3| |Documentation Status| |Coverage|

Overview
--------

A Python client library for Cisco NSO (previously tail-f)

Installation
------------

To install use pip:

::

    $ pip install pynso

Or clone the repo:

::

    $ git clone https://github.com/DimensionDataCBUSydney/pynso.git
    $ python setup.py install

Usage
-----

.. code:: python

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

.. |Build| image:: https://travis-ci.org/DimensionDataCBUSydney/pynso.svg?branch=master
   :target: https://travis-ci.org/DimensionDataCBUSydney/pynso
.. |PyPI1| image:: https://img.shields.io/pypi/v/pynso.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/pynso
.. |PyPI2| image:: https://img.shields.io/pypi/l/pynso.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/pynso
.. |PyPI3| image:: https://img.shields.io/pypi/pyversions/pynso.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/pynso
.. |Documentation Status| image:: https://readthedocs.org/projects/pynso/badge/?version=latest
   :target: http://pynso.readthedocs.io/en/latest/?badge=latest
.. |Coverage| image:: https://coveralls.io/repos/github/DimensionDataCBUSydney/pynso/badge.svg?branch=master
   :target: https://coveralls.io/github/DimensionDataCBUSydney/pynso?branch=master
