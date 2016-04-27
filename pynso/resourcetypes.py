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

__all__ = ['ResourceType',
           'MediaType',
           'resource_type_to_media_type',
           'media_type_to_resource_type']


class ResourceType(object):
    '''
    An enum of the resource types in the API.

    The RESTCONF protocol defines some application
    specific media types to identify each of the available resource types
    '''
    API = 'api'
    DATASTORE = 'datastore'
    DATA = 'data'
    COLLECTION = 'collection'
    OPERATION = 'operation'


class MediaType(object):
    '''
    An enum of the media types available for each resource
    '''
    API = 'application/vnd.yang.api'
    DATASTORE = 'application/vnd.yang.datastore'
    DATA = 'application/vnd.yang.data'
    COLLECTION = 'application/vnd.yang.collection'
    OPERATION = 'application/vnd.yang.operation'


_resource_type_to_media_type_mapping = {
    ResourceType.API: MediaType.API,
    ResourceType.COLLECTION: MediaType.COLLECTION,
    ResourceType.DATA: MediaType.DATA,
    ResourceType.DATASTORE: MediaType.DATASTORE,
    ResourceType.OPERATION: MediaType.OPERATION
}
_media_type_to_resource_type_mapping = dict(
    (v, k) for k, v in _resource_type_to_media_type_mapping.items())


def resource_type_to_media_type(resource):
    '''
    Returns the media type for a resource type

    :param resource: The resource type
    :type  resource: :class:`ResourceType`

    :return: An instance of :class:`MediaType`
    :rtype: :class:`MediaType`
    '''
    return _resource_type_to_media_type_mapping[resource]


def media_type_to_resource_type(media_type):
    '''
    Returns the media type for a resource type

    :param resource: The resource type
    :type  resource: :class:`ResourceType`

    :return: An instance of :class:`MediaType`
    :rtype: :class:`MediaType`
    '''
    return _media_type_to_resource_type_mapping[media_type]
