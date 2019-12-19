# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.microsegmentation_api import MicrosegmentationApi


class TestMicrosegmentationApi(unittest.TestCase):
    """ MicrosegmentationApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.microsegmentation_api.MicrosegmentationApi()

    def tearDown(self):
        pass

    def test_export_nsx_recommended_rules(self):
        """
        Test case for export_nsx_recommended_rules

        Export recommended rules for NSX-V
        """
        pass

    def test_list_recommended_rules(self):
        """
        Test case for list_recommended_rules

        Get logical recommended rules
        """
        pass


if __name__ == '__main__':
    unittest.main()
