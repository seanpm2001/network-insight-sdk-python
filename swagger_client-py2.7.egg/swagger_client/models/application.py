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


class Application(object):
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
        'name': 'str',
        'entity_type': 'EntityType',
        'create_time': 'int',
        'created_by': 'str',
        'last_modified_time': 'int',
        'last_modified_by': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'create_time': 'create_time',
        'created_by': 'created_by',
        'last_modified_time': 'last_modified_time',
        'last_modified_by': 'last_modified_by'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, create_time=None, created_by=None, last_modified_time=None, last_modified_by=None):
        """
        Application - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._create_time = None
        self._created_by = None
        self._last_modified_time = None
        self._last_modified_by = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if create_time is not None:
          self.create_time = create_time
        if created_by is not None:
          self.created_by = created_by
        if last_modified_time is not None:
          self.last_modified_time = last_modified_time
        if last_modified_by is not None:
          self.last_modified_by = last_modified_by

    @property
    def entity_id(self):
        """
        Gets the entity_id of this Application.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this Application.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this Application.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this Application.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this Application.
        Name of the object

        :return: The name of this Application.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Application.
        Name of the object

        :param name: The name of this Application.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this Application.

        :return: The entity_type of this Application.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this Application.

        :param entity_type: The entity_type of this Application.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def create_time(self):
        """
        Gets the create_time of this Application.
        Timestamp of when the object was created

        :return: The create_time of this Application.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this Application.
        Timestamp of when the object was created

        :param create_time: The create_time of this Application.
        :type: int
        """

        self._create_time = create_time

    @property
    def created_by(self):
        """
        Gets the created_by of this Application.
        The username of who created the object

        :return: The created_by of this Application.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this Application.
        The username of who created the object

        :param created_by: The created_by of this Application.
        :type: str
        """

        self._created_by = created_by

    @property
    def last_modified_time(self):
        """
        Gets the last_modified_time of this Application.
        Timestamp of when the object was last modified

        :return: The last_modified_time of this Application.
        :rtype: int
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """
        Sets the last_modified_time of this Application.
        Timestamp of when the object was last modified

        :param last_modified_time: The last_modified_time of this Application.
        :type: int
        """

        self._last_modified_time = last_modified_time

    @property
    def last_modified_by(self):
        """
        Gets the last_modified_by of this Application.
        The username of who last modified the object

        :return: The last_modified_by of this Application.
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """
        Sets the last_modified_by of this Application.
        The username of who last modified the object

        :param last_modified_by: The last_modified_by of this Application.
        :type: str
        """

        self._last_modified_by = last_modified_by

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
        if not isinstance(other, Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
