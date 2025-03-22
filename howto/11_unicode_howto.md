# Unicode HOWTO in Python

# Python에서의 유니코드 사용 가이드

## Introduction to Unicode

Unicode is a computing industry standard designed to consistently represent and handle text expressed in most of the world's writing systems. Before Unicode, there were hundreds of different encoding systems for assigning numeric values to graphical characters, particularly for languages other than English. This made it difficult to exchange data between different systems or languages.

Unicode solves this by assigning a unique numeric value (code point) to each character, regardless of platform, program, or language.

## 유니코드 소개

유니코드는 전 세계 대부분의 문자 체계로 표현된 텍스트를 일관되게 표현하고 처리하기 위해 설계된 컴퓨팅 산업 표준입니다. 유니코드가 등장하기 전에는 특히 영어 이외의 언어에 대해 그래픽 문자에 숫자 값을 할당하는 수백 가지의 다른 인코딩 시스템이 있었습니다. 이로 인해 서로 다른 시스템이나 언어 간에 데이터를 교환하기 어려웠습니다.

유니코드는 플랫폼, 프로그램 또는 언어에 관계없이 각 문자에 고유한 숫자 값(코드 포인트)을 할당함으로써 이 문제를 해결합니다.

## Unicode in Python

### Python 2 vs. Python 3

One of the most significant changes in Python 3 was the handling of strings. In Python 2, there were two string types: `str` for bytes and `unicode` for Unicode strings. In Python 3, the `str` type is used for Unicode strings, and a separate `bytes` type is used for sequences of bytes.

This change has simplified working with Unicode in Python 3, as all strings are Unicode by default.

### Python 2와 Python 3 비교

Python 3에서 가장 중요한 변경 사항 중 하나는 문자열 처리였습니다. Python 2에서는 두 가지 문자열 유형이 있었습니다: 바이트를 위한 `str`과 유니코드 문자열을 위한 `unicode`입니다. Python 3에서는 `str` 유형이 유니코드 문자열에 사용되고, 별도의 `bytes` 유형이 바이트 시퀀스에 사용됩니다.

이 변경으로 Python 3에서 유니코드 작업이 간소화되었으며, 모든 문자열은 기본적으로 유니코드입니다.

## Unicode Representation

### Code Points and Encodings

A Unicode code point is a unique number assigned to each Unicode character. For example, the character 'A' has the code point U+0041 (the prefix 'U+' means Unicode, and the numbers are hexadecimal).

An encoding is a way to represent these code points as bytes. Common encodings include:

- **UTF-8**: Variable-length encoding that uses 1-4 bytes per character. It's backward compatible with ASCII and is the most widely used encoding on the web.
- **UTF-16**: Uses 2 or 4 bytes per character.
- **UTF-32**: Uses exactly 4 bytes per character, making it fixed-length but memory-intensive.

### Python's Unicode Support

In Python 3, strings are sequences of Unicode code points. You can create a string with Unicode characters in several ways:

```python
# Direct input (if your editor supports it)
s1 = "Hello, 世界"

# Using escape sequences
s2 = "Hello, \u4e16\u754c"  # \u followed by 4-digit hex code
s3 = "Hello, \U0001f600"    # \U followed by 8-digit hex code for characters outside BMP

# Character name
s4 = "Hello, \N{GREEK CAPITAL LETTER DELTA}"  # Using the character name
```

## 유니코드 표현

### 코드 포인트와 인코딩

유니코드 코드 포인트는 각 유니코드 문자에 할당된 고유 번호입니다. 예를 들어, 문자 'A'는 코드 포인트 U+0041을 가집니다('U+' 접두사는 유니코드를 의미하며, 숫자는 16진수입니다).

인코딩은 이러한 코드 포인트를 바이트로 표현하는 방법입니다. 일반적인 인코딩에는 다음이 포함됩니다:

- **UTF-8**: 문자당 1-4바이트를 사용하는 가변 길이 인코딩입니다. ASCII와 역호환이 가능하며 웹에서 가장 널리 사용되는 인코딩입니다.
- **UTF-16**: 문자당 2 또는 4바이트를 사용합니다.
- **UTF-32**: 문자당 정확히 4바이트를 사용하여 고정 길이이지만 메모리 사용량이 많습니다.

### Python의 유니코드 지원

Python 3에서 문자열은 유니코드 코드 포인트의 시퀀스입니다. 여러 방법으로 유니코드 문자가 포함된 문자열을 만들 수 있습니다:

```python
# 직접 입력(편집기가 지원하는 경우)
s1 = "Hello, 世界"

# 이스케이프 시퀀스 사용
s2 = "Hello, \u4e16\u754c"  # \u 다음에 4자리 16진수 코드
s3 = "Hello, \U0001f600"    # \U 다음에 BMP 외부 문자를 위한 8자리 16진수 코드

# 문자 이름
s4 = "Hello, \N{GREEK CAPITAL LETTER DELTA}"  # 문자 이름 사용
```

## Encoding and Decoding

### Encoding: String to Bytes

Encoding is the process of converting a string (sequence of code points) to bytes:

```python
# String to bytes conversion
s = "Hello, 世界"
b1 = s.encode('utf-8')      # UTF-8 encoding
b2 = s.encode('utf-16')     # UTF-16 encoding
b3 = s.encode('iso-8859-1', errors='replace')  # Replace characters that can't be encoded

print(b1)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(b2)  # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x16N\x08u'
```

### Decoding: Bytes to String

Decoding is the process of converting bytes to a string:

```python
# Bytes to string conversion
b = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
s1 = b.decode('utf-8')      # Correctly decodes as UTF-8
s2 = b.decode('utf-8', errors='replace')  # Uses replacement character for invalid bytes

print(s1)  # "Hello, 世界"
```

### Error Handling

Python provides several error handling options for encoding/decoding:

- **strict**: Raises a UnicodeError exception (default)
- **ignore**: Ignores characters that can't be encoded/decoded
- **replace**: Replaces with a replacement character (? for encoding, � for decoding)
- **xmlcharrefreplace**: Replaces with XML character references (encoding only)
- **backslashreplace**: Replaces with backslashed escape sequences
- **surrogateescape**: Special handling for surrogate code points

```python
s = "Hello, 世界"
b = s.encode('ascii', errors='replace')  # b'Hello, ??'
```

## 인코딩 및 디코딩

### 인코딩: 문자열에서 바이트로

인코딩은 문자열(코드 포인트의 시퀀스)을 바이트로 변환하는 과정입니다:

```python
# 문자열에서 바이트로 변환
s = "Hello, 世界"
b1 = s.encode('utf-8')      # UTF-8 인코딩
b2 = s.encode('utf-16')     # UTF-16 인코딩
b3 = s.encode('iso-8859-1', errors='replace')  # 인코딩할 수 없는 문자를 대체

print(b1)  # b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
print(b2)  # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00\x16N\x08u'
```

### 디코딩: 바이트에서 문자열로

디코딩은 바이트를 문자열로 변환하는 과정입니다:

```python
# 바이트에서 문자열로 변환
b = b'Hello, \xe4\xb8\x96\xe7\x95\x8c'
s1 = b.decode('utf-8')      # UTF-8로 올바르게 디코딩
s2 = b.decode('utf-8', errors='replace')  # 잘못된 바이트에 대체 문자 사용

print(s1)  # "Hello, 世界"
```

### 오류 처리

Python은 인코딩/디코딩을 위한 여러 오류 처리 옵션을 제공합니다:

- **strict**: UnicodeError 예외를 발생시킵니다(기본값)
- **ignore**: 인코딩/디코딩할 수 없는 문자를 무시합니다
- **replace**: 대체 문자로 대체합니다(인코딩의 경우 ?, 디코딩의 경우 �)
- **xmlcharrefreplace**: XML 문자 참조로 대체합니다(인코딩만 해당)
- **backslashreplace**: 백슬래시 이스케이프 시퀀스로 대체합니다
- **surrogateescape**: 서로게이트 코드 포인트에 대한 특별 처리

```python
s = "Hello, 世界"
b = s.encode('ascii', errors='replace')  # b'Hello, ??'
```

## Common Unicode Issues

### BOM (Byte Order Mark)

The BOM is a Unicode character used to indicate the byte order (endianness) of a text file. It appears as the first character in a file:

- UTF-8: `\xef\xbb\xbf`
- UTF-16 (BE): `\xfe\xff`
- UTF-16 (LE): `\xff\xfe`

When reading files, you might need to handle the BOM:

```python
# Reading a file with BOM
with open('file.txt', 'r', encoding='utf-8-sig') as f:  # 'utf-8-sig' handles the BOM
    content = f.read()
```

### Unicode Normalization

Some characters can be represented in multiple ways in Unicode. For example, the character 'é' can be represented as a single code point (U+00E9) or as the letter 'e' followed by a combining accent (U+0065 + U+0301).

Python's `unicodedata` module provides functions for normalization:

```python
import unicodedata

# Different representations of the same character
s1 = '\u00e9'  # é as a single code point
s2 = '\u0065\u0301'  # e followed by combining accent

print(s1 == s2)  # False, different representations

# Normalize to NFC (composed form)
n1 = unicodedata.normalize('NFC', s1)
n2 = unicodedata.normalize('NFC', s2)
print(n1 == n2)  # True, same normalized form

# Normalize to NFD (decomposed form)
n3 = unicodedata.normalize('NFD', s1)
n4 = unicodedata.normalize('NFD', s2)
print(n3 == n4)  # True, same normalized form
```

## 일반적인 유니코드 문제

### BOM (바이트 순서 표식)

BOM은 텍스트 파일의 바이트 순서(엔디안)를 나타내는 데 사용되는 유니코드 문자입니다. 파일의 첫 번째 문자로 나타납니다:

- UTF-8: `\xef\xbb\xbf`
- UTF-16 (BE): `\xfe\xff`
- UTF-16 (LE): `\xff\xfe`

파일을 읽을 때 BOM을 처리해야 할 수 있습니다:

```python
# BOM이 있는 파일 읽기
with open('file.txt', 'r', encoding='utf-8-sig') as f:  # 'utf-8-sig'는 BOM을 처리합니다
    content = f.read()
```

### 유니코드 정규화

일부 문자는 유니코드에서 여러 방법으로 표현될 수 있습니다. 예를 들어, 문자 'é'는 단일 코드 포인트(U+00E9) 또는 문자 'e' 다음에 결합 액센트(U+0065 + U+0301)로 표현될 수 있습니다.

Python의 `unicodedata` 모듈은 정규화를 위한 함수를 제공합니다:

```python
import unicodedata

# 동일한 문자의 다른 표현
s1 = '\u00e9'  # 단일 코드 포인트로서의 é
s2 = '\u0065\u0301'  # 결합 액센트가 뒤따르는 e

print(s1 == s2)  # False, 다른 표현

# NFC(합성 형식)로 정규화
n1 = unicodedata.normalize('NFC', s1)
n2 = unicodedata.normalize('NFC', s2)
print(n1 == n2)  # True, 동일한 정규화 형식

# NFD(분해 형식)로 정규화
n3 = unicodedata.normalize('NFD', s1)
n4 = unicodedata.normalize('NFD', s2)
print(n3 == n4)  # True, 동일한 정규화 형식
```

## Working with Files

### Opening Files with the Correct Encoding

When opening a file, specify the encoding:

```python
# Writing a file
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, 世界")

# Reading a file
with open('output.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Detecting Encoding

Sometimes, you might not know the encoding of a file. The `chardet` library can help detect it:

```python
import chardet

# Read the binary data
with open('unknown.txt', 'rb') as f:
    raw_data = f.read()

# Detect the encoding
result = chardet.detect(raw_data)
encoding = result['encoding']
confidence = result['confidence']

print(f"Detected encoding: {encoding} with confidence {confidence}")

# Now read with the detected encoding
with open('unknown.txt', 'r', encoding=encoding) as f:
    content = f.read()
```

## 파일 작업

### 올바른 인코딩으로 파일 열기

파일을 열 때 인코딩을 지정하세요:

```python
# 파일 쓰기
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, 世界")

# 파일 읽기
with open('output.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### 인코딩 감지

때로는 파일의 인코딩을 모를 수 있습니다. `chardet` 라이브러리가 이를 감지하는 데 도움이 될 수 있습니다:

```python
import chardet

# 바이너리 데이터 읽기
with open('unknown.txt', 'rb') as f:
    raw_data = f.read()

# 인코딩 감지
result = chardet.detect(raw_data)
encoding = result['encoding']
confidence = result['confidence']

print(f"감지된 인코딩: {encoding}, 신뢰도 {confidence}")

# 이제 감지된 인코딩으로 읽기
with open('unknown.txt', 'r', encoding=encoding) as f:
    content = f.read()
```

## Unicode in Regular Expressions

### Unicode Categories

Python's `re` module supports Unicode character properties using the `\p{...}` syntax (only in Python 3.8+):

```python
import re

# Match any letter from any language
pattern = r"\p{L}+"  # One or more letters
text = "Hello, 世界, Привет!"
matches = re.findall(pattern, text)
print(matches)  # ['Hello', '世界', 'Привет']

# Match specific scripts
pattern_greek = r"\p{Script=Greek}+"
text_greek = "αβγδ"
matches_greek = re.findall(pattern_greek, text_greek)
print(matches_greek)  # ['αβγδ']
```

For older Python versions, you can use the `\X` character class to match Unicode characters:

```python
import re

# Python 3.7 and earlier
pattern = r"[\w\u0080-\uFFFF]+"
text = "Hello, 世界, Привет!"
matches = re.findall(pattern, text)
print(matches)  # ['Hello', '世界', 'Привет']
```

## 정규 표현식에서의 유니코드

### 유니코드 카테고리

Python의 `re` 모듈은 `\p{...}` 구문을 사용하여 유니코드 문자 속성을 지원합니다(Python 3.8 이상에서만):

```python
import re

# 모든 언어의 문자와 일치
pattern = r"\p{L}+"  # 하나 이상의 문자
text = "Hello, 世界, Привет!"
matches = re.findall(pattern, text)
print(matches)  # ['Hello', '世界', 'Привет']

# 특정 스크립트와 일치
pattern_greek = r"\p{Script=Greek}+"
text_greek = "αβγδ"
matches_greek = re.findall(pattern_greek, text_greek)
print(matches_greek)  # ['αβγδ']
```

이전 Python 버전의 경우, 유니코드 문자와 일치하도록 `\X` 문자 클래스를 사용할 수 있습니다:

```python
import re

# Python 3.7 이하
pattern = r"[\w\u0080-\uFFFF]+"
text = "Hello, 世界, Привет!"
matches = re.findall(pattern, text)
print(matches)  # ['Hello', '世界', 'Привет']
```

## Best Practices

1. **Always Specify Encodings**: When reading from or writing to files or network connections, always specify the encoding (usually UTF-8).

2. **Handle Encoding Errors**: Use appropriate error handling strategies (`errors='replace'`, `errors='ignore'`, etc.) based on your needs.

3. **Normalize Unicode Strings**: When comparing or searching Unicode strings, consider normalizing them first using `unicodedata.normalize()`.

4. **Use UTF-8**: For most applications, UTF-8 is the recommended encoding due to its compatibility with ASCII and wide support.

5. **Be Careful with Input/Output**: Always validate and sanitize user input, especially when dealing with multiple encodings.

6. **Know Your Data**: Understanding the source and destination of your data can help prevent encoding issues.

7. **Use Modern Python**: Python 3's handling of Unicode is much more consistent and less error-prone than Python 2's.

## 모범 사례

1. **항상 인코딩 지정하기**: 파일이나 네트워크 연결에서 읽거나 쓸 때 항상 인코딩을 지정하세요(일반적으로 UTF-8).

2. **인코딩 오류 처리하기**: 필요에 따라 적절한 오류 처리 전략(`errors='replace'`, `errors='ignore'` 등)을 사용하세요.

3. **유니코드 문자열 정규화하기**: 유니코드 문자열을 비교하거나 검색할 때는 먼저 `unicodedata.normalize()`를 사용하여 정규화를 고려하세요.

4. **UTF-8 사용하기**: 대부분의 애플리케이션에서는 ASCII와의 호환성과 광범위한 지원으로 인해 UTF-8이 권장 인코딩입니다.

5. **입력/출력 주의하기**: 특히 여러 인코딩을 다룰 때 사용자 입력을 항상 검증하고 정제하세요.

6. **데이터 알기**: 데이터의 출처와 목적지를 이해하면 인코딩 문제를 예방하는 데 도움이 됩니다.

7. **최신 Python 사용하기**: Python 3의 유니코드 처리는 Python 2보다 훨씬 일관되고 오류가 적습니다.

## Conclusion

Unicode support in Python 3 makes working with text from different languages and scripts much easier than in previous versions. By understanding the basics of Unicode, encodings, and common pitfalls, you can effectively handle text from any language in your Python applications.

Remember that most Unicode-related issues stem from improperly specified encodings or mixing encoded and decoded data. Following the best practices outlined in this guide will help you avoid these common problems.

## 결론

Python 3의 유니코드 지원은 이전 버전보다 다양한 언어와 스크립트의 텍스트 작업을 훨씬 쉽게 만듭니다. 유니코드의 기본, 인코딩 및 일반적인 함정을 이해함으로써 Python 애플리케이션에서 모든 언어의 텍스트를 효과적으로 처리할 수 있습니다.

대부분의 유니코드 관련 문제는 잘못 지정된 인코딩이나 인코딩된 데이터와 디코딩된 데이터의 혼합에서 비롯된다는 점을 기억하세요. 이 가이드에 설명된 모범 사례를 따르면 이러한 일반적인 문제를 피하는 데 도움이 될 것입니다.

