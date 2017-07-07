# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong, Originated by
# Copyright (c) 2017 Eden Yoon, Modified by

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

# # output: [
# #     (한국어, Noun, 0), (를, Josa, 0), (처리, Noun, 0), (하다, Verb, 0),
# #     (예시, Noun, 0), (이다, Adjective, 0), (ㅋㅋ, KoreanParticle, 0)
# # ]
tokens = processor.tokenize(nomalized_text)
print('Tokens:')
print_tokens(tokens)

tokens = processor.extractPhrases(text)
print('Extract Phrases:')
print_tokens(tokens)
