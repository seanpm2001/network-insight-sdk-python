# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EC2Instance(object):
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
        'ip_addresses': 'list[IpV4Address]',
        'default_gateway': 'str',
        'vnics': 'list[Reference]',
        'security_groups': 'list[Reference]',
        'source_firewall_rules': 'list[RuleSet]',
        'destination_firewall_rules': 'list[RuleSet]',
        'ip_sets': 'list[Reference]',
        'vpc': 'Reference',
        'region': 'str',
        'account': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'ip_addresses': 'ip_addresses',
        'default_gateway': 'default_gateway',
        'vnics': 'vnics',
        'security_groups': 'security_groups',
        'source_firewall_rules': 'source_firewall_rules',
        'destination_firewall_rules': 'destination_firewall_rules',
        'ip_sets': 'ip_sets',
        'vpc': 'vpc',
        'region': 'region',
        'account': 'account'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, ip_addresses=None, default_gateway=None, vnics=None, security_groups=None, source_firewall_rules=None, destination_firewall_rules=None, ip_sets=None, vpc=None, region=None, account=None):
        """
        EC2Instance - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._ip_addresses = None
        self._default_gateway = None
        self._vnics = None
        self._security_groups = None
        self._source_firewall_rules = None
        self._destination_firewall_rules = None
        self._ip_sets = None
        self._vpc = None
        self._region = None
        self._account = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if ip_addresses is not None:
          self.ip_addresses = ip_addresses
        if default_gateway is not None:
          self.default_gateway = default_gateway
        if vnics is not None:
          self.vnics = vnics
        if security_groups is not None:
          self.security_groups = security_groups
        if source_firewall_rules is not None:
          self.source_firewall_rules = source_firewall_rules
        if destination_firewall_rules is not None:
          self.destination_firewall_rules = destination_firewall_rules
        if ip_sets is not None:
          self.ip_sets = ip_sets
        if vpc is not None:
          self.vpc = vpc
        if region is not None:
          self.region = region
        if account is not None:
          self.account = account

    @property
    def entity_id(self):
        """
        Gets the entity_id of this EC2Instance.

        :return: The entity_id of this EC2Instance.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this EC2Instance.

        :param entity_id: The entity_id of this EC2Instance.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this EC2Instance.

        :return: The name of this EC2Instance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EC2Instance.

        :param name: The name of this EC2Instance.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this EC2Instance.

        :return: The entity_type of this EC2Instance.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EC2Instance.

        :param entity_type: The entity_type of this EC2Instance.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this EC2Instance.

        :return: The ip_addresses of this EC2Instance.
        :rtype: list[IpV4Address]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this EC2Instance.

        :param ip_addresses: The ip_addresses of this EC2Instance.
        :type: list[IpV4Address]
        """

        self._ip_addresses = ip_addresses

    @property
    def default_gateway(self):
        """
        Gets the default_gateway of this EC2Instance.

        :return: The default_gateway of this EC2Instance.
        :rtype: str
        """
        return self._default_gateway

    @default_gateway.setter
    def default_gateway(self, default_gateway):
        """
        Sets the default_gateway of this EC2Instance.

        :param default_gateway: The default_gateway of this EC2Instance.
        :type: str
        """

        self._default_gateway = default_gateway

    @property
    def vnics(self):
        """
        Gets the vnics of this EC2Instance.

        :return: The vnics of this EC2Instance.
        :rtype: list[Reference]
        """
        return self._vnics

    @vnics.setter
    def vnics(self, vnics):
        """
        Sets the vnics of this EC2Instance.

        :param vnics: The vnics of this EC2Instance.
        :type: list[Reference]
        """

        self._vnics = vnics

    @property
    def security_groups(self):
        """
        Gets the security_groups of this EC2Instance.

        :return: The security_groups of this EC2Instance.
        :rtype: list[Reference]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """
        Sets the security_groups of this EC2Instance.

        :param security_groups: The security_groups of this EC2Instance.
        :type: list[Reference]
        """

        self._security_groups = security_groups

    @property
    def source_firewall_rules(self):
        """
        Gets the source_firewall_rules of this EC2Instance.

        :return: The source_firewall_rules of this EC2Instance.
        :rtype: list[RuleSet]
        """
        return self._source_firewall_rules

    @source_firewall_rules.setter
    def source_firewall_rules(self, source_firewall_rules):
        """
        Sets the source_firewall_rules of this EC2Instance.

        :param source_firewall_rules: The source_firewall_rules of this EC2Instance.
        :type: list[RuleSet]
        """

        self._source_firewall_rules = source_firewall_rules

    @property
    def destination_firewall_rules(self):
        """
        Gets the destination_firewall_rules of this EC2Instance.

        :return: The destination_firewall_rules of this EC2Instance.
        :rtype: list[RuleSet]
        """
        return self._destination_firewall_rules

    @destination_firewall_rules.setter
    def destination_firewall_rules(self, destination_firewall_rules):
        """
        Sets the destination_firewall_rules of this EC2Instance.

        :param destination_firewall_rules: The destination_firewall_rules of this EC2Instance.
        :type: list[RuleSet]
        """

        self._destination_firewall_rules = destination_firewall_rules

    @property
    def ip_sets(self):
        """
        Gets the ip_sets of this EC2Instance.

        :return: The ip_sets of this EC2Instance.
        :rtype: list[Reference]
        """
        return self._ip_sets

    @ip_sets.setter
    def ip_sets(self, ip_sets):
        """
        Sets the ip_sets of this EC2Instance.

        :param ip_sets: The ip_sets of this EC2Instance.
        :type: list[Reference]
        """

        self._ip_sets = ip_sets

    @property
    def vpc(self):
        """
        Gets the vpc of this EC2Instance.

        :return: The vpc of this EC2Instance.
        :rtype: Reference
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """
        Sets the vpc of this EC2Instance.

        :param vpc: The vpc of this EC2Instance.
        :type: Reference
        """

        self._vpc = vpc

    @property
    def region(self):
        """
        Gets the region of this EC2Instance.

        :return: The region of this EC2Instance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this EC2Instance.

        :param region: The region of this EC2Instance.
        :type: str
        """

        self._region = region

    @property
    def account(self):
        """
        Gets the account of this EC2Instance.

        :return: The account of this EC2Instance.
        :rtype: Reference
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this EC2Instance.

        :param account: The account of this EC2Instance.
        :type: Reference
        """

        self._account = account

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
        if not isinstance(other, EC2Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
