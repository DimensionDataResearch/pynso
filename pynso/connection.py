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


def _format_url(resource_type, path):
    return 'api/%s/%s' % (resource_type, path)


class NSOConnection(object):
    response_type = 'json'

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.session = requests.Session()

    def get(self, resource_type, media_type, path):
        url = _format_url(resource_type, path)
        self.session.get(url,
                         headers=self._get_headers(media_type))

    def _get_headers(self, media_type):
        return {
            'Content-Type': '%s+%s' % (media_type,
                                       NSOConnection.response_type)
        }
