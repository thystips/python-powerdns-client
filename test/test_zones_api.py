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
from powerdns_client.api.zones_api import ZonesApi  # noqa: E501
from powerdns_client.rest import ApiException


class TestZonesApi(unittest.TestCase):
    """ZonesApi unit test stubs"""

    def setUp(self):
        self.api = powerdns_client.api.zones_api.ZonesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_axfr_export_zone(self):
        """Test case for axfr_export_zone

        Returns the zone in AXFR format.  # noqa: E501
        """
        pass

    def test_axfr_retrieve_zone(self):
        """Test case for axfr_retrieve_zone

        Retrieve slave zone from its master.  # noqa: E501
        """
        pass

    def test_create_zone(self):
        """Test case for create_zone

        Creates a new domain, returns the Zone on creation.  # noqa: E501
        """
        pass

    def test_delete_zone(self):
        """Test case for delete_zone

        Deletes this zone, all attached metadata and rrsets.  # noqa: E501
        """
        pass

    def test_list_zone(self):
        """Test case for list_zone

        zone managed by a server  # noqa: E501
        """
        pass

    def test_list_zones(self):
        """Test case for list_zones

        List all Zones in a server  # noqa: E501
        """
        pass

    def test_notify_zone(self):
        """Test case for notify_zone

        Send a DNS NOTIFY to all slaves.  # noqa: E501
        """
        pass

    def test_patch_zone(self):
        """Test case for patch_zone

        Creates/modifies/deletes RRsets present in the payload and their comments. Returns 204 No Content on success.  # noqa: E501
        """
        pass

    def test_put_zone(self):
        """Test case for put_zone

        Modifies basic zone data (metadata).  # noqa: E501
        """
        pass

    def test_rectify_zone(self):
        """Test case for rectify_zone

        Rectify the zone data.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
