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


class Cardinality(object):
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
        'value': 'int',
        'is_approx': 'bool'
    }

    attribute_map = {
        'value': 'value',
        'is_approx': 'is_approx'
    }

    def __init__(self, value=None, is_approx=None):
        """
        Cardinality - a model defined in Swagger
        """

        self._value = None
        self._is_approx = None

        if value is not None:
          self.value = value
        if is_approx is not None:
          self.is_approx = is_approx

    @property
    def value(self):
        """
        Gets the value of this Cardinality.

        :return: The value of this Cardinality.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Cardinality.

        :param value: The value of this Cardinality.
        :type: int
        """

        self._value = value

    @property
    def is_approx(self):
        """
        Gets the is_approx of this Cardinality.

        :return: The is_approx of this Cardinality.
        :rtype: bool
        """
        return self._is_approx

    @is_approx.setter
    def is_approx(self, is_approx):
        """
        Sets the is_approx of this Cardinality.

        :param is_approx: The is_approx of this Cardinality.
        :type: bool
        """

        self._is_approx = is_approx

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
        if not isinstance(other, Cardinality):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
