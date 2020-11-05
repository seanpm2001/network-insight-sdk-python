# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSService(object):
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
        'protocol': 'str',
        'port_ranges': 'list[PortRange]',
        'nsxt_managers': 'list[Reference]',
        'vendor_id': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'protocol': 'protocol',
        'port_ranges': 'port_ranges',
        'nsxt_managers': 'nsxt_managers',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, protocol=None, port_ranges=None, nsxt_managers=None, vendor_id=None):
        """
        NSService - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._protocol = None
        self._port_ranges = None
        self._nsxt_managers = None
        self._vendor_id = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if protocol is not None:
          self.protocol = protocol
        if port_ranges is not None:
          self.port_ranges = port_ranges
        if nsxt_managers is not None:
          self.nsxt_managers = nsxt_managers
        if vendor_id is not None:
          self.vendor_id = vendor_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSService.

        :return: The entity_id of this NSService.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSService.

        :param entity_id: The entity_id of this NSService.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSService.

        :return: The name of this NSService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSService.

        :param name: The name of this NSService.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSService.

        :return: The entity_type of this NSService.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSService.

        :param entity_type: The entity_type of this NSService.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def protocol(self):
        """
        Gets the protocol of this NSService.

        :return: The protocol of this NSService.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this NSService.

        :param protocol: The protocol of this NSService.
        :type: str
        """

        self._protocol = protocol

    @property
    def port_ranges(self):
        """
        Gets the port_ranges of this NSService.

        :return: The port_ranges of this NSService.
        :rtype: list[PortRange]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """
        Sets the port_ranges of this NSService.

        :param port_ranges: The port_ranges of this NSService.
        :type: list[PortRange]
        """

        self._port_ranges = port_ranges

    @property
    def nsxt_managers(self):
        """
        Gets the nsxt_managers of this NSService.

        :return: The nsxt_managers of this NSService.
        :rtype: list[Reference]
        """
        return self._nsxt_managers

    @nsxt_managers.setter
    def nsxt_managers(self, nsxt_managers):
        """
        Sets the nsxt_managers of this NSService.

        :param nsxt_managers: The nsxt_managers of this NSService.
        :type: list[Reference]
        """

        self._nsxt_managers = nsxt_managers

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this NSService.

        :return: The vendor_id of this NSService.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this NSService.

        :param vendor_id: The vendor_id of this NSService.
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
        if not isinstance(other, NSService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
