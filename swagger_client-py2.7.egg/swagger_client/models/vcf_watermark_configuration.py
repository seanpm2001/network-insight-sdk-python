# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VCFWatermarkConfiguration(object):
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
        'deployedby': 'str',
        'version': 'str',
        'managedby': 'str',
        'instanceid': 'str',
        'logtoken': 'str'
    }

    attribute_map = {
        'deployedby': 'deployedby',
        'version': 'version',
        'managedby': 'managedby',
        'instanceid': 'instanceid',
        'logtoken': 'logtoken'
    }

    def __init__(self, deployedby=None, version=None, managedby=None, instanceid=None, logtoken=None):
        """
        VCFWatermarkConfiguration - a model defined in Swagger
        """

        self._deployedby = None
        self._version = None
        self._managedby = None
        self._instanceid = None
        self._logtoken = None

        if deployedby is not None:
          self.deployedby = deployedby
        if version is not None:
          self.version = version
        if managedby is not None:
          self.managedby = managedby
        if instanceid is not None:
          self.instanceid = instanceid
        if logtoken is not None:
          self.logtoken = logtoken

    @property
    def deployedby(self):
        """
        Gets the deployedby of this VCFWatermarkConfiguration.
        Deployment owner for vRealize Network Insight.

        :return: The deployedby of this VCFWatermarkConfiguration.
        :rtype: str
        """
        return self._deployedby

    @deployedby.setter
    def deployedby(self, deployedby):
        """
        Sets the deployedby of this VCFWatermarkConfiguration.
        Deployment owner for vRealize Network Insight.

        :param deployedby: The deployedby of this VCFWatermarkConfiguration.
        :type: str
        """

        self._deployedby = deployedby

    @property
    def version(self):
        """
        Gets the version of this VCFWatermarkConfiguration.
        Version of VMware Cloud Foundation(VCF).

        :return: The version of this VCFWatermarkConfiguration.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this VCFWatermarkConfiguration.
        Version of VMware Cloud Foundation(VCF).

        :param version: The version of this VCFWatermarkConfiguration.
        :type: str
        """

        self._version = version

    @property
    def managedby(self):
        """
        Gets the managedby of this VCFWatermarkConfiguration.
        VMware Cloud Foundation (VCF) manager identifier to determine which instance manages the VRNI.

        :return: The managedby of this VCFWatermarkConfiguration.
        :rtype: str
        """
        return self._managedby

    @managedby.setter
    def managedby(self, managedby):
        """
        Sets the managedby of this VCFWatermarkConfiguration.
        VMware Cloud Foundation (VCF) manager identifier to determine which instance manages the VRNI.

        :param managedby: The managedby of this VCFWatermarkConfiguration.
        :type: str
        """

        self._managedby = managedby

    @property
    def instanceid(self):
        """
        Gets the instanceid of this VCFWatermarkConfiguration.
        VMware Cloud Foundation (VCF) instance id.

        :return: The instanceid of this VCFWatermarkConfiguration.
        :rtype: str
        """
        return self._instanceid

    @instanceid.setter
    def instanceid(self, instanceid):
        """
        Sets the instanceid of this VCFWatermarkConfiguration.
        VMware Cloud Foundation (VCF) instance id.

        :param instanceid: The instanceid of this VCFWatermarkConfiguration.
        :type: str
        """

        self._instanceid = instanceid

    @property
    def logtoken(self):
        """
        Gets the logtoken of this VCFWatermarkConfiguration.
        Logtoken for VMware Cloud Foundation (VCF).

        :return: The logtoken of this VCFWatermarkConfiguration.
        :rtype: str
        """
        return self._logtoken

    @logtoken.setter
    def logtoken(self, logtoken):
        """
        Sets the logtoken of this VCFWatermarkConfiguration.
        Logtoken for VMware Cloud Foundation (VCF).

        :param logtoken: The logtoken of this VCFWatermarkConfiguration.
        :type: str
        """

        self._logtoken = logtoken

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
        if not isinstance(other, VCFWatermarkConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
