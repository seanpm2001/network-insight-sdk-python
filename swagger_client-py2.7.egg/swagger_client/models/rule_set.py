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


class RuleSet(object):
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
        'rules': 'list[Reference]',
        'firewall': 'Reference',
        'rule_set_type': 'str'
    }

    attribute_map = {
        'rules': 'rules',
        'firewall': 'firewall',
        'rule_set_type': 'rule_set_type'
    }

    def __init__(self, rules=None, firewall=None, rule_set_type=None):
        """
        RuleSet - a model defined in Swagger
        """

        self._rules = None
        self._firewall = None
        self._rule_set_type = None

        if rules is not None:
          self.rules = rules
        if firewall is not None:
          self.firewall = firewall
        if rule_set_type is not None:
          self.rule_set_type = rule_set_type

    @property
    def rules(self):
        """
        Gets the rules of this RuleSet.

        :return: The rules of this RuleSet.
        :rtype: list[Reference]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this RuleSet.

        :param rules: The rules of this RuleSet.
        :type: list[Reference]
        """

        self._rules = rules

    @property
    def firewall(self):
        """
        Gets the firewall of this RuleSet.

        :return: The firewall of this RuleSet.
        :rtype: Reference
        """
        return self._firewall

    @firewall.setter
    def firewall(self, firewall):
        """
        Sets the firewall of this RuleSet.

        :param firewall: The firewall of this RuleSet.
        :type: Reference
        """

        self._firewall = firewall

    @property
    def rule_set_type(self):
        """
        Gets the rule_set_type of this RuleSet.

        :return: The rule_set_type of this RuleSet.
        :rtype: str
        """
        return self._rule_set_type

    @rule_set_type.setter
    def rule_set_type(self, rule_set_type):
        """
        Sets the rule_set_type of this RuleSet.

        :param rule_set_type: The rule_set_type of this RuleSet.
        :type: str
        """
        allowed_values = ["NSX_STANDARD", "NSX_REDIRECT", "AWS_STANDARD", "NSXT_EDGE_FIREWALL", "ACCESS_RULE", "POLICYMANAGER_EMERGENCY_TYPE", "POLICYMANAGER_INFRASTRUCTURE_TYPE", "POLICYMANAGER_ENVIRONMENT_TYPE", "POLICYMANAGER_APPLICATION_TYPE", "POLICYMANAGER_ETHERNET_TYPE"]
        if rule_set_type not in allowed_values:
            raise ValueError(
                "Invalid value for `rule_set_type` ({0}), must be one of {1}"
                .format(rule_set_type, allowed_values)
            )

        self._rule_set_type = rule_set_type

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
        if not isinstance(other, RuleSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
