# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NSXService(object):
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
        'nsx_managers': 'list[Reference]',
        'scope': 'ScopeEnum',
        'vendor_id': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'protocol': 'protocol',
        'port_ranges': 'port_ranges',
        'nsx_managers': 'nsx_managers',
        'scope': 'scope',
        'vendor_id': 'vendor_id'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, protocol=None, port_ranges=None, nsx_managers=None, scope=None, vendor_id=None):
        """
        NSXService - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._protocol = None
        self._port_ranges = None
        self._nsx_managers = None
        self._scope = None
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
        if nsx_managers is not None:
          self.nsx_managers = nsx_managers
        if scope is not None:
          self.scope = scope
        if vendor_id is not None:
          self.vendor_id = vendor_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this NSXService.

        :return: The entity_id of this NSXService.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this NSXService.

        :param entity_id: The entity_id of this NSXService.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this NSXService.

        :return: The name of this NSXService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NSXService.

        :param name: The name of this NSXService.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this NSXService.

        :return: The entity_type of this NSXService.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this NSXService.

        :param entity_type: The entity_type of this NSXService.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def protocol(self):
        """
        Gets the protocol of this NSXService.

        :return: The protocol of this NSXService.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this NSXService.

        :param protocol: The protocol of this NSXService.
        :type: str
        """

        self._protocol = protocol

    @property
    def port_ranges(self):
        """
        Gets the port_ranges of this NSXService.

        :return: The port_ranges of this NSXService.
        :rtype: list[PortRange]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """
        Sets the port_ranges of this NSXService.

        :param port_ranges: The port_ranges of this NSXService.
        :type: list[PortRange]
        """

        self._port_ranges = port_ranges

    @property
    def nsx_managers(self):
        """
        Gets the nsx_managers of this NSXService.

        :return: The nsx_managers of this NSXService.
        :rtype: list[Reference]
        """
        return self._nsx_managers

    @nsx_managers.setter
    def nsx_managers(self, nsx_managers):
        """
        Sets the nsx_managers of this NSXService.

        :param nsx_managers: The nsx_managers of this NSXService.
        :type: list[Reference]
        """

        self._nsx_managers = nsx_managers

    @property
    def scope(self):
        """
        Gets the scope of this NSXService.

        :return: The scope of this NSXService.
        :rtype: ScopeEnum
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this NSXService.

        :param scope: The scope of this NSXService.
        :type: ScopeEnum
        """

        self._scope = scope

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this NSXService.

        :return: The vendor_id of this NSXService.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this NSXService.

        :param vendor_id: The vendor_id of this NSXService.
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
        if not isinstance(other, NSXService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
