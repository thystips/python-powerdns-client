# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import powerdns_client
from powerdns_client.api.search_api import SearchApi  # noqa: E501
from powerdns_client.rest import ApiException


class TestSearchApi(unittest.TestCase):
    """SearchApi unit test stubs"""

    def setUp(self):
        self.api = powerdns_client.api.search_api.SearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_data(self):
        """Test case for search_data

        Search the data inside PowerDNS  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
