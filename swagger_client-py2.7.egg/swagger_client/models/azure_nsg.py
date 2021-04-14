# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AzureNSG(object):
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
        'firewall_rules': 'list[RuleSet]',
        'exclusions': 'list[Reference]',
        'vendor_id': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'firewall_rules': 'firewall_rules',
        'exclusions': 'exclusions',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, firewall_rules=None, exclusions=None, vendor_id=None):
        """
        AzureNSG - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._firewall_rules = None
        self._exclusions = None
        self._vendor_id = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if firewall_rules is not None:
          self.firewall_rules = firewall_rules
        if exclusions is not None:
          self.exclusions = exclusions
        if vendor_id is not None:
          self.vendor_id = vendor_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this AzureNSG.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this AzureNSG.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this AzureNSG.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this AzureNSG.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this AzureNSG.
        Name of the object

        :return: The name of this AzureNSG.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AzureNSG.
        Name of the object

        :param name: The name of this AzureNSG.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this AzureNSG.

        :return: The entity_type of this AzureNSG.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this AzureNSG.

        :param entity_type: The entity_type of this AzureNSG.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def firewall_rules(self):
        """
        Gets the firewall_rules of this AzureNSG.

        :return: The firewall_rules of this AzureNSG.
        :rtype: list[RuleSet]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """
        Sets the firewall_rules of this AzureNSG.

        :param firewall_rules: The firewall_rules of this AzureNSG.
        :type: list[RuleSet]
        """

        self._firewall_rules = firewall_rules

    @property
    def exclusions(self):
        """
        Gets the exclusions of this AzureNSG.

        :return: The exclusions of this AzureNSG.
        :rtype: list[Reference]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """
        Sets the exclusions of this AzureNSG.

        :param exclusions: The exclusions of this AzureNSG.
        :type: list[Reference]
        """

        self._exclusions = exclusions

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this AzureNSG.

        :return: The vendor_id of this AzureNSG.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this AzureNSG.

        :param vendor_id: The vendor_id of this AzureNSG.
        :type: str
        """

        self._vendor_id = vendor_id

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
        if not isinstance(other, AzureNSG):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
