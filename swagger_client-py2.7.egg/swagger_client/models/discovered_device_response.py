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


class DiscoveredDeviceResponse(object):
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
        'job_name': 'str',
        'entity_id': 'str',
        'discovered_devices': 'list[DiscoveredDeviceDto]',
        'total_count': 'int'
    }

    attribute_map = {
        'job_name': 'job_name',
        'entity_id': 'entity_id',
        'discovered_devices': 'discovered_devices',
        'total_count': 'total_count'
    }

    def __init__(self, job_name=None, entity_id=None, discovered_devices=None, total_count=None):
        """
        DiscoveredDeviceResponse - a model defined in Swagger
        """

        self._job_name = None
        self._entity_id = None
        self._discovered_devices = None
        self._total_count = None

        if job_name is not None:
          self.job_name = job_name
        if entity_id is not None:
          self.entity_id = entity_id
        if discovered_devices is not None:
          self.discovered_devices = discovered_devices
        if total_count is not None:
          self.total_count = total_count

    @property
    def job_name(self):
        """
        Gets the job_name of this DiscoveredDeviceResponse.
        Discovery job name

        :return: The job_name of this DiscoveredDeviceResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this DiscoveredDeviceResponse.
        Discovery job name

        :param job_name: The job_name of this DiscoveredDeviceResponse.
        :type: str
        """

        self._job_name = job_name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this DiscoveredDeviceResponse.
        Discovery Job Model Key

        :return: The entity_id of this DiscoveredDeviceResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this DiscoveredDeviceResponse.
        Discovery Job Model Key

        :param entity_id: The entity_id of this DiscoveredDeviceResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def discovered_devices(self):
        """
        Gets the discovered_devices of this DiscoveredDeviceResponse.
        List of Discovered devices

        :return: The discovered_devices of this DiscoveredDeviceResponse.
        :rtype: list[DiscoveredDeviceDto]
        """
        return self._discovered_devices

    @discovered_devices.setter
    def discovered_devices(self, discovered_devices):
        """
        Sets the discovered_devices of this DiscoveredDeviceResponse.
        List of Discovered devices

        :param discovered_devices: The discovered_devices of this DiscoveredDeviceResponse.
        :type: list[DiscoveredDeviceDto]
        """

        self._discovered_devices = discovered_devices

    @property
    def total_count(self):
        """
        Gets the total_count of this DiscoveredDeviceResponse.

        :return: The total_count of this DiscoveredDeviceResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this DiscoveredDeviceResponse.

        :param total_count: The total_count of this DiscoveredDeviceResponse.
        :type: int
        """

        self._total_count = total_count

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
        if not isinstance(other, DiscoveredDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
