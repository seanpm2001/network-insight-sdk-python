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


class ApplicationTopTalkingMemberData(object):
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
        'application_id': 'str',
        'top_talker_member': 'list[TopTalkingMemberData]'
    }

    attribute_map = {
        'application_id': 'application_id',
        'top_talker_member': 'top_talker_member'
    }

    def __init__(self, application_id=None, top_talker_member=None):
        """
        ApplicationTopTalkingMemberData - a model defined in Swagger
        """

        self._application_id = None
        self._top_talker_member = None

        if application_id is not None:
          self.application_id = application_id
        if top_talker_member is not None:
          self.top_talker_member = top_talker_member

    @property
    def application_id(self):
        """
        Gets the application_id of this ApplicationTopTalkingMemberData.
        The entity ID of the application this flow is attached

        :return: The application_id of this ApplicationTopTalkingMemberData.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this ApplicationTopTalkingMemberData.
        The entity ID of the application this flow is attached

        :param application_id: The application_id of this ApplicationTopTalkingMemberData.
        :type: str
        """

        self._application_id = application_id

    @property
    def top_talker_member(self):
        """
        Gets the top_talker_member of this ApplicationTopTalkingMemberData.
        List of objects that are the top talkers

        :return: The top_talker_member of this ApplicationTopTalkingMemberData.
        :rtype: list[TopTalkingMemberData]
        """
        return self._top_talker_member

    @top_talker_member.setter
    def top_talker_member(self, top_talker_member):
        """
        Sets the top_talker_member of this ApplicationTopTalkingMemberData.
        List of objects that are the top talkers

        :param top_talker_member: The top_talker_member of this ApplicationTopTalkingMemberData.
        :type: list[TopTalkingMemberData]
        """

        self._top_talker_member = top_talker_member

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
        if not isinstance(other, ApplicationTopTalkingMemberData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
