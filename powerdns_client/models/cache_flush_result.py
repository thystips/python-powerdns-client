# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CacheFlushResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'count': 'float',
        'result': 'str'
    }

    attribute_map = {
        'count': 'count',
        'result': 'result'
    }

    def __init__(self, count=None, result=None):  # noqa: E501
        """CacheFlushResult - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._result = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if result is not None:
            self.result = result

    @property
    def count(self):
        """Gets the count of this CacheFlushResult.  # noqa: E501

        Amount of entries flushed  # noqa: E501

        :return: The count of this CacheFlushResult.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CacheFlushResult.

        Amount of entries flushed  # noqa: E501

        :param count: The count of this CacheFlushResult.  # noqa: E501
        :type: float
        """

        self._count = count

    @property
    def result(self):
        """Gets the result of this CacheFlushResult.  # noqa: E501

        A message about the result like \"Flushed cache\"  # noqa: E501

        :return: The result of this CacheFlushResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this CacheFlushResult.

        A message about the result like \"Flushed cache\"  # noqa: E501

        :param result: The result of this CacheFlushResult.  # noqa: E501
        :type: str
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CacheFlushResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CacheFlushResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
