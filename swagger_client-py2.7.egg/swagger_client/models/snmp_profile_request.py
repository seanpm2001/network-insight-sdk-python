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


class SnmpProfileRequest(object):
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
        'nick_name': 'str',
        'target_ip': 'str',
        'target_port': 'int',
        'snmp_version': 'str',
        'snmp_v2c': 'SNMP2cConfig',
        'snmp_v3': 'SNMP3Config'
    }

    attribute_map = {
        'nick_name': 'nick_name',
        'target_ip': 'target_ip',
        'target_port': 'target_port',
        'snmp_version': 'snmp_version',
        'snmp_v2c': 'snmp_v2c',
        'snmp_v3': 'snmp_v3'
    }

    def __init__(self, nick_name=None, target_ip=None, target_port=None, snmp_version=None, snmp_v2c=None, snmp_v3=None):
        """
        SnmpProfileRequest - a model defined in Swagger
        """

        self._nick_name = None
        self._target_ip = None
        self._target_port = None
        self._snmp_version = None
        self._snmp_v2c = None
        self._snmp_v3 = None

        if nick_name is not None:
          self.nick_name = nick_name
        if target_ip is not None:
          self.target_ip = target_ip
        if target_port is not None:
          self.target_port = target_port
        if snmp_version is not None:
          self.snmp_version = snmp_version
        if snmp_v2c is not None:
          self.snmp_v2c = snmp_v2c
        if snmp_v3 is not None:
          self.snmp_v3 = snmp_v3

    @property
    def nick_name(self):
        """
        Gets the nick_name of this SnmpProfileRequest.
        Descriptor or identifier for particular SNMP profile.

        :return: The nick_name of this SnmpProfileRequest.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """
        Sets the nick_name of this SnmpProfileRequest.
        Descriptor or identifier for particular SNMP profile.

        :param nick_name: The nick_name of this SnmpProfileRequest.
        :type: str
        """

        self._nick_name = nick_name

    @property
    def target_ip(self):
        """
        Gets the target_ip of this SnmpProfileRequest.
        IP address of SNMP target destination

        :return: The target_ip of this SnmpProfileRequest.
        :rtype: str
        """
        return self._target_ip

    @target_ip.setter
    def target_ip(self, target_ip):
        """
        Sets the target_ip of this SnmpProfileRequest.
        IP address of SNMP target destination

        :param target_ip: The target_ip of this SnmpProfileRequest.
        :type: str
        """

        self._target_ip = target_ip

    @property
    def target_port(self):
        """
        Gets the target_port of this SnmpProfileRequest.
        Receiving port number of SNMP target destination

        :return: The target_port of this SnmpProfileRequest.
        :rtype: int
        """
        return self._target_port

    @target_port.setter
    def target_port(self, target_port):
        """
        Sets the target_port of this SnmpProfileRequest.
        Receiving port number of SNMP target destination

        :param target_port: The target_port of this SnmpProfileRequest.
        :type: int
        """

        self._target_port = target_port

    @property
    def snmp_version(self):
        """
        Gets the snmp_version of this SnmpProfileRequest.

        :return: The snmp_version of this SnmpProfileRequest.
        :rtype: str
        """
        return self._snmp_version

    @snmp_version.setter
    def snmp_version(self, snmp_version):
        """
        Sets the snmp_version of this SnmpProfileRequest.

        :param snmp_version: The snmp_version of this SnmpProfileRequest.
        :type: str
        """
        allowed_values = ["v2c", "v3"]
        if snmp_version not in allowed_values:
            raise ValueError(
                "Invalid value for `snmp_version` ({0}), must be one of {1}"
                .format(snmp_version, allowed_values)
            )

        self._snmp_version = snmp_version

    @property
    def snmp_v2c(self):
        """
        Gets the snmp_v2c of this SnmpProfileRequest.

        :return: The snmp_v2c of this SnmpProfileRequest.
        :rtype: SNMP2cConfig
        """
        return self._snmp_v2c

    @snmp_v2c.setter
    def snmp_v2c(self, snmp_v2c):
        """
        Sets the snmp_v2c of this SnmpProfileRequest.

        :param snmp_v2c: The snmp_v2c of this SnmpProfileRequest.
        :type: SNMP2cConfig
        """

        self._snmp_v2c = snmp_v2c

    @property
    def snmp_v3(self):
        """
        Gets the snmp_v3 of this SnmpProfileRequest.

        :return: The snmp_v3 of this SnmpProfileRequest.
        :rtype: SNMP3Config
        """
        return self._snmp_v3

    @snmp_v3.setter
    def snmp_v3(self, snmp_v3):
        """
        Sets the snmp_v3 of this SnmpProfileRequest.

        :param snmp_v3: The snmp_v3 of this SnmpProfileRequest.
        :type: SNMP3Config
        """

        self._snmp_v3 = snmp_v3

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
        if not isinstance(other, SnmpProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
