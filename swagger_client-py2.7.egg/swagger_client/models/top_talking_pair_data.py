# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TopTalkingPairData(object):
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
        'sort_criteria': 'TopTalkerSortEnum',
        'sorted_list': 'PagedEntityPairListResponse'
    }

    attribute_map = {
        'sort_criteria': 'sort_criteria',
        'sorted_list': 'sorted_list'
    }

    def __init__(self, sort_criteria=None, sorted_list=None):
        """
        TopTalkingPairData - a model defined in Swagger
        """

        self._sort_criteria = None
        self._sorted_list = None

        if sort_criteria is not None:
          self.sort_criteria = sort_criteria
        if sorted_list is not None:
          self.sorted_list = sorted_list

    @property
    def sort_criteria(self):
        """
        Gets the sort_criteria of this TopTalkingPairData.

        :return: The sort_criteria of this TopTalkingPairData.
        :rtype: TopTalkerSortEnum
        """
        return self._sort_criteria

    @sort_criteria.setter
    def sort_criteria(self, sort_criteria):
        """
        Sets the sort_criteria of this TopTalkingPairData.

        :param sort_criteria: The sort_criteria of this TopTalkingPairData.
        :type: TopTalkerSortEnum
        """

        self._sort_criteria = sort_criteria

    @property
    def sorted_list(self):
        """
        Gets the sorted_list of this TopTalkingPairData.

        :return: The sorted_list of this TopTalkingPairData.
        :rtype: PagedEntityPairListResponse
        """
        return self._sorted_list

    @sorted_list.setter
    def sorted_list(self, sorted_list):
        """
        Sets the sorted_list of this TopTalkingPairData.

        :param sorted_list: The sorted_list of this TopTalkingPairData.
        :type: PagedEntityPairListResponse
        """

        self._sorted_list = sorted_list

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
        if not isinstance(other, TopTalkingPairData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
