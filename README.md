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

## Example

run [example.py](https://github.com/EdenYoon/open-korean-text-wrapper-python/blob/master/example.py).

```bash
> python example.py
Text:  한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ
Nomalized Text:  한국어를 처리하는 예시입니다ㅋㅋㅋ
Tokens:
[(한국어, Noun, 0, 3), (를, Josa, 3, 1), ( , Space, 4, 1), (처리, Noun, 5, 2), (하는, Verb, 7, 2), ( , Space, 9, 1), (예시, Noun, 10, 2), (입니다, Adjective, 12, 3), (ㅋㅋㅋ, KoreanParticle, 15, 3)]
Extract Phrases:
[(한국어, 0, 3), (처리, 5, 2), (처리하는 예시, 5, 7), (예시, 10, 2)]
```

## Links

* [open-korean-text-wrapper-python](https://github.com/open-korean-text/open-korean-text-wrapper-python)
  * Original wrapper for [twitter-korean-text](https://github.com/twitter/twitter-korean-text)
* [OpenKoreanText](https://pypi.python.org/pypi/OpenkoreanText) package on PyPI
