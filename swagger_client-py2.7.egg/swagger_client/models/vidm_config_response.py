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


class VidmConfigResponse(object):
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
        'vidm_appliance': 'str',
        'client_id': 'str',
        'enable': 'bool',
        'certificate_validation_enabled': 'bool'
    }

    attribute_map = {
        'vidm_appliance': 'vidm_appliance',
        'client_id': 'client_id',
        'enable': 'enable',
        'certificate_validation_enabled': 'certificate_validation_enabled'
    }

    def __init__(self, vidm_appliance=None, client_id=None, enable=None, certificate_validation_enabled=False):
        """
        VidmConfigResponse - a model defined in Swagger
        """

        self._vidm_appliance = None
        self._client_id = None
        self._enable = None
        self._certificate_validation_enabled = None

        if vidm_appliance is not None:
          self.vidm_appliance = vidm_appliance
        if client_id is not None:
          self.client_id = client_id
        if enable is not None:
          self.enable = enable
        if certificate_validation_enabled is not None:
          self.certificate_validation_enabled = certificate_validation_enabled

    @property
    def vidm_appliance(self):
        """
        Gets the vidm_appliance of this VidmConfigResponse.
        Fully quallified domain name of VMware Identity Manager

        :return: The vidm_appliance of this VidmConfigResponse.
        :rtype: str
        """
        return self._vidm_appliance

    @vidm_appliance.setter
    def vidm_appliance(self, vidm_appliance):
        """
        Sets the vidm_appliance of this VidmConfigResponse.
        Fully quallified domain name of VMware Identity Manager

        :param vidm_appliance: The vidm_appliance of this VidmConfigResponse.
        :type: str
        """

        self._vidm_appliance = vidm_appliance

    @property
    def client_id(self):
        """
        Gets the client_id of this VidmConfigResponse.
        Client-id of the configured OAuth client

        :return: The client_id of this VidmConfigResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this VidmConfigResponse.
        Client-id of the configured OAuth client

        :param client_id: The client_id of this VidmConfigResponse.
        :type: str
        """

        self._client_id = client_id

    @property
    def enable(self):
        """
        Gets the enable of this VidmConfigResponse.
        True, if VMware Identity Manager integration is enabled

        :return: The enable of this VidmConfigResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """
        Sets the enable of this VidmConfigResponse.
        True, if VMware Identity Manager integration is enabled

        :param enable: The enable of this VidmConfigResponse.
        :type: bool
        """

        self._enable = enable

    @property
    def certificate_validation_enabled(self):
        """
        Gets the certificate_validation_enabled of this VidmConfigResponse.
        True, if SSL certificate check is enabled.

        :return: The certificate_validation_enabled of this VidmConfigResponse.
        :rtype: bool
        """
        return self._certificate_validation_enabled

    @certificate_validation_enabled.setter
    def certificate_validation_enabled(self, certificate_validation_enabled):
        """
        Sets the certificate_validation_enabled of this VidmConfigResponse.
        True, if SSL certificate check is enabled.

        :param certificate_validation_enabled: The certificate_validation_enabled of this VidmConfigResponse.
        :type: bool
        """

        self._certificate_validation_enabled = certificate_validation_enabled

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
        if not isinstance(other, VidmConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
