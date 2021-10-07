# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SnmpProfileIds(object):
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
        'snmp_profiles': 'list[str]'
    }

    attribute_map = {
        'snmp_profiles': 'snmp_profiles'
    }

    def __init__(self, snmp_profiles=None):
        """
        SnmpProfileIds - a model defined in Swagger
        """

        self._snmp_profiles = None

        if snmp_profiles is not None:
          self.snmp_profiles = snmp_profiles

    @property
    def snmp_profiles(self):
        """
        Gets the snmp_profiles of this SnmpProfileIds.

        :return: The snmp_profiles of this SnmpProfileIds.
        :rtype: list[str]
        """
        return self._snmp_profiles

    @snmp_profiles.setter
    def snmp_profiles(self, snmp_profiles):
        """
        Sets the snmp_profiles of this SnmpProfileIds.

        :param snmp_profiles: The snmp_profiles of this SnmpProfileIds.
        :type: list[str]
        """

        self._snmp_profiles = snmp_profiles

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
        if not isinstance(other, SnmpProfileIds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
