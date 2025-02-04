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


class PolicyManagerPolicyBasedIPSecVPNSession(object):
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
        'entity_id': 'str',
        'name': 'str',
        'entity_type': 'EntityType',
        'local_address': 'IpV4Address',
        'remote_public_address': 'IpV4Address',
        'remote_private_address': 'IpV4Address',
        'remote_endpoints': 'list[IpV4Address]',
        'local_endpoints': 'list[IpV4Address]',
        'enabled': 'bool',
        'logical_router': 'Reference',
        'peer_vpn_session': 'Reference',
        'peer_vpn_gateway': 'Reference',
        'peer_vpn_connection': 'Reference',
        'manager': 'Reference',
        'sddc_type': 'str',
        'enforcement_point_uuid': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'name': 'name',
        'entity_type': 'entity_type',
        'local_address': 'local_address',
        'remote_public_address': 'remote_public_address',
        'remote_private_address': 'remote_private_address',
        'remote_endpoints': 'remote_endpoints',
        'local_endpoints': 'local_endpoints',
        'enabled': 'enabled',
        'logical_router': 'logical_router',
        'peer_vpn_session': 'peer_vpn_session',
        'peer_vpn_gateway': 'peer_vpn_gateway',
        'peer_vpn_connection': 'peer_vpn_connection',
        'manager': 'manager',
        'sddc_type': 'sddc_type',
        'enforcement_point_uuid': 'enforcement_point_uuid'
    }

    def __init__(self, entity_id=None, name=None, entity_type=None, local_address=None, remote_public_address=None, remote_private_address=None, remote_endpoints=None, local_endpoints=None, enabled=None, logical_router=None, peer_vpn_session=None, peer_vpn_gateway=None, peer_vpn_connection=None, manager=None, sddc_type=None, enforcement_point_uuid=None):
        """
        PolicyManagerPolicyBasedIPSecVPNSession - a model defined in Swagger
        """

        self._entity_id = None
        self._name = None
        self._entity_type = None
        self._local_address = None
        self._remote_public_address = None
        self._remote_private_address = None
        self._remote_endpoints = None
        self._local_endpoints = None
        self._enabled = None
        self._logical_router = None
        self._peer_vpn_session = None
        self._peer_vpn_gateway = None
        self._peer_vpn_connection = None
        self._manager = None
        self._sddc_type = None
        self._enforcement_point_uuid = None

        if entity_id is not None:
          self.entity_id = entity_id
        if name is not None:
          self.name = name
        if entity_type is not None:
          self.entity_type = entity_type
        if local_address is not None:
          self.local_address = local_address
        if remote_public_address is not None:
          self.remote_public_address = remote_public_address
        if remote_private_address is not None:
          self.remote_private_address = remote_private_address
        if remote_endpoints is not None:
          self.remote_endpoints = remote_endpoints
        if local_endpoints is not None:
          self.local_endpoints = local_endpoints
        if enabled is not None:
          self.enabled = enabled
        if logical_router is not None:
          self.logical_router = logical_router
        if peer_vpn_session is not None:
          self.peer_vpn_session = peer_vpn_session
        if peer_vpn_gateway is not None:
          self.peer_vpn_gateway = peer_vpn_gateway
        if peer_vpn_connection is not None:
          self.peer_vpn_connection = peer_vpn_connection
        if manager is not None:
          self.manager = manager
        if sddc_type is not None:
          self.sddc_type = sddc_type
        if enforcement_point_uuid is not None:
          self.enforcement_point_uuid = enforcement_point_uuid

    @property
    def entity_id(self):
        """
        Gets the entity_id of this PolicyManagerPolicyBasedIPSecVPNSession.
        Entity ID that can be references in detail API calls

        :return: The entity_id of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this PolicyManagerPolicyBasedIPSecVPNSession.
        Entity ID that can be references in detail API calls

        :param entity_id: The entity_id of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def name(self):
        """
        Gets the name of this PolicyManagerPolicyBasedIPSecVPNSession.
        Name of the object

        :return: The name of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyManagerPolicyBasedIPSecVPNSession.
        Name of the object

        :param name: The name of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: str
        """

        self._name = name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The entity_type of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param entity_type: The entity_type of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def local_address(self):
        """
        Gets the local_address of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The local_address of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: IpV4Address
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        """
        Sets the local_address of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param local_address: The local_address of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: IpV4Address
        """

        self._local_address = local_address

    @property
    def remote_public_address(self):
        """
        Gets the remote_public_address of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The remote_public_address of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: IpV4Address
        """
        return self._remote_public_address

    @remote_public_address.setter
    def remote_public_address(self, remote_public_address):
        """
        Sets the remote_public_address of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param remote_public_address: The remote_public_address of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: IpV4Address
        """

        self._remote_public_address = remote_public_address

    @property
    def remote_private_address(self):
        """
        Gets the remote_private_address of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The remote_private_address of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: IpV4Address
        """
        return self._remote_private_address

    @remote_private_address.setter
    def remote_private_address(self, remote_private_address):
        """
        Sets the remote_private_address of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param remote_private_address: The remote_private_address of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: IpV4Address
        """

        self._remote_private_address = remote_private_address

    @property
    def remote_endpoints(self):
        """
        Gets the remote_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The remote_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: list[IpV4Address]
        """
        return self._remote_endpoints

    @remote_endpoints.setter
    def remote_endpoints(self, remote_endpoints):
        """
        Sets the remote_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param remote_endpoints: The remote_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: list[IpV4Address]
        """

        self._remote_endpoints = remote_endpoints

    @property
    def local_endpoints(self):
        """
        Gets the local_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The local_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: list[IpV4Address]
        """
        return self._local_endpoints

    @local_endpoints.setter
    def local_endpoints(self, local_endpoints):
        """
        Sets the local_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param local_endpoints: The local_endpoints of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: list[IpV4Address]
        """

        self._local_endpoints = local_endpoints

    @property
    def enabled(self):
        """
        Gets the enabled of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The enabled of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param enabled: The enabled of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: bool
        """

        self._enabled = enabled

    @property
    def logical_router(self):
        """
        Gets the logical_router of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The logical_router of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: Reference
        """
        return self._logical_router

    @logical_router.setter
    def logical_router(self, logical_router):
        """
        Sets the logical_router of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param logical_router: The logical_router of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: Reference
        """

        self._logical_router = logical_router

    @property
    def peer_vpn_session(self):
        """
        Gets the peer_vpn_session of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The peer_vpn_session of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: Reference
        """
        return self._peer_vpn_session

    @peer_vpn_session.setter
    def peer_vpn_session(self, peer_vpn_session):
        """
        Sets the peer_vpn_session of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param peer_vpn_session: The peer_vpn_session of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: Reference
        """

        self._peer_vpn_session = peer_vpn_session

    @property
    def peer_vpn_gateway(self):
        """
        Gets the peer_vpn_gateway of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The peer_vpn_gateway of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: Reference
        """
        return self._peer_vpn_gateway

    @peer_vpn_gateway.setter
    def peer_vpn_gateway(self, peer_vpn_gateway):
        """
        Sets the peer_vpn_gateway of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param peer_vpn_gateway: The peer_vpn_gateway of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: Reference
        """

        self._peer_vpn_gateway = peer_vpn_gateway

    @property
    def peer_vpn_connection(self):
        """
        Gets the peer_vpn_connection of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The peer_vpn_connection of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: Reference
        """
        return self._peer_vpn_connection

    @peer_vpn_connection.setter
    def peer_vpn_connection(self, peer_vpn_connection):
        """
        Sets the peer_vpn_connection of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param peer_vpn_connection: The peer_vpn_connection of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: Reference
        """

        self._peer_vpn_connection = peer_vpn_connection

    @property
    def manager(self):
        """
        Gets the manager of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The manager of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: Reference
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """
        Sets the manager of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param manager: The manager of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: Reference
        """

        self._manager = manager

    @property
    def sddc_type(self):
        """
        Gets the sddc_type of this PolicyManagerPolicyBasedIPSecVPNSession.

        :return: The sddc_type of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: str
        """
        return self._sddc_type

    @sddc_type.setter
    def sddc_type(self, sddc_type):
        """
        Sets the sddc_type of this PolicyManagerPolicyBasedIPSecVPNSession.

        :param sddc_type: The sddc_type of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: str
        """

        self._sddc_type = sddc_type

    @property
    def enforcement_point_uuid(self):
        """
        Gets the enforcement_point_uuid of this PolicyManagerPolicyBasedIPSecVPNSession.
        Enforcement Point Unique ID of PolicyManager Policy Based IPSec VPN Session

        :return: The enforcement_point_uuid of this PolicyManagerPolicyBasedIPSecVPNSession.
        :rtype: str
        """
        return self._enforcement_point_uuid

    @enforcement_point_uuid.setter
    def enforcement_point_uuid(self, enforcement_point_uuid):
        """
        Sets the enforcement_point_uuid of this PolicyManagerPolicyBasedIPSecVPNSession.
        Enforcement Point Unique ID of PolicyManager Policy Based IPSec VPN Session

        :param enforcement_point_uuid: The enforcement_point_uuid of this PolicyManagerPolicyBasedIPSecVPNSession.
        :type: str
        """

        self._enforcement_point_uuid = enforcement_point_uuid

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
        if not isinstance(other, PolicyManagerPolicyBasedIPSecVPNSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
