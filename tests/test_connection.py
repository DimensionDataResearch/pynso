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

import unittest
from pynso.resourcetypes import (ResourceType, MediaType)
from pynso.connection import (_format_url, NSOConnection)


class TestConnection(unittest.TestCase):
    test_host = 'test.com'

    def test_url_format(self):
        self.assertEqual(_format_url(host=self.test_host,
                                     resource_type=ResourceType.OPERATION,
                                     path='foo/bar'),
                         'https://test.com/api/operation/foo/bar')

    def test_url_format_http(self):
        self.assertEqual(_format_url(host=self.test_host,
                                     resource_type=ResourceType.OPERATION,
                                     path='foo/bar',
                                     ssl=False),
                         'http://test.com/api/operation/foo/bar')

    def test_url_format_base(self):
        self.assertEqual(_format_url(host=self.test_host,
                                     resource_type=None,
                                     path=None,
                                     ssl=True),
                         'https://test.com/api')

    def test_headers(self):
        connection = NSOConnection('test', 'test', 'test')
        headers = connection._get_headers(MediaType.API)
        self.assertEqual(len(headers), 1)
        self.assertTrue(headers['Content-Type'].startswith(MediaType.API))
        self.assertTrue(headers['Content-Type'].endswith(NSOConnection.response_type))


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
