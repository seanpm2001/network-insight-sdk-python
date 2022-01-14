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


class FirewallRuleSet(object):
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
        'firewall_entity_id': 'Reference',
        'vendor_info': 'VendorInfo',
        'manager': 'Reference',
        'rules': 'list[BaseFirewallRule]'
    }

    attribute_map = {
        'firewall_entity_id': 'firewall_entity_id',
        'vendor_info': 'vendor_info',
        'manager': 'manager',
        'rules': 'rules'
    }

    def __init__(self, firewall_entity_id=None, vendor_info=None, manager=None, rules=None):
        """
        FirewallRuleSet - a model defined in Swagger
        """

        self._firewall_entity_id = None
        self._vendor_info = None
        self._manager = None
        self._rules = None

        if firewall_entity_id is not None:
          self.firewall_entity_id = firewall_entity_id
        if vendor_info is not None:
          self.vendor_info = vendor_info
        if manager is not None:
          self.manager = manager
        if rules is not None:
          self.rules = rules

    @property
    def firewall_entity_id(self):
        """
        Gets the firewall_entity_id of this FirewallRuleSet.

        :return: The firewall_entity_id of this FirewallRuleSet.
        :rtype: Reference
        """
        return self._firewall_entity_id

    @firewall_entity_id.setter
    def firewall_entity_id(self, firewall_entity_id):
        """
        Sets the firewall_entity_id of this FirewallRuleSet.

        :param firewall_entity_id: The firewall_entity_id of this FirewallRuleSet.
        :type: Reference
        """

        self._firewall_entity_id = firewall_entity_id

    @property
    def vendor_info(self):
        """
        Gets the vendor_info of this FirewallRuleSet.

        :return: The vendor_info of this FirewallRuleSet.
        :rtype: VendorInfo
        """
        return self._vendor_info

    @vendor_info.setter
    def vendor_info(self, vendor_info):
        """
        Sets the vendor_info of this FirewallRuleSet.

        :param vendor_info: The vendor_info of this FirewallRuleSet.
        :type: VendorInfo
        """

        self._vendor_info = vendor_info

    @property
    def manager(self):
        """
        Gets the manager of this FirewallRuleSet.

        :return: The manager of this FirewallRuleSet.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this FirewallRuleSet.

        :param manager: The manager of this FirewallRuleSet.
        :type: Reference
        """

        self._manager = manager

    @property
    def rules(self):
        """
        Gets the rules of this FirewallRuleSet.

        :return: The rules of this FirewallRuleSet.
        :rtype: list[BaseFirewallRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this FirewallRuleSet.

        :param rules: The rules of this FirewallRuleSet.
        :type: list[BaseFirewallRule]
        """

        self._rules = rules

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
        if not isinstance(other, FirewallRuleSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
