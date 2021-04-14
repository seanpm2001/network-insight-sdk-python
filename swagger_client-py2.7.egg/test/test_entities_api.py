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
from swagger_client.apis.entities_api import EntitiesApi


class TestEntitiesApi(unittest.TestCase):
    """ EntitiesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.entities_api.EntitiesApi()

    def tearDown(self):
        pass

    def test_bulk_fetch_problem_events(self):
        """
        Test case for bulk_fetch_problem_events

        Get details of problem events
        """
        pass

    def test_bulk_fetch_vendor_info(self):
        """
        Test case for bulk_fetch_vendor_info

        Get Vendor Information of entities
        """
        pass

    def test_entities_fetch_post(self):
        """
        Test case for entities_fetch_post

        Get details of entities
        """
        pass

    def test_get_aws_account_manager(self):
        """
        Test case for get_aws_account_manager

        Show AWS Account manager details
        """
        pass

    def test_get_azure_subscription(self):
        """
        Test case for get_azure_subscription

        Show Microsoft Azure Subscription details
        """
        pass

    def test_get_cluster(self):
        """
        Test case for get_cluster

        Show cluster details
        """
        pass

    def test_get_datacenter(self):
        """
        Test case for get_datacenter

        Show vCenter datacenter details
        """
        pass

    def test_get_datastore(self):
        """
        Test case for get_datastore

        Show datastore details
        """
        pass

    def test_get_distributed_virtual_portgroup(self):
        """
        Test case for get_distributed_virtual_portgroup

        Show distributed virtual portgroup details
        """
        pass

    def test_get_distributed_virtual_switch(self):
        """
        Test case for get_distributed_virtual_switch

        Show distributed virtual switch details
        """
        pass

    def test_get_firewall(self):
        """
        Test case for get_firewall

        Show firewall details
        """
        pass

    def test_get_firewall_manager(self):
        """
        Test case for get_firewall_manager

        Show firewall manager details
        """
        pass

    def test_get_firewall_rule(self):
        """
        Test case for get_firewall_rule

        Show firewall rule details
        """
        pass

    def test_get_flow(self):
        """
        Test case for get_flow

        Show flow details
        """
        pass

    def test_get_flows(self):
        """
        Test case for get_flows

        List flows
        """
        pass

    def test_get_folder(self):
        """
        Test case for get_folder

        Show folder details
        """
        pass

    def test_get_host(self):
        """
        Test case for get_host

        Show host details
        """
        pass

    def test_get_ip_set(self):
        """
        Test case for get_ip_set

        Show NSX IP Set details
        """
        pass

    def test_get_kubernetes_service_by_id(self):
        """
        Test case for get_kubernetes_service_by_id

        Show Kubernetes service details
        """
        pass

    def test_get_kubernetes_services(self):
        """
        Test case for get_kubernetes_services

        List Kubernetes Services
        """
        pass

    def test_get_layer2_network(self):
        """
        Test case for get_layer2_network

        Show layer2 network details
        """
        pass

    def test_get_name(self):
        """
        Test case for get_name

        Get name of an entity
        """
        pass

    def test_get_names(self):
        """
        Test case for get_names

        Get names for entities
        """
        pass

    def test_get_nsx_manager(self):
        """
        Test case for get_nsx_manager

        Show NSX manager details
        """
        pass

    def test_get_problem_event(self):
        """
        Test case for get_problem_event

        Show problem details
        """
        pass

    def test_get_security_group(self):
        """
        Test case for get_security_group

        Show security group details
        """
        pass

    def test_get_security_tag(self):
        """
        Test case for get_security_tag

        Show security tag details
        """
        pass

    def test_get_service(self):
        """
        Test case for get_service

        Show service details
        """
        pass

    def test_get_service_group(self):
        """
        Test case for get_service_group

        Show service group details
        """
        pass

    def test_get_vcenter_manager(self):
        """
        Test case for get_vcenter_manager

        Show vCenter manager details
        """
        pass

    def test_get_vm(self):
        """
        Test case for get_vm

        Show VM details
        """
        pass

    def test_get_vmknic(self):
        """
        Test case for get_vmknic

        Show vmknic details
        """
        pass

    def test_get_vnic(self):
        """
        Test case for get_vnic

        Show vNIC details
        """
        pass

    def test_list_aws_account_managers(self):
        """
        Test case for list_aws_account_managers

        List AWS Account managers
        """
        pass

    def test_list_azure_subscription(self):
        """
        Test case for list_azure_subscription

        List Microsoft Azure Subscriptions
        """
        pass

    def test_list_clusters(self):
        """
        Test case for list_clusters

        List clusters
        """
        pass

    def test_list_datacenters(self):
        """
        Test case for list_datacenters

        List vCenter datacenters
        """
        pass

    def test_list_datastores(self):
        """
        Test case for list_datastores

        List datastores
        """
        pass

    def test_list_distributed_virtual_portgroups(self):
        """
        Test case for list_distributed_virtual_portgroups

        List distributed virtual portgroups
        """
        pass

    def test_list_distributed_virtual_switches(self):
        """
        Test case for list_distributed_virtual_switches

        List distributed virtual switches
        """
        pass

    def test_list_firewall_managers(self):
        """
        Test case for list_firewall_managers

        List firewall managers
        """
        pass

    def test_list_firewall_rules(self):
        """
        Test case for list_firewall_rules

        List firewall rules
        """
        pass

    def test_list_firewalls(self):
        """
        Test case for list_firewalls

        List firewalls
        """
        pass

    def test_list_folders(self):
        """
        Test case for list_folders

        List folders
        """
        pass

    def test_list_hosts(self):
        """
        Test case for list_hosts

        List hosts
        """
        pass

    def test_list_ip_sets(self):
        """
        Test case for list_ip_sets

        List NSX IP Sets
        """
        pass

    def test_list_layer2_networks(self):
        """
        Test case for list_layer2_networks

        List layer2 networks
        """
        pass

    def test_list_nsx_managers(self):
        """
        Test case for list_nsx_managers

        List NSX managers
        """
        pass

    def test_list_problem_events(self):
        """
        Test case for list_problem_events

        List problems
        """
        pass

    def test_list_security_groups(self):
        """
        Test case for list_security_groups

        List security groups
        """
        pass

    def test_list_security_tags(self):
        """
        Test case for list_security_tags

        List security tags
        """
        pass

    def test_list_service_groups(self):
        """
        Test case for list_service_groups

        List service groups
        """
        pass

    def test_list_services(self):
        """
        Test case for list_services

        List services
        """
        pass

    def test_list_vcenter_managers(self):
        """
        Test case for list_vcenter_managers

        List vCenter managers
        """
        pass

    def test_list_vmknics(self):
        """
        Test case for list_vmknics

        List vmknics
        """
        pass

    def test_list_vms(self):
        """
        Test case for list_vms

        List vms
        """
        pass

    def test_list_vnics(self):
        """
        Test case for list_vnics

        List vnics
        """
        pass


if __name__ == '__main__':
    unittest.main()
