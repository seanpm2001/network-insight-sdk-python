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


class SearchGroupByResponse(object):
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
        'results': 'list[GroupWithValue]',
        'size': 'int',
        'total_bucket': 'Cardinality',
        'total_count': 'int',
        'time_range': 'TimeRange',
        'cursor': 'str'
    }

    attribute_map = {
        'results': 'results',
        'size': 'size',
        'total_bucket': 'total_bucket',
        'total_count': 'total_count',
        'time_range': 'time_range',
        'cursor': 'cursor'
    }

    def __init__(self, results=None, size=None, total_bucket=None, total_count=None, time_range=None, cursor=None):
        """
        SearchGroupByResponse - a model defined in Swagger
        """

        self._results = None
        self._size = None
        self._total_bucket = None
        self._total_count = None
        self._time_range = None
        self._cursor = None

        if results is not None:
          self.results = results
        if size is not None:
          self.size = size
        if total_bucket is not None:
          self.total_bucket = total_bucket
        if total_count is not None:
          self.total_count = total_count
        if time_range is not None:
          self.time_range = time_range
        if cursor is not None:
          self.cursor = cursor

    @property
    def results(self):
        """
        Gets the results of this SearchGroupByResponse.

        :return: The results of this SearchGroupByResponse.
        :rtype: list[GroupWithValue]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this SearchGroupByResponse.

        :param results: The results of this SearchGroupByResponse.
        :type: list[GroupWithValue]
        """

        self._results = results

    @property
    def size(self):
        """
        Gets the size of this SearchGroupByResponse.

        :return: The size of this SearchGroupByResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SearchGroupByResponse.

        :param size: The size of this SearchGroupByResponse.
        :type: int
        """

        self._size = size

    @property
    def total_bucket(self):
        """
        Gets the total_bucket of this SearchGroupByResponse.

        :return: The total_bucket of this SearchGroupByResponse.
        :rtype: Cardinality
        """
        return self._total_bucket

    @total_bucket.setter
    def total_bucket(self, total_bucket):
        """
        Sets the total_bucket of this SearchGroupByResponse.

        :param total_bucket: The total_bucket of this SearchGroupByResponse.
        :type: Cardinality
        """

        self._total_bucket = total_bucket

    @property
    def total_count(self):
        """
        Gets the total_count of this SearchGroupByResponse.
        Total count of objects returned

        :return: The total_count of this SearchGroupByResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this SearchGroupByResponse.
        Total count of objects returned

        :param total_count: The total_count of this SearchGroupByResponse.
        :type: int
        """

        self._total_count = total_count

    @property
    def time_range(self):
        """
        Gets the time_range of this SearchGroupByResponse.

        :return: The time_range of this SearchGroupByResponse.
        :rtype: TimeRange
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """
        Sets the time_range of this SearchGroupByResponse.

        :param time_range: The time_range of this SearchGroupByResponse.
        :type: TimeRange
        """

        self._time_range = time_range

    @property
    def cursor(self):
        """
        Gets the cursor of this SearchGroupByResponse.
        Cursor for the next page

        :return: The cursor of this SearchGroupByResponse.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this SearchGroupByResponse.
        Cursor for the next page

        :param cursor: The cursor of this SearchGroupByResponse.
        :type: str
        """

        self._cursor = cursor

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
        if not isinstance(other, SearchGroupByResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
