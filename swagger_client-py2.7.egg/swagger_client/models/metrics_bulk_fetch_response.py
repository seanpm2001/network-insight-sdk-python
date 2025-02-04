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


class MetricsBulkFetchResponse(object):
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
        'interval': 'int',
        'start': 'int',
        'end': 'int',
        'display_name': 'str',
        'unit': 'str',
        'results': 'list[MetricResponseForEntity]'
    }

    attribute_map = {
        'metric': 'metric',
        'interval': 'interval',
        'start': 'start',
        'end': 'end',
        'display_name': 'display_name',
        'unit': 'unit',
        'results': 'results'
    }

    def __init__(self, metric=None, interval=None, start=None, end=None, display_name=None, unit=None, results=None):
        """
        MetricsBulkFetchResponse - a model defined in Swagger
        """

        self._metric = None
        self._interval = None
        self._start = None
        self._end = None
        self._display_name = None
        self._unit = None
        self._results = None

        if metric is not None:
          self.metric = metric
        if interval is not None:
          self.interval = interval
        if start is not None:
          self.start = start
        if end is not None:
          self.end = end
        if display_name is not None:
          self.display_name = display_name
        if unit is not None:
          self.unit = unit
        if results is not None:
          self.results = results

    @property
    def metric(self):
        """
        Gets the metric of this MetricsBulkFetchResponse.

        :return: The metric of this MetricsBulkFetchResponse.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this MetricsBulkFetchResponse.

        :param metric: The metric of this MetricsBulkFetchResponse.
        :type: str
        """

        self._metric = metric

    @property
    def interval(self):
        """
        Gets the interval of this MetricsBulkFetchResponse.

        :return: The interval of this MetricsBulkFetchResponse.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this MetricsBulkFetchResponse.

        :param interval: The interval of this MetricsBulkFetchResponse.
        :type: int
        """

        self._interval = interval

    @property
    def start(self):
        """
        Gets the start of this MetricsBulkFetchResponse.

        :return: The start of this MetricsBulkFetchResponse.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this MetricsBulkFetchResponse.

        :param start: The start of this MetricsBulkFetchResponse.
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this MetricsBulkFetchResponse.

        :return: The end of this MetricsBulkFetchResponse.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this MetricsBulkFetchResponse.

        :param end: The end of this MetricsBulkFetchResponse.
        :type: int
        """

        self._end = end

    @property
    def display_name(self):
        """
        Gets the display_name of this MetricsBulkFetchResponse.

        :return: The display_name of this MetricsBulkFetchResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MetricsBulkFetchResponse.

        :param display_name: The display_name of this MetricsBulkFetchResponse.
        :type: str
        """

        self._display_name = display_name

    @property
    def unit(self):
        """
        Gets the unit of this MetricsBulkFetchResponse.

        :return: The unit of this MetricsBulkFetchResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this MetricsBulkFetchResponse.

        :param unit: The unit of this MetricsBulkFetchResponse.
        :type: str
        """

        self._unit = unit

    @property
    def results(self):
        """
        Gets the results of this MetricsBulkFetchResponse.

        :return: The results of this MetricsBulkFetchResponse.
        :rtype: list[MetricResponseForEntity]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this MetricsBulkFetchResponse.

        :param results: The results of this MetricsBulkFetchResponse.
        :type: list[MetricResponseForEntity]
        """

        self._results = results

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
        if not isinstance(other, MetricsBulkFetchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
