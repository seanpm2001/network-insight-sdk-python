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


class S3FileServer(object):
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
        'org_id': 'str',
        'backup_file_name': 'str'
    }

    attribute_map = {
        'org_id': 'orgId',
        'backup_file_name': 'backup_file_name'
    }

    def __init__(self, org_id=None, backup_file_name=None):
        """
        S3FileServer - a model defined in Swagger
        """

        self._org_id = None
        self._backup_file_name = None

        if org_id is not None:
          self.org_id = org_id
        if backup_file_name is not None:
          self.backup_file_name = backup_file_name

    @property
    def org_id(self):
        """
        Gets the org_id of this S3FileServer.
        Organization ID (Only in case of VRNI-Cloud)

        :return: The org_id of this S3FileServer.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """
        Sets the org_id of this S3FileServer.
        Organization ID (Only in case of VRNI-Cloud)

        :param org_id: The org_id of this S3FileServer.
        :type: str
        """

        self._org_id = org_id

    @property
    def backup_file_name(self):
        """
        Gets the backup_file_name of this S3FileServer.
        filename of the backup to be restored (used during restore only)

        :return: The backup_file_name of this S3FileServer.
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """
        Sets the backup_file_name of this S3FileServer.
        filename of the backup to be restored (used during restore only)

        :param backup_file_name: The backup_file_name of this S3FileServer.
        :type: str
        """

        self._backup_file_name = backup_file_name

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
        if not isinstance(other, S3FileServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
