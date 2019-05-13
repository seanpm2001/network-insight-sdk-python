# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ServiceNowDataSourceRequest(object):
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
        'proxy_id': 'str',
        'nickname': 'str',
        'enabled': 'bool',
        'notes': 'str',
        'credentials': 'PasswordCredentials',
        'instance_id': 'str',
        'graph_configuration': 'str',
        'is_graph_config_customized': 'bool'
    }

    attribute_map = {
        'proxy_id': 'proxy_id',
        'nickname': 'nickname',
        'enabled': 'enabled',
        'notes': 'notes',
        'credentials': 'credentials',
        'instance_id': 'instance_id',
        'graph_configuration': 'graph_configuration',
        'is_graph_config_customized': 'is_graph_config_customized'
    }

    def __init__(self, proxy_id=None, nickname=None, enabled=True, notes=None, credentials=None, instance_id=None, graph_configuration=None, is_graph_config_customized=None):
        """
        ServiceNowDataSourceRequest - a model defined in Swagger
        """

        self._proxy_id = None
        self._nickname = None
        self._enabled = None
        self._notes = None
        self._credentials = None
        self._instance_id = None
        self._graph_configuration = None
        self._is_graph_config_customized = None

        self.proxy_id = proxy_id
        self.nickname = nickname
        if enabled is not None:
          self.enabled = enabled
        if notes is not None:
          self.notes = notes
        self.credentials = credentials
        self.instance_id = instance_id
        if graph_configuration is not None:
          self.graph_configuration = graph_configuration
        self.is_graph_config_customized = is_graph_config_customized

    @property
    def proxy_id(self):
        """
        Gets the proxy_id of this ServiceNowDataSourceRequest.
        proxy vm which should register this vcenter

        :return: The proxy_id of this ServiceNowDataSourceRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """
        Sets the proxy_id of this ServiceNowDataSourceRequest.
        proxy vm which should register this vcenter

        :param proxy_id: The proxy_id of this ServiceNowDataSourceRequest.
        :type: str
        """
        if proxy_id is None:
            raise ValueError("Invalid value for `proxy_id`, must not be `None`")

        self._proxy_id = proxy_id

    @property
    def nickname(self):
        """
        Gets the nickname of this ServiceNowDataSourceRequest.

        :return: The nickname of this ServiceNowDataSourceRequest.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this ServiceNowDataSourceRequest.

        :param nickname: The nickname of this ServiceNowDataSourceRequest.
        :type: str
        """
        if nickname is None:
            raise ValueError("Invalid value for `nickname`, must not be `None`")

        self._nickname = nickname

    @property
    def enabled(self):
        """
        Gets the enabled of this ServiceNowDataSourceRequest.

        :return: The enabled of this ServiceNowDataSourceRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this ServiceNowDataSourceRequest.

        :param enabled: The enabled of this ServiceNowDataSourceRequest.
        :type: bool
        """

        self._enabled = enabled

    @property
    def notes(self):
        """
        Gets the notes of this ServiceNowDataSourceRequest.

        :return: The notes of this ServiceNowDataSourceRequest.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this ServiceNowDataSourceRequest.

        :param notes: The notes of this ServiceNowDataSourceRequest.
        :type: str
        """

        self._notes = notes

    @property
    def credentials(self):
        """
        Gets the credentials of this ServiceNowDataSourceRequest.

        :return: The credentials of this ServiceNowDataSourceRequest.
        :rtype: PasswordCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this ServiceNowDataSourceRequest.

        :param credentials: The credentials of this ServiceNowDataSourceRequest.
        :type: PasswordCredentials
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")

        self._credentials = credentials

    @property
    def instance_id(self):
        """
        Gets the instance_id of this ServiceNowDataSourceRequest.
        Associated service now instance

        :return: The instance_id of this ServiceNowDataSourceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this ServiceNowDataSourceRequest.
        Associated service now instance

        :param instance_id: The instance_id of this ServiceNowDataSourceRequest.
        :type: str
        """
        if instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")

        self._instance_id = instance_id

    @property
    def graph_configuration(self):
        """
        Gets the graph_configuration of this ServiceNowDataSourceRequest.
        CMDB configuration for CIs, relationships and graph traversal rules

        :return: The graph_configuration of this ServiceNowDataSourceRequest.
        :rtype: str
        """
        return self._graph_configuration

    @graph_configuration.setter
    def graph_configuration(self, graph_configuration):
        """
        Sets the graph_configuration of this ServiceNowDataSourceRequest.
        CMDB configuration for CIs, relationships and graph traversal rules

        :param graph_configuration: The graph_configuration of this ServiceNowDataSourceRequest.
        :type: str
        """

        self._graph_configuration = graph_configuration

    @property
    def is_graph_config_customized(self):
        """
        Gets the is_graph_config_customized of this ServiceNowDataSourceRequest.
        Has graph configuration been modified from the default configuration

        :return: The is_graph_config_customized of this ServiceNowDataSourceRequest.
        :rtype: bool
        """
        return self._is_graph_config_customized

    @is_graph_config_customized.setter
    def is_graph_config_customized(self, is_graph_config_customized):
        """
        Sets the is_graph_config_customized of this ServiceNowDataSourceRequest.
        Has graph configuration been modified from the default configuration

        :param is_graph_config_customized: The is_graph_config_customized of this ServiceNowDataSourceRequest.
        :type: bool
        """
        if is_graph_config_customized is None:
            raise ValueError("Invalid value for `is_graph_config_customized`, must not be `None`")

        self._is_graph_config_customized = is_graph_config_customized

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
        if not isinstance(other, ServiceNowDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
