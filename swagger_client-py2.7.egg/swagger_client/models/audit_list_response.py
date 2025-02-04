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


class AuditListResponse(object):
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
        'results': 'list[AuditResponse]',
        'cursor': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'results': 'results',
        'cursor': 'cursor',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, results=None, cursor=None, start_time=None, end_time=None):
        """
        AuditListResponse - a model defined in Swagger
        """

        self._results = None
        self._cursor = None
        self._start_time = None
        self._end_time = None

        if results is not None:
          self.results = results
        if cursor is not None:
          self.cursor = cursor
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time

    @property
    def results(self):
        """
        Gets the results of this AuditListResponse.

        :return: The results of this AuditListResponse.
        :rtype: list[AuditResponse]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this AuditListResponse.

        :param results: The results of this AuditListResponse.
        :type: list[AuditResponse]
        """

        self._results = results

    @property
    def cursor(self):
        """
        Gets the cursor of this AuditListResponse.
        Cursor for the next page of logs

        :return: The cursor of this AuditListResponse.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this AuditListResponse.
        Cursor for the next page of logs

        :param cursor: The cursor of this AuditListResponse.
        :type: str
        """

        self._cursor = cursor

    @property
    def start_time(self):
        """
        Gets the start_time of this AuditListResponse.
        Start timestamp of the window of the objects returned

        :return: The start_time of this AuditListResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this AuditListResponse.
        Start timestamp of the window of the objects returned

        :param start_time: The start_time of this AuditListResponse.
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this AuditListResponse.
        End timestamp of the window of the objects returned

        :return: The end_time of this AuditListResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this AuditListResponse.
        End timestamp of the window of the objects returned

        :param end_time: The end_time of this AuditListResponse.
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
        if not isinstance(other, AuditListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
