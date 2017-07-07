# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jaepil Jeong, Originated by
# Copyright (c) 2017 Eden Yoon, Modified by

import os
import imp

from collections import namedtuple

import jpype

from openkoreantext.escape import to_unicode, to_utf8, unicode_type


def _init_jvm():
    if not jpype.isJVMStarted():
        jars = []
        for top, dirs, files in os.walk(imp.find_module("openkoreantext")[1] + "/data/lib"):
            for nm in files:
                jars.append(os.path.join(top, nm))
        jpype.startJVM(jpype.getDefaultJVMPath(),
                       "-Djava.class.path=%s" % os.pathsep.join(jars))

_init_jvm()


_OpenKoreanTextProcessor = jpype.JClass("org.openkoreantext.processor.OpenKoreanTextProcessor")

KoreanToken = namedtuple("KoreanToken", ["text", "pos", "offset", "length"])
KoreanPhrase = namedtuple("KoreanPhrase", ["text", "offset", "length"])


class OpenKoreanTextProcessor(object):
    def __init__(self):
        super(OpenKoreanTextProcessor, self).__init__()
        self._processor = _OpenKoreanTextProcessor

    def normalize(self, text):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type)\
            else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        return decode(self._processor.normalize(encode(text)))

    def tokenize(self, text, normalization=True):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type) else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        if normalization:
            text = self._processor.normalize(encode(text))

        tokens = self._processor.tokenize(encode(text))
        korean_tokens = []
        for idx in range(tokens.length()):
            t = tokens.apply(jpype.java.lang.Integer(idx))
            korean_tokens.append(KoreanToken(
                text=decode(t.text()),
                pos=decode(t.pos().toString()),
                offset=decode(t.offset()),
                length=decode(t.length())
            ))
        return korean_tokens

    def extractPhrases(self, text, normalization=True):
        encode = lambda t: jpype.java.lang.String(t) if isinstance(text, unicode_type) else jpype.java.lang.String(to_unicode(t))
        decode = lambda t: t if isinstance(text, unicode_type) else to_utf8(t)

        if normalization:
            text = self._processor.normalize(encode(text))

        tokens = self._processor.tokenize(encode(text))
        tokens = self._processor.extractPhrases(tokens, True, True)
        korean_tokens = []
        for idx in range(tokens.length()):
            t = tokens.apply(jpype.java.lang.Integer(idx))
            korean_tokens.append(KoreanPhrase(
                text=decode(t.text()),
                offset=decode(t.offset()),
                length=decode(t.length())
            ))
        return korean_tokens
