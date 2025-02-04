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


class DatasourceHealth(object):
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
        'health_status': 'str',
        'health_message': 'str',
        'health_error_code': 'str'
    }

    attribute_map = {
        'health_status': 'health_status',
        'health_message': 'health_message',
        'health_error_code': 'health_error_code'
    }

    def __init__(self, health_status=None, health_message=None, health_error_code=None):
        """
        DatasourceHealth - a model defined in Swagger
        """

        self._health_status = None
        self._health_message = None
        self._health_error_code = None

        if health_status is not None:
          self.health_status = health_status
        if health_message is not None:
          self.health_message = health_message
        if health_error_code is not None:
          self.health_error_code = health_error_code

    @property
    def health_status(self):
        """
        Gets the health_status of this DatasourceHealth.
        Is the data source healthy and data is being collected?

        :return: The health_status of this DatasourceHealth.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        """
        Sets the health_status of this DatasourceHealth.
        Is the data source healthy and data is being collected?

        :param health_status: The health_status of this DatasourceHealth.
        :type: str
        """
        allowed_values = ["HEALTHY", "HEALTHY_WITH_WARNINGS", "UNHEALTHY"]
        if health_status not in allowed_values:
            raise ValueError(
                "Invalid value for `health_status` ({0}), must be one of {1}"
                .format(health_status, allowed_values)
            )

        self._health_status = health_status

    @property
    def health_message(self):
        """
        Gets the health_message of this DatasourceHealth.
        Message for when the data source is not healthy

        :return: The health_message of this DatasourceHealth.
        :rtype: str
        """
        return self._health_message

    @health_message.setter
    def health_message(self, health_message):
        """
        Sets the health_message of this DatasourceHealth.
        Message for when the data source is not healthy

        :param health_message: The health_message of this DatasourceHealth.
        :type: str
        """

        self._health_message = health_message

    @property
    def health_error_code(self):
        """
        Gets the health_error_code of this DatasourceHealth.

        :return: The health_error_code of this DatasourceHealth.
        :rtype: str
        """
        return self._health_error_code

    @health_error_code.setter
    def health_error_code(self, health_error_code):
        """
        Sets the health_error_code of this DatasourceHealth.

        :param health_error_code: The health_error_code of this DatasourceHealth.
        :type: str
        """

        self._health_error_code = health_error_code

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
        if not isinstance(other, DatasourceHealth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
