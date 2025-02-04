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


class PolicyManagerFirewall(object):
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
        'firewall_sections': 'list[Reference]',
        'sddc_type': 'SddcType'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'firewall_rules': 'firewall_rules',
        'exclusions': 'exclusions',
        'firewall_sections': 'firewall_sections',
        'sddc_type': 'sddc_type'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, firewall_rules=None, exclusions=None, firewall_sections=None, sddc_type=None):
        """
        PolicyManagerFirewall - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._firewall_rules = None
        self._exclusions = None
        self._firewall_sections = None
        self._sddc_type = None

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
        if firewall_sections is not None:
          self.firewall_sections = firewall_sections
        if sddc_type is not None:
          self.sddc_type = sddc_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this PolicyManagerFirewall.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this PolicyManagerFirewall.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this PolicyManagerFirewall.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this PolicyManagerFirewall.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this PolicyManagerFirewall.
        Name of the object

        :return: The name of this PolicyManagerFirewall.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyManagerFirewall.
        Name of the object

        :param name: The name of this PolicyManagerFirewall.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this PolicyManagerFirewall.

        :return: The entity_type of this PolicyManagerFirewall.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this PolicyManagerFirewall.

        :param entity_type: The entity_type of this PolicyManagerFirewall.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def firewall_rules(self):
        """
        Gets the firewall_rules of this PolicyManagerFirewall.

        :return: The firewall_rules of this PolicyManagerFirewall.
        :rtype: list[RuleSet]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """
        Sets the firewall_rules of this PolicyManagerFirewall.

        :param firewall_rules: The firewall_rules of this PolicyManagerFirewall.
        :type: list[RuleSet]
        """

        self._firewall_rules = firewall_rules

    @property
    def exclusions(self):
        """
        Gets the exclusions of this PolicyManagerFirewall.

        :return: The exclusions of this PolicyManagerFirewall.
        :rtype: list[Reference]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """
        Sets the exclusions of this PolicyManagerFirewall.

        :param exclusions: The exclusions of this PolicyManagerFirewall.
        :type: list[Reference]
        """

        self._exclusions = exclusions

    @property
    def firewall_sections(self):
        """
        Gets the firewall_sections of this PolicyManagerFirewall.

        :return: The firewall_sections of this PolicyManagerFirewall.
        :rtype: list[Reference]
        """
        return self._firewall_sections

    @firewall_sections.setter
    def firewall_sections(self, firewall_sections):
        """
        Sets the firewall_sections of this PolicyManagerFirewall.

        :param firewall_sections: The firewall_sections of this PolicyManagerFirewall.
        :type: list[Reference]
        """

        self._firewall_sections = firewall_sections

    @property
    def sddc_type(self):
        """
        Gets the sddc_type of this PolicyManagerFirewall.

        :return: The sddc_type of this PolicyManagerFirewall.
        :rtype: SddcType
        """
        return self._sddc_type

    @sddc_type.setter
    def sddc_type(self, sddc_type):
        """
        Sets the sddc_type of this PolicyManagerFirewall.

        :param sddc_type: The sddc_type of this PolicyManagerFirewall.
        :type: SddcType
        """

        self._sddc_type = sddc_type

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
        if not isinstance(other, PolicyManagerFirewall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
