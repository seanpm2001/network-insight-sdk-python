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


class BaseFirewallSection(object):
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
        'section_id': 'str',
        'precedence': 'int',
        'firewall_rules': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'section_id': 'section_id',
        'precedence': 'precedence',
        'firewall_rules': 'firewall_rules'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, section_id=None, precedence=None, firewall_rules=None):
        """
        BaseFirewallSection - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._section_id = None
        self._precedence = None
        self._firewall_rules = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if section_id is not None:
          self.section_id = section_id
        if precedence is not None:
          self.precedence = precedence
        if firewall_rules is not None:
          self.firewall_rules = firewall_rules

    @property
    def entity_id(self):
        """
        Gets the entity_id of this BaseFirewallSection.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this BaseFirewallSection.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this BaseFirewallSection.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this BaseFirewallSection.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this BaseFirewallSection.
        Name of the object

        :return: The name of this BaseFirewallSection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BaseFirewallSection.
        Name of the object

        :param name: The name of this BaseFirewallSection.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this BaseFirewallSection.

        :return: The entity_type of this BaseFirewallSection.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this BaseFirewallSection.

        :param entity_type: The entity_type of this BaseFirewallSection.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def section_id(self):
        """
        Gets the section_id of this BaseFirewallSection.

        :return: The section_id of this BaseFirewallSection.
        :rtype: str
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        """
        Sets the section_id of this BaseFirewallSection.

        :param section_id: The section_id of this BaseFirewallSection.
        :type: str
        """

        self._section_id = section_id

    @property
    def precedence(self):
        """
        Gets the precedence of this BaseFirewallSection.

        :return: The precedence of this BaseFirewallSection.
        :rtype: int
        """
        return self._precedence

    @precedence.setter
    def precedence(self, precedence):
        """
        Sets the precedence of this BaseFirewallSection.

        :param precedence: The precedence of this BaseFirewallSection.
        :type: int
        """

        self._precedence = precedence

    @property
    def firewall_rules(self):
        """
        Gets the firewall_rules of this BaseFirewallSection.

        :return: The firewall_rules of this BaseFirewallSection.
        :rtype: list[Reference]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """
        Sets the firewall_rules of this BaseFirewallSection.

        :param firewall_rules: The firewall_rules of this BaseFirewallSection.
        :type: list[Reference]
        """

        self._firewall_rules = firewall_rules

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
        if not isinstance(other, BaseFirewallSection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
