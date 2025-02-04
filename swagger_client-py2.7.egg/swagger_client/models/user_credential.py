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


class UserCredential(object):
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
        'username': 'str',
        'password': 'str',
        'domain': 'Domain'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'domain': 'domain'
    }

    def __init__(self, username=None, password=None, domain=None):
        """
        UserCredential - a model defined in Swagger
        """

        self._username = None
        self._password = None
        self._domain = None

        if username is not None:
          self.username = username
        if password is not None:
          self.password = password
        if domain is not None:
          self.domain = domain

    @property
    def username(self):
        """
        Gets the username of this UserCredential.

        :return: The username of this UserCredential.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserCredential.

        :param username: The username of this UserCredential.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UserCredential.

        :return: The password of this UserCredential.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserCredential.

        :param password: The password of this UserCredential.
        :type: str
        """

        self._password = password

    @property
    def domain(self):
        """
        Gets the domain of this UserCredential.

        :return: The domain of this UserCredential.
        :rtype: Domain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this UserCredential.

        :param domain: The domain of this UserCredential.
        :type: Domain
        """

        self._domain = domain

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
        if not isinstance(other, UserCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
