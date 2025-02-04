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


class DiscoveredDeviceDto(object):
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
        'ip_or_fqdn': 'str',
        'supported_data_source': 'str',
        'ds_subtype': 'str',
        'os': 'str',
        'version': 'str',
        'model': 'str',
        'collector': 'str',
        'ssh_credential': 'PasswordCredentials',
        'api_credential': 'PasswordCredentials',
        'snmp_credential': 'SNMPConfig'
    }

    attribute_map = {
        'ip_or_fqdn': 'ip_or_fqdn',
        'supported_data_source': 'supported_data_source',
        'ds_subtype': 'ds_subtype',
        'os': 'os',
        'version': 'version',
        'model': 'model',
        'collector': 'collector',
        'ssh_credential': 'ssh_credential',
        'api_credential': 'api_credential',
        'snmp_credential': 'snmp_credential'
    }

    def __init__(self, ip_or_fqdn=None, supported_data_source=None, ds_subtype=None, os=None, version=None, model=None, collector=None, ssh_credential=None, api_credential=None, snmp_credential=None):
        """
        DiscoveredDeviceDto - a model defined in Swagger
        """

        self._ip_or_fqdn = None
        self._supported_data_source = None
        self._ds_subtype = None
        self._os = None
        self._version = None
        self._model = None
        self._collector = None
        self._ssh_credential = None
        self._api_credential = None
        self._snmp_credential = None

        if ip_or_fqdn is not None:
          self.ip_or_fqdn = ip_or_fqdn
        if supported_data_source is not None:
          self.supported_data_source = supported_data_source
        if ds_subtype is not None:
          self.ds_subtype = ds_subtype
        if os is not None:
          self.os = os
        if version is not None:
          self.version = version
        if model is not None:
          self.model = model
        if collector is not None:
          self.collector = collector
        if ssh_credential is not None:
          self.ssh_credential = ssh_credential
        if api_credential is not None:
          self.api_credential = api_credential
        if snmp_credential is not None:
          self.snmp_credential = snmp_credential

    @property
    def ip_or_fqdn(self):
        """
        Gets the ip_or_fqdn of this DiscoveredDeviceDto.
        device ip or fqdn

        :return: The ip_or_fqdn of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._ip_or_fqdn

    @ip_or_fqdn.setter
    def ip_or_fqdn(self, ip_or_fqdn):
        """
        Sets the ip_or_fqdn of this DiscoveredDeviceDto.
        device ip or fqdn

        :param ip_or_fqdn: The ip_or_fqdn of this DiscoveredDeviceDto.
        :type: str
        """

        self._ip_or_fqdn = ip_or_fqdn

    @property
    def supported_data_source(self):
        """
        Gets the supported_data_source of this DiscoveredDeviceDto.
        data source type

        :return: The supported_data_source of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._supported_data_source

    @supported_data_source.setter
    def supported_data_source(self, supported_data_source):
        """
        Sets the supported_data_source of this DiscoveredDeviceDto.
        data source type

        :param supported_data_source: The supported_data_source of this DiscoveredDeviceDto.
        :type: str
        """

        self._supported_data_source = supported_data_source

    @property
    def ds_subtype(self):
        """
        Gets the ds_subtype of this DiscoveredDeviceDto.
        data source subtype

        :return: The ds_subtype of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._ds_subtype

    @ds_subtype.setter
    def ds_subtype(self, ds_subtype):
        """
        Sets the ds_subtype of this DiscoveredDeviceDto.
        data source subtype

        :param ds_subtype: The ds_subtype of this DiscoveredDeviceDto.
        :type: str
        """

        self._ds_subtype = ds_subtype

    @property
    def os(self):
        """
        Gets the os of this DiscoveredDeviceDto.
        Device OS type

        :return: The os of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this DiscoveredDeviceDto.
        Device OS type

        :param os: The os of this DiscoveredDeviceDto.
        :type: str
        """

        self._os = os

    @property
    def version(self):
        """
        Gets the version of this DiscoveredDeviceDto.
        Device OS version

        :return: The version of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DiscoveredDeviceDto.
        Device OS version

        :param version: The version of this DiscoveredDeviceDto.
        :type: str
        """

        self._version = version

    @property
    def model(self):
        """
        Gets the model of this DiscoveredDeviceDto.
        Device Model

        :return: The model of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this DiscoveredDeviceDto.
        Device Model

        :param model: The model of this DiscoveredDeviceDto.
        :type: str
        """

        self._model = model

    @property
    def collector(self):
        """
        Gets the collector of this DiscoveredDeviceDto.
        Collector IP

        :return: The collector of this DiscoveredDeviceDto.
        :rtype: str
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """
        Sets the collector of this DiscoveredDeviceDto.
        Collector IP

        :param collector: The collector of this DiscoveredDeviceDto.
        :type: str
        """

        self._collector = collector

    @property
    def ssh_credential(self):
        """
        Gets the ssh_credential of this DiscoveredDeviceDto.

        :return: The ssh_credential of this DiscoveredDeviceDto.
        :rtype: PasswordCredentials
        """
        return self._ssh_credential

    @ssh_credential.setter
    def ssh_credential(self, ssh_credential):
        """
        Sets the ssh_credential of this DiscoveredDeviceDto.

        :param ssh_credential: The ssh_credential of this DiscoveredDeviceDto.
        :type: PasswordCredentials
        """

        self._ssh_credential = ssh_credential

    @property
    def api_credential(self):
        """
        Gets the api_credential of this DiscoveredDeviceDto.

        :return: The api_credential of this DiscoveredDeviceDto.
        :rtype: PasswordCredentials
        """
        return self._api_credential

    @api_credential.setter
    def api_credential(self, api_credential):
        """
        Sets the api_credential of this DiscoveredDeviceDto.

        :param api_credential: The api_credential of this DiscoveredDeviceDto.
        :type: PasswordCredentials
        """

        self._api_credential = api_credential

    @property
    def snmp_credential(self):
        """
        Gets the snmp_credential of this DiscoveredDeviceDto.

        :return: The snmp_credential of this DiscoveredDeviceDto.
        :rtype: SNMPConfig
        """
        return self._snmp_credential

    @snmp_credential.setter
    def snmp_credential(self, snmp_credential):
        """
        Sets the snmp_credential of this DiscoveredDeviceDto.

        :param snmp_credential: The snmp_credential of this DiscoveredDeviceDto.
        :type: SNMPConfig
        """

        self._snmp_credential = snmp_credential

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
        if not isinstance(other, DiscoveredDeviceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
