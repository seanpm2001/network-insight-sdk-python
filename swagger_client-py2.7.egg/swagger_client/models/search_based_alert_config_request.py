# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 6.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchBasedAlertConfigRequest(object):
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
        'alert_name': 'str',
        'search_criteria': 'str',
        'generate_alert_criteria': 'GenerateEventCritera',
        'alert_type': 'AlertType',
        'severity': 'Severity',
        'notification_settings': 'list[NotificationSetting]'
    }

    attribute_map = {
        'alert_name': 'alert_name',
        'search_criteria': 'search_criteria',
        'generate_alert_criteria': 'generate_alert_criteria',
        'alert_type': 'alert_type',
        'severity': 'severity',
        'notification_settings': 'notification_settings'
    }

    def __init__(self, alert_name=None, search_criteria=None, generate_alert_criteria=None, alert_type=None, severity=None, notification_settings=None):
        """
        SearchBasedAlertConfigRequest - a model defined in Swagger
        """

        self._alert_name = None
        self._search_criteria = None
        self._generate_alert_criteria = None
        self._alert_type = None
        self._severity = None
        self._notification_settings = None

        if alert_name is not None:
          self.alert_name = alert_name
        if search_criteria is not None:
          self.search_criteria = search_criteria
        if generate_alert_criteria is not None:
          self.generate_alert_criteria = generate_alert_criteria
        if alert_type is not None:
          self.alert_type = alert_type
        if severity is not None:
          self.severity = severity
        if notification_settings is not None:
          self.notification_settings = notification_settings

    @property
    def alert_name(self):
        """
        Gets the alert_name of this SearchBasedAlertConfigRequest.
        Name of the Search based Alert Configuration.

        :return: The alert_name of this SearchBasedAlertConfigRequest.
        :rtype: str
        """
        return self._alert_name

    @alert_name.setter
    def alert_name(self, alert_name):
        """
        Sets the alert_name of this SearchBasedAlertConfigRequest.
        Name of the Search based Alert Configuration.

        :param alert_name: The alert_name of this SearchBasedAlertConfigRequest.
        :type: str
        """

        self._alert_name = alert_name

    @property
    def search_criteria(self):
        """
        Gets the search_criteria of this SearchBasedAlertConfigRequest.
        The search query for the search-based alert configuration.

        :return: The search_criteria of this SearchBasedAlertConfigRequest.
        :rtype: str
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """
        Sets the search_criteria of this SearchBasedAlertConfigRequest.
        The search query for the search-based alert configuration.

        :param search_criteria: The search_criteria of this SearchBasedAlertConfigRequest.
        :type: str
        """

        self._search_criteria = search_criteria

    @property
    def generate_alert_criteria(self):
        """
        Gets the generate_alert_criteria of this SearchBasedAlertConfigRequest.
        Basis of generation of alerts. It can take a value - SEARCH_RESULT_CHANGE or ZERO_SEARCH_RESULTS.

        :return: The generate_alert_criteria of this SearchBasedAlertConfigRequest.
        :rtype: GenerateEventCritera
        """
        return self._generate_alert_criteria

    @generate_alert_criteria.setter
    def generate_alert_criteria(self, generate_alert_criteria):
        """
        Sets the generate_alert_criteria of this SearchBasedAlertConfigRequest.
        Basis of generation of alerts. It can take a value - SEARCH_RESULT_CHANGE or ZERO_SEARCH_RESULTS.

        :param generate_alert_criteria: The generate_alert_criteria of this SearchBasedAlertConfigRequest.
        :type: GenerateEventCritera
        """

        self._generate_alert_criteria = generate_alert_criteria

    @property
    def alert_type(self):
        """
        Gets the alert_type of this SearchBasedAlertConfigRequest.
        Type of alerts to be raised. It can take a value - PROBLEM or CHANGE.

        :return: The alert_type of this SearchBasedAlertConfigRequest.
        :rtype: AlertType
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this SearchBasedAlertConfigRequest.
        Type of alerts to be raised. It can take a value - PROBLEM or CHANGE.

        :param alert_type: The alert_type of this SearchBasedAlertConfigRequest.
        :type: AlertType
        """

        self._alert_type = alert_type

    @property
    def severity(self):
        """
        Gets the severity of this SearchBasedAlertConfigRequest.
        Severity of the alerts raised from this alert configuration. It can take a value - Critical, Moderate, Warning or Info

        :return: The severity of this SearchBasedAlertConfigRequest.
        :rtype: Severity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this SearchBasedAlertConfigRequest.
        Severity of the alerts raised from this alert configuration. It can take a value - Critical, Moderate, Warning or Info

        :param severity: The severity of this SearchBasedAlertConfigRequest.
        :type: Severity
        """

        self._severity = severity

    @property
    def notification_settings(self):
        """
        Gets the notification_settings of this SearchBasedAlertConfigRequest.
        Notifications configured for alerts corresponding to this alert configuration.

        :return: The notification_settings of this SearchBasedAlertConfigRequest.
        :rtype: list[NotificationSetting]
        """
        return self._notification_settings

    @notification_settings.setter
    def notification_settings(self, notification_settings):
        """
        Sets the notification_settings of this SearchBasedAlertConfigRequest.
        Notifications configured for alerts corresponding to this alert configuration.

        :param notification_settings: The notification_settings of this SearchBasedAlertConfigRequest.
        :type: list[NotificationSetting]
        """

        self._notification_settings = notification_settings

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
        if not isinstance(other, SearchBasedAlertConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
