# coding: utf-8
#
# Copyright (c) 2017 Eden Yoon

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function


def normalize_word(word):
    word = word.strip()
    return word


def parse_case(case):
    case = case.rstrip('\n')
    return case.split('\t')


def generate_test_expected_word(metafunc):
    cases = []
    with open('test.txt', 'r', encoding='utf-8') as test_case:
        cases.extend([parse_case(case) for case in test_case])

    metafunc.parametrize('word,expected', cases)


def generate_test_word(metafunc):
    words = []
    # with open('fashion.txt', 'r', encoding='utf-8') as fashion_words:
    #     words.extend([normalize_word(word) for word in fashion_words])

    # with open('nouns.txt', 'r', encoding='utf-8') as nouns:
    #   words.extend([normalize_word(word) for word in nouns])

    with open('neologism.txt', 'r', encoding='utf-8') as neologism_words:
        words.extend([normalize_word(word) for word in neologism_words])

    metafunc.parametrize('word', words)


def pytest_generate_tests(metafunc):
    if ['word', 'expected'] == metafunc.fixturenames:
        generate_test_expected_word(metafunc)
    elif ['word'] == metafunc.fixturenames:
        generate_test_word(metafunc)
