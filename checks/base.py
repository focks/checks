import json

from collections import Iterable

from io import IOBase


# Numbers
def is_int(n):
    """
    :return: Returns `True` if n is an integer.
    """
    return isinstance(n, int)


def is_integer(n):
    """
    :return: Returns `True` if n is an integer.
    """
    return isinstance(n, int)


def is_decimal(n):
    """
    :return: Returns `True` if n is an decimal/float.
    """
    return isinstance(n, float)


def is_number(n):
    """
    :return: Returns `True` if n is an integer or decimal.
    """
    return isinstance(n, int) or isinstance(n, float)


def is_even(n):
    """
    :return: Returns `True` if n is even.
    """
    return n % 2 == 0


def is_odd(n):
    """
    :return: Returns `True` if n is even.
    """
    return n % 2 == 1


def is_positive(n):
    """
    :return: Returns `True` if n is positive.
    """
    return n > 0


def is_negative(n):
    """
    :return: Returns `True` if n is negative.
    """
    return n < 0


def is_pow2(n):
    pass


def is_powx(n, x):
    pass


def is_under(n, max_):
    """
    :return: Returns `True` if n is less than max_.
    """
    return n < max_


def is_above(n, min_):
    """
    :return: Returns `True` if n is greater than min_.
    """
    return n > min_


def is_within(n, min_, max_):
    """
    :return: Returns `True` if n is within range (min_, max_).
    """
    return min_ < n < max_


def is_divisible():
    pass


def is_boolean(b):
    """
    :return: Returns `True` if b is of boolean type.
    """
    return isinstance(b, bool)


def is_string(s):
    """
    :return: Returns `True` if s is a string.
    """
    return isinstance(s, str)


def is_char(c):
    """
    :return: Returns `True` if c is a character.
    """
    return isinstance(c, str) and len(c) == 1


def is_allcap(s):
    """
    :return: Returns `True` if all characters in s are uppercase.
    """
    return s.isupper()


def is_upper(s):
    """
    :return: Returns `True` if  all characters in s are uppercase.
    """
    return s.isupper()


def is_lower(s):
    """
    :return: Returns `True` if all characters in s are lowercase.
    """
    return s.islower()


def is_digit(s):
    """
    :return: Returns `True` if string s is an integer number.
    """
    return s.isdigit()


# strings


def is_space(s):
    """
    :return: Returns `True` if s contains ' ', tab, newlines only.
    """
    return s.isspace()


def is_palindrome(s):
    """
    :return: Returns `True` if s is a palindrome.
    """
    return s == s[::-1]


def is_start_with(s, t):
    """
    :return: Returns `True` if t starts with s
    """
    return t.startswith(s)


def is_end_with(s, t):
    """
    :return: Returns `True` if t ends with s.
    """
    return t.endswith(s)


def is_include(s, t):
    """
    :return: Returns `True` if s is part of string t.
    """
    return s in t


# lists
def is_empty(o):
    return len(o) == 0


def is_list(o):
    """
    :return: Returns `True` if the given value is list.
    """
    return isinstance(o, list)


def is_empty_list(o):
    """
    :return: Returns `True` if the given list is empty.
    """
    return is_empty(o)


def is_set(s):
    """
    :return: Returns `True` if s is an set.
    """
    return isinstance(s, set)


def is_tuple(t):
    """
    :return: Returns `True` if t is a tuple.
    """
    return isinstance(t, tuple)


def is_empty_set(s):
    """
    :return: Returns `True` if set s is an empty.
    """
    return is_empty(s)


def is_empty_tuple(t):
    """
    :return: Returns `True` if tuple t is empty.
    """
    return is_empty(t)


# dicts
def is_dict(o):
    """
    :return: Returns `True` if the given value is python dict.
    """
    return isinstance(o, dict)


def is_json(o):
    """
    :return: Returns `True` if string given is stringified json.
    """
    try:
        _ = json.loads(o)
    except ValueError:
        return False
    return True


def is_object(o):
    """
    :return: Returns `True` if o is an object.
    """
    return isinstance(o, type)


# other
def is_iterable(o):
    """
    :return: Returns `True` if o is an iterable.
    """
    return isinstance(o, Iterable)


def is_error(e):
    """
    :return: Returns `True` if e is an exception.
    """
    return isinstance(e, Exception)


def is_fileobject(f):
    """
    :return: Returns `True` if f is a file object.
    """
    return isinstance(f, IOBase)


def is_none(o):
    """
    :return: Returns `True` if o is of NoneType
    """
    return o is None
