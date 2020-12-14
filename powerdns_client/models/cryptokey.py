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


class Cryptokey(object):
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
        'type': 'str',
        'id': 'int',
        'keytype': 'str',
        'active': 'bool',
        'published': 'bool',
        'dnskey': 'str',
        'ds': 'list[str]',
        'privatekey': 'str',
        'algorithm': 'str',
        'bits': 'int'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'keytype': 'keytype',
        'active': 'active',
        'published': 'published',
        'dnskey': 'dnskey',
        'ds': 'ds',
        'privatekey': 'privatekey',
        'algorithm': 'algorithm',
        'bits': 'bits'
    }

    def __init__(self, type=None, id=None, keytype=None, active=None, published=None, dnskey=None, ds=None, privatekey=None, algorithm=None, bits=None):  # noqa: E501
        """Cryptokey - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._id = None
        self._keytype = None
        self._active = None
        self._published = None
        self._dnskey = None
        self._ds = None
        self._privatekey = None
        self._algorithm = None
        self._bits = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if keytype is not None:
            self.keytype = keytype
        if active is not None:
            self.active = active
        if published is not None:
            self.published = published
        if dnskey is not None:
            self.dnskey = dnskey
        if ds is not None:
            self.ds = ds
        if privatekey is not None:
            self.privatekey = privatekey
        if algorithm is not None:
            self.algorithm = algorithm
        if bits is not None:
            self.bits = bits

    @property
    def type(self):
        """Gets the type of this Cryptokey.  # noqa: E501

        set to \"Cryptokey\"  # noqa: E501

        :return: The type of this Cryptokey.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Cryptokey.

        set to \"Cryptokey\"  # noqa: E501

        :param type: The type of this Cryptokey.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this Cryptokey.  # noqa: E501

        The internal identifier, read only  # noqa: E501

        :return: The id of this Cryptokey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Cryptokey.

        The internal identifier, read only  # noqa: E501

        :param id: The id of this Cryptokey.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def keytype(self):
        """Gets the keytype of this Cryptokey.  # noqa: E501


        :return: The keytype of this Cryptokey.  # noqa: E501
        :rtype: str
        """
        return self._keytype

    @keytype.setter
    def keytype(self, keytype):
        """Sets the keytype of this Cryptokey.


        :param keytype: The keytype of this Cryptokey.  # noqa: E501
        :type: str
        """
        allowed_values = ["ksk", "zsk", "csk"]  # noqa: E501
        if keytype not in allowed_values:
            raise ValueError(
                "Invalid value for `keytype` ({0}), must be one of {1}"  # noqa: E501
                .format(keytype, allowed_values)
            )

        self._keytype = keytype

    @property
    def active(self):
        """Gets the active of this Cryptokey.  # noqa: E501

        Whether or not the key is in active use  # noqa: E501

        :return: The active of this Cryptokey.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Cryptokey.

        Whether or not the key is in active use  # noqa: E501

        :param active: The active of this Cryptokey.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def published(self):
        """Gets the published of this Cryptokey.  # noqa: E501

        Whether or not the DNSKEY record is published in the zone  # noqa: E501

        :return: The published of this Cryptokey.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this Cryptokey.

        Whether or not the DNSKEY record is published in the zone  # noqa: E501

        :param published: The published of this Cryptokey.  # noqa: E501
        :type: bool
        """

        self._published = published

    @property
    def dnskey(self):
        """Gets the dnskey of this Cryptokey.  # noqa: E501

        The DNSKEY record for this key  # noqa: E501

        :return: The dnskey of this Cryptokey.  # noqa: E501
        :rtype: str
        """
        return self._dnskey

    @dnskey.setter
    def dnskey(self, dnskey):
        """Sets the dnskey of this Cryptokey.

        The DNSKEY record for this key  # noqa: E501

        :param dnskey: The dnskey of this Cryptokey.  # noqa: E501
        :type: str
        """

        self._dnskey = dnskey

    @property
    def ds(self):
        """Gets the ds of this Cryptokey.  # noqa: E501

        An array of DS records for this key  # noqa: E501

        :return: The ds of this Cryptokey.  # noqa: E501
        :rtype: list[str]
        """
        return self._ds

    @ds.setter
    def ds(self, ds):
        """Sets the ds of this Cryptokey.

        An array of DS records for this key  # noqa: E501

        :param ds: The ds of this Cryptokey.  # noqa: E501
        :type: list[str]
        """

        self._ds = ds

    @property
    def privatekey(self):
        """Gets the privatekey of this Cryptokey.  # noqa: E501

        The private key in ISC format  # noqa: E501

        :return: The privatekey of this Cryptokey.  # noqa: E501
        :rtype: str
        """
        return self._privatekey

    @privatekey.setter
    def privatekey(self, privatekey):
        """Sets the privatekey of this Cryptokey.

        The private key in ISC format  # noqa: E501

        :param privatekey: The privatekey of this Cryptokey.  # noqa: E501
        :type: str
        """

        self._privatekey = privatekey

    @property
    def algorithm(self):
        """Gets the algorithm of this Cryptokey.  # noqa: E501

        The name of the algorithm of the key, should be a mnemonic  # noqa: E501

        :return: The algorithm of this Cryptokey.  # noqa: E501
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this Cryptokey.

        The name of the algorithm of the key, should be a mnemonic  # noqa: E501

        :param algorithm: The algorithm of this Cryptokey.  # noqa: E501
        :type: str
        """

        self._algorithm = algorithm

    @property
    def bits(self):
        """Gets the bits of this Cryptokey.  # noqa: E501

        The size of the key  # noqa: E501

        :return: The bits of this Cryptokey.  # noqa: E501
        :rtype: int
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this Cryptokey.

        The size of the key  # noqa: E501

        :param bits: The bits of this Cryptokey.  # noqa: E501
        :type: int
        """

        self._bits = bits

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
        if issubclass(Cryptokey, dict):
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
        if not isinstance(other, Cryptokey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
