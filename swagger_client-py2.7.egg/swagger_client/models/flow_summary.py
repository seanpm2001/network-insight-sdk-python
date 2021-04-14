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


class FlowSummary(object):
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
        'ingress_bytes': 'int',
        'egress_bytes': 'int'
    }

    attribute_map = {
        'ingress_bytes': 'ingress_bytes',
        'egress_bytes': 'egress_bytes'
    }

    def __init__(self, ingress_bytes=0, egress_bytes=0):
        """
        FlowSummary - a model defined in Swagger
        """

        self._ingress_bytes = None
        self._egress_bytes = None

        if ingress_bytes is not None:
          self.ingress_bytes = ingress_bytes
        if egress_bytes is not None:
          self.egress_bytes = egress_bytes

    @property
    def ingress_bytes(self):
        """
        Gets the ingress_bytes of this FlowSummary.
        Incoming traffic in bytes

        :return: The ingress_bytes of this FlowSummary.
        :rtype: int
        """
        return self._ingress_bytes

    @ingress_bytes.setter
    def ingress_bytes(self, ingress_bytes):
        """
        Sets the ingress_bytes of this FlowSummary.
        Incoming traffic in bytes

        :param ingress_bytes: The ingress_bytes of this FlowSummary.
        :type: int
        """

        self._ingress_bytes = ingress_bytes

    @property
    def egress_bytes(self):
        """
        Gets the egress_bytes of this FlowSummary.
        Outgoing traffic in bytes

        :return: The egress_bytes of this FlowSummary.
        :rtype: int
        """
        return self._egress_bytes

    @egress_bytes.setter
    def egress_bytes(self, egress_bytes):
        """
        Sets the egress_bytes of this FlowSummary.
        Outgoing traffic in bytes

        :param egress_bytes: The egress_bytes of this FlowSummary.
        :type: int
        """

        self._egress_bytes = egress_bytes

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
        if not isinstance(other, FlowSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
