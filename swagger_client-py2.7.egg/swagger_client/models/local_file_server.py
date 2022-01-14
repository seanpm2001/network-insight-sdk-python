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


class LocalFileServer(object):
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
        'backup_directory': 'str',
        'backup_file_name': 'str'
    }

    attribute_map = {
        'backup_directory': 'backup_directory',
        'backup_file_name': 'backup_file_name'
    }

    def __init__(self, backup_directory=None, backup_file_name=None):
        """
        LocalFileServer - a model defined in Swagger
        """

        self._backup_directory = None
        self._backup_file_name = None

        if backup_directory is not None:
          self.backup_directory = backup_directory
        if backup_file_name is not None:
          self.backup_file_name = backup_file_name

    @property
    def backup_directory(self):
        """
        Gets the backup_directory of this LocalFileServer.
        Directory on file server to store/fetch backups

        :return: The backup_directory of this LocalFileServer.
        :rtype: str
        """
        return self._backup_directory

    @backup_directory.setter
    def backup_directory(self, backup_directory):
        """
        Sets the backup_directory of this LocalFileServer.
        Directory on file server to store/fetch backups

        :param backup_directory: The backup_directory of this LocalFileServer.
        :type: str
        """

        self._backup_directory = backup_directory

    @property
    def backup_file_name(self):
        """
        Gets the backup_file_name of this LocalFileServer.
        filename of the backup to be restored (used during restore only)

        :return: The backup_file_name of this LocalFileServer.
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        """
        Sets the backup_file_name of this LocalFileServer.
        filename of the backup to be restored (used during restore only)

        :param backup_file_name: The backup_file_name of this LocalFileServer.
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
        if not isinstance(other, LocalFileServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
