#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Parsing tools.
"""

from __future__ import print_function, absolute_import, unicode_literals, division

import footprints.loggers

logger = footprints.loggers.getLogger(__name__)

#: No automatic export
__all__ = []


def str2dict(string, try_convert=None):
    """
    Parse a **string** (of syntax 'key1:value1,key2=value2') to a dict.

    :param try_convert: try to convert values as type **try_convert**,
                        e.g. try_convert=int
    """
    if ':' not in string and '=' not in string:
        raise SyntaxError("string: '{}' is not convertible to a dict".format(string))
    d = {i.replace('=', ':').split(':')[0].strip() : i.replace('=', ':').split(':')[1].strip()
         for i in string.split(',')}
    if try_convert is not None:
        for k, v in d.items():
            try:
                d[k] = try_convert(v)
            except ValueError:
                pass
    return d
