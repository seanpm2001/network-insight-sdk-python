# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AuditResponse(object):
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
        'ip_address': 'str',
        'user_name': 'str',
        'entity_type': 'str',
        'entity_id': 'str',
        'operation': 'str',
        'response': 'str',
        'value': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'user_name': 'user_name',
        'entity_type': 'entity_type',
        'entity_id': 'entity_id',
        'operation': 'operation',
        'response': 'response',
        'value': 'value',
        'timestamp': 'timestamp'
    }

    def __init__(self, ip_address=None, user_name=None, entity_type=None, entity_id=None, operation=None, response=None, value=None, timestamp=None):
        """
        AuditResponse - a model defined in Swagger
        """

        self._ip_address = None
        self._user_name = None
        self._entity_type = None
        self._entity_id = None
        self._operation = None
        self._response = None
        self._value = None
        self._timestamp = None

        if ip_address is not None:
          self.ip_address = ip_address
        if user_name is not None:
          self.user_name = user_name
        if entity_type is not None:
          self.entity_type = entity_type
        if entity_id is not None:
          self.entity_id = entity_id
        if operation is not None:
          self.operation = operation
        if response is not None:
          self.response = response
        if value is not None:
          self.value = value
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def ip_address(self):
        """
        Gets the ip_address of this AuditResponse.

        :return: The ip_address of this AuditResponse.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this AuditResponse.

        :param ip_address: The ip_address of this AuditResponse.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def user_name(self):
        """
        Gets the user_name of this AuditResponse.

        :return: The user_name of this AuditResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this AuditResponse.

        :param user_name: The user_name of this AuditResponse.
        :type: str
        """

        self._user_name = user_name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this AuditResponse.

        :return: The entity_type of this AuditResponse.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this AuditResponse.

        :param entity_type: The entity_type of this AuditResponse.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def entity_id(self):
        """
        Gets the entity_id of this AuditResponse.

        :return: The entity_id of this AuditResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this AuditResponse.

        :param entity_id: The entity_id of this AuditResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def operation(self):
        """
        Gets the operation of this AuditResponse.

        :return: The operation of this AuditResponse.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this AuditResponse.

        :param operation: The operation of this AuditResponse.
        :type: str
        """

        self._operation = operation

    @property
    def response(self):
        """
        Gets the response of this AuditResponse.

        :return: The response of this AuditResponse.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this AuditResponse.

        :param response: The response of this AuditResponse.
        :type: str
        """

        self._response = response

    @property
    def value(self):
        """
        Gets the value of this AuditResponse.

        :return: The value of this AuditResponse.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AuditResponse.

        :param value: The value of this AuditResponse.
        :type: str
        """

        self._value = value

    @property
    def timestamp(self):
        """
        Gets the timestamp of this AuditResponse.

        :return: The timestamp of this AuditResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this AuditResponse.

        :param timestamp: The timestamp of this AuditResponse.
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, AuditResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
