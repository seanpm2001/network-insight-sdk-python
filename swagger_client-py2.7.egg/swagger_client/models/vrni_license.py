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


class VRNILicense(object):
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
        'product_name': 'str',
        'evaluation': 'bool',
        'license_key': 'str',
        'number_of_sockets': 'int',
        'service_tag': 'str',
        'deployment_type': 'str',
        'capacity_type': 'LicenseCapacityType',
        'edition': 'LicenseEdition',
        'suspended': 'bool',
        'deleted': 'bool',
        'invalid': 'bool',
        'entitlements': 'list[VRNILicenseEntitlements]'
    }

    attribute_map = {
        'product_name': 'productName',
        'evaluation': 'evaluation',
        'license_key': 'licenseKey',
        'number_of_sockets': 'numberOfSockets',
        'service_tag': 'serviceTag',
        'deployment_type': 'deploymentType',
        'capacity_type': 'capacityType',
        'edition': 'edition',
        'suspended': 'suspended',
        'deleted': 'deleted',
        'invalid': 'invalid',
        'entitlements': 'entitlements'
    }

    def __init__(self, product_name=None, evaluation=None, license_key=None, number_of_sockets=None, service_tag=None, deployment_type=None, capacity_type=None, edition=None, suspended=None, deleted=None, invalid=None, entitlements=None):
        """
        VRNILicense - a model defined in Swagger
        """

        self._product_name = None
        self._evaluation = None
        self._license_key = None
        self._number_of_sockets = None
        self._service_tag = None
        self._deployment_type = None
        self._capacity_type = None
        self._edition = None
        self._suspended = None
        self._deleted = None
        self._invalid = None
        self._entitlements = None

        if product_name is not None:
          self.product_name = product_name
        if evaluation is not None:
          self.evaluation = evaluation
        if license_key is not None:
          self.license_key = license_key
        if number_of_sockets is not None:
          self.number_of_sockets = number_of_sockets
        if service_tag is not None:
          self.service_tag = service_tag
        if deployment_type is not None:
          self.deployment_type = deployment_type
        if capacity_type is not None:
          self.capacity_type = capacity_type
        if edition is not None:
          self.edition = edition
        if suspended is not None:
          self.suspended = suspended
        if deleted is not None:
          self.deleted = deleted
        if invalid is not None:
          self.invalid = invalid
        if entitlements is not None:
          self.entitlements = entitlements

    @property
    def product_name(self):
        """
        Gets the product_name of this VRNILicense.

        :return: The product_name of this VRNILicense.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this VRNILicense.

        :param product_name: The product_name of this VRNILicense.
        :type: str
        """

        self._product_name = product_name

    @property
    def evaluation(self):
        """
        Gets the evaluation of this VRNILicense.
        true if license is evaluation license

        :return: The evaluation of this VRNILicense.
        :rtype: bool
        """
        return self._evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        """
        Sets the evaluation of this VRNILicense.
        true if license is evaluation license

        :param evaluation: The evaluation of this VRNILicense.
        :type: bool
        """

        self._evaluation = evaluation

    @property
    def license_key(self):
        """
        Gets the license_key of this VRNILicense.
        license serial key

        :return: The license_key of this VRNILicense.
        :rtype: str
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """
        Sets the license_key of this VRNILicense.
        license serial key

        :param license_key: The license_key of this VRNILicense.
        :type: str
        """

        self._license_key = license_key

    @property
    def number_of_sockets(self):
        """
        Gets the number_of_sockets of this VRNILicense.
        sockets entitlement for this license

        :return: The number_of_sockets of this VRNILicense.
        :rtype: int
        """
        return self._number_of_sockets

    @number_of_sockets.setter
    def number_of_sockets(self, number_of_sockets):
        """
        Sets the number_of_sockets of this VRNILicense.
        sockets entitlement for this license

        :param number_of_sockets: The number_of_sockets of this VRNILicense.
        :type: int
        """

        self._number_of_sockets = number_of_sockets

    @property
    def service_tag(self):
        """
        Gets the service_tag of this VRNILicense.
        service tag

        :return: The service_tag of this VRNILicense.
        :rtype: str
        """
        return self._service_tag

    @service_tag.setter
    def service_tag(self, service_tag):
        """
        Sets the service_tag of this VRNILicense.
        service tag

        :param service_tag: The service_tag of this VRNILicense.
        :type: str
        """

        self._service_tag = service_tag

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this VRNILicense.
        environment deployment type

        :return: The deployment_type of this VRNILicense.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this VRNILicense.
        environment deployment type

        :param deployment_type: The deployment_type of this VRNILicense.
        :type: str
        """

        self._deployment_type = deployment_type

    @property
    def capacity_type(self):
        """
        Gets the capacity_type of this VRNILicense.

        :return: The capacity_type of this VRNILicense.
        :rtype: LicenseCapacityType
        """
        return self._capacity_type

    @capacity_type.setter
    def capacity_type(self, capacity_type):
        """
        Sets the capacity_type of this VRNILicense.

        :param capacity_type: The capacity_type of this VRNILicense.
        :type: LicenseCapacityType
        """

        self._capacity_type = capacity_type

    @property
    def edition(self):
        """
        Gets the edition of this VRNILicense.

        :return: The edition of this VRNILicense.
        :rtype: LicenseEdition
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """
        Sets the edition of this VRNILicense.

        :param edition: The edition of this VRNILicense.
        :type: LicenseEdition
        """

        self._edition = edition

    @property
    def suspended(self):
        """
        Gets the suspended of this VRNILicense.
        true if customer state is suspended

        :return: The suspended of this VRNILicense.
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        """
        Sets the suspended of this VRNILicense.
        true if customer state is suspended

        :param suspended: The suspended of this VRNILicense.
        :type: bool
        """

        self._suspended = suspended

    @property
    def deleted(self):
        """
        Gets the deleted of this VRNILicense.
        true if customer state is deleted

        :return: The deleted of this VRNILicense.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this VRNILicense.
        true if customer state is deleted

        :param deleted: The deleted of this VRNILicense.
        :type: bool
        """

        self._deleted = deleted

    @property
    def invalid(self):
        """
        Gets the invalid of this VRNILicense.
        true for license keys from last version, which are active only for grace period

        :return: The invalid of this VRNILicense.
        :rtype: bool
        """
        return self._invalid

    @invalid.setter
    def invalid(self, invalid):
        """
        Sets the invalid of this VRNILicense.
        true for license keys from last version, which are active only for grace period

        :param invalid: The invalid of this VRNILicense.
        :type: bool
        """

        self._invalid = invalid

    @property
    def entitlements(self):
        """
        Gets the entitlements of this VRNILicense.
        list of entitlements supported by the license

        :return: The entitlements of this VRNILicense.
        :rtype: list[VRNILicenseEntitlements]
        """
        return self._entitlements

    @entitlements.setter
    def entitlements(self, entitlements):
        """
        Sets the entitlements of this VRNILicense.
        list of entitlements supported by the license

        :param entitlements: The entitlements of this VRNILicense.
        :type: list[VRNILicenseEntitlements]
        """

        self._entitlements = entitlements

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
        if not isinstance(other, VRNILicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
