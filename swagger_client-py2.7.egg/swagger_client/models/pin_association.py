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


class PinAssociation(object):
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
        'id': 'str',
        'name': 'str',
        'query': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'query': 'query'
    }

    def __init__(self, id=None, name=None, query=None):
        """
        PinAssociation - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._query = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if query is not None:
          self.query = query

    @property
    def id(self):
        """
        Gets the id of this PinAssociation.
        Pin model key

        :return: The id of this PinAssociation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PinAssociation.
        Pin model key

        :param id: The id of this PinAssociation.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PinAssociation.
        Name of the pin

        :return: The name of this PinAssociation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PinAssociation.
        Name of the pin

        :param name: The name of this PinAssociation.
        :type: str
        """

        self._name = name

    @property
    def query(self):
        """
        Gets the query of this PinAssociation.
        Search query behind the pin

        :return: The query of this PinAssociation.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this PinAssociation.
        Search query behind the pin

        :param query: The query of this PinAssociation.
        :type: str
        """

        self._query = query

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
        if not isinstance(other, PinAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
