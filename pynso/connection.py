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

import requests

__all__ = ['NSOConnection']


def _format_url(host, resource_type, path, ssl=True):
    protocol = 'https' if ssl else 'http'
    if resource_type is None:
        if path is None:
            return '%s://%s/api' % (protocol, host)
        return '%s://%s/api/%s' % (protocol, host, path)
    return '%s://%s/api/%s/%s' % (protocol, host, resource_type, path)


class NSOConnection(object):
    response_type = 'json'

    def __init__(self, host, username, password):
        self.host = host
        self.session = requests.Session()
        self.session.auth = (username, password)

    def get(self, resource_type, media_type, path):
        url = _format_url(self.host, resource_type, path)
        response = self.session.get(
            url,
            headers=self._get_headers(media_type))
        return response.json()

    def _get_headers(self, media_type):
        return {
            'Accept': '%s+%s' % (media_type,
                                       NSOConnection.response_type)
        }
