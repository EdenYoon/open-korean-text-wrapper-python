# coding: utf-8
#
# Copyright (c) 2017 Eden Yoon

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from openkoreantext import OpenKoreanTextProcessor


processor = OpenKoreanTextProcessor()


def parse_tokens(tokens):
    parsed_tokens = []
    format_token = '{text}({pos}: {offset}, {length})'
    for token in tokens:
        parsed_tokens.append(format_token.format(
            text=token.text,
            pos=token.pos,
            offset=token.offset,
            length=token.length,
        ))
    return '/'.join(parsed_tokens)


def test_expected_word(word, expected):
    print(word, expected)
    tokens = processor.tokenize(word)
    assert parse_tokens(tokens) == expected
