# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RRSet(object):
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
        'name': 'str',
        'type': 'str',
        'ttl': 'int',
        'changetype': 'str',
        'records': 'list[Record]',
        'comments': 'list[Comment]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'ttl': 'ttl',
        'changetype': 'changetype',
        'records': 'records',
        'comments': 'comments'
    }

    def __init__(self, name=None, type=None, ttl=None, changetype=None, records=None, comments=None):  # noqa: E501
        """RRSet - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._ttl = None
        self._changetype = None
        self._records = None
        self._comments = None
        self.discriminator = None
        self.name = name
        self.type = type
        self.ttl = ttl
        self.changetype = changetype if changetype is not None else "NOT_SET"
        self.records = records
        if comments is not None:
            self.comments = comments

    @property
    def name(self):
        """Gets the name of this RRSet.  # noqa: E501

        Name for record set (e.g. “www.powerdns.com.”)  # noqa: E501

        :return: The name of this RRSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RRSet.

        Name for record set (e.g. “www.powerdns.com.”)  # noqa: E501

        :param name: The name of this RRSet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this RRSet.  # noqa: E501

        Type of this record (e.g. “A”, “PTR”, “MX”)  # noqa: E501

        :return: The type of this RRSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RRSet.

        Type of this record (e.g. “A”, “PTR”, “MX”)  # noqa: E501

        :param type: The type of this RRSet.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this RRSet.  # noqa: E501

        DNS TTL of the records, in seconds. MUST NOT be included when changetype is set to “DELETE”.  # noqa: E501

        :return: The ttl of this RRSet.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this RRSet.

        DNS TTL of the records, in seconds. MUST NOT be included when changetype is set to “DELETE”.  # noqa: E501

        :param ttl: The ttl of this RRSet.  # noqa: E501
        :type: int
        """
        if ttl is None:
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

    @property
    def changetype(self):
        """Gets the changetype of this RRSet.  # noqa: E501

        MUST be added when updating the RRSet. Must be REPLACE or DELETE. With DELETE, all existing RRs matching name and type will be deleted, including all comments. With REPLACE: when records is present, all existing RRs matching name and type will be deleted, and then new records given in records will be created. If no records are left, any existing comments will be deleted as well. When comments is present, all existing comments for the RRs matching name and type will be deleted, and then new comments given in comments will be created.  # noqa: E501

        :return: The changetype of this RRSet.  # noqa: E501
        :rtype: str
        """
        return self._changetype

    @changetype.setter
    def changetype(self, changetype):
        """Sets the changetype of this RRSet.

        MUST be added when updating the RRSet. Must be REPLACE or DELETE. With DELETE, all existing RRs matching name and type will be deleted, including all comments. With REPLACE: when records is present, all existing RRs matching name and type will be deleted, and then new records given in records will be created. If no records are left, any existing comments will be deleted as well. When comments is present, all existing comments for the RRs matching name and type will be deleted, and then new comments given in comments will be created.  # noqa: E501

        :param changetype: The changetype of this RRSet.  # noqa: E501
        :type: str
        """
        if changetype is None:
            raise ValueError("Invalid value for `changetype`, must not be `None`")  # noqa: E501

        self._changetype = changetype

    @property
    def records(self):
        """Gets the records of this RRSet.  # noqa: E501

        All records in this RRSet. When updating Records, this is the list of new records (replacing the old ones). Must be empty when changetype is set to DELETE. An empty list results in deletion of all records (and comments).  # noqa: E501

        :return: The records of this RRSet.  # noqa: E501
        :rtype: list[Record]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this RRSet.

        All records in this RRSet. When updating Records, this is the list of new records (replacing the old ones). Must be empty when changetype is set to DELETE. An empty list results in deletion of all records (and comments).  # noqa: E501

        :param records: The records of this RRSet.  # noqa: E501
        :type: list[Record]
        """
        if records is None:
            raise ValueError("Invalid value for `records`, must not be `None`")  # noqa: E501

        self._records = records

    @property
    def comments(self):
        """Gets the comments of this RRSet.  # noqa: E501

        List of Comment. Must be empty when changetype is set to DELETE. An empty list results in deletion of all comments. modified_at is optional and defaults to the current server time.  # noqa: E501

        :return: The comments of this RRSet.  # noqa: E501
        :rtype: list[Comment]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this RRSet.

        List of Comment. Must be empty when changetype is set to DELETE. An empty list results in deletion of all comments. modified_at is optional and defaults to the current server time.  # noqa: E501

        :param comments: The comments of this RRSet.  # noqa: E501
        :type: list[Comment]
        """

        self._comments = comments

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
        if issubclass(RRSet, dict):
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
        if not isinstance(other, RRSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
