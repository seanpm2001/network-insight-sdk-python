# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.path_api import PathApi


class TestPathApi(unittest.TestCase):
    """ PathApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.path_api.PathApi()

    def tearDown(self):
        pass

    def test_path_firewall_rules(self):
        """
        Test case for path_firewall_rules

        Get firewall rules for specified client server ips and port/protocol
        """
        pass


if __name__ == '__main__':
    unittest.main()
