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
import requests
import requests_mock

from pynso.resourcetypes import (ResourceType, MediaType)
from pynso.connection import (_format_url, NSOConnection)


class TestConnection(unittest.TestCase):
    test_host = 'test.com'
    test_error = {'errors': {'error': [{'error-message': 'test'}]}}

    def setUp(self):
        self.connection = NSOConnection('test.com', 'test', 'test', False)
        self.adapter = requests_mock.Adapter()
        self.connection.session.mount('http://test.com/', self.adapter)

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

    def test_url_format_http_no_path(self):
        self.assertEqual(_format_url(host=self.test_host,
                                     resource_type=ResourceType.OPERATION,
                                     path=None,
                                     ssl=False),
                         'http://test.com/api/operation')

    def test_url_format_base(self):
        self.assertEqual(_format_url(host=self.test_host,
                                     resource_type=None,
                                     path=None,
                                     ssl=True),
                         'https://test.com/api')

    def test_url_format_path_(self):
        self.assertEqual(_format_url(host=self.test_host,
                                     resource_type=None,
                                     path='foo/bar',
                                     ssl=True),
                         'https://test.com/api/foo/bar')

    def test_headers(self):
        connection = NSOConnection('test', 'test', 'test', False)
        headers = connection._get_headers(MediaType.API)
        self.assertEqual(len(headers), 1)
        self.assertTrue(headers['Accept'].startswith(MediaType.API))
        self.assertTrue(headers['Accept'].endswith(NSOConnection.response_type))

    def test_get(self):
        test = {'a': 'b'}
        self.adapter.register_uri('GET', '/api/api', json=test, status_code=200)
        response = self.connection.get(ResourceType.API, MediaType.API)
        self.assertTrue(test['a'] == response['a'])

    def test_get_error(self):
        self.adapter.register_uri('GET', '/api/api', json=self.test_error, status_code=404)
        with self.assertRaises(requests.HTTPError):
            self.connection.get(ResourceType.API, MediaType.API)

    def test_get_error_plain(self):
        self.adapter.register_uri('GET', '/api/api', json={'test': 'a'}, status_code=404)
        with self.assertRaises(requests.HTTPError):
            self.connection.get(ResourceType.API, MediaType.API)

    def test_get_plain(self):
        test = 'hello world'
        self.adapter.register_uri('GET', '/api/api', text=test, status_code=200)
        response = self.connection.get_plain(ResourceType.API, MediaType.API)
        self.assertTrue(test == response)

    def test_get_plain_error(self):
        self.adapter.register_uri('GET', '/api/api', json=self.test_error, status_code=404)
        with self.assertRaises(requests.HTTPError):
            self.connection.get_plain(ResourceType.API, MediaType.API)

    def test_put(self):
        test = {'a': 'b'}
        self.adapter.register_uri('PUT', '/api/api', json=test, status_code=200)
        response = self.connection.put(ResourceType.API, MediaType.API, data={'test': 'data'})
        self.assertTrue(test == response)

    def test_put_no_response(self):
        self.adapter.register_uri('PUT', '/api/api', status_code=204)
        response = self.connection.put(ResourceType.API, MediaType.API, data={'test': 'data'})
        self.assertTrue(response)

    def test_put_error(self):
        self.adapter.register_uri('PUT', '/api/api', json=self.test_error, status_code=404)
        with self.assertRaises(requests.HTTPError):
            self.connection.put(ResourceType.API, MediaType.API, data={'test': 'data'})

    def test_delete(self):
        test = {'a': 'b'}
        self.adapter.register_uri('DELETE', '/api/api', json=test, status_code=200)
        response = self.connection.delete(ResourceType.API, MediaType.API, data={'test': 'data'})
        self.assertTrue(test == response)

    def test_delete_no_response(self):
        self.adapter.register_uri('DELETE', '/api/api', status_code=204)
        response = self.connection.delete(ResourceType.API, MediaType.API, data={'test': 'data'})
        self.assertTrue(response)

    def test_delete_error(self):
        self.adapter.register_uri('DELETE', '/api/api', json=self.test_error, status_code=404)
        with self.assertRaises(requests.HTTPError):
            self.connection.delete(ResourceType.API, MediaType.API, data={'test': 'data'})

    def test_post(self):
        test = {'a': 'b'}
        self.adapter.register_uri('POST', '/api/api', json=test, status_code=200)
        response = self.connection.post(ResourceType.API, MediaType.API, data={'test': 'data'})
        self.assertTrue(test == response)

    def test_post_no_response(self):
        self.adapter.register_uri('POST', '/api/api', status_code=204)
        response = self.connection.post(ResourceType.API, MediaType.API, data={'test': 'data'})
        self.assertTrue(response)

    def test_post_error(self):
        self.adapter.register_uri('POST', '/api/api', json=self.test_error, status_code=404)
        with self.assertRaises(requests.HTTPError):
            self.connection.post(ResourceType.API, MediaType.API, data={'test': 'data'})

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
