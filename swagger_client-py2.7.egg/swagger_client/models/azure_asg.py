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


class AzureASG(object):
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
        'members': 'list[Reference]',
        'direct_source_rules': 'list[RuleSet]',
        'direct_destination_rules': 'list[RuleSet]',
        'indirect_source_rules': 'list[RuleSet]',
        'indirect_destination_rules': 'list[RuleSet]',
        'parents': 'list[Reference]',
        'direct_members': 'list[Reference]',
        'vendor_id': 'str',
        'excluded_members': 'list[Reference]',
        'vnet': 'Reference',
        'region': 'str',
        'security_tags': 'list[Reference]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'members': 'members',
        'direct_source_rules': 'direct_source_rules',
        'direct_destination_rules': 'direct_destination_rules',
        'indirect_source_rules': 'indirect_source_rules',
        'indirect_destination_rules': 'indirect_destination_rules',
        'parents': 'parents',
        'direct_members': 'direct_members',
        'vendor_id': 'vendor_id',
        'excluded_members': 'excluded_members',
        'vnet': 'vnet',
        'region': 'region',
        'security_tags': 'security_tags'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, members=None, direct_source_rules=None, direct_destination_rules=None, indirect_source_rules=None, indirect_destination_rules=None, parents=None, direct_members=None, vendor_id=None, excluded_members=None, vnet=None, region=None, security_tags=None):
        """
        AzureASG - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._members = None
        self._direct_source_rules = None
        self._direct_destination_rules = None
        self._indirect_source_rules = None
        self._indirect_destination_rules = None
        self._parents = None
        self._direct_members = None
        self._vendor_id = None
        self._excluded_members = None
        self._vnet = None
        self._region = None
        self._security_tags = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if members is not None:
          self.members = members
        if direct_source_rules is not None:
          self.direct_source_rules = direct_source_rules
        if direct_destination_rules is not None:
          self.direct_destination_rules = direct_destination_rules
        if indirect_source_rules is not None:
          self.indirect_source_rules = indirect_source_rules
        if indirect_destination_rules is not None:
          self.indirect_destination_rules = indirect_destination_rules
        if parents is not None:
          self.parents = parents
        if direct_members is not None:
          self.direct_members = direct_members
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if excluded_members is not None:
          self.excluded_members = excluded_members
        if vnet is not None:
          self.vnet = vnet
        if region is not None:
          self.region = region
        if security_tags is not None:
          self.security_tags = security_tags

    @property
    def entity_id(self):
        """
        Gets the entity_id of this AzureASG.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this AzureASG.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this AzureASG.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this AzureASG.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this AzureASG.
        Name of the object

        :return: The name of this AzureASG.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AzureASG.
        Name of the object

        :param name: The name of this AzureASG.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this AzureASG.

        :return: The entity_type of this AzureASG.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this AzureASG.

        :param entity_type: The entity_type of this AzureASG.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def members(self):
        """
        Gets the members of this AzureASG.

        :return: The members of this AzureASG.
        :rtype: list[Reference]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this AzureASG.

        :param members: The members of this AzureASG.
        :type: list[Reference]
        """

        self._members = members

    @property
    def direct_source_rules(self):
        """
        Gets the direct_source_rules of this AzureASG.

        :return: The direct_source_rules of this AzureASG.
        :rtype: list[RuleSet]
        """
        return self._direct_source_rules

    @direct_source_rules.setter
    def direct_source_rules(self, direct_source_rules):
        """
        Sets the direct_source_rules of this AzureASG.

        :param direct_source_rules: The direct_source_rules of this AzureASG.
        :type: list[RuleSet]
        """

        self._direct_source_rules = direct_source_rules

    @property
    def direct_destination_rules(self):
        """
        Gets the direct_destination_rules of this AzureASG.

        :return: The direct_destination_rules of this AzureASG.
        :rtype: list[RuleSet]
        """
        return self._direct_destination_rules

    @direct_destination_rules.setter
    def direct_destination_rules(self, direct_destination_rules):
        """
        Sets the direct_destination_rules of this AzureASG.

        :param direct_destination_rules: The direct_destination_rules of this AzureASG.
        :type: list[RuleSet]
        """

        self._direct_destination_rules = direct_destination_rules

    @property
    def indirect_source_rules(self):
        """
        Gets the indirect_source_rules of this AzureASG.

        :return: The indirect_source_rules of this AzureASG.
        :rtype: list[RuleSet]
        """
        return self._indirect_source_rules

    @indirect_source_rules.setter
    def indirect_source_rules(self, indirect_source_rules):
        """
        Sets the indirect_source_rules of this AzureASG.

        :param indirect_source_rules: The indirect_source_rules of this AzureASG.
        :type: list[RuleSet]
        """

        self._indirect_source_rules = indirect_source_rules

    @property
    def indirect_destination_rules(self):
        """
        Gets the indirect_destination_rules of this AzureASG.

        :return: The indirect_destination_rules of this AzureASG.
        :rtype: list[RuleSet]
        """
        return self._indirect_destination_rules

    @indirect_destination_rules.setter
    def indirect_destination_rules(self, indirect_destination_rules):
        """
        Sets the indirect_destination_rules of this AzureASG.

        :param indirect_destination_rules: The indirect_destination_rules of this AzureASG.
        :type: list[RuleSet]
        """

        self._indirect_destination_rules = indirect_destination_rules

    @property
    def parents(self):
        """
        Gets the parents of this AzureASG.

        :return: The parents of this AzureASG.
        :rtype: list[Reference]
        """
        return self._parents

    @parents.setter
    def parents(self, parents):
        """
        Sets the parents of this AzureASG.

        :param parents: The parents of this AzureASG.
        :type: list[Reference]
        """

        self._parents = parents

    @property
    def direct_members(self):
        """
        Gets the direct_members of this AzureASG.

        :return: The direct_members of this AzureASG.
        :rtype: list[Reference]
        """
        return self._direct_members

    @direct_members.setter
    def direct_members(self, direct_members):
        """
        Sets the direct_members of this AzureASG.

        :param direct_members: The direct_members of this AzureASG.
        :type: list[Reference]
        """

        self._direct_members = direct_members

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this AzureASG.

        :return: The vendor_id of this AzureASG.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this AzureASG.

        :param vendor_id: The vendor_id of this AzureASG.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def excluded_members(self):
        """
        Gets the excluded_members of this AzureASG.

        :return: The excluded_members of this AzureASG.
        :rtype: list[Reference]
        """
        return self._excluded_members

    @excluded_members.setter
    def excluded_members(self, excluded_members):
        """
        Sets the excluded_members of this AzureASG.

        :param excluded_members: The excluded_members of this AzureASG.
        :type: list[Reference]
        """

        self._excluded_members = excluded_members

    @property
    def vnet(self):
        """
        Gets the vnet of this AzureASG.

        :return: The vnet of this AzureASG.
        :rtype: Reference
        """
        return self._vnet

    @vnet.setter
    def vnet(self, vnet):
        """
        Sets the vnet of this AzureASG.

        :param vnet: The vnet of this AzureASG.
        :type: Reference
        """

        self._vnet = vnet

    @property
    def region(self):
        """
        Gets the region of this AzureASG.

        :return: The region of this AzureASG.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this AzureASG.

        :param region: The region of this AzureASG.
        :type: str
        """

        self._region = region

    @property
    def security_tags(self):
        """
        Gets the security_tags of this AzureASG.

        :return: The security_tags of this AzureASG.
        :rtype: list[Reference]
        """
        return self._security_tags

    @security_tags.setter
    def security_tags(self, security_tags):
        """
        Sets the security_tags of this AzureASG.

        :param security_tags: The security_tags of this AzureASG.
        :type: list[Reference]
        """

        self._security_tags = security_tags

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
        if not isinstance(other, AzureASG):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
