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


class NSXVManagerDataSourceRequest(object):
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
        'vcenter_id': 'str',
        'ipfix_enabled': 'bool',
        'central_cli_enabled': 'bool',
        'latency_enabled': 'bool'
    }

    attribute_map = {
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'credentials': 'credentials',
        'vcenter_id': 'vcenter_id',
        'ipfix_enabled': 'ipfix_enabled',
        'central_cli_enabled': 'central_cli_enabled',
        'latency_enabled': 'latency_enabled'
    }

    def __init__(self, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, credentials=None, vcenter_id=None, ipfix_enabled=False, central_cli_enabled=False, latency_enabled=False):
        """
        NSXVManagerDataSourceRequest - a model defined in Swagger
        """

        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._credentials = None
        self._vcenter_id = None
        self._ipfix_enabled = None
        self._central_cli_enabled = None
        self._latency_enabled = None

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
        self.vcenter_id = vcenter_id
        if ipfix_enabled is not None:
          self.ipfix_enabled = ipfix_enabled
        if central_cli_enabled is not None:
          self.central_cli_enabled = central_cli_enabled
        if latency_enabled is not None:
          self.latency_enabled = latency_enabled

    @property
    def ip(self):
        """
        Gets the ip of this NSXVManagerDataSourceRequest.

        :return: The ip of this NSXVManagerDataSourceRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this NSXVManagerDataSourceRequest.

        :param ip: The ip of this NSXVManagerDataSourceRequest.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this NSXVManagerDataSourceRequest.

        :return: The fqdn of this NSXVManagerDataSourceRequest.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this NSXVManagerDataSourceRequest.

        :param fqdn: The fqdn of this NSXVManagerDataSourceRequest.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this NSXVManagerDataSourceRequest.
        proxy vm which should register this vcenter

        :return: The proxy_id of this NSXVManagerDataSourceRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this NSXVManagerDataSourceRequest.
        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this NSXVManagerDataSourceRequest.
        :type: str
        """
        if proxy_id is None:
            raise ValueError("Invalid value for `proxy_id`, must not be `None`")

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this NSXVManagerDataSourceRequest.

        :return: The nickname of this NSXVManagerDataSourceRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this NSXVManagerDataSourceRequest.

        :param nickname: The nickname of this NSXVManagerDataSourceRequest.
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this NSXVManagerDataSourceRequest.

        :return: The enabled of this NSXVManagerDataSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NSXVManagerDataSourceRequest.

        :param enabled: The enabled of this NSXVManagerDataSourceRequest.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this NSXVManagerDataSourceRequest.

        :return: The notes of this NSXVManagerDataSourceRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this NSXVManagerDataSourceRequest.

        :param notes: The notes of this NSXVManagerDataSourceRequest.
        :type: str
        """

        self._notes = notes

    @property
    def credentials(self):
        """
        Gets the credentials of this NSXVManagerDataSourceRequest.

        :return: The credentials of this NSXVManagerDataSourceRequest.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this NSXVManagerDataSourceRequest.

        :param credentials: The credentials of this NSXVManagerDataSourceRequest.
        :type: PasswordCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")

        self._credentials = credentials

    @property
    def vcenter_id(self):
        """
        Gets the vcenter_id of this NSXVManagerDataSourceRequest.
        Associated vcenter data source entity Id

        :return: The vcenter_id of this NSXVManagerDataSourceRequest.
        :rtype: str
        """
        return self._vcenter_id

    @vcenter_id.setter
    def vcenter_id(self, vcenter_id):
        """
        Sets the vcenter_id of this NSXVManagerDataSourceRequest.
        Associated vcenter data source entity Id

        :param vcenter_id: The vcenter_id of this NSXVManagerDataSourceRequest.
        :type: str
        """
        if vcenter_id is None:
            raise ValueError("Invalid value for `vcenter_id`, must not be `None`")

        self._vcenter_id = vcenter_id

    @property
    def ipfix_enabled(self):
        """
        Gets the ipfix_enabled of this NSXVManagerDataSourceRequest.

        :return: The ipfix_enabled of this NSXVManagerDataSourceRequest.
        :rtype: bool
        """
        return self._ipfix_enabled

    @ipfix_enabled.setter
    def ipfix_enabled(self, ipfix_enabled):
        """
        Sets the ipfix_enabled of this NSXVManagerDataSourceRequest.

        :param ipfix_enabled: The ipfix_enabled of this NSXVManagerDataSourceRequest.
        :type: bool
        """

        self._ipfix_enabled = ipfix_enabled

    @property
    def central_cli_enabled(self):
        """
        Gets the central_cli_enabled of this NSXVManagerDataSourceRequest.

        :return: The central_cli_enabled of this NSXVManagerDataSourceRequest.
        :rtype: bool
        """
        return self._central_cli_enabled

    @central_cli_enabled.setter
    def central_cli_enabled(self, central_cli_enabled):
        """
        Sets the central_cli_enabled of this NSXVManagerDataSourceRequest.

        :param central_cli_enabled: The central_cli_enabled of this NSXVManagerDataSourceRequest.
        :type: bool
        """

        self._central_cli_enabled = central_cli_enabled

    @property
    def latency_enabled(self):
        """
        Gets the latency_enabled of this NSXVManagerDataSourceRequest.

        :return: The latency_enabled of this NSXVManagerDataSourceRequest.
        :rtype: bool
        """
        return self._latency_enabled

    @latency_enabled.setter
    def latency_enabled(self, latency_enabled):
        """
        Sets the latency_enabled of this NSXVManagerDataSourceRequest.

        :param latency_enabled: The latency_enabled of this NSXVManagerDataSourceRequest.
        :type: bool
        """

        self._latency_enabled = latency_enabled

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
        if not isinstance(other, NSXVManagerDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
