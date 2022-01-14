# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.settings_api import SettingsApi


class TestSettingsApi(unittest.TestCase):
    """ SettingsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.settings_api.SettingsApi()

    def tearDown(self):
        pass

    def test_activate_serial_number(self):
        """
        Test case for activate_serial_number

        Activates a valid license key. This API is not applicable for on-boarding.
        """
        pass

    def test_add_backup_config(self):
        """
        Test case for add_backup_config

        Configure backup of configuration
        """
        pass

    def test_add_ip_tag(self):
        """
        Test case for add_ip_tag

        Tag IP addresses with tag-id
        """
        pass

    def test_add_login_banner(self):
        """
        Test case for add_login_banner

        Add new Login Banner in the system
        """
        pass

    def test_add_restore_config(self):
        """
        Test case for add_restore_config

        Configure restore of configuration and triggers restore operation
        """
        pass

    def test_add_search_based_alert_config(self):
        """
        Test case for add_search_based_alert_config

        Add a new Search Based Alert Configuration
        """
        pass

    def test_add_vidm_user(self):
        """
        Test case for add_vidm_user

        Add a VMware Identity manager user to vRealize Network Insight
        """
        pass

    def test_add_vidm_user_group(self):
        """
        Test case for add_vidm_user_group

        Add a VMware Identity Manager user-group to vRealize Network Insight
        """
        pass

    def test_add_web_proxy(self):
        """
        Test case for add_web_proxy

        Add new Web Proxy in the system
        """
        pass

    def test_create_subnet_mapping(self):
        """
        Test case for create_subnet_mapping

        Create subnet mapping
        """
        pass

    def test_create_subscriber(self):
        """
        Test case for create_subscriber

        Add 'Databus' subsciption
        """
        pass

    def test_create_user_defined_event(self):
        """
        Test case for create_user_defined_event

        Add new User-Defined event
        """
        pass

    def test_deactivate_serial_number(self):
        """
        Test case for deactivate_serial_number

        Deactivates an existing license key
        """
        pass

    def test_delete_backup_config(self):
        """
        Test case for delete_backup_config

        Delete existing Backup configuration
        """
        pass

    def test_delete_login_banner(self):
        """
        Test case for delete_login_banner

        Delete login banner from the system
        """
        pass

    def test_delete_restore_config(self):
        """
        Test case for delete_restore_config

        Delete existing restore configuration
        """
        pass

    def test_delete_search_based_alert_config(self):
        """
        Test case for delete_search_based_alert_config

        Delete an existing Search Based Alert Configuration.
        """
        pass

    def test_delete_subnet_mapping(self):
        """
        Test case for delete_subnet_mapping

        Delete subnet mapping
        """
        pass

    def test_delete_subscriber(self):
        """
        Test case for delete_subscriber

        Delete a 'Databus' subscription
        """
        pass

    def test_delete_user(self):
        """
        Test case for delete_user

        Delete an existing user.
        """
        pass

    def test_delete_user_defined_event(self):
        """
        Test case for delete_user_defined_event

        Delete an existing User-Defined event
        """
        pass

    def test_delete_user_group(self):
        """
        Test case for delete_user_group

        Delete an existing user-group
        """
        pass

    def test_delete_vidm_configuration(self):
        """
        Test case for delete_vidm_configuration

        Delete VMware Identity Manager configuration
        """
        pass

    def test_delete_web_proxy(self):
        """
        Test case for delete_web_proxy

        Delete an existing Web Proxy server
        """
        pass

    def test_disable_search_based_alert_config(self):
        """
        Test case for disable_search_based_alert_config

        Disable an existing Search Based Alert Configuration.
        """
        pass

    def test_disable_user_defined_event(self):
        """
        Test case for disable_user_defined_event

        Disable an existing User-Defined event
        """
        pass

    def test_disable_vidm(self):
        """
        Test case for disable_vidm

        Disable VMware Identity Manager integration
        """
        pass

    def test_enable_search_based_alert_config(self):
        """
        Test case for enable_search_based_alert_config

        Enable an existing Search Based Alert Configuration
        """
        pass

    def test_enable_user_defined_event(self):
        """
        Test case for enable_user_defined_event

        Enable an existing User-Defined event
        """
        pass

    def test_enable_vidm(self):
        """
        Test case for enable_vidm

        Enable VMware Identity Manager integration
        """
        pass

    def test_get_all_search_based_alert_configs(self):
        """
        Test case for get_all_search_based_alert_configs

        List all Search Based Alert Configurations.
        """
        pass

    def test_get_all_subscriber(self):
        """
        Test case for get_all_subscriber

        Get the list of 'Databus' subscriptions
        """
        pass

    def test_get_all_user_defined_events(self):
        """
        Test case for get_all_user_defined_events

        List the created User Defined Event defintions.
        """
        pass

    def test_get_all_users(self):
        """
        Test case for get_all_users

        List all the users
        """
        pass

    def test_get_backup_config(self):
        """
        Test case for get_backup_config

        Get Backup configuration
        """
        pass

    def test_get_backup_status_report(self):
        """
        Test case for get_backup_status_report

        Get currently running or last Backup job status
        """
        pass

    def test_get_certificate(self):
        """
        Test case for get_certificate

        Get certificate for given url
        """
        pass

    def test_get_connected_clients_to_web_proxy(self):
        """
        Test case for get_connected_clients_to_web_proxy

        Get details of connected clients to Web Proxy Server
        """
        pass

    def test_get_infra_nodes_web_proxy(self):
        """
        Test case for get_infra_nodes_web_proxy

        Get details of web proxy config associated with infra nodes
        """
        pass

    def test_get_ip_tag(self):
        """
        Test case for get_ip_tag

        Show IP tag details
        """
        pass

    def test_get_ip_tag_ids(self):
        """
        Test case for get_ip_tag_ids

        Show IP tag IDs
        """
        pass

    def test_get_licenses(self):
        """
        Test case for get_licenses

        Get current licensing and license usage information
        """
        pass

    def test_get_login_banner(self):
        """
        Test case for get_login_banner

        Get Login banner
        """
        pass

    def test_get_restore_config(self):
        """
        Test case for get_restore_config

        Get Restore configuration
        """
        pass

    def test_get_restore_status_report(self):
        """
        Test case for get_restore_status_report

        Get currently running or last Restore job status
        """
        pass

    def test_get_search_based_alert_config(self):
        """
        Test case for get_search_based_alert_config

        Get details of an existing Search Based Alert Configuration.
        """
        pass

    def test_get_subnet_mappings(self):
        """
        Test case for get_subnet_mappings

        Get all subnet mappings
        """
        pass

    def test_get_subscriber(self):
        """
        Test case for get_subscriber

        Retrieve a 'Databus' subscriptions
        """
        pass

    def test_get_user(self):
        """
        Test case for get_user

        Get details of a user
        """
        pass

    def test_get_user_defined_event(self):
        """
        Test case for get_user_defined_event

        Get details of an existing User-Defined event.
        """
        pass

    def test_get_user_group(self):
        """
        Test case for get_user_group

        Get details of a user-group
        """
        pass

    def test_get_user_groups(self):
        """
        Test case for get_user_groups

        List user-groups
        """
        pass

    def test_get_users(self):
        """
        Test case for get_users

        List the users
        """
        pass

    def test_get_vidm_configuration(self):
        """
        Test case for get_vidm_configuration

        Get configuration details of VMware Identity Manager
        """
        pass

    def test_get_web_proxies(self):
        """
        Test case for get_web_proxies

        List of configured web proxy servers
        """
        pass

    def test_get_web_proxy(self):
        """
        Test case for get_web_proxy

        Get details of an existing Web Proxy Server
        """
        pass

    def test_remove_ip_tag(self):
        """
        Test case for remove_ip_tag

        Remove tag from IP addresses
        """
        pass

    def test_save_vidm_configuration(self):
        """
        Test case for save_vidm_configuration

        Configure VMware Identity Manager
        """
        pass

    def test_settings_snmp_profiles_get(self):
        """
        Test case for settings_snmp_profiles_get

        List the configured SNMP Trap destination profiles
        """
        pass

    def test_settings_snmp_profiles_id_delete(self):
        """
        Test case for settings_snmp_profiles_id_delete

        Delete an existing SNMP Trap destination profile
        """
        pass

    def test_settings_snmp_profiles_id_get(self):
        """
        Test case for settings_snmp_profiles_id_get

        Get details of an existing SNMP destination profile
        """
        pass

    def test_settings_snmp_profiles_id_migrate_events_post(self):
        """
        Test case for settings_snmp_profiles_id_migrate_events_post

        Migrate event subscriptions to other SNMP Trap destination profiles
        """
        pass

    def test_settings_snmp_profiles_id_put(self):
        """
        Test case for settings_snmp_profiles_id_put

        Update an existing SNMP destination profile
        """
        pass

    def test_settings_snmp_profiles_post(self):
        """
        Test case for settings_snmp_profiles_post

        Add new SNMP Trap destination profile
        """
        pass

    def test_settings_snmp_profiles_send_test_trap_post(self):
        """
        Test case for settings_snmp_profiles_send_test_trap_post

        Send Test trap to SNMP destination profile
        """
        pass

    def test_settings_users_password_put(self):
        """
        Test case for settings_users_password_put

        Update user password
        """
        pass

    def test_update_backup_config(self):
        """
        Test case for update_backup_config

        Update Backup configuration
        """
        pass

    def test_update_login_banner(self):
        """
        Test case for update_login_banner

        Edit login banner details in the system
        """
        pass

    def test_update_search_based_alert_config(self):
        """
        Test case for update_search_based_alert_config

        Update an existing Search Based Alert Configuration.
        """
        pass

    def test_update_subnet_mapping(self):
        """
        Test case for update_subnet_mapping

        Update subnet mapping
        """
        pass

    def test_update_subscriber(self):
        """
        Test case for update_subscriber

        Update 'Databus' subsciption
        """
        pass

    def test_update_user_defined_event(self):
        """
        Test case for update_user_defined_event

        Update an existing User-Defined event.
        """
        pass

    def test_update_vidm_configuration(self):
        """
        Test case for update_vidm_configuration

        Update VMware Identity Manager configuration
        """
        pass

    def test_update_vidm_user_group_role(self):
        """
        Test case for update_vidm_user_group_role

        Update role for user-group mapped through VMware Identity Manager
        """
        pass

    def test_update_vidm_user_role(self):
        """
        Test case for update_vidm_user_role

        Update role for user mapped through VMware Identity Manager
        """
        pass

    def test_update_web_proxy(self):
        """
        Test case for update_web_proxy

        Update the existing web proxy server
        """
        pass

    def test_validate_connections_via_web_proxy(self):
        """
        Test case for validate_connections_via_web_proxy

        Validate the connections via web proxy
        """
        pass

    def test_validate_serial_number(self):
        """
        Test case for validate_serial_number

        Validates license key
        """
        pass

    def test_validate_web_proxy_migration(self):
        """
        Test case for validate_web_proxy_migration

        Validate the connections when migrating from one web proxy to another
        """
        pass


if __name__ == '__main__':
    unittest.main()
