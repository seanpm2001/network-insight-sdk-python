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


class ApplicationMember(object):
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
        'entity_type': 'str',
        'vendor_infos': 'list[VendorInfo]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'vendor_infos': 'vendor_infos'
    }

    def __init__(self, entity_id=None, entity_type=None, vendor_infos=None):
        """
        ApplicationMember - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._vendor_infos = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if vendor_infos is not None:
          self.vendor_infos = vendor_infos

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ApplicationMember.

        :return: The entity_id of this ApplicationMember.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ApplicationMember.

        :param entity_id: The entity_id of this ApplicationMember.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this ApplicationMember.

        :return: The entity_type of this ApplicationMember.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ApplicationMember.

        :param entity_type: The entity_type of this ApplicationMember.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def vendor_infos(self):
        """
        Gets the vendor_infos of this ApplicationMember.

        :return: The vendor_infos of this ApplicationMember.
        :rtype: list[VendorInfo]
        """
        return self._vendor_infos

    @vendor_infos.setter
    def vendor_infos(self, vendor_infos):
        """
        Sets the vendor_infos of this ApplicationMember.

        :param vendor_infos: The vendor_infos of this ApplicationMember.
        :type: list[VendorInfo]
        """

        self._vendor_infos = vendor_infos

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
        if not isinstance(other, ApplicationMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
