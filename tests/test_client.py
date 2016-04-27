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
import os
import json
import unittest
from pynso.client import NSOClient
from pynso.datastores import DatastoreType


class TestClient(unittest.TestCase):
    def setUp(self):
        NSOClient.connectionCls = MockConnection
        self.client = NSOClient('test.com', 'test', 'testpass')

    def test_info(self):
        info = self.client.info()
        self.assertEqual(info['version'], '0.5')

    def test_get_datastore(self):
        store = self.client.get_datastore(DatastoreType.RUNNING)
        self.assertEqual(store['operations']['lock'], '/api/running/_lock')

    def test_get_rollbacks(self):
        rollbacks = self.client.get_rollbacks()
        self.assertEqual(rollbacks['rollbacks']['file']['name'], '86')

    def test_get_rollback(self):
        rollback = self.client.get_rollback('86')
        self.assertEqual(len(rollback), 45)


class MockConnection(object):
    def __init__(self, host, username, password, ssl):
        pass

    path_to_fixture_mapping = {
        'None-application/vnd.yang.api-None': 'api-info.json',
        'running-application/vnd.yang.datastore-None': 'api-running-datastore.json',
        'rollbacks-application/vnd.yang.api-None': 'api-rollbacks.json',
        'rollbacks-application/vnd.yang.api-86': 'api-rollbacks-86.txt'
    }

    def _path_to(self, file):
        fixture_dir = os.path.join(
            os.path.abspath(os.path.split(__file__)[0]),
            'fixtures')
        return os.path.join(fixture_dir, file)

    def get(self, resource_type, media_type, path=None, params=None):
        key = '%s-%s-%s' % (resource_type,
                            media_type,
                            path)
        with open(self._path_to(MockConnection.path_to_fixture_mapping[key])) as json_file:
            json_data = json.load(json_file)
        return json_data

    def get_plain(self, resource_type, media_type, path=None, params=None):
        key = '%s-%s-%s' % (resource_type,
                            media_type,
                            path)
        with open(self._path_to(MockConnection.path_to_fixture_mapping[key])) as file_:
            data = file_.readlines()
        return data

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
