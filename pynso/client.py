# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''
The main client class for the NSO APIs
'''
from .connection import NSOConnection
from .resourcetypes import MediaType

__all__ = ['NSOClient']


class NSOClient(object):
    connectionCls = NSOConnection

    def __init__(self, host, username, password,
                 port=8080, ssl=False):
        self.connection = self.connectionCls('%s:%s' % (host, port),
                                             username,
                                             password,
                                             ssl)

    def info(self):
        """
        Returns API information
        """
        return self.connection.get(resource_type=None,
                                   media_type=MediaType.API,
                                   path=None)['api']

    def get_datastore(self, datastore, params=None):
        """
        Get the details of a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`
        """
        return self.connection.get(resource_type=datastore,
                                   media_type=MediaType.DATASTORE,
                                   path=None,
                                   params=params)

    def get_data(self, datastore, data_path, params=None):
        """
        Get a data entry in a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`

        :param data_path: The list of paths
        :type  data_path: ``list`` of ``str`` or ``tuple``
        """
        data_path = '/'.join(data_path)
        return self.connection.get(resource_type=datastore,
                                   media_type=MediaType.DATA,
                                   path=data_path,
                                   params=params)
