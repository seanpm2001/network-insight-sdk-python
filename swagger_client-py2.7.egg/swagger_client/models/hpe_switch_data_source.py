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


class HPESwitchDataSource(object):
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
        'entity_id': 'str',
        'entity_type': 'DataSourceType',
        'ip': 'str',
        'fqdn': 'str',
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'certificate': 'str',
        'sha_thumbprint': 'str',
        'new_certificate': 'str',
        'new_sha_thumbprint': 'str',
        'config_polling_interval_in_min': 'str',
        'scheduled_config_polling_time': 'str',
        'scheduled_config_polling_days': 'str',
        'config_polling_interval_type': 'ConfigPollingIntervalType',
        'credentials': 'PasswordCredentials'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'ip': 'ip',
        'fqdn': 'fqdn',
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'certificate': 'certificate',
        'sha_thumbprint': 'sha_thumbprint',
        'new_certificate': 'new_certificate',
        'new_sha_thumbprint': 'new_sha_thumbprint',
        'config_polling_interval_in_min': 'config_polling_interval_in_min',
        'scheduled_config_polling_time': 'scheduled_config_polling_time',
        'scheduled_config_polling_days': 'scheduled_config_polling_days',
        'config_polling_interval_type': 'config_polling_interval_type',
        'credentials': 'credentials'
    }

    def __init__(self, entity_id=None, entity_type=None, ip=None, fqdn=None, proxy_id=None, nickname=None, enabled=True, notes=None, certificate=None, sha_thumbprint=None, new_certificate=None, new_sha_thumbprint=None, config_polling_interval_in_min=None, scheduled_config_polling_time=None, scheduled_config_polling_days=None, config_polling_interval_type=None, credentials=None):
        """
        HPESwitchDataSource - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._ip = None
        self._fqdn = None
        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._certificate = None
        self._sha_thumbprint = None
        self._new_certificate = None
        self._new_sha_thumbprint = None
        self._config_polling_interval_in_min = None
        self._scheduled_config_polling_time = None
        self._scheduled_config_polling_days = None
        self._config_polling_interval_type = None
        self._credentials = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if ip is not None:
          self.ip = ip
        if fqdn is not None:
          self.fqdn = fqdn
        if proxy_id is not None:
          self.proxy_id = proxy_id
        if nickname is not None:
          self.nickname = nickname
        if enabled is not None:
          self.enabled = enabled
        if notes is not None:
          self.notes = notes
        if certificate is not None:
          self.certificate = certificate
        if sha_thumbprint is not None:
          self.sha_thumbprint = sha_thumbprint
        if new_certificate is not None:
          self.new_certificate = new_certificate
        if new_sha_thumbprint is not None:
          self.new_sha_thumbprint = new_sha_thumbprint
        if config_polling_interval_in_min is not None:
          self.config_polling_interval_in_min = config_polling_interval_in_min
        if scheduled_config_polling_time is not None:
          self.scheduled_config_polling_time = scheduled_config_polling_time
        if scheduled_config_polling_days is not None:
          self.scheduled_config_polling_days = scheduled_config_polling_days
        if config_polling_interval_type is not None:
          self.config_polling_interval_type = config_polling_interval_type
        if credentials is not None:
          self.credentials = credentials

    @property
    def entity_id(self):
        """
        Gets the entity_id of this HPESwitchDataSource.
        Internal ID of data source, to be used in subsequent API calls

        :return: The entity_id of this HPESwitchDataSource.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this HPESwitchDataSource.
        Internal ID of data source, to be used in subsequent API calls

        :param entity_id: The entity_id of this HPESwitchDataSource.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this HPESwitchDataSource.

        :return: The entity_type of this HPESwitchDataSource.
        :rtype: DataSourceType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this HPESwitchDataSource.

        :param entity_type: The entity_type of this HPESwitchDataSource.
        :type: DataSourceType
        """

        self._entity_type = entity_type

    @property
    def ip(self):
        """
        Gets the ip of this HPESwitchDataSource.
        IP address of data source (use either IP or FQDN, not both)

        :return: The ip of this HPESwitchDataSource.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this HPESwitchDataSource.
        IP address of data source (use either IP or FQDN, not both)

        :param ip: The ip of this HPESwitchDataSource.
        :type: str
        """

        self._ip = ip

    @property
    def fqdn(self):
        """
        Gets the fqdn of this HPESwitchDataSource.
        Hostname of data source (use either IP or FQDN, not both)

        :return: The fqdn of this HPESwitchDataSource.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this HPESwitchDataSource.
        Hostname of data source (use either IP or FQDN, not both)

        :param fqdn: The fqdn of this HPESwitchDataSource.
        :type: str
        """

        self._fqdn = fqdn

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this HPESwitchDataSource.
        ID of Collector VM which should register this vcenter

        :return: The proxy_id of this HPESwitchDataSource.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this HPESwitchDataSource.
        ID of Collector VM which should register this vcenter

        :param proxy_id: The proxy_id of this HPESwitchDataSource.
        :type: str
        """

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this HPESwitchDataSource.
        A friendly nickname for the data source

        :return: The nickname of this HPESwitchDataSource.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this HPESwitchDataSource.
        A friendly nickname for the data source

        :param nickname: The nickname of this HPESwitchDataSource.
        :type: str
        """

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this HPESwitchDataSource.
        Whether or not data collection is enabled

        :return: The enabled of this HPESwitchDataSource.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this HPESwitchDataSource.
        Whether or not data collection is enabled

        :param enabled: The enabled of this HPESwitchDataSource.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this HPESwitchDataSource.
        Room for notes or comments about the data source

        :return: The notes of this HPESwitchDataSource.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this HPESwitchDataSource.
        Room for notes or comments about the data source

        :param notes: The notes of this HPESwitchDataSource.
        :type: str
        """

        self._notes = notes

    @property
    def certificate(self):
        """
        Gets the certificate of this HPESwitchDataSource.
        Certificate of data source

        :return: The certificate of this HPESwitchDataSource.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """
        Sets the certificate of this HPESwitchDataSource.
        Certificate of data source

        :param certificate: The certificate of this HPESwitchDataSource.
        :type: str
        """

        self._certificate = certificate

    @property
    def sha_thumbprint(self):
        """
        Gets the sha_thumbprint of this HPESwitchDataSource.
        SHA thumbprint of data source

        :return: The sha_thumbprint of this HPESwitchDataSource.
        :rtype: str
        """
        return self._sha_thumbprint

    @sha_thumbprint.setter
    def sha_thumbprint(self, sha_thumbprint):
        """
        Sets the sha_thumbprint of this HPESwitchDataSource.
        SHA thumbprint of data source

        :param sha_thumbprint: The sha_thumbprint of this HPESwitchDataSource.
        :type: str
        """

        self._sha_thumbprint = sha_thumbprint

    @property
    def new_certificate(self):
        """
        Gets the new_certificate of this HPESwitchDataSource.
        New certificate of data source

        :return: The new_certificate of this HPESwitchDataSource.
        :rtype: str
        """
        return self._new_certificate

    @new_certificate.setter
    def new_certificate(self, new_certificate):
        """
        Sets the new_certificate of this HPESwitchDataSource.
        New certificate of data source

        :param new_certificate: The new_certificate of this HPESwitchDataSource.
        :type: str
        """

        self._new_certificate = new_certificate

    @property
    def new_sha_thumbprint(self):
        """
        Gets the new_sha_thumbprint of this HPESwitchDataSource.
        New SHA thumbprint of data source

        :return: The new_sha_thumbprint of this HPESwitchDataSource.
        :rtype: str
        """
        return self._new_sha_thumbprint

    @new_sha_thumbprint.setter
    def new_sha_thumbprint(self, new_sha_thumbprint):
        """
        Sets the new_sha_thumbprint of this HPESwitchDataSource.
        New SHA thumbprint of data source

        :param new_sha_thumbprint: The new_sha_thumbprint of this HPESwitchDataSource.
        :type: str
        """

        self._new_sha_thumbprint = new_sha_thumbprint

    @property
    def config_polling_interval_in_min(self):
        """
        Gets the config_polling_interval_in_min of this HPESwitchDataSource.
        Config polling interval to be provided in minutes. Preset values are [10 min, 15 min, 30 min, 1 hour, 12 hours, 1 day, 3 days, 5 days, 7 days]. For any other polling interval, CUSTOM polling interval type should be used. Minimum- 10 minutes, Maximum- 7 days

        :return: The config_polling_interval_in_min of this HPESwitchDataSource.
        :rtype: str
        """
        return self._config_polling_interval_in_min

    @config_polling_interval_in_min.setter
    def config_polling_interval_in_min(self, config_polling_interval_in_min):
        """
        Sets the config_polling_interval_in_min of this HPESwitchDataSource.
        Config polling interval to be provided in minutes. Preset values are [10 min, 15 min, 30 min, 1 hour, 12 hours, 1 day, 3 days, 5 days, 7 days]. For any other polling interval, CUSTOM polling interval type should be used. Minimum- 10 minutes, Maximum- 7 days

        :param config_polling_interval_in_min: The config_polling_interval_in_min of this HPESwitchDataSource.
        :type: str
        """

        self._config_polling_interval_in_min = config_polling_interval_in_min

    @property
    def scheduled_config_polling_time(self):
        """
        Gets the scheduled_config_polling_time of this HPESwitchDataSource.
        Scheduled time (UTC) to be provided. This is only applicable when config_polling_interval_type is SCHEDULED

        :return: The scheduled_config_polling_time of this HPESwitchDataSource.
        :rtype: str
        """
        return self._scheduled_config_polling_time

    @scheduled_config_polling_time.setter
    def scheduled_config_polling_time(self, scheduled_config_polling_time):
        """
        Sets the scheduled_config_polling_time of this HPESwitchDataSource.
        Scheduled time (UTC) to be provided. This is only applicable when config_polling_interval_type is SCHEDULED

        :param scheduled_config_polling_time: The scheduled_config_polling_time of this HPESwitchDataSource.
        :type: str
        """

        self._scheduled_config_polling_time = scheduled_config_polling_time

    @property
    def scheduled_config_polling_days(self):
        """
        Gets the scheduled_config_polling_days of this HPESwitchDataSource.
        Scheduled config polling days. Supported values are weekdays. Multiple days separated with comma can be supplied. This is only applicable when config_polling_interval_type is SCHEDULED

        :return: The scheduled_config_polling_days of this HPESwitchDataSource.
        :rtype: str
        """
        return self._scheduled_config_polling_days

    @scheduled_config_polling_days.setter
    def scheduled_config_polling_days(self, scheduled_config_polling_days):
        """
        Sets the scheduled_config_polling_days of this HPESwitchDataSource.
        Scheduled config polling days. Supported values are weekdays. Multiple days separated with comma can be supplied. This is only applicable when config_polling_interval_type is SCHEDULED

        :param scheduled_config_polling_days: The scheduled_config_polling_days of this HPESwitchDataSource.
        :type: str
        """

        self._scheduled_config_polling_days = scheduled_config_polling_days

    @property
    def config_polling_interval_type(self):
        """
        Gets the config_polling_interval_type of this HPESwitchDataSource.

        :return: The config_polling_interval_type of this HPESwitchDataSource.
        :rtype: ConfigPollingIntervalType
        """
        return self._config_polling_interval_type

    @config_polling_interval_type.setter
    def config_polling_interval_type(self, config_polling_interval_type):
        """
        Sets the config_polling_interval_type of this HPESwitchDataSource.

        :param config_polling_interval_type: The config_polling_interval_type of this HPESwitchDataSource.
        :type: ConfigPollingIntervalType
        """

        self._config_polling_interval_type = config_polling_interval_type

    @property
    def credentials(self):
        """
        Gets the credentials of this HPESwitchDataSource.

        :return: The credentials of this HPESwitchDataSource.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this HPESwitchDataSource.

        :param credentials: The credentials of this HPESwitchDataSource.
        :type: PasswordCredentials
        """

        self._credentials = credentials

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
        if not isinstance(other, HPESwitchDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
