# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXTManagerDataSourceRequest(object):
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
        'ip': 'str',
        'fqdn': 'str',
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'credentials': 'PasswordCredentials',
        'ipfix_enabled': 'bool',
        'latency_enabled': 'bool',
        'nsxi_enabled': 'bool'
    }

    attribute_map = {
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'credentials': 'credentials',
        'ipfix_enabled': 'ipfix_enabled',
        'latency_enabled': 'latency_enabled',
        'nsxi_enabled': 'nsxi_enabled'
    }

    def __init__(self, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, credentials=None, ipfix_enabled=False, latency_enabled=False, nsxi_enabled=False):
        """
        NSXTManagerDataSourceRequest - a model defined in Swagger
        """

        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._credentials = None
        self._ipfix_enabled = None
        self._latency_enabled = None
        self._nsxi_enabled = None

        if ip is not None:
          self.ip = ip
        if fqdn is not None:
          self.fqdn = fqdn
        self.proxy_id = proxy_id
        self.nickname = nickname
        if enabled is not None:
          self.enabled = enabled
        if notes is not None:
          self.notes = notes
        self.credentials = credentials
        if ipfix_enabled is not None:
          self.ipfix_enabled = ipfix_enabled
        if latency_enabled is not None:
          self.latency_enabled = latency_enabled
        if nsxi_enabled is not None:
          self.nsxi_enabled = nsxi_enabled

    @property
    def ip(self):
        """
        Gets the ip of this NSXTManagerDataSourceRequest.

        :return: The ip of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NSXTManagerDataSourceRequest.

        :param ip: The ip of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this NSXTManagerDataSourceRequest.

        :return: The fqdn of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this NSXTManagerDataSourceRequest.

        :param fqdn: The fqdn of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this NSXTManagerDataSourceRequest.
        proxy vm which should register this vcenter

        :return: The proxy_id of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this NSXTManagerDataSourceRequest.
        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this NSXTManagerDataSourceRequest.
        :type: str
        """
        if proxy_id is None:
            raise ValueError("Invalid value for `proxy_id`, must not be `None`")

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this NSXTManagerDataSourceRequest.

        :return: The nickname of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this NSXTManagerDataSourceRequest.

        :param nickname: The nickname of this NSXTManagerDataSourceRequest.
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this NSXTManagerDataSourceRequest.

        :return: The enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NSXTManagerDataSourceRequest.

        :param enabled: The enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this NSXTManagerDataSourceRequest.

        :return: The notes of this NSXTManagerDataSourceRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this NSXTManagerDataSourceRequest.

        :param notes: The notes of this NSXTManagerDataSourceRequest.
        :type: str
        """

        self._notes = notes

    @property
    def credentials(self):
        """
        Gets the credentials of this NSXTManagerDataSourceRequest.

        :return: The credentials of this NSXTManagerDataSourceRequest.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this NSXTManagerDataSourceRequest.

        :param credentials: The credentials of this NSXTManagerDataSourceRequest.
        :type: PasswordCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")

        self._credentials = credentials

    @property
    def ipfix_enabled(self):
        """
        Gets the ipfix_enabled of this NSXTManagerDataSourceRequest.

        :return: The ipfix_enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._ipfix_enabled

    @ipfix_enabled.setter
    def ipfix_enabled(self, ipfix_enabled):
        """
        Sets the ipfix_enabled of this NSXTManagerDataSourceRequest.

        :param ipfix_enabled: The ipfix_enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._ipfix_enabled = ipfix_enabled

    @property
    def latency_enabled(self):
        """
        Gets the latency_enabled of this NSXTManagerDataSourceRequest.

        :return: The latency_enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._latency_enabled

    @latency_enabled.setter
    def latency_enabled(self, latency_enabled):
        """
        Sets the latency_enabled of this NSXTManagerDataSourceRequest.

        :param latency_enabled: The latency_enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._latency_enabled = latency_enabled

    @property
    def nsxi_enabled(self):
        """
        Gets the nsxi_enabled of this NSXTManagerDataSourceRequest.

        :return: The nsxi_enabled of this NSXTManagerDataSourceRequest.
        :rtype: bool
        """
        return self._nsxi_enabled

    @nsxi_enabled.setter
    def nsxi_enabled(self, nsxi_enabled):
        """
        Sets the nsxi_enabled of this NSXTManagerDataSourceRequest.

        :param nsxi_enabled: The nsxi_enabled of this NSXTManagerDataSourceRequest.
        :type: bool
        """

        self._nsxi_enabled = nsxi_enabled

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
        if not isinstance(other, NSXTManagerDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
