# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VendorId(object):
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
        'id_type': 'str',
        'id_value': 'str'
    }

    attribute_map = {
        'id_type': 'id_type',
        'id_value': 'id_value'
    }

    def __init__(self, id_type=None, id_value=None):
        """
        VendorId - a model defined in Swagger
        """

        self._id_type = None
        self._id_value = None

        if id_type is not None:
          self.id_type = id_type
        if id_value is not None:
          self.id_value = id_value

    @property
    def id_type(self):
        """
        Gets the id_type of this VendorId.

        :return: The id_type of this VendorId.
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """
        Sets the id_type of this VendorId.

        :param id_type: The id_type of this VendorId.
        :type: str
        """

        self._id_type = id_type

    @property
    def id_value(self):
        """
        Gets the id_value of this VendorId.

        :return: The id_value of this VendorId.
        :rtype: str
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        """
        Sets the id_value of this VendorId.

        :param id_value: The id_value of this VendorId.
        :type: str
        """

        self._id_value = id_value

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
        if not isinstance(other, VendorId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
