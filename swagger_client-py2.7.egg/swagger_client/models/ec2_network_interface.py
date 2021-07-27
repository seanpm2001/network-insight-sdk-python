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


class EC2NetworkInterface(object):
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
        'ip_addresses': 'list[IpV4Address]',
        'layer2_network': 'Reference',
        'vlan': 'Vlan',
        'vm': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'ip_addresses': 'ip_addresses',
        'layer2_network': 'layer2_network',
        'vlan': 'vlan',
        'vm': 'vm'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, ip_addresses=None, layer2_network=None, vlan=None, vm=None):
        """
        EC2NetworkInterface - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._ip_addresses = None
        self._layer2_network = None
        self._vlan = None
        self._vm = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if ip_addresses is not None:
          self.ip_addresses = ip_addresses
        if layer2_network is not None:
          self.layer2_network = layer2_network
        if vlan is not None:
          self.vlan = vlan
        if vm is not None:
          self.vm = vm

    @property
    def entity_id(self):
        """
        Gets the entity_id of this EC2NetworkInterface.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this EC2NetworkInterface.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this EC2NetworkInterface.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this EC2NetworkInterface.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this EC2NetworkInterface.
        Name of the object

        :return: The name of this EC2NetworkInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EC2NetworkInterface.
        Name of the object

        :param name: The name of this EC2NetworkInterface.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this EC2NetworkInterface.

        :return: The entity_type of this EC2NetworkInterface.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this EC2NetworkInterface.

        :param entity_type: The entity_type of this EC2NetworkInterface.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def ip_addresses(self):
        """
        Gets the ip_addresses of this EC2NetworkInterface.

        :return: The ip_addresses of this EC2NetworkInterface.
        :rtype: list[IpV4Address]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """
        Sets the ip_addresses of this EC2NetworkInterface.

        :param ip_addresses: The ip_addresses of this EC2NetworkInterface.
        :type: list[IpV4Address]
        """

        self._ip_addresses = ip_addresses

    @property
    def layer2_network(self):
        """
        Gets the layer2_network of this EC2NetworkInterface.

        :return: The layer2_network of this EC2NetworkInterface.
        :rtype: Reference
        """
        return self._layer2_network

    @layer2_network.setter
    def layer2_network(self, layer2_network):
        """
        Sets the layer2_network of this EC2NetworkInterface.

        :param layer2_network: The layer2_network of this EC2NetworkInterface.
        :type: Reference
        """

        self._layer2_network = layer2_network

    @property
    def vlan(self):
        """
        Gets the vlan of this EC2NetworkInterface.

        :return: The vlan of this EC2NetworkInterface.
        :rtype: Vlan
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """
        Sets the vlan of this EC2NetworkInterface.

        :param vlan: The vlan of this EC2NetworkInterface.
        :type: Vlan
        """

        self._vlan = vlan

    @property
    def vm(self):
        """
        Gets the vm of this EC2NetworkInterface.

        :return: The vm of this EC2NetworkInterface.
        :rtype: Reference
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """
        Sets the vm of this EC2NetworkInterface.

        :param vm: The vm of this EC2NetworkInterface.
        :type: Reference
        """

        self._vm = vm

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
        if not isinstance(other, EC2NetworkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
