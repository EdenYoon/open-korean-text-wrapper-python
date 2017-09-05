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
_OpenKoreanTextProcessorJava = jpype.JClass("org.openkoreantext.processor.OpenKoreanTextProcessorJava")

KoreanToken = namedtuple("KoreanToken", ["text", "pos", "offset", "length"])
KoreanPhrase = namedtuple("KoreanPhrase", ["text", "offset", "length"])


class OpenKoreanTextProcessor(object):
    def __init__(self):
        super(OpenKoreanTextProcessor, self).__init__()
        self._processor = _OpenKoreanTextProcessor
        self._processor_java = _OpenKoreanTextProcessorJava

        self.encode = lambda t: jpype.java.lang.String(t) if isinstance(t, unicode_type) else jpype.java.lang.String(to_unicode(t))
        self.decode = lambda t: t if isinstance(t, unicode_type) else to_utf8(t)

    def normalize(self, text):
        return self.decode(self._processor.normalize(self.encode(text)))

    def tokenize(self, text, normalization=True):
        if normalization:
            text = self._processor.normalize(self.encode(text))

        tokens = self._processor.tokenize(self.encode(text))
        korean_tokens = []
        for idx in range(tokens.length()):
            t = tokens.apply(jpype.java.lang.Integer(idx))
            korean_tokens.append(KoreanToken(
                text=self.decode(t.text()),
                pos=self.decode(t.pos().toString()),
                offset=self.decode(t.offset()),
                length=self.decode(t.length())
            ))
        return korean_tokens

    def extract_phrases(self, text, normalization=True):
        if normalization:
            text = self._processor.normalize(self.encode(text))

        tokens = self._processor.tokenize(self.encode(text))
        tokens = self._processor.extractPhrases(tokens, True, True)
        korean_tokens = []
        for idx in range(tokens.length()):
            t = tokens.apply(jpype.java.lang.Integer(idx))
            korean_tokens.append(KoreanPhrase(
                text=self.decode(t.text()),
                offset=self.decode(t.offset()),
                length=self.decode(t.length())
            ))
        return korean_tokens

    def add_nouns_to_dictionary(self, nouns):
        jlist_nouns = jpype.java.util.ArrayList()
        for noun in nouns:
            jlist_nouns.add(self.encode(noun))

        self._processor_java.addNounsToDictionary(jlist_nouns)
