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


class CheckpointMDSManager(object):
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
        'name': 'str',
        'entity_type': 'EntityType',
        'nsx_manager': 'Reference',
        'version': 'str',
        'ip_address': 'IpV4Address'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'nsx_manager': 'nsx_manager',
        'version': 'version',
        'ip_address': 'ip_address'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, nsx_manager=None, version=None, ip_address=None):
        """
        CheckpointMDSManager - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._nsx_manager = None
        self._version = None
        self._ip_address = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if nsx_manager is not None:
          self.nsx_manager = nsx_manager
        if version is not None:
          self.version = version
        if ip_address is not None:
          self.ip_address = ip_address

    @property
    def entity_id(self):
        """
        Gets the entity_id of this CheckpointMDSManager.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this CheckpointMDSManager.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this CheckpointMDSManager.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this CheckpointMDSManager.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this CheckpointMDSManager.
        Name of the object

        :return: The name of this CheckpointMDSManager.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CheckpointMDSManager.
        Name of the object

        :param name: The name of this CheckpointMDSManager.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this CheckpointMDSManager.

        :return: The entity_type of this CheckpointMDSManager.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this CheckpointMDSManager.

        :param entity_type: The entity_type of this CheckpointMDSManager.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def nsx_manager(self):
        """
        Gets the nsx_manager of this CheckpointMDSManager.

        :return: The nsx_manager of this CheckpointMDSManager.
        :rtype: Reference
        """
        return self._nsx_manager

    @nsx_manager.setter
    def nsx_manager(self, nsx_manager):
        """
        Sets the nsx_manager of this CheckpointMDSManager.

        :param nsx_manager: The nsx_manager of this CheckpointMDSManager.
        :type: Reference
        """

        self._nsx_manager = nsx_manager

    @property
    def version(self):
        """
        Gets the version of this CheckpointMDSManager.

        :return: The version of this CheckpointMDSManager.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CheckpointMDSManager.

        :param version: The version of this CheckpointMDSManager.
        :type: str
        """

        self._version = version

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CheckpointMDSManager.

        :return: The ip_address of this CheckpointMDSManager.
        :rtype: IpV4Address
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CheckpointMDSManager.

        :param ip_address: The ip_address of this CheckpointMDSManager.
        :type: IpV4Address
        """

        self._ip_address = ip_address

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
        if not isinstance(other, CheckpointMDSManager):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
