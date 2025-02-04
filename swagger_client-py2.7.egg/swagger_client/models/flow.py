# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Flow(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_id': 'str',
        'name': 'str',
        'entity_type': 'EntityType',
        'source_vm': 'Reference',
        'destination_vm': 'Reference',
        'source_vnic': 'Reference',
        'destination_vnic': 'Reference',
        'source_vpc': 'Reference',
        'destination_vpc': 'Reference',
        'source_cloud_network': 'Reference',
        'destination_cloud_network': 'Reference',
        'source_azure_nsg': 'Reference',
        'destination_azure_nsg': 'Reference',
        'source_datacenter': 'Reference',
        'destination_datacenter': 'Reference',
        'source_ip': 'IpV4Address',
        'destination_ip': 'IpV4Address',
        'source_l2_network': 'Reference',
        'destination_l2_network': 'Reference',
        'port': 'PortRange',
        'source_folders': 'list[Reference]',
        'destination_folders': 'list[Reference]',
        'source_resource_pool': 'Reference',
        'destination_resource_pool': 'Reference',
        'source_cluster': 'Reference',
        'destination_cluster': 'Reference',
        'protocol': 'Protocol',
        'source_ip_sets': 'list[Reference]',
        'destination_ip_sets': 'list[Reference]',
        'source_security_groups': 'list[Reference]',
        'destination_security_groups': 'list[Reference]',
        'traffic_type': 'FlowTrafficType',
        'source_security_tags': 'list[Reference]',
        'destination_security_tags': 'list[Reference]',
        'source_host': 'Reference',
        'destination_host': 'Reference',
        'source_vm_tags': 'list[str]',
        'destination_vm_tags': 'list[str]',
        'within_host': 'bool',
        'firewall_action': 'FirewallAction',
        'firewall_rule_id': 'str',
        'flow_tag': 'list[FlowTag]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'source_vm': 'source_vm',
        'destination_vm': 'destination_vm',
        'source_vnic': 'source_vnic',
        'destination_vnic': 'destination_vnic',
        'source_vpc': 'source_vpc',
        'destination_vpc': 'destination_vpc',
        'source_cloud_network': 'source_cloud_network',
        'destination_cloud_network': 'destination_cloud_network',
        'source_azure_nsg': 'source_azure_nsg',
        'destination_azure_nsg': 'destination_azure_nsg',
        'source_datacenter': 'source_datacenter',
        'destination_datacenter': 'destination_datacenter',
        'source_ip': 'source_ip',
        'destination_ip': 'destination_ip',
        'source_l2_network': 'source_l2_network',
        'destination_l2_network': 'destination_l2_network',
        'port': 'port',
        'source_folders': 'source_folders',
        'destination_folders': 'destination_folders',
        'source_resource_pool': 'source_resource_pool',
        'destination_resource_pool': 'destination_resource_pool',
        'source_cluster': 'source_cluster',
        'destination_cluster': 'destination_cluster',
        'protocol': 'protocol',
        'source_ip_sets': 'source_ip_sets',
        'destination_ip_sets': 'destination_ip_sets',
        'source_security_groups': 'source_security_groups',
        'destination_security_groups': 'destination_security_groups',
        'traffic_type': 'traffic_type',
        'source_security_tags': 'source_security_tags',
        'destination_security_tags': 'destination_security_tags',
        'source_host': 'source_host',
        'destination_host': 'destination_host',
        'source_vm_tags': 'source_vm_tags',
        'destination_vm_tags': 'destination_vm_tags',
        'within_host': 'within_host',
        'firewall_action': 'firewall_action',
        'firewall_rule_id': 'firewall_rule_id',
        'flow_tag': 'flow_tag'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, source_vm=None, destination_vm=None, source_vnic=None, destination_vnic=None, source_vpc=None, destination_vpc=None, source_cloud_network=None, destination_cloud_network=None, source_azure_nsg=None, destination_azure_nsg=None, source_datacenter=None, destination_datacenter=None, source_ip=None, destination_ip=None, source_l2_network=None, destination_l2_network=None, port=None, source_folders=None, destination_folders=None, source_resource_pool=None, destination_resource_pool=None, source_cluster=None, destination_cluster=None, protocol=None, source_ip_sets=None, destination_ip_sets=None, source_security_groups=None, destination_security_groups=None, traffic_type=None, source_security_tags=None, destination_security_tags=None, source_host=None, destination_host=None, source_vm_tags=None, destination_vm_tags=None, within_host=None, firewall_action=None, firewall_rule_id=None, flow_tag=None):
        """
        Flow - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._source_vm = None
        self._destination_vm = None
        self._source_vnic = None
        self._destination_vnic = None
        self._source_vpc = None
        self._destination_vpc = None
        self._source_cloud_network = None
        self._destination_cloud_network = None
        self._source_azure_nsg = None
        self._destination_azure_nsg = None
        self._source_datacenter = None
        self._destination_datacenter = None
        self._source_ip = None
        self._destination_ip = None
        self._source_l2_network = None
        self._destination_l2_network = None
        self._port = None
        self._source_folders = None
        self._destination_folders = None
        self._source_resource_pool = None
        self._destination_resource_pool = None
        self._source_cluster = None
        self._destination_cluster = None
        self._protocol = None
        self._source_ip_sets = None
        self._destination_ip_sets = None
        self._source_security_groups = None
        self._destination_security_groups = None
        self._traffic_type = None
        self._source_security_tags = None
        self._destination_security_tags = None
        self._source_host = None
        self._destination_host = None
        self._source_vm_tags = None
        self._destination_vm_tags = None
        self._within_host = None
        self._firewall_action = None
        self._firewall_rule_id = None
        self._flow_tag = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if source_vm is not None:
          self.source_vm = source_vm
        if destination_vm is not None:
          self.destination_vm = destination_vm
        if source_vnic is not None:
          self.source_vnic = source_vnic
        if destination_vnic is not None:
          self.destination_vnic = destination_vnic
        if source_vpc is not None:
          self.source_vpc = source_vpc
        if destination_vpc is not None:
          self.destination_vpc = destination_vpc
        if source_cloud_network is not None:
          self.source_cloud_network = source_cloud_network
        if destination_cloud_network is not None:
          self.destination_cloud_network = destination_cloud_network
        if source_azure_nsg is not None:
          self.source_azure_nsg = source_azure_nsg
        if destination_azure_nsg is not None:
          self.destination_azure_nsg = destination_azure_nsg
        if source_datacenter is not None:
          self.source_datacenter = source_datacenter
        if destination_datacenter is not None:
          self.destination_datacenter = destination_datacenter
        if source_ip is not None:
          self.source_ip = source_ip
        if destination_ip is not None:
          self.destination_ip = destination_ip
        if source_l2_network is not None:
          self.source_l2_network = source_l2_network
        if destination_l2_network is not None:
          self.destination_l2_network = destination_l2_network
        if port is not None:
          self.port = port
        if source_folders is not None:
          self.source_folders = source_folders
        if destination_folders is not None:
          self.destination_folders = destination_folders
        if source_resource_pool is not None:
          self.source_resource_pool = source_resource_pool
        if destination_resource_pool is not None:
          self.destination_resource_pool = destination_resource_pool
        if source_cluster is not None:
          self.source_cluster = source_cluster
        if destination_cluster is not None:
          self.destination_cluster = destination_cluster
        if protocol is not None:
          self.protocol = protocol
        if source_ip_sets is not None:
          self.source_ip_sets = source_ip_sets
        if destination_ip_sets is not None:
          self.destination_ip_sets = destination_ip_sets
        if source_security_groups is not None:
          self.source_security_groups = source_security_groups
        if destination_security_groups is not None:
          self.destination_security_groups = destination_security_groups
        if traffic_type is not None:
          self.traffic_type = traffic_type
        if source_security_tags is not None:
          self.source_security_tags = source_security_tags
        if destination_security_tags is not None:
          self.destination_security_tags = destination_security_tags
        if source_host is not None:
          self.source_host = source_host
        if destination_host is not None:
          self.destination_host = destination_host
        if source_vm_tags is not None:
          self.source_vm_tags = source_vm_tags
        if destination_vm_tags is not None:
          self.destination_vm_tags = destination_vm_tags
        if within_host is not None:
          self.within_host = within_host
        if firewall_action is not None:
          self.firewall_action = firewall_action
        if firewall_rule_id is not None:
          self.firewall_rule_id = firewall_rule_id
        if flow_tag is not None:
          self.flow_tag = flow_tag

    @property
    def entity_id(self):
        """
        Gets the entity_id of this Flow.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this Flow.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this Flow.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this Flow.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this Flow.
        Name of the object

        :return: The name of this Flow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Flow.
        Name of the object

        :param name: The name of this Flow.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this Flow.

        :return: The entity_type of this Flow.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Flow.

        :param entity_type: The entity_type of this Flow.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def source_vm(self):
        """
        Gets the source_vm of this Flow.

        :return: The source_vm of this Flow.
        :rtype: Reference
        """
        return self._source_vm

    @source_vm.setter
    def source_vm(self, source_vm):
        """
        Sets the source_vm of this Flow.

        :param source_vm: The source_vm of this Flow.
        :type: Reference
        """

        self._source_vm = source_vm

    @property
    def destination_vm(self):
        """
        Gets the destination_vm of this Flow.

        :return: The destination_vm of this Flow.
        :rtype: Reference
        """
        return self._destination_vm

    @destination_vm.setter
    def destination_vm(self, destination_vm):
        """
        Sets the destination_vm of this Flow.

        :param destination_vm: The destination_vm of this Flow.
        :type: Reference
        """

        self._destination_vm = destination_vm

    @property
    def source_vnic(self):
        """
        Gets the source_vnic of this Flow.

        :return: The source_vnic of this Flow.
        :rtype: Reference
        """
        return self._source_vnic

    @source_vnic.setter
    def source_vnic(self, source_vnic):
        """
        Sets the source_vnic of this Flow.

        :param source_vnic: The source_vnic of this Flow.
        :type: Reference
        """

        self._source_vnic = source_vnic

    @property
    def destination_vnic(self):
        """
        Gets the destination_vnic of this Flow.

        :return: The destination_vnic of this Flow.
        :rtype: Reference
        """
        return self._destination_vnic

    @destination_vnic.setter
    def destination_vnic(self, destination_vnic):
        """
        Sets the destination_vnic of this Flow.

        :param destination_vnic: The destination_vnic of this Flow.
        :type: Reference
        """

        self._destination_vnic = destination_vnic

    @property
    def source_vpc(self):
        """
        Gets the source_vpc of this Flow.

        :return: The source_vpc of this Flow.
        :rtype: Reference
        """
        return self._source_vpc

    @source_vpc.setter
    def source_vpc(self, source_vpc):
        """
        Sets the source_vpc of this Flow.

        :param source_vpc: The source_vpc of this Flow.
        :type: Reference
        """

        self._source_vpc = source_vpc

    @property
    def destination_vpc(self):
        """
        Gets the destination_vpc of this Flow.

        :return: The destination_vpc of this Flow.
        :rtype: Reference
        """
        return self._destination_vpc

    @destination_vpc.setter
    def destination_vpc(self, destination_vpc):
        """
        Sets the destination_vpc of this Flow.

        :param destination_vpc: The destination_vpc of this Flow.
        :type: Reference
        """

        self._destination_vpc = destination_vpc

    @property
    def source_cloud_network(self):
        """
        Gets the source_cloud_network of this Flow.

        :return: The source_cloud_network of this Flow.
        :rtype: Reference
        """
        return self._source_cloud_network

    @source_cloud_network.setter
    def source_cloud_network(self, source_cloud_network):
        """
        Sets the source_cloud_network of this Flow.

        :param source_cloud_network: The source_cloud_network of this Flow.
        :type: Reference
        """

        self._source_cloud_network = source_cloud_network

    @property
    def destination_cloud_network(self):
        """
        Gets the destination_cloud_network of this Flow.

        :return: The destination_cloud_network of this Flow.
        :rtype: Reference
        """
        return self._destination_cloud_network

    @destination_cloud_network.setter
    def destination_cloud_network(self, destination_cloud_network):
        """
        Sets the destination_cloud_network of this Flow.

        :param destination_cloud_network: The destination_cloud_network of this Flow.
        :type: Reference
        """

        self._destination_cloud_network = destination_cloud_network

    @property
    def source_azure_nsg(self):
        """
        Gets the source_azure_nsg of this Flow.

        :return: The source_azure_nsg of this Flow.
        :rtype: Reference
        """
        return self._source_azure_nsg

    @source_azure_nsg.setter
    def source_azure_nsg(self, source_azure_nsg):
        """
        Sets the source_azure_nsg of this Flow.

        :param source_azure_nsg: The source_azure_nsg of this Flow.
        :type: Reference
        """

        self._source_azure_nsg = source_azure_nsg

    @property
    def destination_azure_nsg(self):
        """
        Gets the destination_azure_nsg of this Flow.

        :return: The destination_azure_nsg of this Flow.
        :rtype: Reference
        """
        return self._destination_azure_nsg

    @destination_azure_nsg.setter
    def destination_azure_nsg(self, destination_azure_nsg):
        """
        Sets the destination_azure_nsg of this Flow.

        :param destination_azure_nsg: The destination_azure_nsg of this Flow.
        :type: Reference
        """

        self._destination_azure_nsg = destination_azure_nsg

    @property
    def source_datacenter(self):
        """
        Gets the source_datacenter of this Flow.

        :return: The source_datacenter of this Flow.
        :rtype: Reference
        """
        return self._source_datacenter

    @source_datacenter.setter
    def source_datacenter(self, source_datacenter):
        """
        Sets the source_datacenter of this Flow.

        :param source_datacenter: The source_datacenter of this Flow.
        :type: Reference
        """

        self._source_datacenter = source_datacenter

    @property
    def destination_datacenter(self):
        """
        Gets the destination_datacenter of this Flow.

        :return: The destination_datacenter of this Flow.
        :rtype: Reference
        """
        return self._destination_datacenter

    @destination_datacenter.setter
    def destination_datacenter(self, destination_datacenter):
        """
        Sets the destination_datacenter of this Flow.

        :param destination_datacenter: The destination_datacenter of this Flow.
        :type: Reference
        """

        self._destination_datacenter = destination_datacenter

    @property
    def source_ip(self):
        """
        Gets the source_ip of this Flow.

        :return: The source_ip of this Flow.
        :rtype: IpV4Address
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """
        Sets the source_ip of this Flow.

        :param source_ip: The source_ip of this Flow.
        :type: IpV4Address
        """

        self._source_ip = source_ip

    @property
    def destination_ip(self):
        """
        Gets the destination_ip of this Flow.

        :return: The destination_ip of this Flow.
        :rtype: IpV4Address
        """
        return self._destination_ip

    @destination_ip.setter
    def destination_ip(self, destination_ip):
        """
        Sets the destination_ip of this Flow.

        :param destination_ip: The destination_ip of this Flow.
        :type: IpV4Address
        """

        self._destination_ip = destination_ip

    @property
    def source_l2_network(self):
        """
        Gets the source_l2_network of this Flow.

        :return: The source_l2_network of this Flow.
        :rtype: Reference
        """
        return self._source_l2_network

    @source_l2_network.setter
    def source_l2_network(self, source_l2_network):
        """
        Sets the source_l2_network of this Flow.

        :param source_l2_network: The source_l2_network of this Flow.
        :type: Reference
        """

        self._source_l2_network = source_l2_network

    @property
    def destination_l2_network(self):
        """
        Gets the destination_l2_network of this Flow.

        :return: The destination_l2_network of this Flow.
        :rtype: Reference
        """
        return self._destination_l2_network

    @destination_l2_network.setter
    def destination_l2_network(self, destination_l2_network):
        """
        Sets the destination_l2_network of this Flow.

        :param destination_l2_network: The destination_l2_network of this Flow.
        :type: Reference
        """

        self._destination_l2_network = destination_l2_network

    @property
    def port(self):
        """
        Gets the port of this Flow.

        :return: The port of this Flow.
        :rtype: PortRange
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Flow.

        :param port: The port of this Flow.
        :type: PortRange
        """

        self._port = port

    @property
    def source_folders(self):
        """
        Gets the source_folders of this Flow.

        :return: The source_folders of this Flow.
        :rtype: list[Reference]
        """
        return self._source_folders

    @source_folders.setter
    def source_folders(self, source_folders):
        """
        Sets the source_folders of this Flow.

        :param source_folders: The source_folders of this Flow.
        :type: list[Reference]
        """

        self._source_folders = source_folders

    @property
    def destination_folders(self):
        """
        Gets the destination_folders of this Flow.

        :return: The destination_folders of this Flow.
        :rtype: list[Reference]
        """
        return self._destination_folders

    @destination_folders.setter
    def destination_folders(self, destination_folders):
        """
        Sets the destination_folders of this Flow.

        :param destination_folders: The destination_folders of this Flow.
        :type: list[Reference]
        """

        self._destination_folders = destination_folders

    @property
    def source_resource_pool(self):
        """
        Gets the source_resource_pool of this Flow.

        :return: The source_resource_pool of this Flow.
        :rtype: Reference
        """
        return self._source_resource_pool

    @source_resource_pool.setter
    def source_resource_pool(self, source_resource_pool):
        """
        Sets the source_resource_pool of this Flow.

        :param source_resource_pool: The source_resource_pool of this Flow.
        :type: Reference
        """

        self._source_resource_pool = source_resource_pool

    @property
    def destination_resource_pool(self):
        """
        Gets the destination_resource_pool of this Flow.

        :return: The destination_resource_pool of this Flow.
        :rtype: Reference
        """
        return self._destination_resource_pool

    @destination_resource_pool.setter
    def destination_resource_pool(self, destination_resource_pool):
        """
        Sets the destination_resource_pool of this Flow.

        :param destination_resource_pool: The destination_resource_pool of this Flow.
        :type: Reference
        """

        self._destination_resource_pool = destination_resource_pool

    @property
    def source_cluster(self):
        """
        Gets the source_cluster of this Flow.

        :return: The source_cluster of this Flow.
        :rtype: Reference
        """
        return self._source_cluster

    @source_cluster.setter
    def source_cluster(self, source_cluster):
        """
        Sets the source_cluster of this Flow.

        :param source_cluster: The source_cluster of this Flow.
        :type: Reference
        """

        self._source_cluster = source_cluster

    @property
    def destination_cluster(self):
        """
        Gets the destination_cluster of this Flow.

        :return: The destination_cluster of this Flow.
        :rtype: Reference
        """
        return self._destination_cluster

    @destination_cluster.setter
    def destination_cluster(self, destination_cluster):
        """
        Sets the destination_cluster of this Flow.

        :param destination_cluster: The destination_cluster of this Flow.
        :type: Reference
        """

        self._destination_cluster = destination_cluster

    @property
    def protocol(self):
        """
        Gets the protocol of this Flow.

        :return: The protocol of this Flow.
        :rtype: Protocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this Flow.

        :param protocol: The protocol of this Flow.
        :type: Protocol
        """

        self._protocol = protocol

    @property
    def source_ip_sets(self):
        """
        Gets the source_ip_sets of this Flow.

        :return: The source_ip_sets of this Flow.
        :rtype: list[Reference]
        """
        return self._source_ip_sets

    @source_ip_sets.setter
    def source_ip_sets(self, source_ip_sets):
        """
        Sets the source_ip_sets of this Flow.

        :param source_ip_sets: The source_ip_sets of this Flow.
        :type: list[Reference]
        """

        self._source_ip_sets = source_ip_sets

    @property
    def destination_ip_sets(self):
        """
        Gets the destination_ip_sets of this Flow.

        :return: The destination_ip_sets of this Flow.
        :rtype: list[Reference]
        """
        return self._destination_ip_sets

    @destination_ip_sets.setter
    def destination_ip_sets(self, destination_ip_sets):
        """
        Sets the destination_ip_sets of this Flow.

        :param destination_ip_sets: The destination_ip_sets of this Flow.
        :type: list[Reference]
        """

        self._destination_ip_sets = destination_ip_sets

    @property
    def source_security_groups(self):
        """
        Gets the source_security_groups of this Flow.

        :return: The source_security_groups of this Flow.
        :rtype: list[Reference]
        """
        return self._source_security_groups

    @source_security_groups.setter
    def source_security_groups(self, source_security_groups):
        """
        Sets the source_security_groups of this Flow.

        :param source_security_groups: The source_security_groups of this Flow.
        :type: list[Reference]
        """

        self._source_security_groups = source_security_groups

    @property
    def destination_security_groups(self):
        """
        Gets the destination_security_groups of this Flow.

        :return: The destination_security_groups of this Flow.
        :rtype: list[Reference]
        """
        return self._destination_security_groups

    @destination_security_groups.setter
    def destination_security_groups(self, destination_security_groups):
        """
        Sets the destination_security_groups of this Flow.

        :param destination_security_groups: The destination_security_groups of this Flow.
        :type: list[Reference]
        """

        self._destination_security_groups = destination_security_groups

    @property
    def traffic_type(self):
        """
        Gets the traffic_type of this Flow.

        :return: The traffic_type of this Flow.
        :rtype: FlowTrafficType
        """
        return self._traffic_type

    @traffic_type.setter
    def traffic_type(self, traffic_type):
        """
        Sets the traffic_type of this Flow.

        :param traffic_type: The traffic_type of this Flow.
        :type: FlowTrafficType
        """

        self._traffic_type = traffic_type

    @property
    def source_security_tags(self):
        """
        Gets the source_security_tags of this Flow.

        :return: The source_security_tags of this Flow.
        :rtype: list[Reference]
        """
        return self._source_security_tags

    @source_security_tags.setter
    def source_security_tags(self, source_security_tags):
        """
        Sets the source_security_tags of this Flow.

        :param source_security_tags: The source_security_tags of this Flow.
        :type: list[Reference]
        """

        self._source_security_tags = source_security_tags

    @property
    def destination_security_tags(self):
        """
        Gets the destination_security_tags of this Flow.

        :return: The destination_security_tags of this Flow.
        :rtype: list[Reference]
        """
        return self._destination_security_tags

    @destination_security_tags.setter
    def destination_security_tags(self, destination_security_tags):
        """
        Sets the destination_security_tags of this Flow.

        :param destination_security_tags: The destination_security_tags of this Flow.
        :type: list[Reference]
        """

        self._destination_security_tags = destination_security_tags

    @property
    def source_host(self):
        """
        Gets the source_host of this Flow.

        :return: The source_host of this Flow.
        :rtype: Reference
        """
        return self._source_host

    @source_host.setter
    def source_host(self, source_host):
        """
        Sets the source_host of this Flow.

        :param source_host: The source_host of this Flow.
        :type: Reference
        """

        self._source_host = source_host

    @property
    def destination_host(self):
        """
        Gets the destination_host of this Flow.

        :return: The destination_host of this Flow.
        :rtype: Reference
        """
        return self._destination_host

    @destination_host.setter
    def destination_host(self, destination_host):
        """
        Sets the destination_host of this Flow.

        :param destination_host: The destination_host of this Flow.
        :type: Reference
        """

        self._destination_host = destination_host

    @property
    def source_vm_tags(self):
        """
        Gets the source_vm_tags of this Flow.

        :return: The source_vm_tags of this Flow.
        :rtype: list[str]
        """
        return self._source_vm_tags

    @source_vm_tags.setter
    def source_vm_tags(self, source_vm_tags):
        """
        Sets the source_vm_tags of this Flow.

        :param source_vm_tags: The source_vm_tags of this Flow.
        :type: list[str]
        """

        self._source_vm_tags = source_vm_tags

    @property
    def destination_vm_tags(self):
        """
        Gets the destination_vm_tags of this Flow.

        :return: The destination_vm_tags of this Flow.
        :rtype: list[str]
        """
        return self._destination_vm_tags

    @destination_vm_tags.setter
    def destination_vm_tags(self, destination_vm_tags):
        """
        Sets the destination_vm_tags of this Flow.

        :param destination_vm_tags: The destination_vm_tags of this Flow.
        :type: list[str]
        """

        self._destination_vm_tags = destination_vm_tags

    @property
    def within_host(self):
        """
        Gets the within_host of this Flow.

        :return: The within_host of this Flow.
        :rtype: bool
        """
        return self._within_host

    @within_host.setter
    def within_host(self, within_host):
        """
        Sets the within_host of this Flow.

        :param within_host: The within_host of this Flow.
        :type: bool
        """

        self._within_host = within_host

    @property
    def firewall_action(self):
        """
        Gets the firewall_action of this Flow.

        :return: The firewall_action of this Flow.
        :rtype: FirewallAction
        """
        return self._firewall_action

    @firewall_action.setter
    def firewall_action(self, firewall_action):
        """
        Sets the firewall_action of this Flow.

        :param firewall_action: The firewall_action of this Flow.
        :type: FirewallAction
        """

        self._firewall_action = firewall_action

    @property
    def firewall_rule_id(self):
        """
        Gets the firewall_rule_id of this Flow.

        :return: The firewall_rule_id of this Flow.
        :rtype: str
        """
        return self._firewall_rule_id

    @firewall_rule_id.setter
    def firewall_rule_id(self, firewall_rule_id):
        """
        Sets the firewall_rule_id of this Flow.

        :param firewall_rule_id: The firewall_rule_id of this Flow.
        :type: str
        """

        self._firewall_rule_id = firewall_rule_id

    @property
    def flow_tag(self):
        """
        Gets the flow_tag of this Flow.

        :return: The flow_tag of this Flow.
        :rtype: list[FlowTag]
        """
        return self._flow_tag

    @flow_tag.setter
    def flow_tag(self, flow_tag):
        """
        Sets the flow_tag of this Flow.

        :param flow_tag: The flow_tag of this Flow.
        :type: list[FlowTag]
        """

        self._flow_tag = flow_tag

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Flow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
