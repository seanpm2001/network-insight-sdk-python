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


class MetricSchema(object):
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
        'metric': 'str',
        'display_name': 'str',
        'intervals': 'list[int]',
        'description': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'display_name': 'display_name',
        'intervals': 'intervals',
        'description': 'description',
        'unit': 'unit'
    }

    def __init__(self, metric=None, display_name=None, intervals=None, description=None, unit=None):
        """
        MetricSchema - a model defined in Swagger
        """

        self._metric = None
        self._display_name = None
        self._intervals = None
        self._description = None
        self._unit = None

        if metric is not None:
          self.metric = metric
        if display_name is not None:
          self.display_name = display_name
        if intervals is not None:
          self.intervals = intervals
        if description is not None:
          self.description = description
        if unit is not None:
          self.unit = unit

    @property
    def metric(self):
        """
        Gets the metric of this MetricSchema.

        :return: The metric of this MetricSchema.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MetricSchema.

        :param metric: The metric of this MetricSchema.
        :type: str
        """

        self._metric = metric

    @property
    def display_name(self):
        """
        Gets the display_name of this MetricSchema.

        :return: The display_name of this MetricSchema.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MetricSchema.

        :param display_name: The display_name of this MetricSchema.
        :type: str
        """

        self._display_name = display_name

    @property
    def intervals(self):
        """
        Gets the intervals of this MetricSchema.

        :return: The intervals of this MetricSchema.
        :rtype: list[int]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """
        Sets the intervals of this MetricSchema.

        :param intervals: The intervals of this MetricSchema.
        :type: list[int]
        """

        self._intervals = intervals

    @property
    def description(self):
        """
        Gets the description of this MetricSchema.

        :return: The description of this MetricSchema.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MetricSchema.

        :param description: The description of this MetricSchema.
        :type: str
        """

        self._description = description

    @property
    def unit(self):
        """
        Gets the unit of this MetricSchema.

        :return: The unit of this MetricSchema.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricSchema.

        :param unit: The unit of this MetricSchema.
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, MetricSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
