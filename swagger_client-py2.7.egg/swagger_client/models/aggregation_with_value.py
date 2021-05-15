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


class AggregationWithValue(object):
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
        'field': 'str',
        'aggregation_type': 'str',
        'value': 'float'
    }

    attribute_map = {
        'field': 'field',
        'aggregation_type': 'aggregation_type',
        'value': 'value'
    }

    def __init__(self, field=None, aggregation_type=None, value=None):
        """
        AggregationWithValue - a model defined in Swagger
        """

        self._field = None
        self._aggregation_type = None
        self._value = None

        if field is not None:
          self.field = field
        if aggregation_type is not None:
          self.aggregation_type = aggregation_type
        if value is not None:
          self.value = value

    @property
    def field(self):
        """
        Gets the field of this AggregationWithValue.

        :return: The field of this AggregationWithValue.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this AggregationWithValue.

        :param field: The field of this AggregationWithValue.
        :type: str
        """

        self._field = field

    @property
    def aggregation_type(self):
        """
        Gets the aggregation_type of this AggregationWithValue.

        :return: The aggregation_type of this AggregationWithValue.
        :rtype: str
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """
        Sets the aggregation_type of this AggregationWithValue.

        :param aggregation_type: The aggregation_type of this AggregationWithValue.
        :type: str
        """
        allowed_values = ["SUM", "MIN", "MAX", "AVG"]
        if aggregation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_type` ({0}), must be one of {1}"
                .format(aggregation_type, allowed_values)
            )

        self._aggregation_type = aggregation_type

    @property
    def value(self):
        """
        Gets the value of this AggregationWithValue.

        :return: The value of this AggregationWithValue.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AggregationWithValue.

        :param value: The value of this AggregationWithValue.
        :type: float
        """

        self._value = value

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
        if not isinstance(other, AggregationWithValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
