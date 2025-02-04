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


class SearchQueryResponse(object):
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
        'search_response_total_hits': 'int',
        'entity_list_response': 'object',
        'aggregation_response': 'object',
        'groupby_response': 'object'
    }

    attribute_map = {
        'search_response_total_hits': 'search_response_total_hits',
        'entity_list_response': 'entity_list_response',
        'aggregation_response': 'aggregation_response',
        'groupby_response': 'groupby_response'
    }

    def __init__(self, search_response_total_hits=None, entity_list_response=None, aggregation_response=None, groupby_response=None):
        """
        SearchQueryResponse - a model defined in Swagger
        """

        self._search_response_total_hits = None
        self._entity_list_response = None
        self._aggregation_response = None
        self._groupby_response = None

        if search_response_total_hits is not None:
          self.search_response_total_hits = search_response_total_hits
        if entity_list_response is not None:
          self.entity_list_response = entity_list_response
        if aggregation_response is not None:
          self.aggregation_response = aggregation_response
        if groupby_response is not None:
          self.groupby_response = groupby_response

    @property
    def search_response_total_hits(self):
        """
        Gets the search_response_total_hits of this SearchQueryResponse.
        Total number of results

        :return: The search_response_total_hits of this SearchQueryResponse.
        :rtype: int
        """
        return self._search_response_total_hits

    @search_response_total_hits.setter
    def search_response_total_hits(self, search_response_total_hits):
        """
        Sets the search_response_total_hits of this SearchQueryResponse.
        Total number of results

        :param search_response_total_hits: The search_response_total_hits of this SearchQueryResponse.
        :type: int
        """

        self._search_response_total_hits = search_response_total_hits

    @property
    def entity_list_response(self):
        """
        Gets the entity_list_response of this SearchQueryResponse.

        :return: The entity_list_response of this SearchQueryResponse.
        :rtype: object
        """
        return self._entity_list_response

    @entity_list_response.setter
    def entity_list_response(self, entity_list_response):
        """
        Sets the entity_list_response of this SearchQueryResponse.

        :param entity_list_response: The entity_list_response of this SearchQueryResponse.
        :type: object
        """

        self._entity_list_response = entity_list_response

    @property
    def aggregation_response(self):
        """
        Gets the aggregation_response of this SearchQueryResponse.

        :return: The aggregation_response of this SearchQueryResponse.
        :rtype: object
        """
        return self._aggregation_response

    @aggregation_response.setter
    def aggregation_response(self, aggregation_response):
        """
        Sets the aggregation_response of this SearchQueryResponse.

        :param aggregation_response: The aggregation_response of this SearchQueryResponse.
        :type: object
        """

        self._aggregation_response = aggregation_response

    @property
    def groupby_response(self):
        """
        Gets the groupby_response of this SearchQueryResponse.

        :return: The groupby_response of this SearchQueryResponse.
        :rtype: object
        """
        return self._groupby_response

    @groupby_response.setter
    def groupby_response(self, groupby_response):
        """
        Sets the groupby_response of this SearchQueryResponse.

        :param groupby_response: The groupby_response of this SearchQueryResponse.
        :type: object
        """

        self._groupby_response = groupby_response

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
        if not isinstance(other, SearchQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
