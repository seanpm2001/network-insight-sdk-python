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


class WebProxyMigrationRequest(object):
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
        'source_webproxy_id': 'str',
        'target_webproxy_id': 'str'
    }

    attribute_map = {
        'source_webproxy_id': 'source_webproxy_id',
        'target_webproxy_id': 'target_webproxy_id'
    }

    def __init__(self, source_webproxy_id=None, target_webproxy_id=None):
        """
        WebProxyMigrationRequest - a model defined in Swagger
        """

        self._source_webproxy_id = None
        self._target_webproxy_id = None

        if source_webproxy_id is not None:
          self.source_webproxy_id = source_webproxy_id
        if target_webproxy_id is not None:
          self.target_webproxy_id = target_webproxy_id

    @property
    def source_webproxy_id(self):
        """
        Gets the source_webproxy_id of this WebProxyMigrationRequest.
        Identifier of web proxy which needs migration

        :return: The source_webproxy_id of this WebProxyMigrationRequest.
        :rtype: str
        """
        return self._source_webproxy_id

    @source_webproxy_id.setter
    def source_webproxy_id(self, source_webproxy_id):
        """
        Sets the source_webproxy_id of this WebProxyMigrationRequest.
        Identifier of web proxy which needs migration

        :param source_webproxy_id: The source_webproxy_id of this WebProxyMigrationRequest.
        :type: str
        """

        self._source_webproxy_id = source_webproxy_id

    @property
    def target_webproxy_id(self):
        """
        Gets the target_webproxy_id of this WebProxyMigrationRequest.
        Identifier of web proxy to which entities connected to source_webproxy_id will be migrated

        :return: The target_webproxy_id of this WebProxyMigrationRequest.
        :rtype: str
        """
        return self._target_webproxy_id

    @target_webproxy_id.setter
    def target_webproxy_id(self, target_webproxy_id):
        """
        Sets the target_webproxy_id of this WebProxyMigrationRequest.
        Identifier of web proxy to which entities connected to source_webproxy_id will be migrated

        :param target_webproxy_id: The target_webproxy_id of this WebProxyMigrationRequest.
        :type: str
        """

        self._target_webproxy_id = target_webproxy_id

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
        if not isinstance(other, WebProxyMigrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
