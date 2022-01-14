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


class DeviceDiscoveryRequest(object):
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
        'config_polling_interval_in_min': 'str',
        'scheduled_config_polling_time': 'str',
        'scheduled_config_polling_days': 'str',
        'config_polling_interval_type': 'ConfigPollingIntervalType',
        'name': 'str',
        'network_ranges': 'list[str]',
        'seeds': 'list[str]',
        'seed_depth': 'int',
        'ignored_list': 'list[str]',
        'credential_profiles': 'list[str]',
        'proxy_id': 'str'
    }

    attribute_map = {
        'config_polling_interval_in_min': 'config_polling_interval_in_min',
        'scheduled_config_polling_time': 'scheduled_config_polling_time',
        'scheduled_config_polling_days': 'scheduled_config_polling_days',
        'config_polling_interval_type': 'config_polling_interval_type',
        'name': 'name',
        'network_ranges': 'network_ranges',
        'seeds': 'seeds',
        'seed_depth': 'seedDepth',
        'ignored_list': 'ignored_list',
        'credential_profiles': 'credential_profiles',
        'proxy_id': 'proxy_id'
    }

    def __init__(self, config_polling_interval_in_min=None, scheduled_config_polling_time=None, scheduled_config_polling_days=None, config_polling_interval_type=None, name=None, network_ranges=None, seeds=None, seed_depth=None, ignored_list=None, credential_profiles=None, proxy_id=None):
        """
        DeviceDiscoveryRequest - a model defined in Swagger
        """

        self._config_polling_interval_in_min = None
        self._scheduled_config_polling_time = None
        self._scheduled_config_polling_days = None
        self._config_polling_interval_type = None
        self._name = None
        self._network_ranges = None
        self._seeds = None
        self._seed_depth = None
        self._ignored_list = None
        self._credential_profiles = None
        self._proxy_id = None

        if config_polling_interval_in_min is not None:
          self.config_polling_interval_in_min = config_polling_interval_in_min
        if scheduled_config_polling_time is not None:
          self.scheduled_config_polling_time = scheduled_config_polling_time
        if scheduled_config_polling_days is not None:
          self.scheduled_config_polling_days = scheduled_config_polling_days
        if config_polling_interval_type is not None:
          self.config_polling_interval_type = config_polling_interval_type
        if name is not None:
          self.name = name
        if network_ranges is not None:
          self.network_ranges = network_ranges
        if seeds is not None:
          self.seeds = seeds
        if seed_depth is not None:
          self.seed_depth = seed_depth
        if ignored_list is not None:
          self.ignored_list = ignored_list
        if credential_profiles is not None:
          self.credential_profiles = credential_profiles
        if proxy_id is not None:
          self.proxy_id = proxy_id

    @property
    def config_polling_interval_in_min(self):
        """
        Gets the config_polling_interval_in_min of this DeviceDiscoveryRequest.
        Config polling interval to be provided in minutes. Preset values are [10 min, 15 min, 30 min, 1 hour, 12 hours, 1 day, 3 days, 5 days, 7 days]. For any other polling interval, CUSTOM polling interval type should be used. Minimum- 10 minutes, Maximum- 7 days

        :return: The config_polling_interval_in_min of this DeviceDiscoveryRequest.
        :rtype: str
        """
        return self._config_polling_interval_in_min

    @config_polling_interval_in_min.setter
    def config_polling_interval_in_min(self, config_polling_interval_in_min):
        """
        Sets the config_polling_interval_in_min of this DeviceDiscoveryRequest.
        Config polling interval to be provided in minutes. Preset values are [10 min, 15 min, 30 min, 1 hour, 12 hours, 1 day, 3 days, 5 days, 7 days]. For any other polling interval, CUSTOM polling interval type should be used. Minimum- 10 minutes, Maximum- 7 days

        :param config_polling_interval_in_min: The config_polling_interval_in_min of this DeviceDiscoveryRequest.
        :type: str
        """

        self._config_polling_interval_in_min = config_polling_interval_in_min

    @property
    def scheduled_config_polling_time(self):
        """
        Gets the scheduled_config_polling_time of this DeviceDiscoveryRequest.
        Scheduled time (UTC) to be provided. This is only applicable when config_polling_interval_type is SCHEDULED

        :return: The scheduled_config_polling_time of this DeviceDiscoveryRequest.
        :rtype: str
        """
        return self._scheduled_config_polling_time

    @scheduled_config_polling_time.setter
    def scheduled_config_polling_time(self, scheduled_config_polling_time):
        """
        Sets the scheduled_config_polling_time of this DeviceDiscoveryRequest.
        Scheduled time (UTC) to be provided. This is only applicable when config_polling_interval_type is SCHEDULED

        :param scheduled_config_polling_time: The scheduled_config_polling_time of this DeviceDiscoveryRequest.
        :type: str
        """

        self._scheduled_config_polling_time = scheduled_config_polling_time

    @property
    def scheduled_config_polling_days(self):
        """
        Gets the scheduled_config_polling_days of this DeviceDiscoveryRequest.
        Scheduled config polling days. Supported values are weekdays. Multiple days separated with comma can be supplied. This is only applicable when config_polling_interval_type is SCHEDULED

        :return: The scheduled_config_polling_days of this DeviceDiscoveryRequest.
        :rtype: str
        """
        return self._scheduled_config_polling_days

    @scheduled_config_polling_days.setter
    def scheduled_config_polling_days(self, scheduled_config_polling_days):
        """
        Sets the scheduled_config_polling_days of this DeviceDiscoveryRequest.
        Scheduled config polling days. Supported values are weekdays. Multiple days separated with comma can be supplied. This is only applicable when config_polling_interval_type is SCHEDULED

        :param scheduled_config_polling_days: The scheduled_config_polling_days of this DeviceDiscoveryRequest.
        :type: str
        """

        self._scheduled_config_polling_days = scheduled_config_polling_days

    @property
    def config_polling_interval_type(self):
        """
        Gets the config_polling_interval_type of this DeviceDiscoveryRequest.

        :return: The config_polling_interval_type of this DeviceDiscoveryRequest.
        :rtype: ConfigPollingIntervalType
        """
        return self._config_polling_interval_type

    @config_polling_interval_type.setter
    def config_polling_interval_type(self, config_polling_interval_type):
        """
        Sets the config_polling_interval_type of this DeviceDiscoveryRequest.

        :param config_polling_interval_type: The config_polling_interval_type of this DeviceDiscoveryRequest.
        :type: ConfigPollingIntervalType
        """

        self._config_polling_interval_type = config_polling_interval_type

    @property
    def name(self):
        """
        Gets the name of this DeviceDiscoveryRequest.
        Discovery Job Name

        :return: The name of this DeviceDiscoveryRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceDiscoveryRequest.
        Discovery Job Name

        :param name: The name of this DeviceDiscoveryRequest.
        :type: str
        """

        self._name = name

    @property
    def network_ranges(self):
        """
        Gets the network_ranges of this DeviceDiscoveryRequest.
        list of network or CIDR range for network discovery

        :return: The network_ranges of this DeviceDiscoveryRequest.
        :rtype: list[str]
        """
        return self._network_ranges

    @network_ranges.setter
    def network_ranges(self, network_ranges):
        """
        Sets the network_ranges of this DeviceDiscoveryRequest.
        list of network or CIDR range for network discovery

        :param network_ranges: The network_ranges of this DeviceDiscoveryRequest.
        :type: list[str]
        """

        self._network_ranges = network_ranges

    @property
    def seeds(self):
        """
        Gets the seeds of this DeviceDiscoveryRequest.
        list of seed device for network discovery

        :return: The seeds of this DeviceDiscoveryRequest.
        :rtype: list[str]
        """
        return self._seeds

    @seeds.setter
    def seeds(self, seeds):
        """
        Sets the seeds of this DeviceDiscoveryRequest.
        list of seed device for network discovery

        :param seeds: The seeds of this DeviceDiscoveryRequest.
        :type: list[str]
        """

        self._seeds = seeds

    @property
    def seed_depth(self):
        """
        Gets the seed_depth of this DeviceDiscoveryRequest.
        depth of seed discovery

        :return: The seed_depth of this DeviceDiscoveryRequest.
        :rtype: int
        """
        return self._seed_depth

    @seed_depth.setter
    def seed_depth(self, seed_depth):
        """
        Sets the seed_depth of this DeviceDiscoveryRequest.
        depth of seed discovery

        :param seed_depth: The seed_depth of this DeviceDiscoveryRequest.
        :type: int
        """

        self._seed_depth = seed_depth

    @property
    def ignored_list(self):
        """
        Gets the ignored_list of this DeviceDiscoveryRequest.
        list of ip/fqdn which needs to be ignored during discovery

        :return: The ignored_list of this DeviceDiscoveryRequest.
        :rtype: list[str]
        """
        return self._ignored_list

    @ignored_list.setter
    def ignored_list(self, ignored_list):
        """
        Sets the ignored_list of this DeviceDiscoveryRequest.
        list of ip/fqdn which needs to be ignored during discovery

        :param ignored_list: The ignored_list of this DeviceDiscoveryRequest.
        :type: list[str]
        """

        self._ignored_list = ignored_list

    @property
    def credential_profiles(self):
        """
        Gets the credential_profiles of this DeviceDiscoveryRequest.
        list of credential profile entity ids to be used during discovery

        :return: The credential_profiles of this DeviceDiscoveryRequest.
        :rtype: list[str]
        """
        return self._credential_profiles

    @credential_profiles.setter
    def credential_profiles(self, credential_profiles):
        """
        Sets the credential_profiles of this DeviceDiscoveryRequest.
        list of credential profile entity ids to be used during discovery

        :param credential_profiles: The credential_profiles of this DeviceDiscoveryRequest.
        :type: list[str]
        """

        self._credential_profiles = credential_profiles

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this DeviceDiscoveryRequest.
        modelKey of proxy node

        :return: The proxy_id of this DeviceDiscoveryRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this DeviceDiscoveryRequest.
        modelKey of proxy node

        :param proxy_id: The proxy_id of this DeviceDiscoveryRequest.
        :type: str
        """

        self._proxy_id = proxy_id

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
        if not isinstance(other, DeviceDiscoveryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
