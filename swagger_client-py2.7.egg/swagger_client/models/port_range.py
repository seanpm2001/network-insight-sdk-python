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


class PortRange(object):
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
        'start': 'int',
        'end': 'int',
        'display': 'str',
        'iana_name': 'str',
        'iana_port_display': 'str'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'display': 'display',
        'iana_name': 'iana_name',
        'iana_port_display': 'iana_port_display'
    }

    def __init__(self, start=None, end=None, display=None, iana_name=None, iana_port_display=None):
        """
        PortRange - a model defined in Swagger
        """

        self._start = None
        self._end = None
        self._display = None
        self._iana_name = None
        self._iana_port_display = None

        if start is not None:
          self.start = start
        if end is not None:
          self.end = end
        if display is not None:
          self.display = display
        if iana_name is not None:
          self.iana_name = iana_name
        if iana_port_display is not None:
          self.iana_port_display = iana_port_display

    @property
    def start(self):
        """
        Gets the start of this PortRange.

        :return: The start of this PortRange.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this PortRange.

        :param start: The start of this PortRange.
        :type: int
        """

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this PortRange.

        :return: The end of this PortRange.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this PortRange.

        :param end: The end of this PortRange.
        :type: int
        """

        self._end = end

    @property
    def display(self):
        """
        Gets the display of this PortRange.

        :return: The display of this PortRange.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this PortRange.

        :param display: The display of this PortRange.
        :type: str
        """

        self._display = display

    @property
    def iana_name(self):
        """
        Gets the iana_name of this PortRange.

        :return: The iana_name of this PortRange.
        :rtype: str
        """
        return self._iana_name

    @iana_name.setter
    def iana_name(self, iana_name):
        """
        Sets the iana_name of this PortRange.

        :param iana_name: The iana_name of this PortRange.
        :type: str
        """

        self._iana_name = iana_name

    @property
    def iana_port_display(self):
        """
        Gets the iana_port_display of this PortRange.

        :return: The iana_port_display of this PortRange.
        :rtype: str
        """
        return self._iana_port_display

    @iana_port_display.setter
    def iana_port_display(self, iana_port_display):
        """
        Sets the iana_port_display of this PortRange.

        :param iana_port_display: The iana_port_display of this PortRange.
        :type: str
        """

        self._iana_port_display = iana_port_display

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
        if not isinstance(other, PortRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
