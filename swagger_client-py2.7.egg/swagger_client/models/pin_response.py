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


class PinResponse(object):
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
        'pinboard_id': 'str',
        'name': 'str',
        'created_timestamp': 'str',
        'last_updated_timestamp': 'str',
        'query': 'str',
        'pinned_timestamp': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pinboard_id': 'pinboard_id',
        'name': 'name',
        'created_timestamp': 'created_timestamp',
        'last_updated_timestamp': 'last_updated_timestamp',
        'query': 'query',
        'pinned_timestamp': 'pinned_timestamp',
        'owner': 'owner'
    }

    def __init__(self, id=None, pinboard_id=None, name=None, created_timestamp=None, last_updated_timestamp=None, query=None, pinned_timestamp=None, owner=None):
        """
        PinResponse - a model defined in Swagger
        """

        self._id = None
        self._pinboard_id = None
        self._name = None
        self._created_timestamp = None
        self._last_updated_timestamp = None
        self._query = None
        self._pinned_timestamp = None
        self._owner = None

        if id is not None:
          self.id = id
        if pinboard_id is not None:
          self.pinboard_id = pinboard_id
        if name is not None:
          self.name = name
        if created_timestamp is not None:
          self.created_timestamp = created_timestamp
        if last_updated_timestamp is not None:
          self.last_updated_timestamp = last_updated_timestamp
        if query is not None:
          self.query = query
        if pinned_timestamp is not None:
          self.pinned_timestamp = pinned_timestamp
        if owner is not None:
          self.owner = owner

    @property
    def id(self):
        """
        Gets the id of this PinResponse.
        Model key for the pin

        :return: The id of this PinResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PinResponse.
        Model key for the pin

        :param id: The id of this PinResponse.
        :type: str
        """

        self._id = id

    @property
    def pinboard_id(self):
        """
        Gets the pinboard_id of this PinResponse.
        Model key of the pinboard of which the pin is part of

        :return: The pinboard_id of this PinResponse.
        :rtype: str
        """
        return self._pinboard_id

    @pinboard_id.setter
    def pinboard_id(self, pinboard_id):
        """
        Sets the pinboard_id of this PinResponse.
        Model key of the pinboard of which the pin is part of

        :param pinboard_id: The pinboard_id of this PinResponse.
        :type: str
        """

        self._pinboard_id = pinboard_id

    @property
    def name(self):
        """
        Gets the name of this PinResponse.
        Name of the pin

        :return: The name of this PinResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PinResponse.
        Name of the pin

        :param name: The name of this PinResponse.
        :type: str
        """

        self._name = name

    @property
    def created_timestamp(self):
        """
        Gets the created_timestamp of this PinResponse.
        Create timestmp of the pin

        :return: The created_timestamp of this PinResponse.
        :rtype: str
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """
        Sets the created_timestamp of this PinResponse.
        Create timestmp of the pin

        :param created_timestamp: The created_timestamp of this PinResponse.
        :type: str
        """

        self._created_timestamp = created_timestamp

    @property
    def last_updated_timestamp(self):
        """
        Gets the last_updated_timestamp of this PinResponse.
        Last update timestamop of the pin

        :return: The last_updated_timestamp of this PinResponse.
        :rtype: str
        """
        return self._last_updated_timestamp

    @last_updated_timestamp.setter
    def last_updated_timestamp(self, last_updated_timestamp):
        """
        Sets the last_updated_timestamp of this PinResponse.
        Last update timestamop of the pin

        :param last_updated_timestamp: The last_updated_timestamp of this PinResponse.
        :type: str
        """

        self._last_updated_timestamp = last_updated_timestamp

    @property
    def query(self):
        """
        Gets the query of this PinResponse.
        Query behind the pin

        :return: The query of this PinResponse.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this PinResponse.
        Query behind the pin

        :param query: The query of this PinResponse.
        :type: str
        """

        self._query = query

    @property
    def pinned_timestamp(self):
        """
        Gets the pinned_timestamp of this PinResponse.
        Timestamp when the pin was pinned

        :return: The pinned_timestamp of this PinResponse.
        :rtype: str
        """
        return self._pinned_timestamp

    @pinned_timestamp.setter
    def pinned_timestamp(self, pinned_timestamp):
        """
        Sets the pinned_timestamp of this PinResponse.
        Timestamp when the pin was pinned

        :param pinned_timestamp: The pinned_timestamp of this PinResponse.
        :type: str
        """

        self._pinned_timestamp = pinned_timestamp

    @property
    def owner(self):
        """
        Gets the owner of this PinResponse.
        Owner of the pin

        :return: The owner of this PinResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this PinResponse.
        Owner of the pin

        :param owner: The owner of this PinResponse.
        :type: str
        """

        self._owner = owner

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
        if not isinstance(other, PinResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
