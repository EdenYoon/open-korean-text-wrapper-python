OpenKoreanText
========

Python interface to [open-korean-text](https://github.com/open-korean-text/open-korean-text).


## Required packages
The following tools and libraries are required to build SentencePiece:

* [JPype1](https://pypi.python.org/pypi/JPype1)

## Intall

```bash
sudo pip install openkoreantext
```

## Upgrade

```bash
sudo pip install openkoreantext --upgrade
```

## Example

Run [example.py](https://github.com/EdenYoon/open-korean-text-wrapper-python/blob/master/example.py).

```bash
> python example.py
Text:  한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ
Nomalized Text:  한국어를 처리하는 예시입니다ㅋㅋㅋ
Tokens:
[(한국어, Noun, 0, 3), (를, Josa, 3, 1), ( , Space, 4, 1), (처리, Noun, 5, 2), (하는, Verb, 7, 2), ( , Space, 9, 1), (예시, Noun, 10, 2), (입니다, Adjective, 12, 3), (ㅋㅋㅋ, KoreanParticle, 15, 3)]
Extract Phrases:
[(한국어, 0, 3), (처리, 5, 2), (처리하는 예시, 5, 7), (예시, 10, 2)]
```

## Test
* Python `2.7`, `3.5`, `3.6` on `Mac 10.12.5` and `Ubuntu 16.04.2 LTS`

## Trouble Shooting
* If you met similar error with following, use `Java 8`.
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/ubuntu/.pyenv/versions/ko-nlp/lib/python3.6/site-packages/openkoreantext/__init__.py", line 28, in <module>
    _OpenKoreanTextProcessor = jpype.JClass("org.openkoreantext.processor.OpenKoreanTextProcessor")
  File "/home/ubuntu/.pyenv/versions/ko-nlp/lib/python3.6/site-packages/jpype/_jclass.py", line 55, in JClass
    raise _RUNTIMEEXCEPTION.PYEXC("Class %s not found" % name)
jpype._jexception.RuntimeExceptionPyRaisable: java.lang.RuntimeException: Class org.openkoreantext.processor.OpenKoreanTextProcessor not found```
```

## Links

* [open-korean-text-wrapper-python](https://github.com/open-korean-text/open-korean-text-wrapper-python)
  * Original wrapper for [twitter-korean-text](https://github.com/twitter/twitter-korean-text)
* [OpenKoreanText](https://pypi.python.org/pypi/OpenkoreanText) package on PyPI
