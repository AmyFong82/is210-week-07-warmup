#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function returns the max. min and average length of words in a speech."""

import decimal


def lexicographics(to_analyze):
    """It calculates the max. min. and the average length of words in a speech.

    Args:
        to_analyze (str): a string to be analyzed.

    Returns:
        tuple: the max line in to_analyze, the min line, and the average line.

    Examples:
        >>>lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal('4'))

        >>>lexicographics('''Don't stop believing,
        Hold on to that feeling.
        Forever and ever.''')
        (5, 3, Decimal('3.666666666666666666666666667'))
    """
    line = to_analyze.split('\n')
    word_count = []
    for words in line:
        len_line = len(words.split())
        word_count.append(len_line)
    ave = decimal.Decimal(sum(word_count))/len(word_count)
    return max(word_count), min(word_count), ave
