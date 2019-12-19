# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class MicrosegmentationApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def export_nsx_recommended_rules(self, **kwargs):
        """
        Export recommended rules for NSX-V
        Export recommended firewall rules based on the flow data gathered by vRealize Network Insight in NSX-V compatible format
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export_nsx_recommended_rules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RecommendedRulesRequest body: NSX Recommended Rules Request
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.export_nsx_recommended_rules_with_http_info(**kwargs)
        else:
            (data) = self.export_nsx_recommended_rules_with_http_info(**kwargs)
            return data

    def export_nsx_recommended_rules_with_http_info(self, **kwargs):
        """
        Export recommended rules for NSX-V
        Export recommended firewall rules based on the flow data gathered by vRealize Network Insight in NSX-V compatible format
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.export_nsx_recommended_rules_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RecommendedRulesRequest body: NSX Recommended Rules Request
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export_nsx_recommended_rules" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/micro-seg/recommended-rules/nsx', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_recommended_rules(self, **kwargs):
        """
        Get logical recommended rules
        Get recommended firewall rules based on the flow data gathered by vRealize Network Insight. This API provides service to retrieve recommended rules based on flow traffic that is observed between two groups OR for a single group based on all the inbound and outboud traffic for that group. In case two groups are provided, both the groups should be of same type. Currently supported groups are Application, Tier, NSXSecurityGroup, EC2SecurityGroup.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_recommended_rules(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RecommendedRulesRequest body: Recommended Rules Request
        :return: RecommendedRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_recommended_rules_with_http_info(**kwargs)
        else:
            (data) = self.list_recommended_rules_with_http_info(**kwargs)
            return data

    def list_recommended_rules_with_http_info(self, **kwargs):
        """
        Get logical recommended rules
        Get recommended firewall rules based on the flow data gathered by vRealize Network Insight. This API provides service to retrieve recommended rules based on flow traffic that is observed between two groups OR for a single group based on all the inbound and outboud traffic for that group. In case two groups are provided, both the groups should be of same type. Currently supported groups are Application, Tier, NSXSecurityGroup, EC2SecurityGroup.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_recommended_rules_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RecommendedRulesRequest body: Recommended Rules Request
        :return: RecommendedRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_recommended_rules" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKeyAuth']

        return self.api_client.call_api('/micro-seg/recommended-rules', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RecommendedRules',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
