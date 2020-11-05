# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WANConfig(object):
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
        'site': 'str',
        'region': 'str',
        'interfaces': 'list[InterfaceWANConfig]'
    }

    attribute_map = {
        'site': 'site',
        'region': 'region',
        'interfaces': 'interfaces'
    }

    def __init__(self, site=None, region=None, interfaces=None):
        """
        WANConfig - a model defined in Swagger
        """

        self._site = None
        self._region = None
        self._interfaces = None

        if site is not None:
          self.site = site
        if region is not None:
          self.region = region
        if interfaces is not None:
          self.interfaces = interfaces

    @property
    def site(self):
        """
        Gets the site of this WANConfig.

        :return: The site of this WANConfig.
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """
        Sets the site of this WANConfig.

        :param site: The site of this WANConfig.
        :type: str
        """

        self._site = site

    @property
    def region(self):
        """
        Gets the region of this WANConfig.

        :return: The region of this WANConfig.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this WANConfig.

        :param region: The region of this WANConfig.
        :type: str
        """

        self._region = region

    @property
    def interfaces(self):
        """
        Gets the interfaces of this WANConfig.

        :return: The interfaces of this WANConfig.
        :rtype: list[InterfaceWANConfig]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """
        Sets the interfaces of this WANConfig.

        :param interfaces: The interfaces of this WANConfig.
        :type: list[InterfaceWANConfig]
        """

        self._interfaces = interfaces

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
        if not isinstance(other, WANConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
