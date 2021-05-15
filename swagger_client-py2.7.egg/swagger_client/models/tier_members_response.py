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


class TierMembersResponse(object):
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
        'name': 'str',
        'members': 'list[ApplicationMember]'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_type': 'entity_type',
        'name': 'name',
        'members': 'members'
    }

    def __init__(self, entity_id=None, entity_type=None, name=None, members=None):
        """
        TierMembersResponse - a model defined in Swagger
        """

        self._entity_id = None
        self._entity_type = None
        self._name = None
        self._members = None

        if entity_id is not None:
          self.entity_id = entity_id
        if entity_type is not None:
          self.entity_type = entity_type
        if name is not None:
          self.name = name
        if members is not None:
          self.members = members

    @property
    def entity_id(self):
        """
        Gets the entity_id of this TierMembersResponse.

        :return: The entity_id of this TierMembersResponse.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this TierMembersResponse.

        :param entity_id: The entity_id of this TierMembersResponse.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this TierMembersResponse.

        :return: The entity_type of this TierMembersResponse.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this TierMembersResponse.

        :param entity_type: The entity_type of this TierMembersResponse.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def name(self):
        """
        Gets the name of this TierMembersResponse.

        :return: The name of this TierMembersResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TierMembersResponse.

        :param name: The name of this TierMembersResponse.
        :type: str
        """

        self._name = name

    @property
    def members(self):
        """
        Gets the members of this TierMembersResponse.

        :return: The members of this TierMembersResponse.
        :rtype: list[ApplicationMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this TierMembersResponse.

        :param members: The members of this TierMembersResponse.
        :type: list[ApplicationMember]
        """

        self._members = members

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
        if not isinstance(other, TierMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
