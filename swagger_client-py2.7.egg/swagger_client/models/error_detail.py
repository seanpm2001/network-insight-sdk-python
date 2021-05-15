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


class ErrorDetail(object):
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
        'code': 'int',
        'message': 'str',
        'target': 'list[str]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'target': 'target'
    }

    def __init__(self, code=None, message=None, target=None):
        """
        ErrorDetail - a model defined in Swagger
        """

        self._code = None
        self._message = None
        self._target = None

        if code is not None:
          self.code = code
        if message is not None:
          self.message = message
        if target is not None:
          self.target = target

    @property
    def code(self):
        """
        Gets the code of this ErrorDetail.

        :return: The code of this ErrorDetail.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorDetail.

        :param code: The code of this ErrorDetail.
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ErrorDetail.

        :return: The message of this ErrorDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorDetail.

        :param message: The message of this ErrorDetail.
        :type: str
        """

        self._message = message

    @property
    def target(self):
        """
        Gets the target of this ErrorDetail.

        :return: The target of this ErrorDetail.
        :rtype: list[str]
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this ErrorDetail.

        :param target: The target of this ErrorDetail.
        :type: list[str]
        """

        self._target = target

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
