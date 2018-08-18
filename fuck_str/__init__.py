# coding: utf-8
"""
python2 str(bytes) unicode
python3 bytes      str
"""
import sys

if sys.version_info[0] < 3:
    is_py2 = True
else:
    is_py2 = False

is_py3 = not is_py2


class NonStringLikeException(Exception):
    pass


def ensure_str_like(x):
    if is_py2:
        if not isinstance(x, (str, unicode)):
            raise NonStringLikeException(
                "expect a string like type, got {}".format(type(x))
            )
    else:
        if not isinstance(x, (bytes, str)):
            raise NonStringLikeException(
                "expect a string like type, got {}".format(type(x))
            )


def ensure_str(x):
    if isinstance(x, str):
        return x

    ensure_str_like(x)

    if is_py2:
        if isinstance(x, unicode):
            return x.encode("utf-8")
    else:
        if isinstance(x, bytes):
            return x.decode("utf-8")


def is_unicode(x):
    if is_py2:
        if isinstance(x, unicode):
            return True
    else:
        if isinstance(x, str):
            return True
    return False


def ensure_unicode(x):
    if is_unicode(x):
        return True

    ensure_str_like(x)
    return x.decode("utf-8")


def is_bytes(x):
    if is_py2:
        if isinstance(x, str):
            return True
    else:
        if isinstance(x, bytes):
            return True
    return False


def ensure_bytes(x):
    if is_bytes(x):
        return x

    ensure_str_like(x)
    return x.encode("utf-8")
