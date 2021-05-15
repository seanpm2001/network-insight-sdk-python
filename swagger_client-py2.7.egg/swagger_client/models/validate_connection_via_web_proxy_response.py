# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ValidateConnectionViaWebProxyResponse(object):
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
        'entity_type': 'str',
        'name': 'str',
        'identifier': 'str',
        'status': 'str',
        'error_code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'name': 'name',
        'identifier': 'identifier',
        'status': 'status',
        'error_code': 'error_code',
        'message': 'message'
    }

    def __init__(self, entity_id=None, entity_type=None, name=None, identifier=None, status=None, error_code=None, message=None):
        """
        ValidateConnectionViaWebProxyResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._name = None
        self._identifier = None
        self._status = None
        self._error_code = None
        self._message = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if name is not None:
          self.name = name
        if identifier is not None:
          self.identifier = identifier
        if status is not None:
          self.status = status
        if error_code is not None:
          self.error_code = error_code
        if message is not None:
          self.message = message

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ValidateConnectionViaWebProxyResponse.
        Entity ID for a connected client

        :return: The entity_id of this ValidateConnectionViaWebProxyResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ValidateConnectionViaWebProxyResponse.
        Entity ID for a connected client

        :param entity_id: The entity_id of this ValidateConnectionViaWebProxyResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this ValidateConnectionViaWebProxyResponse.
        Type of Entity

        :return: The entity_type of this ValidateConnectionViaWebProxyResponse.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ValidateConnectionViaWebProxyResponse.
        Type of Entity

        :param entity_type: The entity_type of this ValidateConnectionViaWebProxyResponse.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this ValidateConnectionViaWebProxyResponse.
        Name of connected client

        :return: The name of this ValidateConnectionViaWebProxyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ValidateConnectionViaWebProxyResponse.
        Name of connected client

        :param name: The name of this ValidateConnectionViaWebProxyResponse.
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this ValidateConnectionViaWebProxyResponse.
        Identifier/AccessKey/IP Adress of connected client

        :return: The identifier of this ValidateConnectionViaWebProxyResponse.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ValidateConnectionViaWebProxyResponse.
        Identifier/AccessKey/IP Adress of connected client

        :param identifier: The identifier of this ValidateConnectionViaWebProxyResponse.
        :type: str
        """

        self._identifier = identifier

    @property
    def status(self):
        """
        Gets the status of this ValidateConnectionViaWebProxyResponse.
        Validation status of a connected entity with the updated web proxy details

        :return: The status of this ValidateConnectionViaWebProxyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ValidateConnectionViaWebProxyResponse.
        Validation status of a connected entity with the updated web proxy details

        :param status: The status of this ValidateConnectionViaWebProxyResponse.
        :type: str
        """

        self._status = status

    @property
    def error_code(self):
        """
        Gets the error_code of this ValidateConnectionViaWebProxyResponse.
        Error code in case validation failed

        :return: The error_code of this ValidateConnectionViaWebProxyResponse.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this ValidateConnectionViaWebProxyResponse.
        Error code in case validation failed

        :param error_code: The error_code of this ValidateConnectionViaWebProxyResponse.
        :type: int
        """

        self._error_code = error_code

    @property
    def message(self):
        """
        Gets the message of this ValidateConnectionViaWebProxyResponse.
        Error message in case validation failed

        :return: The message of this ValidateConnectionViaWebProxyResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ValidateConnectionViaWebProxyResponse.
        Error message in case validation failed

        :param message: The message of this ValidateConnectionViaWebProxyResponse.
        :type: str
        """

        self._message = message

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
        if not isinstance(other, ValidateConnectionViaWebProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
