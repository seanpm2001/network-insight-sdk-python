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


class WebProxyConfigForNode(object):
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
        'node_id': 'str',
        'web_proxy_id': 'str',
        'web_nick_name': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'web_proxy_id': 'web_proxy_id',
        'web_nick_name': 'web_nick_name'
    }

    def __init__(self, node_id=None, web_proxy_id=None, web_nick_name=None):
        """
        WebProxyConfigForNode - a model defined in Swagger
        """

        self._node_id = None
        self._web_proxy_id = None
        self._web_nick_name = None

        if node_id is not None:
          self.node_id = node_id
        if web_proxy_id is not None:
          self.web_proxy_id = web_proxy_id
        if web_nick_name is not None:
          self.web_nick_name = web_nick_name

    @property
    def node_id(self):
        """
        Gets the node_id of this WebProxyConfigForNode.
        vRNI Node Identifier (Collector or Platform)

        :return: The node_id of this WebProxyConfigForNode.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this WebProxyConfigForNode.
        vRNI Node Identifier (Collector or Platform)

        :param node_id: The node_id of this WebProxyConfigForNode.
        :type: str
        """

        self._node_id = node_id

    @property
    def web_proxy_id(self):
        """
        Gets the web_proxy_id of this WebProxyConfigForNode.
        Entity Identifier for a web proxy server

        :return: The web_proxy_id of this WebProxyConfigForNode.
        :rtype: str
        """
        return self._web_proxy_id

    @web_proxy_id.setter
    def web_proxy_id(self, web_proxy_id):
        """
        Sets the web_proxy_id of this WebProxyConfigForNode.
        Entity Identifier for a web proxy server

        :param web_proxy_id: The web_proxy_id of this WebProxyConfigForNode.
        :type: str
        """

        self._web_proxy_id = web_proxy_id

    @property
    def web_nick_name(self):
        """
        Gets the web_nick_name of this WebProxyConfigForNode.
        Descriptor or identifier for particular web proxy.

        :return: The web_nick_name of this WebProxyConfigForNode.
        :rtype: str
        """
        return self._web_nick_name

    @web_nick_name.setter
    def web_nick_name(self, web_nick_name):
        """
        Sets the web_nick_name of this WebProxyConfigForNode.
        Descriptor or identifier for particular web proxy.

        :param web_nick_name: The web_nick_name of this WebProxyConfigForNode.
        :type: str
        """

        self._web_nick_name = web_nick_name

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
        if not isinstance(other, WebProxyConfigForNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
