# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PagedListResponseWithTime(object):
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
        'results': 'list[EntityIdWithTime]',
        'cursor': 'str',
        'total_count': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'results': 'results',
        'cursor': 'cursor',
        'total_count': 'total_count',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, results=None, cursor=None, total_count=None, start_time=None, end_time=None):
        """
        PagedListResponseWithTime - a model defined in Swagger
        """

        self._results = None
        self._cursor = None
        self._total_count = None
        self._start_time = None
        self._end_time = None

        if results is not None:
          self.results = results
        if cursor is not None:
          self.cursor = cursor
        if total_count is not None:
          self.total_count = total_count
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time

    @property
    def results(self):
        """
        Gets the results of this PagedListResponseWithTime.

        :return: The results of this PagedListResponseWithTime.
        :rtype: list[EntityIdWithTime]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this PagedListResponseWithTime.

        :param results: The results of this PagedListResponseWithTime.
        :type: list[EntityIdWithTime]
        """

        self._results = results

    @property
    def cursor(self):
        """
        Gets the cursor of this PagedListResponseWithTime.
        Cursor for the next page

        :return: The cursor of this PagedListResponseWithTime.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this PagedListResponseWithTime.
        Cursor for the next page

        :param cursor: The cursor of this PagedListResponseWithTime.
        :type: str
        """

        self._cursor = cursor

    @property
    def total_count(self):
        """
        Gets the total_count of this PagedListResponseWithTime.
        Total number of objects returned

        :return: The total_count of this PagedListResponseWithTime.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this PagedListResponseWithTime.
        Total number of objects returned

        :param total_count: The total_count of this PagedListResponseWithTime.
        :type: int
        """

        self._total_count = total_count

    @property
    def start_time(self):
        """
        Gets the start_time of this PagedListResponseWithTime.
        Start timestamp of the window of the objects returned

        :return: The start_time of this PagedListResponseWithTime.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this PagedListResponseWithTime.
        Start timestamp of the window of the objects returned

        :param start_time: The start_time of this PagedListResponseWithTime.
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this PagedListResponseWithTime.
        End timestamp of the window of the objects returned

        :return: The end_time of this PagedListResponseWithTime.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this PagedListResponseWithTime.
        End timestamp of the window of the objects returned

        :param end_time: The end_time of this PagedListResponseWithTime.
        :type: int
        """

        self._end_time = end_time

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
        if not isinstance(other, PagedListResponseWithTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
