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


class NotificationSetting(object):
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
        'type': 'NotificationType',
        'frequency': 'NotificationFrequency',
        'notification_time': 'str',
        'receivers': 'list[str]',
        'enabled': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'frequency': 'frequency',
        'notification_time': 'notification_time',
        'receivers': 'receivers',
        'enabled': 'enabled'
    }

    def __init__(self, type=None, frequency=None, notification_time=None, receivers=None, enabled=None):
        """
        NotificationSetting - a model defined in Swagger
        """

        self._type = None
        self._frequency = None
        self._notification_time = None
        self._receivers = None
        self._enabled = None

        if type is not None:
          self.type = type
        if frequency is not None:
          self.frequency = frequency
        if notification_time is not None:
          self.notification_time = notification_time
        if receivers is not None:
          self.receivers = receivers
        if enabled is not None:
          self.enabled = enabled

    @property
    def type(self):
        """
        Gets the type of this NotificationSetting.

        :return: The type of this NotificationSetting.
        :rtype: NotificationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NotificationSetting.

        :param type: The type of this NotificationSetting.
        :type: NotificationType
        """

        self._type = type

    @property
    def frequency(self):
        """
        Gets the frequency of this NotificationSetting.

        :return: The frequency of this NotificationSetting.
        :rtype: NotificationFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this NotificationSetting.

        :param frequency: The frequency of this NotificationSetting.
        :type: NotificationFrequency
        """

        self._frequency = frequency

    @property
    def notification_time(self):
        """
        Gets the notification_time of this NotificationSetting.
        The custom time of notification. This field needs to be set ONLY in case of Daily Digest Emails.

        :return: The notification_time of this NotificationSetting.
        :rtype: str
        """
        return self._notification_time

    @notification_time.setter
    def notification_time(self, notification_time):
        """
        Sets the notification_time of this NotificationSetting.
        The custom time of notification. This field needs to be set ONLY in case of Daily Digest Emails.

        :param notification_time: The notification_time of this NotificationSetting.
        :type: str
        """

        self._notification_time = notification_time

    @property
    def receivers(self):
        """
        Gets the receivers of this NotificationSetting.
        List of notification receivers.

        :return: The receivers of this NotificationSetting.
        :rtype: list[str]
        """
        return self._receivers

    @receivers.setter
    def receivers(self, receivers):
        """
        Sets the receivers of this NotificationSetting.
        List of notification receivers.

        :param receivers: The receivers of this NotificationSetting.
        :type: list[str]
        """

        self._receivers = receivers

    @property
    def enabled(self):
        """
        Gets the enabled of this NotificationSetting.
        Set this field to true to enable push notification for current user. This field will be ignored for other notification settings.

        :return: The enabled of this NotificationSetting.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NotificationSetting.
        Set this field to true to enable push notification for current user. This field will be ignored for other notification settings.

        :param enabled: The enabled of this NotificationSetting.
        :type: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, NotificationSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
