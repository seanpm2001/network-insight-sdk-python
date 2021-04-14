# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SecurityTag(object):
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
        'description': 'str',
        'direct_security_groups': 'list[Reference]',
        'security_groups': 'list[Reference]',
        'vendor_id': 'str',
        'nsx_manager': 'Reference'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'description': 'description',
        'direct_security_groups': 'direct_security_groups',
        'security_groups': 'security_groups',
        'vendor_id': 'vendor_id',
        'nsx_manager': 'nsx_manager'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, description=None, direct_security_groups=None, security_groups=None, vendor_id=None, nsx_manager=None):
        """
        SecurityTag - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._description = None
        self._direct_security_groups = None
        self._security_groups = None
        self._vendor_id = None
        self._nsx_manager = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if description is not None:
          self.description = description
        if direct_security_groups is not None:
          self.direct_security_groups = direct_security_groups
        if security_groups is not None:
          self.security_groups = security_groups
        if vendor_id is not None:
          self.vendor_id = vendor_id
        if nsx_manager is not None:
          self.nsx_manager = nsx_manager

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SecurityTag.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this SecurityTag.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SecurityTag.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this SecurityTag.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this SecurityTag.
        Name of the object

        :return: The name of this SecurityTag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SecurityTag.
        Name of the object

        :param name: The name of this SecurityTag.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this SecurityTag.

        :return: The entity_type of this SecurityTag.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this SecurityTag.

        :param entity_type: The entity_type of this SecurityTag.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def description(self):
        """
        Gets the description of this SecurityTag.

        :return: The description of this SecurityTag.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SecurityTag.

        :param description: The description of this SecurityTag.
        :type: str
        """

        self._description = description

    @property
    def direct_security_groups(self):
        """
        Gets the direct_security_groups of this SecurityTag.

        :return: The direct_security_groups of this SecurityTag.
        :rtype: list[Reference]
        """
        return self._direct_security_groups

    @direct_security_groups.setter
    def direct_security_groups(self, direct_security_groups):
        """
        Sets the direct_security_groups of this SecurityTag.

        :param direct_security_groups: The direct_security_groups of this SecurityTag.
        :type: list[Reference]
        """

        self._direct_security_groups = direct_security_groups

    @property
    def security_groups(self):
        """
        Gets the security_groups of this SecurityTag.

        :return: The security_groups of this SecurityTag.
        :rtype: list[Reference]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """
        Sets the security_groups of this SecurityTag.

        :param security_groups: The security_groups of this SecurityTag.
        :type: list[Reference]
        """

        self._security_groups = security_groups

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this SecurityTag.

        :return: The vendor_id of this SecurityTag.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this SecurityTag.

        :param vendor_id: The vendor_id of this SecurityTag.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def nsx_manager(self):
        """
        Gets the nsx_manager of this SecurityTag.

        :return: The nsx_manager of this SecurityTag.
        :rtype: Reference
        """
        return self._nsx_manager

    @nsx_manager.setter
    def nsx_manager(self, nsx_manager):
        """
        Sets the nsx_manager of this SecurityTag.

        :param nsx_manager: The nsx_manager of this SecurityTag.
        :type: Reference
        """

        self._nsx_manager = nsx_manager

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
        if not isinstance(other, SecurityTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
