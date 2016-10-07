#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function testing the truthiness of the argument."""


def bool_to_str(bval):
    """A function returns 'Yes' or 'No' to the truthiness of the argument.

    Args:
        bval (mixed): a boolean or boolean-like value to be tested.

    Returns:
        Str: 'Yes' for truthy value, 'No' for falsy value.

    Examples:
        >>> bool_to_str(1)
        'Yes'

        >>> bool_to_str('')
        'No'
    """
    if bval:
        string = 'Yes'
    else:
        string = 'No'
    return string
