# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NameRequestParam(object):
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
        'time': 'int'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'time': 'time'
    }

    def __init__(self, entity_id=None, time=None):
        """
        NameRequestParam - a model defined in Swagger
        """

        self._entity_id = None
        self._time = None

        if entity_id is not None:
          self.entity_id = entity_id
        if time is not None:
          self.time = time

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NameRequestParam.

        :return: The entity_id of this NameRequestParam.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NameRequestParam.

        :param entity_id: The entity_id of this NameRequestParam.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def time(self):
        """
        Gets the time of this NameRequestParam.

        :return: The time of this NameRequestParam.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this NameRequestParam.

        :param time: The time of this NameRequestParam.
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
        if not isinstance(other, NameRequestParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
