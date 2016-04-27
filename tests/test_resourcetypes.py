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
from pynso.resourcetypes import (ResourceType, MediaType,
                                 resource_type_to_media_type,
                                 media_type_to_resource_type)


class TestResourceTypes(unittest.TestCase):
    def test_dict_sizes(self):
        self.assertEqual(len(dir(ResourceType)), len(dir(MediaType)))

    def test_map(self):
        self.assertEqual(resource_type_to_media_type(ResourceType.API), MediaType.API)

    def test_reverse_map(self):
        self.assertEqual(media_type_to_resource_type(MediaType.API), ResourceType.API)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
