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


class EntityUsingOrBehindWebProxyResponse(object):
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
        'identifier': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'name': 'name',
        'identifier': 'identifier'
    }

    def __init__(self, entity_id=None, entity_type=None, name=None, identifier=None):
        """
        EntityUsingOrBehindWebProxyResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._name = None
        self._identifier = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if name is not None:
          self.name = name
        if identifier is not None:
          self.identifier = identifier

    @property
    def entity_id(self):
        """
        Gets the entity_id of this EntityUsingOrBehindWebProxyResponse.
        Entity ID for a connected client

        :return: The entity_id of this EntityUsingOrBehindWebProxyResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this EntityUsingOrBehindWebProxyResponse.
        Entity ID for a connected client

        :param entity_id: The entity_id of this EntityUsingOrBehindWebProxyResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this EntityUsingOrBehindWebProxyResponse.
        Type of Entity

        :return: The entity_type of this EntityUsingOrBehindWebProxyResponse.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EntityUsingOrBehindWebProxyResponse.
        Type of Entity

        :param entity_type: The entity_type of this EntityUsingOrBehindWebProxyResponse.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this EntityUsingOrBehindWebProxyResponse.
        Name of connected client

        :return: The name of this EntityUsingOrBehindWebProxyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EntityUsingOrBehindWebProxyResponse.
        Name of connected client

        :param name: The name of this EntityUsingOrBehindWebProxyResponse.
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this EntityUsingOrBehindWebProxyResponse.
        Identifier/AccessKey/IP Adress of connected client

        :return: The identifier of this EntityUsingOrBehindWebProxyResponse.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this EntityUsingOrBehindWebProxyResponse.
        Identifier/AccessKey/IP Adress of connected client

        :param identifier: The identifier of this EntityUsingOrBehindWebProxyResponse.
        :type: str
        """

        self._identifier = identifier

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
        if not isinstance(other, EntityUsingOrBehindWebProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
