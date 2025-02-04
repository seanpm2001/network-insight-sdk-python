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


class UserDefinedProblemWithTime(object):
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
        'entity_type': 'EntityType',
        'entity': 'UserDefinedProblemEvent',
        'time': 'int'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'entity': 'entity',
        'time': 'time'
    }

    def __init__(self, entity_id=None, entity_type=None, entity=None, time=None):
        """
        UserDefinedProblemWithTime - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._entity = None
        self._time = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if entity is not None:
          self.entity = entity
        if time is not None:
          self.time = time

    @property
    def entity_id(self):
        """
        Gets the entity_id of this UserDefinedProblemWithTime.
        Entity Identifier

        :return: The entity_id of this UserDefinedProblemWithTime.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this UserDefinedProblemWithTime.
        Entity Identifier

        :param entity_id: The entity_id of this UserDefinedProblemWithTime.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this UserDefinedProblemWithTime.

        :return: The entity_type of this UserDefinedProblemWithTime.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this UserDefinedProblemWithTime.

        :param entity_type: The entity_type of this UserDefinedProblemWithTime.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def entity(self):
        """
        Gets the entity of this UserDefinedProblemWithTime.

        :return: The entity of this UserDefinedProblemWithTime.
        :rtype: UserDefinedProblemEvent
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this UserDefinedProblemWithTime.

        :param entity: The entity of this UserDefinedProblemWithTime.
        :type: UserDefinedProblemEvent
        """

        self._entity = entity

    @property
    def time(self):
        """
        Gets the time of this UserDefinedProblemWithTime.

        :return: The time of this UserDefinedProblemWithTime.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this UserDefinedProblemWithTime.

        :param time: The time of this UserDefinedProblemWithTime.
        :type: int
        """

        self._time = time

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
        if not isinstance(other, UserDefinedProblemWithTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
