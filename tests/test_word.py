# coding: utf-8
#
# Copyright (c) 2017 Eden Yoon

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from openkoreantext import OpenKoreanTextProcessor


processor = OpenKoreanTextProcessor()


def test_word(word):
    tokens = processor.tokenize(word)
    assert len(tokens) == 1
    assert tokens[0].text == word
    assert tokens[0].pos == 'Noun'
