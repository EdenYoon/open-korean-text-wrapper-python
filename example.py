# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong, Originated by
# Copyright (c) 2017 Eden Yoon, Modified by

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from openkoreantext import OpenKoreanTextProcessor


def print_tokens(tokens, end="\n"):
    if isinstance(tokens, list):
        print("[", end="")
    elif isinstance(tokens, tuple):
        print("(", end="")

    for t in tokens:
        if t != tokens[-1]:
            elem_end = ", "
        else:
            elem_end = ""

        if isinstance(t, (list, tuple)):
            print_tokens(t, end=elem_end)
        else:
            print(t, end=elem_end)

    if isinstance(tokens, list):
        print("]", end=end)
    elif isinstance(tokens, tuple):
        print(")", end=end)


text = u"한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ"
print('Text: ', text)

# Tokenize with normalization + stemmer
processor = OpenKoreanTextProcessor()

nomalized_text = processor.normalize(text)
print('Nomalized Text: ', nomalized_text)

tokens = processor.tokenize(nomalized_text)
print('\nTokens:')
print_tokens(tokens)

tokens = processor.extract_phrases(text)
print('\nExtract Phrases:')
print_tokens(tokens)

# Add nouns to dictionary
print('\nExample of add_nouns_to_dictionary:')
tokens = processor.tokenize('오픈코리안텍스트을 사용합니다.')
print_tokens(tokens)
print('\nAdded "오픈코리안텍스트" to dictionary as Noun.')
processor.add_nouns_to_dictionary(['오픈코리안텍스트'])
tokens = processor.tokenize('오픈코리안텍스트을 사용합니다.')
print_tokens(tokens)
