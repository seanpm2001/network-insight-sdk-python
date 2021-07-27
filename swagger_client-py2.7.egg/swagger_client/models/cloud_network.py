# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CloudNetwork(object):
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
        'peer_cloud_networks': 'list[Reference]',
        'address_spaces': 'list[IpV4Address]',
        'provisioned_state': 'str',
        'regions': 'list[str]',
        'vendor_id': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'peer_cloud_networks': 'peer_cloud_networks',
        'address_spaces': 'address_spaces',
        'provisioned_state': 'provisioned_state',
        'regions': 'regions',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, peer_cloud_networks=None, address_spaces=None, provisioned_state=None, regions=None, vendor_id=None):
        """
        CloudNetwork - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._peer_cloud_networks = None
        self._address_spaces = None
        self._provisioned_state = None
        self._regions = None
        self._vendor_id = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if peer_cloud_networks is not None:
          self.peer_cloud_networks = peer_cloud_networks
        if address_spaces is not None:
          self.address_spaces = address_spaces
        if provisioned_state is not None:
          self.provisioned_state = provisioned_state
        if regions is not None:
          self.regions = regions
        if vendor_id is not None:
          self.vendor_id = vendor_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this CloudNetwork.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this CloudNetwork.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this CloudNetwork.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this CloudNetwork.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this CloudNetwork.
        Name of the object

        :return: The name of this CloudNetwork.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudNetwork.
        Name of the object

        :param name: The name of this CloudNetwork.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this CloudNetwork.

        :return: The entity_type of this CloudNetwork.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this CloudNetwork.

        :param entity_type: The entity_type of this CloudNetwork.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def peer_cloud_networks(self):
        """
        Gets the peer_cloud_networks of this CloudNetwork.

        :return: The peer_cloud_networks of this CloudNetwork.
        :rtype: list[Reference]
        """
        return self._peer_cloud_networks

    @peer_cloud_networks.setter
    def peer_cloud_networks(self, peer_cloud_networks):
        """
        Sets the peer_cloud_networks of this CloudNetwork.

        :param peer_cloud_networks: The peer_cloud_networks of this CloudNetwork.
        :type: list[Reference]
        """

        self._peer_cloud_networks = peer_cloud_networks

    @property
    def address_spaces(self):
        """
        Gets the address_spaces of this CloudNetwork.

        :return: The address_spaces of this CloudNetwork.
        :rtype: list[IpV4Address]
        """
        return self._address_spaces

    @address_spaces.setter
    def address_spaces(self, address_spaces):
        """
        Sets the address_spaces of this CloudNetwork.

        :param address_spaces: The address_spaces of this CloudNetwork.
        :type: list[IpV4Address]
        """

        self._address_spaces = address_spaces

    @property
    def provisioned_state(self):
        """
        Gets the provisioned_state of this CloudNetwork.

        :return: The provisioned_state of this CloudNetwork.
        :rtype: str
        """
        return self._provisioned_state

    @provisioned_state.setter
    def provisioned_state(self, provisioned_state):
        """
        Sets the provisioned_state of this CloudNetwork.

        :param provisioned_state: The provisioned_state of this CloudNetwork.
        :type: str
        """

        self._provisioned_state = provisioned_state

    @property
    def regions(self):
        """
        Gets the regions of this CloudNetwork.

        :return: The regions of this CloudNetwork.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """
        Sets the regions of this CloudNetwork.

        :param regions: The regions of this CloudNetwork.
        :type: list[str]
        """

        self._regions = regions

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this CloudNetwork.

        :return: The vendor_id of this CloudNetwork.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this CloudNetwork.

        :param vendor_id: The vendor_id of this CloudNetwork.
        :type: str
        """

        self._vendor_id = vendor_id

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
        if not isinstance(other, CloudNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
