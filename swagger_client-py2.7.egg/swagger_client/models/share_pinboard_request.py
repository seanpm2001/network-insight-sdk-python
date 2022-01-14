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


class SharePinboardRequest(object):
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
        'users_read_access': 'list[str]',
        'users_write_access': 'list[str]',
        'groups_read_access': 'list[str]',
        'groups_write_access': 'list[str]'
    }

    attribute_map = {
        'users_read_access': 'users_read_access',
        'users_write_access': 'users_write_access',
        'groups_read_access': 'groups_read_access',
        'groups_write_access': 'groups_write_access'
    }

    def __init__(self, users_read_access=None, users_write_access=None, groups_read_access=None, groups_write_access=None):
        """
        SharePinboardRequest - a model defined in Swagger
        """

        self._users_read_access = None
        self._users_write_access = None
        self._groups_read_access = None
        self._groups_write_access = None

        if users_read_access is not None:
          self.users_read_access = users_read_access
        if users_write_access is not None:
          self.users_write_access = users_write_access
        if groups_read_access is not None:
          self.groups_read_access = groups_read_access
        if groups_write_access is not None:
          self.groups_write_access = groups_write_access

    @property
    def users_read_access(self):
        """
        Gets the users_read_access of this SharePinboardRequest.
        List of users with read privilege for the pinboard

        :return: The users_read_access of this SharePinboardRequest.
        :rtype: list[str]
        """
        return self._users_read_access

    @users_read_access.setter
    def users_read_access(self, users_read_access):
        """
        Sets the users_read_access of this SharePinboardRequest.
        List of users with read privilege for the pinboard

        :param users_read_access: The users_read_access of this SharePinboardRequest.
        :type: list[str]
        """

        self._users_read_access = users_read_access

    @property
    def users_write_access(self):
        """
        Gets the users_write_access of this SharePinboardRequest.
        List of users with all privileges for the pinboard

        :return: The users_write_access of this SharePinboardRequest.
        :rtype: list[str]
        """
        return self._users_write_access

    @users_write_access.setter
    def users_write_access(self, users_write_access):
        """
        Sets the users_write_access of this SharePinboardRequest.
        List of users with all privileges for the pinboard

        :param users_write_access: The users_write_access of this SharePinboardRequest.
        :type: list[str]
        """

        self._users_write_access = users_write_access

    @property
    def groups_read_access(self):
        """
        Gets the groups_read_access of this SharePinboardRequest.
        List of groups with read privilege for the pinboard

        :return: The groups_read_access of this SharePinboardRequest.
        :rtype: list[str]
        """
        return self._groups_read_access

    @groups_read_access.setter
    def groups_read_access(self, groups_read_access):
        """
        Sets the groups_read_access of this SharePinboardRequest.
        List of groups with read privilege for the pinboard

        :param groups_read_access: The groups_read_access of this SharePinboardRequest.
        :type: list[str]
        """

        self._groups_read_access = groups_read_access

    @property
    def groups_write_access(self):
        """
        Gets the groups_write_access of this SharePinboardRequest.
        List of groups with read and write privilege for the pinboard

        :return: The groups_write_access of this SharePinboardRequest.
        :rtype: list[str]
        """
        return self._groups_write_access

    @groups_write_access.setter
    def groups_write_access(self, groups_write_access):
        """
        Sets the groups_write_access of this SharePinboardRequest.
        List of groups with read and write privilege for the pinboard

        :param groups_write_access: The groups_write_access of this SharePinboardRequest.
        :type: list[str]
        """

        self._groups_write_access = groups_write_access

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
        if not isinstance(other, SharePinboardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
