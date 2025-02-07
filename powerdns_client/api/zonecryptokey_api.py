# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from powerdns_client.api_client import ApiClient


class ZonecryptokeyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_cryptokey(self, cryptokey, server_id, zone_id, **kwargs):  # noqa: E501
        """Creates a Cryptokey  # noqa: E501

        This method adds a new key to a zone. The key can either be generated or imported by supplying the content parameter. if content, bits and algo are null, a key will be generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and the default-zsk-algorithm and default-zsk-size options for a ZSK.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cryptokey(cryptokey, server_id, zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Cryptokey cryptokey: Add a Cryptokey (required)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_cryptokey_with_http_info(cryptokey, server_id, zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_cryptokey_with_http_info(cryptokey, server_id, zone_id, **kwargs)  # noqa: E501
            return data

    def create_cryptokey_with_http_info(self, cryptokey, server_id, zone_id, **kwargs):  # noqa: E501
        """Creates a Cryptokey  # noqa: E501

        This method adds a new key to a zone. The key can either be generated or imported by supplying the content parameter. if content, bits and algo are null, a key will be generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and the default-zsk-algorithm and default-zsk-size options for a ZSK.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_cryptokey_with_http_info(cryptokey, server_id, zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Cryptokey cryptokey: Add a Cryptokey (required)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cryptokey', 'server_id', 'zone_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cryptokey' is set
        if ('cryptokey' not in params or
                params['cryptokey'] is None):
            raise ValueError("Missing the required parameter `cryptokey` when calling `create_cryptokey`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `create_cryptokey`")  # noqa: E501
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `create_cryptokey`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cryptokey' in params:
            body_params = params['cryptokey']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/zones/{zone_id}/cryptokeys', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Cryptokey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_cryptokey(self, server_id, zone_id, cryptokey_id, **kwargs):  # noqa: E501
        """This method deletes a key specified by cryptokey_id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_cryptokey(server_id, zone_id, cryptokey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the Cryptokey (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)  # noqa: E501
            return data

    def delete_cryptokey_with_http_info(self, server_id, zone_id, cryptokey_id, **kwargs):  # noqa: E501
        """This method deletes a key specified by cryptokey_id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the Cryptokey (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id', 'cryptokey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `delete_cryptokey`")  # noqa: E501
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `delete_cryptokey`")  # noqa: E501
        # verify the required parameter 'cryptokey_id' is set
        if ('cryptokey_id' not in params or
                params['cryptokey_id'] is None):
            raise ValueError("Missing the required parameter `cryptokey_id` when calling `delete_cryptokey`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']  # noqa: E501
        if 'cryptokey_id' in params:
            path_params['cryptokey_id'] = params['cryptokey_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cryptokey(self, server_id, zone_id, cryptokey_id, **kwargs):  # noqa: E501
        """Returns all data about the CryptoKey, including the privatekey.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cryptokey(server_id, zone_id, cryptokey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the CryptoKey (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)  # noqa: E501
            return data

    def get_cryptokey_with_http_info(self, server_id, zone_id, cryptokey_id, **kwargs):  # noqa: E501
        """Returns all data about the CryptoKey, including the privatekey.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the CryptoKey (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id', 'cryptokey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `get_cryptokey`")  # noqa: E501
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `get_cryptokey`")  # noqa: E501
        # verify the required parameter 'cryptokey_id' is set
        if ('cryptokey_id' not in params or
                params['cryptokey_id'] is None):
            raise ValueError("Missing the required parameter `cryptokey_id` when calling `get_cryptokey`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']  # noqa: E501
        if 'cryptokey_id' in params:
            path_params['cryptokey_id'] = params['cryptokey_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Cryptokey',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_cryptokeys(self, server_id, zone_id, **kwargs):  # noqa: E501
        """Get all CryptoKeys for a zone, except the privatekey  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cryptokeys(server_id, zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :return: list[Cryptokey]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_cryptokeys_with_http_info(server_id, zone_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_cryptokeys_with_http_info(server_id, zone_id, **kwargs)  # noqa: E501
            return data

    def list_cryptokeys_with_http_info(self, server_id, zone_id, **kwargs):  # noqa: E501
        """Get all CryptoKeys for a zone, except the privatekey  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_cryptokeys_with_http_info(server_id, zone_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :return: list[Cryptokey]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_cryptokeys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `list_cryptokeys`")  # noqa: E501
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `list_cryptokeys`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/zones/{zone_id}/cryptokeys', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Cryptokey]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_cryptokey(self, cryptokey, server_id, zone_id, cryptokey_id, **kwargs):  # noqa: E501
        """This method (de)activates a key from zone_name specified by cryptokey_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_cryptokey(cryptokey, server_id, zone_id, cryptokey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Cryptokey cryptokey: the Cryptokey (required)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :param str cryptokey_id: Cryptokey to manipulate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_cryptokey_with_http_info(cryptokey, server_id, zone_id, cryptokey_id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_cryptokey_with_http_info(cryptokey, server_id, zone_id, cryptokey_id, **kwargs)  # noqa: E501
            return data

    def modify_cryptokey_with_http_info(self, cryptokey, server_id, zone_id, cryptokey_id, **kwargs):  # noqa: E501
        """This method (de)activates a key from zone_name specified by cryptokey_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_cryptokey_with_http_info(cryptokey, server_id, zone_id, cryptokey_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Cryptokey cryptokey: the Cryptokey (required)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :param str cryptokey_id: Cryptokey to manipulate (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cryptokey', 'server_id', 'zone_id', 'cryptokey_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cryptokey' is set
        if ('cryptokey' not in params or
                params['cryptokey'] is None):
            raise ValueError("Missing the required parameter `cryptokey` when calling `modify_cryptokey`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `modify_cryptokey`")  # noqa: E501
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params or
                params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `modify_cryptokey`")  # noqa: E501
        # verify the required parameter 'cryptokey_id' is set
        if ('cryptokey_id' not in params or
                params['cryptokey_id'] is None):
            raise ValueError("Missing the required parameter `cryptokey_id` when calling `modify_cryptokey`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']  # noqa: E501
        if 'cryptokey_id' in params:
            path_params['cryptokey_id'] = params['cryptokey_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cryptokey' in params:
            body_params = params['cryptokey']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
