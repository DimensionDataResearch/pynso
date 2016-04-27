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
Utility methods for converting media and resource types, with their ENUMs
'''

__all__ = ['DatastoreType']


class DatastoreType(object):
    '''
    An enum of the resource types in the API.

    :cvar config: Link to the "config" resource
    :cvar running: Link to the "running" resource.
    :cvar operational: Link to the "operational" resource.
    :cvar operations: Container for available operations (i.e: YANG rpc statements).
    :cvar rollbacks: Container for available rollback files.
    '''
    CONFIG = 'config'
    RUNNING = 'running'
    OPERATIONAL = 'operational'
    OPERATIONS = 'operations'
    ROLLBACKS = 'rollbacks'
