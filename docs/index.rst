Welcome to PyNSO Documentation
==============================

PyNSO is a Python library to interface to Cisco Network Services Orchestration (NSO).

Cisco® Network Services Orchestrator (NSO) provides a single pane
of glass for orchestrating a multivendor network. To offer an exceptional
range of support for multivendor devices, it uses network element drivers (NEDs).
Traditionally, device adaptors are a major roadblock, since they are not upgraded at
the same pace as device interfaces. But adding support for new devices can take months.
Cisco NSO NEDs, in contrast, can add new commands and devices in weeks. These drivers also
provide extremely fine-grained representation of relevant configuration commands. Using NEDs,
NSO also makes device configuration commands available over a networkwide, multivendor command
line interface (CLI), APIs, and user interface. In addition, NSO services like VPN can configure
a complex multivendor network.

NED Overview
------------
Network element drivers comprise the network-facing part of NSO.
They communicate over the native protocol supported by the device,
such as Network Configuration Protocol (NETCONF), Representational State Transfer (REST),
Extensible Markup Language (XML), CLI, and Simple Network Management Protocol (SNMP).

Authors
-------

This Python module was developed by the Research and Development team at `Dimension Data`_. This module is
provided under the `Apache 2.0 license`_ and the source code is available at `github.com`_.

Installation (stable version)
-----------------------------

PyNSO is available on PyPi. You can install latest stable version using pip:

.. sourcecode:: bash

    pip install pynso

Installation (development version)
----------------------------------

You can install latest development version from our Git repository:

.. sourcecode:: bash

    pip install -e git+https://github.com/DimensionDataCBUSydney/pynso.git@trunk#egg=pynso

Upgrading
---------

If you used pip to install the library you can also use it to upgrade it:

.. sourcecode:: bash

    pip install --upgrade pynso

Using it
--------

Using PyNSO is simple, the datastores are based on the NETCONF standard and the translation between Python
dictionaries and YANG is completed by the module automatically.

.. sourcecode:: python

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


Documentation
=============

Main
----

.. toctree::
    :glob:
    :maxdepth: 3

    setup
    api


.. note::

    Unless noted otherwise, all of the examples and code snippets in the
    documentation are licensed under the `Apache 2.0 license`_.

.. _`Apache 2.0 license`: https://www.apache.org/licenses/LICENSE-2.0.html

.. _`Dimension Data`: http://www.dimensiondata.com/
.. _`github.com`: https://github.com/DimensionDataCBUSydney/pynso