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


class DuplicatePinboardRequest(object):
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
        'name': 'str',
        'description': 'str',
        'retain_access_permissions': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'retain_access_permissions': 'retain_access_permissions'
    }

    def __init__(self, name=None, description=None, retain_access_permissions=None):
        """
        DuplicatePinboardRequest - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._retain_access_permissions = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if retain_access_permissions is not None:
          self.retain_access_permissions = retain_access_permissions

    @property
    def name(self):
        """
        Gets the name of this DuplicatePinboardRequest.
        Name of the pinboard

        :return: The name of this DuplicatePinboardRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DuplicatePinboardRequest.
        Name of the pinboard

        :param name: The name of this DuplicatePinboardRequest.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DuplicatePinboardRequest.
        Description of the pinboard

        :return: The description of this DuplicatePinboardRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DuplicatePinboardRequest.
        Description of the pinboard

        :param description: The description of this DuplicatePinboardRequest.
        :type: str
        """

        self._description = description

    @property
    def retain_access_permissions(self):
        """
        Gets the retain_access_permissions of this DuplicatePinboardRequest.
        Should pinboard permissions be copied while duplicating the pinboard.

        :return: The retain_access_permissions of this DuplicatePinboardRequest.
        :rtype: bool
        """
        return self._retain_access_permissions

    @retain_access_permissions.setter
    def retain_access_permissions(self, retain_access_permissions):
        """
        Sets the retain_access_permissions of this DuplicatePinboardRequest.
        Should pinboard permissions be copied while duplicating the pinboard.

        :param retain_access_permissions: The retain_access_permissions of this DuplicatePinboardRequest.
        :type: bool
        """

        self._retain_access_permissions = retain_access_permissions

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
        if not isinstance(other, DuplicatePinboardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
