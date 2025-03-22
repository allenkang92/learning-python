# Regular Expression HOWTO in Python

# Python에서의 정규 표현식 사용 가이드

## Introduction

Regular expressions (or regexes) are a powerful language for matching text patterns. This guide explains Python's regular expression features and helps you use them effectively.

## 소개

정규 표현식(또는 정규식)은 텍스트 패턴을 매칭하기 위한 강력한 언어입니다. 이 가이드는 Python의 정규 표현식 기능을 설명하고 효과적으로 사용하도록 도와줍니다.

## Regular Expression Basics

A regular expression specifies a set of strings that matches it. Functions in the `re` module let you check if a string matches a given pattern or find occurrences within a string.

### Basic Patterns

Here are some basic patterns:

```python
import re

# Simple pattern matching
match = re.search('pattern', 'text with pattern')
if match:
    print("Pattern found!")
    
# Match at beginning of string
match = re.match('start', 'start of the text')
if match:
    print("Pattern at start!")
    
# Find all occurrences
matches = re.findall('a', 'abracadabra')
print(matches)  # ['a', 'a', 'a', 'a', 'a']
```

## 정규 표현식 기초

정규 표현식은 그것과 일치하는 문자열 집합을 지정합니다. `re` 모듈의 함수를 사용하면 문자열이 주어진 패턴과 일치하는지 확인하거나 문자열 내의 발생을 찾을 수 있습니다.

### 기본 패턴

다음은 몇 가지 기본 패턴입니다:

```python
import re

# 간단한 패턴 매칭
match = re.search('pattern', 'text with pattern')
if match:
    print("패턴을 찾았습니다!")
    
# 문자열 시작 부분에서 매칭
match = re.match('start', 'start of the text')
if match:
    print("시작 부분에 패턴이 있습니다!")
    
# 모든 발생 찾기
matches = re.findall('a', 'abracadabra')
print(matches)  # ['a', 'a', 'a', 'a', 'a']
```

## Regular Expression Syntax

### Metacharacters

Metacharacters are characters with special meaning:

. ^ $ * + ? { } [ ] \ | ( )

The first metacharacters we’ll look at are [ and ]. They’re used for specifying a character class, which is a set of characters that you wish to match. Characters can be listed individually, or a range of characters can be indicated by giving two characters and separating them by a '-'. For example, [abc] will match any of the characters a, b, or c; this is the same as [a-c], which uses a range to express the same set of characters. If you wanted to match only lowercase letters, your RE would be [a-z].

Metacharacters (except \) are not active inside classes. For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'; '$' is usually a metacharacter, but inside a character class it’s stripped of its special nature.

You can match the characters not listed within the class by complementing the set. This is indicated by including a '^' as the first character of the class. For example, [^5] will match any character except '5'. If the caret appears elsewhere in a character class, it does not have special meaning. For example: [5^] will match either a '5' or a '^'.

Perhaps the most important metacharacter is the backslash, \. As in Python string literals, the backslash can be followed by various characters to signal various special sequences. It’s also used to escape all the metacharacters so you can still match them in patterns; for example, if you need to match a [ or \, you can precede them with a backslash to remove their special meaning: \[ or \\.

Some of the special sequences beginning with '\' represent predefined sets of characters that are often useful, such as the set of digits, the set of letters, or the set of anything that isn’t whitespace.

Let’s take an example: \w matches any alphanumeric character. If the regex pattern is expressed in bytes, this is equivalent to the class [a-zA-Z0-9_]. If the regex pattern is a string, \w will match all the characters marked as letters in the Unicode database provided by the unicodedata module. You can use the more restricted definition of \w in a string pattern by supplying the re.ASCII flag when compiling the regular expression.

The following list of special sequences isn’t complete. For a complete list of sequences and expanded class definitions for Unicode string patterns, see the last part of Regular Expression Syntax in the Standard Library reference. In general, the Unicode versions match any character that’s in the appropriate category in the Unicode database.

\d
Matches any decimal digit; this is equivalent to the class [0-9].

\D
Matches any non-digit character; this is equivalent to the class [^0-9].

\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

These sequences can be included inside a character class. For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.

The final metacharacter in this section is .. It matches anything except a newline character, and there’s an alternate mode (re.DOTALL) where it will match even a newline. . is often used where you want to match “any character”.

## 정규 표현식 구문

### 메타문자

메타문자는 특별한 의미를 가진 문자입니다:

. ^ $ * + ? { } [ ] \ | ( )

우리가 살펴볼 첫 번째 메타문자는 [와 ]입니다. 이들은 매칭하고자 하는 문자 집합을 지정하는 데 사용됩니다. 문자는 개별적으로 나열할 수 있으며, 두 문자를 '-'로 구분하여 문자 범위를 나타낼 수 있습니다. 예를 들어, [abc]는 a, b 또는 c 문자를 매칭합니다. 이는 동일한 문자 집합을 표현하기 위해 범위를 사용하는 [a-c]와 동일합니다. 소문자만 매칭하려면, 정규식은 [a-z]가 됩니다.

메타문자(\ 제외)는 클래스 내에서 활성화되지 않습니다. 예를 들어, [akm$]는 'a', 'k', 'm' 또는 '$' 문자를 매칭합니다. '$'는 일반적으로 메타문자이지만, 문자 클래스 내에서는 특별한 성격이 제거됩니다.

클래스 내에 나열되지 않은 문자를 매칭하려면 집합을 보완할 수 있습니다. 이는 클래스의 첫 번째 문자로 '^'를 포함하여 표시됩니다. 예를 들어, [^5]는 '5'를 제외한 모든 문자를 매칭합니다. 캐럿이 문자 클래스 내 다른 위치에 나타나면 특별한 의미가 없습니다. 예를 들어: [5^]는 '5' 또는 '^'를 매칭합니다.

아마도 가장 중요한 메타문자는 백슬래시(\)일 것입니다. Python 문자열 리터럴에서와 같이, 백슬래시는 다양한 문자를 따라와서 다양한 특수 시퀀스를 신호할 수 있습니다. 또한 모든 메타문자를 이스케이프하여 패턴에서 여전히 매칭할 수 있습니다. 예를 들어, [ 또는 \를 매칭해야 하는 경우, 백슬래시를 앞에 두어 특별한 의미를 제거할 수 있습니다: \[ 또는 \\.

백슬래시로 시작하는 일부 특수 시퀀스는 종종 유용한 미리 정의된 문자 집합을 나타냅니다. 예를 들어, 숫자 집합, 문자 집합 또는 공백이 아닌 모든 것의 집합이 있습니다.

예를 들어 보겠습니다: \w는 모든 영숫자 문자를 매칭합니다. 정규식 패턴이 바이트로 표현되면, 이는 클래스 [a-zA-Z0-9_]와 동일합니다. 정규식 패턴이 문자열이면, \w는 unicodedata 모듈에서 제공하는 유니코드 데이터베이스에서 문자로 표시된 모든 문자를 매칭합니다. 정규식을 컴파일할 때 re.ASCII 플래그를 제공하여 문자열 패턴에서 \w의 더 제한된 정의를 사용할 수 있습니다.

다음은 특수 시퀀스의 전체 목록이 아닙니다. 유니코드 문자열 패턴에 대한 시퀀스 및 확장 클래스 정의의 전체 목록은 표준 라이브러리 참조의 정규 표현식 구문 마지막 부분을 참조하십시오. 일반적으로 유니코드 버전은 유니코드 데이터베이스의 적절한 범주에 있는 모든 문자를 매칭합니다.

\d
모든 십진수를 매칭합니다. 이는 클래스 [0-9]와 동일합니다.

\D
숫자가 아닌 모든 문자를 매칭합니다. 이는 클래스 [^0-9]와 동일합니다.

\s
모든 공백 문자를 매칭합니다. 이는 클래스 [ \t\n\r\f\v]와 동일합니다.

\S
공백이 아닌 모든 문자를 매칭합니다. 이는 클래스 [^ \t\n\r\f\v]와 동일합니다.

\w
모든 영숫자 문자를 매칭합니다. 이는 클래스 [a-zA-Z0-9_]와 동일합니다.

\W
영숫자가 아닌 모든 문자를 매칭합니다. 이는 클래스 [^a-zA-Z0-9_]와 동일합니다.

이러한 시퀀스는 문자 클래스 내에 포함될 수 있습니다. 예를 들어, [\s,.]는 공백 문자, ',' 또는 '.'를 매칭하는 문자 클래스입니다.

이 섹션의 마지막 메타문자는 .입니다. 이는 줄 바꿈 문자를 제외한 모든 것을 매칭합니다. re.DOTALL 모드에서는 줄 바꿈까지 매칭합니다. .은 종종 "모든 문자"를 매칭하고자 할 때 사용됩니다.

### Repeating Things

Being able to match varying sets of characters is the first thing regular expressions can do that isn't already possible with the methods available on strings. However, if that was the only additional capability of regexes, they wouldn't be much of an advance. Another capability is that you can specify that portions of the RE must be repeated a certain number of times.

The first metacharacter for repeating things that we'll look at is *. * doesn't match the literal character '*'; instead, it specifies that the previous character can be matched zero or more times, instead of exactly once.

For example, ca*t will match 'ct' (0 'a' characters), 'cat' (1 'a'), 'caaat' (3 'a' characters), and so forth.

### 반복하기

다양한 문자 집합을 매칭할 수 있는 능력은 정규 표현식이 문자열에서 사용 가능한 방법으로는 이미 불가능한 첫 번째 기능입니다. 하지만 그것이 정규식의 유일한 추가 기능이라면, 그다지 발전이 없을 것입니다. 또 다른 기능은 정규식의 일부를 특정 횟수만큼 반복해야 한다고 지정할 수 있다는 것입니다.

살펴볼 첫 번째 반복 메타문자는 *입니다. *는 문자 그대로의 '*'와 매칭되지 않습니다. 대신, 이전 문자가 정확히 한 번이 아니라 0번 이상 반복될 수 있음을 지정합니다.

예를 들어, ca*t는 'ct'(0개의 'a' 문자), 'cat'(1개의 'a'), 'caaat'(3개의 'a' 문자) 등과 매칭됩니다.

Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with fewer repetitions.

* 와 같은 반복은 탐욕적입니다; 정규 표현식을 반복할 때, 매칭 엔진은 가능한 한 많이 반복하려고 시도합니다. 만약 패턴의 뒷부분이 매칭되지 않으면, 매칭 엔진은 되돌아가서 더 적은 반복으로 다시 시도합니다.

A step-by-step example will make this more obvious. Let’s consider the expression a[bcd]*b. This matches the letter 'a', zero or more letters from the class [bcd], and finally ends with a 'b'. Now imagine matching this RE against the string 'abcbd'.

단계별 예제를 통해 이를 더 명확하게 이해해 봅시다. 표현식 a[bcd]*b를 고려해봅시다. 이것은 'a' 문자, [bcd] 클래스에서 0개 이상의 문자, 그리고 마지막으로 'b'로 끝나는 패턴입니다. 이제 이 정규식이 'abcbd' 문자열과 매칭되는 과정을 살펴봅시다.

Step | Matched | Explanation
-----|---------|------------
1 | a | The a in the RE matches.
2 | abcbd | The engine matches [bcd]*, going as far as it can, which is to the end of the string.
3 | Failure | The engine tries to match b, but the current position is at the end of the string, so it fails.
4 | abcb | Back up, so that [bcd]* matches one less character.
5 | Failure | Try b again, but the current position is at the last character, which is a 'd'.
6 | abc | Back up again, so that [bcd]* is only matching bc.
6 | abcb | Try b again. This time the character at the current position is 'b', so it succeeds.

단계 | 매칭됨 | 설명
-----|---------|------------
1 | a | 정규식의 a가 매칭됩니다.
2 | abcbd | 엔진이 [bcd]*를 매칭하며, 문자열의 끝까지 최대한 진행합니다.
3 | 실패 | 엔진이 b를 매칭하려고 시도하지만, 현재 위치는 문자열의 끝이어서 실패합니다.
4 | abcb | 되돌아가서 [bcd]*가 한 문자 적게 매칭하도록 합니다.
5 | 실패 | b를 다시 시도하지만, 현재 위치는 'd'인 마지막 문자에 있습니다.
6 | abc | 다시 되돌아가서 [bcd]*가 bc만 매칭하도록 합니다.
6 | abcb | b를 다시 시도합니다. 이번에는 현재 위치의 문자가 'b'이므로 성공합니다.

The end of the RE has now been reached, and it has matched 'abcb'. This demonstrates how the matching engine goes as far as it can at first, and if no match is found it will then progressively back up and retry the rest of the RE again and again. It will back up until it has tried zero matches for [bcd]*, and if that subsequently fails, the engine will conclude that the string doesn’t match the RE at all.

이제 정규식의 끝에 도달했고, 'abcb'가 매칭되었습니다. 이는 매칭 엔진이 처음에는 가능한 한 멀리 진행하고, 매칭이 없으면 점진적으로 되돌아가서 정규식의 나머지 부분을 반복해서 다시 시도하는 방식을 보여줍니다. [bcd]*에 대해 0번 매칭을 시도할 때까지 되돌아가고, 그래도 실패하면 엔진은 문자열이 정규식과 전혀 매칭되지 않는다고 판단합니다.

Another repeating metacharacter is +, which matches one or more times. Pay careful attention to the difference between * and +; * matches zero or more times, so whatever’s being repeated may not be present at all, while + requires at least one occurrence. To use a similar example, ca+t will match 'cat' (1 'a'), 'caaat' (3 'a's), but won’t match 'ct'.

또 다른 반복 메타문자는 +로, 1번 이상 매칭됩니다. *와 +의 차이점에 주의하세요; *는 0번 이상 매칭되므로 반복되는 것이 전혀 없을 수도 있지만, +는 최소한 1번의 발생이 필요합니다. 비슷한 예로, ca+t는 'cat'(1개의 'a'), 'caaat'(3개의 'a')와 매칭되지만, 'ct'와는 매칭되지 않습니다.

There are two more repeating operators or quantifiers. The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional. For example, home-?brew matches either 'homebrew' or 'home-brew'.

두 가지 추가 반복 연산자 또는 수량자가 있습니다. 물음표 문자 ?는 0번 또는 1번 매칭됩니다; 이를 무언가를 선택적으로 표시한다고 생각할 수 있습니다. 예를 들어, home-?brew는 'homebrew' 또는 'home-brew'와 매칭됩니다.

The most complicated quantifier is {m,n}, where m and n are decimal integers. This quantifier means there must be at least m repetitions, and at most n. For example, a/{1,3}b will match 'a/b', 'a//b', and 'a///b'. It won’t match 'ab', which has no slashes, or 'a////b', which has four.

가장 복잡한 수량자는 {m,n}입니다. 여기서 m과 n은 십진수 정수입니다. 이 수량자는 최소 m번, 최대 n번 반복되어야 함을 의미합니다. 예를 들어, a/{1,3}b는 'a/b', 'a//b', 'a///b'와 매칭됩니다. 슬래시가 없는 'ab'나 네 개의 슬래시가 있는 'a////b'와는 매칭되지 않습니다.

You can omit either m or n; in that case, a reasonable value is assumed for the missing value. Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity.

m이나 n을 생략할 수 있습니다; 이 경우, 빠진 값에 대해 합리적인 값이 가정됩니다. m을 생략하면 하한이 0으로 해석되고, n을 생략하면 상한이 무한대가 됩니다.

The simplest case {m} matches the preceding item exactly m times. For example, a/{2}b will only match 'a//b'.

가장 단순한 경우인 {m}은 앞의 항목이 정확히 m번 반복될 때 매칭됩니다. 예를 들어, a/{2}b는 'a//b'만 매칭합니다.

Readers of a reductionist bent may notice that the three other quantifiers can all be expressed using this notation. {0,} is the same as *, {1,} is equivalent to +, and {0,1} is the same as ?. It’s better to use *, +, or ? when you can, simply because they’re shorter and easier to read.

축소주의적 성향의 독자들은 다른 세 개의 수량자가 모두 이 표기법으로 표현될 수 있음을 알아차릴 수 있습니다. {0,}은 *와 같고, {1,}은 +와 동일하며, {0,1}은 ?와 같습니다. 가능하다면 *, +, ?를 사용하는 것이 좋습니다. 단순히 더 짧고 읽기 쉽기 때문입니다.

## Using Regular Expressions

Now that we've looked at some simple regular expressions, how do we actually use them in Python? The re module provides an interface to the regular expression engine, allowing you to compile REs into objects and then perform matches with them.

## 정규 표현식 사용하기

이제 몇 가지 간단한 정규 표현식을 살펴보았으니, Python에서 실제로 어떻게 사용하는지 알아보겠습니다. re 모듈은 정규 표현식 엔진에 인터페이스를 제공하여 정규식을 객체로 컴파일한 다음 이를 사용하여 매칭을 수행할 수 있게 해줍니다.

### Compiling Regular Expressions

Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.

```python
import re
p = re.compile('ab*')
p
re.compile('ab*')
```

re.compile() also accepts an optional flags argument, used to enable various special features and syntax variations. We'll go over the available settings later, but for now a single example will do:

```python
p = re.compile('ab*', re.IGNORECASE)
```

### 정규 표현식 컴파일하기

정규 표현식은 패턴 매칭이나 문자열 대체와 같은 다양한 작업을 위한 메서드가 있는 패턴 객체로 컴파일됩니다.

```python
import re
p = re.compile('ab*')
p
re.compile('ab*')
```

re.compile()은 또한 다양한 특수 기능과 구문 변형을 활성화하는 데 사용되는 선택적 flags 인수를 받습니다. 나중에 사용 가능한 설정을 살펴보겠지만, 지금은 하나의 예만 제시하겠습니다:

```python
p = re.compile('ab*', re.IGNORECASE)
```

The RE is passed to re.compile() as a string. REs are handled as strings because regular expressions aren't part of the core Python language, and no special syntax was created for expressing them. (There are applications that don't need REs at all, so there's no need to bloat the language specification by including them.) Instead, the re module is simply a C extension module included with Python, just like the socket or zlib modules.

Putting REs in strings keeps the Python language simpler, but has one disadvantage which is the topic of the next section.

정규식은 문자열로 re.compile()에 전달됩니다. 정규 표현식은 문자열로 처리되는데, 이는 정규 표현식이 Python 핵심 언어의 일부가 아니며, 이를 표현하기 위한 특별한 구문이 만들어지지 않았기 때문입니다. (정규식이 전혀 필요하지 않은 애플리케이션도 있으므로, 이를 포함하여 언어 사양을 비대하게 만들 필요가 없습니다.) 대신, re 모듈은 socket이나 zlib 모듈과 같이 Python에 포함된 단순한 C 확장 모듈입니다.

정규식을 문자열에 넣으면 Python 언어가 더 단순해지지만, 다음 섹션의 주제인 하나의 단점이 있습니다.

### The Backslash Plague

As stated earlier, regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their special meaning. This conflicts with Python's usage of the same character for the same purpose in string literals.

### 백슬래시 역병

앞서 언급했듯이, 정규 표현식은 특수 형식을 나타내거나 특수 문자를 특별한 의미 없이 사용할 수 있도록 백슬래시 문자 ('\\')를 사용합니다. 이는 문자열 리터럴에서 동일한 목적으로 동일한 문자를 사용하는 Python과 충돌합니다.

Let’s say you want to write a RE that matches the string \section, which might be found in a LaTeX file. To figure out what to write in the program code, start with the desired string to be matched. Next, you must escape any backslashes and other metacharacters by preceding them with a backslash, resulting in the string \\section. The resulting string that must be passed to re.compile() must be \\section. However, to express this as a Python string literal, both backslashes must be escaped again.

Characters

Stage

\section

Text string to be matched

\\section

Escaped backslash for re.compile()

"\\\\section"

Escaped backslashes for a string literal

In short, to match a literal backslash, one has to write '\\\\' as the RE string, because the regular expression must be \\, and each backslash must be expressed as \\ inside a regular Python string literal. In REs that feature backslashes repeatedly, this leads to lots of repeated backslashes and makes the resulting strings difficult to understand.

The solution is to use Python’s raw string notation for regular expressions; backslashes are not handled in any special way in a string literal prefixed with 'r', so r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline. Regular expressions will often be written in Python code using this raw string notation.

In addition, special escape sequences that are valid in regular expressions, but not valid as Python string literals, now result in a DeprecationWarning and will eventually become a SyntaxError, which means the sequences will be invalid if raw string notation or escaping the backslashes isn’t used.

정규식이 \section 문자열과 매칭되도록 작성하려고 한다고 가정해 보겠습니다. 이는 LaTeX 파일에서 찾을 수 있습니다. 프로그램 코드에 무엇을 작성할지 알아내려면, 매칭할 문자열을 시작으로 합니다. 다음으로, 모든 백슬래시와 다른 메타문자를 백슬래시로 앞에 두어 이스케이프해야 하며, 결과적으로 \\section 문자열이 됩니다. re.compile()에 전달해야 하는 최종 문자열은 \\section이어야 합니다. 그러나 이를 Python 문자열 리터럴로 표현하려면, 두 백슬래시를 다시 이스케이프해야 합니다.

문자

단계

\section

매칭할 텍스트 문자열

\\section

re.compile()를 위한 이스케이프된 백슬래시

"\\\\section"

문자열 리터럴을 위한 이스케이프된 백슬래시

간단히 말해, 리터럴 백슬래시와 매칭하려면, 정규식 문자열로 '\\\\'를 작성해야 합니다. 정규 표현식은 \\이어야 하며, 각 백슬래시는 정규 Python 문자열 리터럴 내에서 \\로 표현되어야 합니다. 백슬래시가 반복적으로 나타나는 정규식에서는 많은 반복된 백슬래시가 발생하여 결과 문자열을 이해하기 어렵게 만듭니다.

해결책은 정규 표현식을 위한 Python의 raw 문자열 표기법을 사용하는 것입니다. 백슬래시는 'r'로 접두사로 붙은 문자열 리터럴에서 특별한 방식으로 처리되지 않으므로, r"\n"은 '\'와 'n'을 포함하는 두 문자 문자열이고, "\n"은 줄 바꿈을 포함하는 한 문자 문자열입니다. 정규 표현식은 종종 이 raw 문자열 표기법을 사용하여 Python 코드에서 작성됩니다.

또한, 정규 표현식에서 유효하지만 Python 문자열 리터럴로는 유효하지 않은 특수 이스케이프 시퀀스는 이제 DeprecationWarning을 발생시키며, 결국 SyntaxError가 됩니다. 이는 raw 문자열 표기법을 사용하지 않거나 백슬래시를 이스케이프하지 않으면 시퀀스가 유효하지 않음을 의미합니다.

Regular String

Raw string

"ab*"

r"ab*"

"\\\\section"

r"\\section"

"\\w+\\s+\\1"

r"\w+\s+\1"

## Performing Matches

Once you have an object representing a compiled regular expression, what do you do with it? Pattern objects have several methods and attributes. Only the most significant ones will be covered here; consult the re docs for a complete listing.

## 매칭 수행하기

컴파일된 정규 표현식을 나타내는 객체가 있으면 그것으로 무엇을 합니까? 패턴 객체에는 여러 메서드와 속성이 있습니다. 여기서는 가장 중요한 것들만 다룰 것입니다. 전체 목록은 re 문서를 참조하세요.

Method/Attribute | Purpose
----------------|--------
match() | Determine if the RE matches at the beginning of the string.
search() | Scan through a string, looking for any location where this RE matches.
findall() | Find all substrings where the RE matches, and returns them as a list.
finditer() | Find all substrings where the RE matches, and returns them as an iterator.

메서드/속성 | 목적
-----------|------
match() | 정규식이 문자열 시작 부분에서 매칭되는지 확인합니다.
search() | 문자열을 스캔하여, 이 정규식이 매칭되는 모든 위치를 찾습니다.
findall() | 정규식이 매칭되는 모든 부분 문자열을 찾아 리스트로 반환합니다.
finditer() | 정규식이 매칭되는 모든 부분 문자열을 찾아 반복자로 반환합니다.

match() and search() return None if no match can be found. If they're successful, a match object instance is returned, containing information about the match: where it starts and ends, the substring it matched, and more.

match()와 search()는 매칭을 찾을 수 없으면 None을 반환합니다. 성공적이면, 매치 객체 인스턴스가 반환되어 매칭에 대한 정보를 포함합니다: 시작과 끝 위치, 매칭된 부분 문자열 등 더 많은 정보가 포함됩니다.

You can learn about this by interactively experimenting with the re module.

This HOWTO uses the standard Python interpreter for its examples. First, run the Python interpreter, import the re module, and compile a RE:

>>>
import re
p = re.compile('[a-z]+')
p
re.compile('[a-z]+')
Now, you can try matching various strings against the RE [a-z]+. An empty string shouldn’t match at all, since + means ‘one or more repetitions’. match() should return None in this case, which will cause the interpreter to print no output. You can explicitly print the result of match() to make this clear.

>>>
p.match("")
print(p.match(""))
None
Now, let’s try it on a string that it should match, such as tempo. In this case, match() will return a match object, so you should store the result in a variable for later use.

>>>
m = p.match('tempo')
m
<re.Match object; span=(0, 5), match='tempo'>
Now you can query the match object for information about the matching string. Match object instances also have several methods and attributes; the most important ones are:

Method/Attribute

Purpose

group()

Return the string matched by the RE

start()

Return the starting position of the match

end()

Return the ending position of the match

span()

Return a tuple containing the (start, end) positions of the match

Trying these methods will soon clarify their meaning:

>>>
m.group()
'tempo'
m.start(), m.end()
(0, 5)
m.span()
(0, 5)
group() returns the substring that was matched by the RE. start() and end() return the starting and ending index of the match. span() returns both start and end indexes in a single tuple. Since the match() method only checks if the RE matches at the start of a string, start() will always be zero. However, the search() method of patterns scans through the string, so the match may not start at zero in that case.

>>>
print(p.match('::: message'))
None
m = p.search('::: message'); print(m)
<re.Match object; span=(4, 11), match='message'>
m.group()
'message'
m.span()
(4, 11)
In actual programs, the most common style is to store the match object in a variable, and then check if it was None. This usually looks like:

p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
Two pattern methods return all of the matches for a pattern. findall() returns a list of matching strings:

>>>
p = re.compile(r'\d+')
p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
The r prefix, making the literal a raw string literal, is needed in this example because escape sequences in a normal “cooked” string literal that are not recognized by Python, as opposed to regular expressions, now result in a DeprecationWarning and will eventually become a SyntaxError. See The Backslash Plague.

findall() has to create the entire list before it can be returned as the result. The finditer() method returns a sequence of match object instances as an iterator:

>>>
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
iterator
<callable_iterator object at 0x...>
for match in iterator:
    print(match.span())

(0, 2)
(22, 24)
(29, 31)
## Module-Level Functions

You don't have to create a pattern object and call its methods; the re module also provides top-level functions called match(), search(), findall(), sub(), and so forth. These functions take the same arguments as the corresponding pattern method with the RE string added as the first argument, and still return either None or a match object instance.

## 모듈 수준 함수

패턴 객체를 생성하고 그 메서드를 호출할 필요는 없습니다. re 모듈은 match(), search(), findall(), sub() 등과 같은 최상위 함수도 제공합니다. 이 함수들은 첫 번째 인수로 정규식 문자열을 추가하고, 해당 패턴 메서드와 동일한 인수를 취하며, 여전히 None 또는 매치 객체 인스턴스를 반환합니다.

```python
print(re.match(r'From\s+', 'Fromage amk'))
None
re.match(r'From\s+', 'From amk Thu May 14 19:12:10 1998')
<re.Match object; span=(0, 5), match='From '>
```

Under the hood, these functions simply create a pattern object for you and call the appropriate method on it. They also store the compiled object in a cache, so future calls using the same RE won't need to parse the pattern again and again.

내부적으로, 이 함수들은 단순히 패턴 객체를 생성하고 적절한 메서드를 호출합니다. 또한 컴파일된 객체를 캐시에 저장하므로, 동일한 정규식을 사용하는 향후 호출에서는 패턴을 다시 파싱할 필요가 없습니다.

Should you use these module-level functions, or should you get the pattern and call its methods yourself? If you're accessing a regex within a loop, pre-compiling it will save a few function calls. Outside of loops, there's not much difference thanks to the internal cache.

이러한 모듈 수준 함수를 사용해야 할까요, 아니면 패턴을 가져와서 직접 메서드를 호출해야 할까요? 루프 내에서 정규식에 접근하는 경우, 미리 컴파일하면 몇 가지 함수 호출을 절약할 수 있습니다. 루프 외부에서는 내부 캐시 덕분에 큰 차이가 없습니다.

## Compilation Flags

Compilation flags let you modify some aspects of how regular expressions work. Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I. (If you're familiar with Perl's pattern modifiers, the one-letter forms use the same letters; the short form of re.VERBOSE is re.X, for example.) Multiple flags can be specified by bitwise OR-ing them; re.I | re.M sets both the I and M flags, for example.

## 컴파일 플래그

컴파일 플래그를 사용하면 정규 표현식의 작동 방식의 일부 측면을 수정할 수 있습니다. 플래그는 re 모듈에서 IGNORECASE와 같은 긴 이름과 I와 같은 짧은 한 글자 형식의 두 가지 이름으로 사용할 수 있습니다. (Perl의 패턴 수정자에 익숙하다면, 한 글자 형식은 동일한 글자를 사용합니다. 예를 들어, re.VERBOSE의 짧은 형식은 re.X입니다.) 여러 플래그는 비트 단위 OR 연산으로 지정할 수 있습니다. 예를 들어, re.I | re.M은 I와 M 플래그를 모두 설정합니다.

Here's a table of the available flags, followed by a more detailed explanation of each one.

다음은 사용 가능한 플래그 표와 각각에 대한 자세한 설명입니다.

Flag | Meaning
-----|--------
ASCII, A | Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
DOTALL, S | Make . match any character, including newlines.
IGNORECASE, I | Do case-insensitive matches.
LOCALE, L | Do a locale-aware match.
MULTILINE, M | Multi-line matching, affecting ^ and $.
VERBOSE, X (for 'extended') | Enable verbose REs, which can be organized more cleanly and understandably.

플래그 | 의미
-------|------
ASCII, A | \w, \b, \s, \d와 같은 여러 이스케이프가 해당 속성을 가진 ASCII 문자에만 매칭되도록 합니다.
DOTALL, S | .이 줄바꿈을 포함한 모든 문자와 매칭되도록 합니다.
IGNORECASE, I | 대소문자를 구분하지 않는 매칭을 수행합니다.
LOCALE, L | 로케일을 인식하는 매칭을 수행합니다.
MULTILINE, M | 여러 줄 매칭으로, ^와 $에 영향을 줍니다.
VERBOSE, X ('확장'을 의미) | 더 깔끔하고 이해하기 쉽게 구성할 수 있는 상세한 정규식을 활성화합니다.

re.I
re.IGNORECASE
Perform case-insensitive matching; character class and literal strings will match letters by ignoring case. For example, [A-Z] will match lowercase letters, too. Full Unicode matching also works unless the ASCII flag is used to disable non-ASCII matches. When the Unicode patterns [a-z] or [A-Z] are used in combination with the IGNORECASE flag, they will match the 52 ASCII letters and 4 additional non-ASCII letters: 'İ' (U+0130, Latin capital letter I with dot above), 'ı' (U+0131, Latin small letter dotless i), 'ſ' (U+017F, Latin small letter long s) and 'K' (U+212A, Kelvin sign). Spam will match 'Spam', 'spam', 'spAM', or 'ſpam' (the latter is matched only in Unicode mode). This lowercasing doesn't take the current locale into account; it will if you also set the LOCALE flag.

re.I
re.IGNORECASE
대소문자를 구분하지 않는 매칭을 수행합니다. 문자 클래스와 리터럴 문자열은 대소문자를 무시하고 문자와 매칭됩니다. 예를 들어, [A-Z]는 소문자와도 매칭됩니다. ASCII 플래그를 사용하여 비ASCII 매칭을 비활성화하지 않는 한 전체 유니코드 매칭도 작동합니다. IGNORECASE 플래그와 함께 유니코드 패턴 [a-z] 또는 [A-Z]가 사용되면, 이들은 52개의 ASCII 문자와 4개의 추가 비ASCII 문자와 매칭됩니다: 'İ' (U+0130, 점이 있는 라틴 대문자 I), 'ı' (U+0131, 점이 없는 라틴 소문자 i), 'ſ' (U+017F, 라틴 소문자 긴 s) 및 'K' (U+212A, 켈빈 기호). Spam은 'Spam', 'spam', 'spAM' 또는 'ſpam'(후자는 유니코드 모드에서만 매칭됨)과 매칭됩니다. 이 소문자화는 현재 로케일을 고려하지 않습니다. LOCALE 플래그도 설정하면 고려합니다.

re.L
re.LOCALE
Make \w, \W, \b, \B and case-insensitive matching dependent on the current locale instead of the Unicode database.

re.L
re.LOCALE
\w, \W, \b, \B 및 대소문자 구분 없는 매칭을 유니코드 데이터베이스 대신 현재 로케일에 의존하도록 만듭니다.

Locales are a feature of the C library intended to help in writing programs that take account of language differences. For example, if you’re processing encoded French text, you’d want to be able to write \w+ to match words, but \w only matches the character class [A-Za-z] in bytes patterns; it won’t match bytes corresponding to é or ç. If your system is configured properly and a French locale is selected, certain C functions will tell the program that the byte corresponding to é should also be considered a letter. Setting the LOCALE flag when compiling a regular expression will cause the resulting compiled object to use these C functions for \w; this is slower, but also enables \w+ to match French words as you’d expect. The use of this flag is discouraged in Python 3 as the locale mechanism is very unreliable, it only handles one “culture” at a time, and it only works with 8-bit locales. Unicode matching is already enabled by default in Python 3 for Unicode (str) patterns, and it is able to handle different locales/languages.

로케일은 언어 차이를 고려한 프로그램 작성을 돕기 위해 C 라이브러리의 기능입니다. 예를 들어, 인코딩된 프랑스어 텍스트를 처리하는 경우, 단어를 매칭하기 위해 \w+를 작성할 수 있기를 원할 것입니다. 그러나 \w는 바이트 패턴에서 문자 클래스 [A-Za-z]와만 매칭됩니다. é 또는 ç에 해당하는 바이트와는 매칭되지 않습니다. 시스템이 적절하게 구성되고 프랑스어 로케일이 선택된 경우, 특정 C 함수는 프로그램에 é에 해당하는 바이트도 문자로 간주해야 한다고 알려줍니다. 정규 표현식을 컴파일할 때 LOCALE 플래그를 설정하면, 결과적으로 컴파일된 객체가 \w에 대해 이러한 C 함수를 사용하게 됩니다. 이는 느리지만, 예상대로 프랑스어 단어와 매칭할 수 있게 합니다. 이 플래그의 사용은 Python 3에서 권장되지 않습니다. 로케일 메커니즘이 매우 신뢰할 수 없고, 한 번에 하나의 "문화"만 처리하며, 8비트 로케일에서만 작동하기 때문입니다. 유니코드 매칭은 이미 Python 3에서 유니코드(str) 패턴에 대해 기본적으로 활성화되어 있으며, 다양한 로케일/언어를 처리할 수 있습니다.

re.M
re.MULTILINE
(^ and $ haven’t been explained yet; they’ll be introduced in section More Metacharacters.)

re.M
re.MULTILINE
(^와 $는 아직 설명되지 않았습니다. 이는 추가 메타문자 섹션에서 소개될 것입니다.)

Usually ^ matches only at the beginning of the string, and $ matches only at the end of the string and immediately before the newline (if any) at the end of the string. When this flag is specified, ^ matches at the beginning of the string and at the beginning of each line within the string, immediately following each newline. Similarly, the $ metacharacter matches either at the end of the string and at the end of each line (immediately preceding each newline).

일반적으로 ^는 문자열의 시작 부분에서만 매칭되고, $는 문자열의 끝과 문자열 끝의 줄 바꿈(있는 경우) 바로 앞에서만 매칭됩니다. 이 플래그가 지정되면, ^는 문자열의 시작 부분과 문자열 내 각 줄의 시작 부분에서 매칭됩니다. 마찬가지로, $ 메타문자는 문자열의 끝과 각 줄의 끝(각 줄 바꿈 바로 앞)에서 매칭됩니다.

re.S
re.DOTALL
Makes the '.' special character match any character at all, including a newline; without this flag, '.' will match anything except a newline.

re.S
re.DOTALL
'.' 특수 문자가 줄 바꿈을 포함한 모든 문자와 매칭되도록 합니다. 이 플래그가 없으면, '.'은 줄 바꿈을 제외한 모든 것과 매칭됩니다.

re.A
re.ASCII
Make \w, \W, \b, \B, \s and \S perform ASCII-only matching instead of full Unicode matching. This is only meaningful for Unicode patterns, and is ignored for byte patterns.

re.A
re.ASCII
\w, \W, \b, \B, \s 및 \S가 전체 유니코드 매칭 대신 ASCII 전용 매칭을 수행하도록 합니다. 이는 유니코드 패턴에만 의미가 있으며, 바이트 패턴에서는 무시됩니다.

re.X
re.VERBOSE
This flag allows you to write regular expressions that are more readable by granting you more flexibility in how you can format them. When this flag has been specified, whitespace within the RE string is ignored, except when the whitespace is in a character class or preceded by an unescaped backslash; this lets you organize and indent the RE more clearly. This flag also lets you put comments within a RE that will be ignored by the engine; comments are marked by a '#' that’s neither in a character class or preceded by an unescaped backslash.

re.X
re.VERBOSE
이 플래그를 사용하면 정규 표현식을 더 읽기 쉽게 작성할 수 있으며, 이를 형식화하는 방법에 더 많은 유연성을 부여합니다. 이 플래그가 지정되면, 문자 클래스 내에 있거나 이스케이프되지 않은 백슬래시가 앞에 있는 경우를 제외하고, 정규 표현식 문자열 내의 공백은 무시됩니다. 이를 통해 정규 표현식을 더 명확하게 구성하고 들여쓰기 할 수 있습니다. 이 플래그는 또한 정규 표현식 내에 주석을 넣을 수 있게 하며, 이는 엔진에 의해 무시됩니다. 주석은 문자 클래스 내에 있지 않거나 이스케이프되지 않은 백슬래시가 앞에 있는 경우를 제외하고, '#'로 표시됩니다.

For example, here’s a RE that uses re.VERBOSE; see how much easier it is to read?

예를 들어, re.VERBOSE를 사용하는 정규 표현식입니다. 얼마나 읽기 쉬운지 보세요.

```python
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

Without the verbose setting, the RE would look like this:

상세 설정 없이, 정규 표현식은 다음과 같이 보일 것입니다:

```python
charref = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")
```

In the above example, Python’s automatic concatenation of string literals has been used to break up the RE into smaller pieces, but it’s still more difficult to understand than the version using re.VERBOSE.

위의 예에서, Python의 문자열 리터럴 자동 연결이 사용되어 정규 표현식을 더 작은 조각으로 나누었지만, 여전히 re.VERBOSE를 사용하는 버전보다 이해하기 어렵습니다.

## More Pattern Power

So far we’ve only covered a part of the features of regular expressions. In this section, we’ll cover some new metacharacters, and how to use groups to retrieve portions of the text that was matched.

## 더 많은 패턴 기능

지금까지 우리는 정규 표현식의 일부 기능만 다루었습니다. 이 섹션에서는 새로운 메타문자와 매칭된 텍스트의 일부를 검색하기 위해 그룹을 사용하는 방법을 다룰 것입니다.

### More Metacharacters

There are some metacharacters that we haven’t covered yet. Most of them will be covered in this section.

### 추가 메타문자

아직 다루지 않은 몇 가지 메타문자가 있습니다. 대부분은 이 섹션에서 다룰 것입니다.

Some of the remaining metacharacters to be discussed are zero-width assertions. They don’t cause the engine to advance through the string; instead, they consume no characters at all, and simply succeed or fail. For example, \b is an assertion that the current position is located at a word boundary; the position isn’t changed by the \b at all. This means that zero-width assertions should never be repeated, because if they match once at a given location, they can obviously be matched an infinite number of times.

남은 메타문자 중 일부는 폭이 없는 어설션입니다. 이들은 엔진이 문자열을 통해 진행하지 않게 합니다. 대신, 전혀 문자를 소비하지 않으며, 단순히 성공하거나 실패합니다. 예를 들어, \b는 현재 위치가 단어 경계에 있음을 나타내는 어설션입니다. \b에 의해 위치가 전혀 변경되지 않습니다. 이는 폭이 없는 어설션이 절대 반복되어서는 안 된다는 것을 의미합니다. 주어진 위치에서 한 번 매칭되면, 무한히 많은 횟수로 매칭될 수 있기 때문입니다.

|
Alternation, or the “or” operator. If A and B are regular expressions, A|B will match any string that matches either A or B. | has very low precedence in order to make it work reasonably when you’re alternating multi-character strings. Crow|Servo will match either 'Crow' or 'Servo', not 'Cro', a 'w' or an 'S', and 'ervo'.

To match a literal '|', use \|, or enclose it inside a character class, as in [|].

|
대체 또는 "또는" 연산자. A와 B가 정규 표현식인 경우, A|B는 A 또는 B와 일치하는 모든 문자열과 매칭됩니다. |는 다중 문자 문자열을 번갈아 사용할 때 합리적으로 작동하도록 매우 낮은 우선순위를 가집니다. Crow|Servo는 'Crow' 또는 'Servo'와 매칭되며, 'Cro', 'w', 'S', 'ervo'와는 매칭되지 않습니다.

리터럴 '|'와 매칭하려면, \|를 사용하거나 [|]와 같이 문자 클래스 내에 넣으세요.

^
Matches at the beginning of lines. Unless the MULTILINE flag has been set, this will only match at the beginning of the string. In MULTILINE mode, this also matches immediately after each newline within the string.

For example, if you wish to match the word From only at the beginning of a line, the RE to use is ^From.

^
줄의 시작 부분에서 매칭됩니다. MULTILINE 플래그가 설정되지 않은 경우, 이는 문자열의 시작 부분에서만 매칭됩니다. MULTILINE 모드에서는 문자열 내 각 줄 바꿈 직후에도 매칭됩니다.

예를 들어, 줄의 시작 부분에서만 From 단어와 매칭하려면, 사용할 정규 표현식은 ^From입니다.

```python
print(re.search('^From', 'From Here to Eternity'))
<re.Match object; span=(0, 4), match='From'>
print(re.search('^From', 'Reciting From Memory'))
None
```

To match a literal '^', use \^.

리터럴 '^'와 매칭하려면, \^를 사용하세요.

$
Matches at the end of a line, which is defined as either the end of the string, or any location followed by a newline character.

$
줄의 끝에서 매칭됩니다. 이는 문자열의 끝 또는 줄 바꿈 문자가 뒤따르는 모든 위치로 정의됩니다.

```python
print(re.search('}$', '{block}'))
<re.Match object; span=(6, 7), match='}'>
print(re.search('}$', '{block} '))
None
print(re.search('}$', '{block}\n'))
<re.Match object; span=(6, 7), match='}'>
```

To match a literal '$', use \$ or enclose it inside a character class, as in [$].

리터럴 '$'와 매칭하려면, \$를 사용하거나 [$]와 같이 문자 클래스 내에 넣으세요.

\A
Matches only at the start of the string. When not in MULTILINE mode, \A and ^ are effectively the same. In MULTILINE mode, they’re different: \A still matches only at the beginning of the string, but ^ may match at any location inside the string that follows a newline character.

\A
문자열의 시작 부분에서만 매칭됩니다. MULTILINE 모드가 아닌 경우, \A와 ^는 사실상 동일합니다. MULTILINE 모드에서는 다릅니다: \A는 여전히 문자열의 시작 부분에서만 매칭되지만, ^는 줄 바꿈 문자가 뒤따르는 문자열 내의 모든 위치에서 매칭될 수 있습니다.

\Z
Matches only at the end of the string.

\Z
문자열의 끝에서만 매칭됩니다.

\b
Word boundary. This is a zero-width assertion that matches only at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.

The following example matches class only when it’s a complete word; it won’t match when it’s contained inside another word.

\b
단어 경계. 이는 단어의 시작 또는 끝에서만 매칭되는 폭이 없는 어설션입니다. 단어는 영숫자 문자의 시퀀스로 정의되므로, 단어의 끝은 공백 또는 비영숫자 문자로 표시됩니다.

다음 예제는 class가 완전한 단어일 때만 매칭됩니다. 다른 단어 내에 포함된 경우에는 매칭되지 않습니다.

```python
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
<re.Match object; span=(3, 8), match='class'>
print(p.search('the declassified algorithm'))
None
print(p.search('one subclass is'))
None
```

There are two subtleties you should remember when using this special sequence. First, this is the worst collision between Python’s string literals and regular expression sequences. In Python’s string literals, \b is the backspace character, ASCII value 8. If you’re not using raw strings, then Python will convert the \b to a backspace, and your RE won’t match as you expect it to. The following example looks the same as our previous RE, but omits the 'r' in front of the RE string.

이 특수 시퀀스를 사용할 때 기억해야 할 두 가지 미묘한 점이 있습니다. 첫째, 이는 Python의 문자열 리터럴과 정규 표현식 시퀀스 간의 최악의 충돌입니다. Python의 문자열 리터럴에서 \b는 백스페이스 문자이며, ASCII 값은 8입니다. raw 문자열을 사용하지 않으면, Python은 \b를 백스페이스로 변환하고, 정규 표현식은 예상대로 매칭되지 않습니다. 다음 예제는 이전 정규 표현식과 동일해 보이지만, 정규 표현식 문자열 앞의 'r'을 생략했습니다.

```python
p = re.compile('\bclass\b')
print(p.search('no class at all'))
None
print(p.search('\b' + 'class' + '\b'))
<re.Match object; span=(0, 7), match='\x08class\x08'>
```

Second, inside a character class, where there’s no use for this assertion, \b represents the backspace character, for compatibility with Python’s string literals.

둘째, 이 어설션이 필요 없는 문자 클래스 내에서 \b는 Python의 문자열 리터럴과의 호환성을 위해 백스페이스 문자를 나타냅니다.

\B
Another zero-width assertion, this is the opposite of \b, only matching when the current position is not at a word boundary.

\B
또 다른 폭이 없는 어설션으로, 이는 \b의 반대이며, 현재 위치가 단어 경계에 있지 않을 때만 매칭됩니다.

## Grouping

Frequently you need to obtain more information than just whether the RE matched or not. Regular expressions are often used to dissect strings by writing a RE divided into several subgroups which match different components of interest. For example, an RFC-822 header line is divided into a header name and a value, separated by a ':', like this:

## 그룹화

정규 표현식이 매칭되었는지 여부만 확인하는 것보다 더 많은 정보를 얻어야 할 때가 많습니다. 정규 표현식은 종종 문자열을 해부하여 여러 하위 그룹으로 나누어 관심 있는 다양한 구성 요소와 매칭되는 정규 표현식을 작성하는 데 사용됩니다. 예를 들어, RFC-822 헤더 라인은 헤더 이름과 값으로 나누어지며, ':'로 구분됩니다. 다음과 같습니다:

```
From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com
```

This can be handled by writing a regular expression which matches an entire header line, and has one group which matches the header name, and another group which matches the header’s value.

이는 전체 헤더 라인과 매칭되는 정규 표현식을 작성하고, 헤더 이름과 매칭되는 그룹 하나와 헤더 값과 매칭되는 그룹 하나를 포함하여 처리할 수 있습니다.

Groups are marked by the '(', ')' metacharacters. '(' and ')' have much the same meaning as they do in mathematical expressions; they group together the expressions contained inside them, and you can repeat the contents of a group with a quantifier, such as *, +, ?, or {m,n}. For example, (ab)* will match zero or more repetitions of ab.

그룹은 '(', ')' 메타문자로 표시됩니다. '('와 ')'는 수학적 표현에서와 거의 동일한 의미를 가집니다. 이들은 내부에 포함된 표현식을 그룹화하며, *, +, ?, {m,n}과 같은 수량자로 그룹의 내용을 반복할 수 있습니다. 예를 들어, (ab)*는 ab의 0번 이상의 반복과 매칭됩니다.

```python
p = re.compile('(ab)*')
print(p.match('ababababab').span())
(0, 10)
```

Groups indicated with '(', ')' also capture the starting and ending index of the text that they match; this can be retrieved by passing an argument to group(), start(), end(), and span(). Groups are numbered starting with 0. Group 0 is always present; it’s the whole RE, so match object methods all have group 0 as their default argument. Later we’ll see how to express groups that don’t capture the span of text that they match.

'(', ')'로 표시된 그룹은 매칭된 텍스트의 시작 및 끝 인덱스도 캡처합니다. 이는 group(), start(), end(), span()에 인수를 전달하여 검색할 수 있습니다. 그룹은 0부터 번호가 매겨집니다. 그룹 0은 항상 존재합니다. 이는 전체 정규 표현식이므로, 매치 객체 메서드는 모두 기본 인수로 그룹 0을 가집니다. 나중에 매칭된 텍스트의 범위를 캡처하지 않는 그룹을 표현하는 방법을 살펴보겠습니다.

```python
p = re.compile('(a)b')
m = p.match('ab')
m.group()
'ab'
m.group(0)
'ab'
```

Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to determine the number, just count the opening parenthesis characters, going from left to right.

하위 그룹은 왼쪽에서 오른쪽으로 1부터 번호가 매겨집니다. 그룹은 중첩될 수 있습니다. 번호를 결정하려면, 왼쪽에서 오른쪽으로 여는 괄호 문자를 세기만 하면 됩니다.

```python
p = re.compile('(a(b)c)d')
m = p.match('abcd')
m.group(0)
'abcd'
m.group(1)
'abc'
m.group(2)
'b'
```

group() can be passed multiple group numbers at a time, in which case it will return a tuple containing the corresponding values for those groups.

group()은 한 번에 여러 그룹 번호를 전달할 수 있으며, 이 경우 해당 그룹의 값을 포함하는 튜플을 반환합니다.

```python
m.group(2,1,2)
('b', 'abc', 'b')
```

The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are.

groups() 메서드는 1부터 시작하여 모든 하위 그룹의 문자열을 포함하는 튜플을 반환합니다.

```python
m.groups()
('abc', 'b')
```

Backreferences in a pattern allow you to specify that the contents of an earlier capturing group must also be found at the current location in the string. For example, \1 will succeed if the exact contents of group 1 can be found at the current position, and fails otherwise. Remember that Python’s string literals also use a backslash followed by numbers to allow including arbitrary characters in a string, so be sure to use a raw string when incorporating backreferences in a RE.

패턴의 역참조를 사용하면 이전 캡처 그룹의 내용이 문자열의 현재 위치에서도 발견되어야 한다고 지정할 수 있습니다. 예를 들어, \1은 그룹 1의 정확한 내용이 현재 위치에서 발견되면 성공하고, 그렇지 않으면 실패합니다. Python의 문자열 리터럴도 숫자가 뒤따르는 백슬래시를 사용하여 문자열에 임의의 문자를 포함할 수 있도록 하므로, 정규 표현식에 역참조를 포함할 때는 반드시 raw 문자열을 사용해야 합니다.

For example, the following RE detects doubled words in a string.

예를 들어, 다음 정규 표현식은 문자열에서 중복된 단어를 감지합니다.

```python
p = re.compile(r'\b(\w+)\s+\1\b')
p.search('Paris in the the spring').group()
'the the'
```

Backreferences like this aren’t often useful for just searching through a string — there are few text formats which repeat data in this way — but you’ll soon find out that they’re very useful when performing string substitutions.

이와 같은 역참조는 단순히 문자열을 검색하는 데는 자주 유용하지 않습니다. 이 방식으로 데이터를 반복하는 텍스트 형식은 거의 없기 때문입니다. 그러나 문자열 대체를 수행할 때 매우 유용하다는 것을 곧 알게 될 것입니다.

## Non-capturing and Named Groups

Elaborate REs may use many groups, both to capture substrings of interest, and to group and structure the RE itself. In complex REs, it becomes difficult to keep track of the group numbers. There are two features which help with this problem. Both of them use a common syntax for regular expression extensions, so we’ll look at that first.

## 비캡처 및 명명된 그룹

정교한 정규 표현식은 관심 있는 하위 문자열을 캡처하고, 정규 표현식 자체를 그룹화하고 구조화하기 위해 많은 그룹을 사용할 수 있습니다. 복잡한 정규 표현식에서는 그룹 번호를 추적하기 어려워집니다. 이 문제를 해결하는 두 가지 기능이 있습니다. 두 기능 모두 정규 표현식 확장을 위한 공통 구문을 사용하므로, 먼저 이를 살펴보겠습니다.

Perl 5 is well known for its powerful additions to standard regular expressions. For these new features the Perl developers couldn’t choose new single-keystroke metacharacters or new special sequences beginning with \ without making Perl’s regular expressions confusingly different from standard REs. If they chose & as a new metacharacter, for example, old expressions would be assuming that & was a regular character and wouldn’t have escaped it by writing \& or [&].

Perl 5는 표준 정규 표현식에 강력한 추가 기능을 제공하는 것으로 잘 알려져 있습니다. 이러한 새로운 기능을 위해 Perl 개발자는 Perl의 정규 표현식을 표준 정규 표현식과 혼동되지 않게 하기 위해 새로운 단일 키 입력 메타문자나 \로 시작하는 새로운 특수 시퀀스를 선택할 수 없었습니다. 예를 들어, &를 새로운 메타문자로 선택하면, 이전 표현식은 &가 일반 문자라고 가정하고 \& 또는 [&]로 이스케이프하지 않았을 것입니다.

The solution chosen by the Perl developers was to use (?...) as the extension syntax. ? immediately after a parenthesis was a syntax error because the ? would have nothing to repeat, so this didn’t introduce any compatibility problems. The characters immediately after the ? indicate what extension is being used, so (?=foo) is one thing (a positive lookahead assertion) and (?:foo) is something else (a non-capturing group containing the subexpression foo).

Perl 개발자가 선택한 해결책은 (?...)를 확장 구문으로 사용하는 것이었습니다. 괄호 바로 뒤에 오는 ?는 반복할 것이 없기 때문에 구문 오류였으므로, 이는 호환성 문제를 일으키지 않았습니다. ? 바로 뒤의 문자는 어떤 확장이 사용되는지 나타내므로, (?=foo)는 하나의 것(긍정적 전방 탐색 어설션)이고, (?:foo)는 다른 것(하위 표현식 foo를 포함하는 비캡처 그룹)입니다.

Python supports several of Perl’s extensions and adds an extension syntax to Perl’s extension syntax. If the first character after the question mark is a P, you know that it’s an extension that’s specific to Python.

Python은 Perl의 여러 확장을 지원하며, Perl의 확장 구문에 확장 구문을 추가합니다. 물음표 뒤의 첫 번째 문자가 P인 경우, 이는 Python에 특정한 확장임을 알 수 있습니다.

Now that we’ve looked at the general extension syntax, we can return to the features that simplify working with groups in complex REs.

이제 일반적인 확장 구문을 살펴보았으므로, 복잡한 정규 표현식에서 그룹 작업을 단순화하는 기능으로 돌아갈 수 있습니다.

Sometimes you’ll want to use a group to denote a part of a regular expression, but aren’t interested in retrieving the group’s contents. You can make this fact explicit by using a non-capturing group: (?:...), where you can replace the ... with any other regular expression.

때로는 그룹을 사용하여 정규 표현식의 일부를 나타내고 싶지만, 그룹의 내용을 검색하는 데 관심이 없을 수 있습니다. 비캡처 그룹을 사용하여 이 사실을 명확히 할 수 있습니다: (?:...), 여기서 ...를 다른 정규 표현식으로 대체할 수 있습니다.

```python
m = re.match("([abc])+", "abc")
m.groups()
('c',)
m = re.match("(?:[abc])+", "abc")
m.groups()
()
```

Except for the fact that you can’t retrieve the contents of what the group matched, a non-capturing group behaves exactly the same as a capturing group; you can put anything inside it, repeat it with a repetition metacharacter such as *, and nest it within other groups (capturing or non-capturing). (?:...) is particularly useful when modifying an existing pattern, since you can add new groups without changing how all the other groups are numbered. It should be mentioned that there’s no performance difference in searching between capturing and non-capturing groups; neither form is any faster than the other.

그룹이 매칭한 내용을 검색할 수 없다는 사실을 제외하고, 비캡처 그룹은 캡처 그룹과 정확히 동일하게 동작합니다. 내부에 아무 것이나 넣을 수 있으며, *, +, ?, {m,n}과 같은 반복 메타문자로 반복할 수 있으며, 다른 그룹(캡처 또는 비캡처) 내에 중첩할 수 있습니다. (?:...)는 기존 패턴을 수정할 때 특히 유용합니다. 모든 다른 그룹의 번호를 변경하지 않고 새 그룹을 추가할 수 있기 때문입니다. 캡처 그룹과 비캡처 그룹 간의 검색 성능 차이는 없다는 점을 언급해야 합니다. 어느 형태도 다른 형태보다 빠르지 않습니다.

A more significant feature is named groups: instead of referring to them by numbers, groups can be referenced by a name.

더 중요한 기능은 명명된 그룹입니다. 번호로 참조하는 대신, 그룹을 이름으로 참조할 수 있습니다.

The syntax for a named group is one of the Python-specific extensions: (?P<name>...). name is, obviously, the name of the group. Named groups behave exactly like capturing groups, and additionally associate a name with a group. The match object methods that deal with capturing groups all accept either integers that refer to the group by number or strings that contain the desired group’s name. Named groups are still given numbers, so you can retrieve information about a group in two ways:

명명된 그룹의 구문은 Python에 특정한 확장 중 하나입니다: (?P<name>...). name은 당연히 그룹의 이름입니다. 명명된 그룹은 캡처 그룹과 정확히 동일하게 동작하며, 추가로 그룹에 이름을 연결합니다. 캡처 그룹을 다루는 매치 객체 메서드는 모두 번호로 그룹을 참조하는 정수 또는 원하는 그룹의 이름을 포함하는 문자열을 허용합니다. 명명된 그룹은 여전히 번호가 부여되므로, 두 가지 방법으로 그룹에 대한 정보를 검색할 수 있습니다:

```python
p = re.compile(r'(?P<word>\b\w+\b)')
m = p.search( '(((( Lots of punctuation )))' )
m.group('word')
'Lots'
m.group(1)
'Lots'
```

Additionally, you can retrieve named groups as a dictionary with groupdict():

또한, groupdict()를 사용하여 명명된 그룹을 사전으로 검색할 수 있습니다:

```python
m = re.match(r'(?P<first>\w+) (?P<last>\w+)', 'Jane Doe')
m.groupdict()
{'first': 'Jane', 'last': 'Doe'}
```

Named groups are handy because they let you use easily remembered names, instead of having to remember numbers. Here’s an example RE from the imaplib module:

명명된 그룹은 번호를 기억할 필요 없이 쉽게 기억할 수 있는 이름을 사용할 수 있으므로 편리합니다. 다음은 imaplib 모듈의 예제 정규 표현식입니다:

```python
InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')
```

It’s obviously much easier to retrieve m.group('zonem'), instead of having to remember to retrieve group 9.

그룹 9를 검색하는 것을 기억할 필요 없이 m.group('zonem')을 검색하는 것이 훨씬 더 쉽습니다.

The syntax for backreferences in an expression such as (...)\1 refers to the number of the group. There’s naturally a variant that uses the group name instead of the number. This is another Python extension: (?P=name) indicates that the contents of the group called name should again be matched at the current point. The regular expression for finding doubled words, \b(\w+)\s+\1\b can also be written as \b(?P<word>\w+)\s+(?P=word)\b:

(...)\1과 같은 표현식에서 역참조의 구문은 그룹의 번호를 참조합니다. 자연스럽게 번호 대신 그룹 이름을 사용하는 변형이 있습니다. 이것은 또 다른 Python 확장입니다: (?P=name)은 name이라는 그룹의 내용이 현재 지점에서 다시 매칭되어야 함을 나타냅니다. 중복된 단어를 찾는 정규 표현식 \b(\w+)\s+\1\b는 \b(?P<word>\w+)\s+(?P=word)\b로도 작성할 수 있습니다:

```python
p = re.compile(r'\b(?P<word>\w+)\s+(?P=word)\b')
p.search('Paris in the the spring').group()
'the the'
```

## Lookahead Assertions

Another zero-width assertion is the lookahead assertion. Lookahead assertions are available in both positive and negative form, and look like this:

## 전방 탐색 어설션

또 다른 폭이 없는 어설션은 전방 탐색 어설션입니다. 전방 탐색 어설션은 긍정적 형태와 부정적 형태 모두에서 사용할 수 있으며, 다음과 같이 보입니다:

(?=...)
Positive lookahead assertion. This succeeds if the contained regular expression, represented here by ..., successfully matches at the current location, and fails otherwise. But, once the contained expression has been tried, the matching engine doesn’t advance at all; the rest of the pattern is tried right where the assertion started.

(?=...)
긍정적 전방 탐색 어설션. 여기서 ...로 표현된 포함된 정규 표현식이 현재 위치에서 성공적으로 매칭되면 성공하고, 그렇지 않으면 실패합니다. 그러나 포함된 표현식이 시도된 후에는 매칭 엔진이 전혀 진행하지 않습니다. 패턴의 나머지 부분은 어설션이 시작된 바로 그 지점에서 시도됩니다.

(?!...)
Negative lookahead assertion. This is the opposite of the positive assertion; it succeeds if the contained expression doesn’t match at the current position in the string.

(?!...)
부정적 전방 탐색 어설션. 이는 긍정적 어설션의 반대입니다. 포함된 표현식이 문자열의 현재 위치에서 매칭되지 않으면 성공합니다.

To make this concrete, let’s look at a case where a lookahead is useful. Consider a simple pattern to match a filename and split it apart into a base name and an extension, separated by a .. For example, in news.rc, news is the base name, and rc is the filename’s extension.

이것을 구체적으로 설명하기 위해, 전방 탐색이 유용한 경우를 살펴보겠습니다. 파일 이름을 매칭하고 이를 기본 이름과 확장자로 나누는 간단한 패턴을 고려해보세요. 예를 들어, news.rc에서 news는 기본 이름이고, rc는 파일 이름의 확장자입니다.

The pattern to match this is quite simple:

이를 매칭하는 패턴은 매우 간단합니다:

.*[.].*$

Notice that the . needs to be treated specially because it’s a metacharacter, so it’s inside a character class to only match that specific character. Also notice the trailing $; this is added to ensure that all the rest of the string must be included in the extension. This regular expression matches foo.bar and autoexec.bat and sendmail.cf and printers.conf.

.은 메타문자이기 때문에 특별히 처리해야 하므로, 특정 문자와만 매칭되도록 문자 클래스 내에 있습니다. 또한, 끝에 $가 있는 것을 주목하세요. 이는 문자열의 나머지 부분이 모두 확장자에 포함되도록 추가된 것입니다. 이 정규 표현식은 foo.bar, autoexec.bat, sendmail.cf, printers.conf와 매칭됩니다.

Now, consider complicating the problem a bit; what if you want to match filenames where the extension is not bat? Some incorrect attempts:

이제 문제를 조금 복잡하게 만들어 보겠습니다. 확장자가 bat가 아닌 파일 이름과 매칭하려면 어떻게 해야 할까요? 몇 가지 잘못된 시도:

.*[.][^b].*$ The first attempt above tries to exclude bat by requiring that the first character of the extension is not a b. This is wrong, because the pattern also doesn’t match foo.bar.

.*[.][^b].*$ 위의 첫 번째 시도는 확장자의 첫 번째 문자가 b가 아니어야 한다고 요구하여 bat를 제외하려고 합니다. 이는 잘못된 것입니다. 패턴이 foo.bar와도 매칭되지 않기 때문입니다.

.*[.]([^b]..|.[^a].|..[^t])$

The expression gets messier when you try to patch up the first solution by requiring one of the following cases to match: the first character of the extension isn’t b; the second character isn’t a; or the third character isn’t t. This accepts foo.bar and rejects autoexec.bat, but it requires a three-letter extension and won’t accept a filename with a two-letter extension such as sendmail.cf. We’ll complicate the pattern again in an effort to fix it.

.*[.]([^b]..|.[^a].|..[^t])$

첫 번째 해결책을 수정하려고 할 때, 다음 경우 중 하나가 매칭되도록 요구하면 표현식이 더 복잡해집니다: 확장자의 첫 번째 문자가 b가 아니거나, 두 번째 문자가 a가 아니거나, 세 번째 문자가 t가 아닙니다. 이는 foo.bar를 허용하고 autoexec.bat를 거부하지만, 세 글자 확장자가 필요하며 sendmail.cf와 같은 두 글자 확장자를 가진 파일 이름은 허용하지 않습니다. 이를 수정하기 위해 패턴을 다시 복잡하게 만들 것입니다.

.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$

In the third attempt, the second and third letters are all made optional in order to allow matching extensions shorter than three characters, such as sendmail.cf.

세 번째 시도에서는 두 번째와 세 번째 문자를 모두 선택 사항으로 만들어 sendmail.cf와 같이 세 글자보다 짧은 확장자와 매칭할 수 있도록 합니다.

The pattern’s getting really complicated now, which makes it hard to read and understand. Worse, if the problem changes and you want to exclude both bat and exe as extensions, the pattern would get even more complicated and confusing.

패턴이 매우 복잡해져서 읽고 이해하기 어려워집니다. 더 나쁜 것은, 문제가 변경되어 bat와 exe를 확장자로 제외하려고 하면, 패턴이 더욱 복잡하고 혼란스러워질 것입니다.

A negative lookahead cuts through all this confusion:

부정적 전방 탐색은 이 모든 혼란을 해결합니다:

.*[.](?!bat$)[^.]*$ The negative lookahead means: if the expression bat doesn’t match at this point, try the rest of the pattern; if bat$ does match, the whole pattern will fail. The trailing $ is required to ensure that something like sample.batch, where the extension only starts with bat, will be allowed. The [^.]* makes sure that the pattern works when there are multiple dots in the filename.

.*[.](?!bat$)[^.]*$ 부정적 전방 탐색은 다음을 의미합니다: 이 지점에서 bat 표현식이 매칭되지 않으면, 패턴의 나머지 부분을 시도합니다. bat$가 매칭되면, 전체 패턴이 실패합니다. 확장자가 bat로 시작하는 sample.batch와 같은 것이 허용되도록 끝에 $가 필요합니다. [^.]*는 파일 이름에 여러 개의 점이 있을 때 패턴이 작동하도록 합니다.

Excluding another filename extension is now easy; simply add it as an alternative inside the assertion. The following pattern excludes filenames that end in either bat or exe:

다른 파일 이름 확장자를 제외하는 것은 이제 쉽습니다. 단순히 어설션 내에 대안으로 추가하면 됩니다. 다음 패턴은 bat 또는 exe로 끝나는 파일 이름을 제외합니다:

.*[.](?!bat$|exe$)[^.]*$

## Modifying Strings

Up to this point, we’ve simply performed searches against a static string. Regular expressions are also commonly used to modify strings in various ways, using the following pattern methods:

## 문자열 수정하기

지금까지 우리는 단순히 정적 문자열에 대해 검색을 수행했습니다. 정규 표현식은 다음 패턴 메서드를 사용하여 다양한 방식으로 문자열을 수정하는 데도 일반적으로 사용됩니다:

Method/Attribute

Purpose

split()

Split the string into a list, splitting it wherever the RE matches

sub()

Find all substrings where the RE matches, and replace them with a different string

subn()

Does the same thing as sub(), but returns the new string and the number of replacements

메서드/속성

목적

split()

정규 표현식이 매칭되는 곳에서 문자열을 분할하여 리스트로 만듭니다

sub()

정규 표현식이 매칭되는 모든 부분 문자열을 찾아 다른 문자열로 대체합니다

subn()

sub()와 동일한 작업을 수행하지만, 새 문자열과 대체 횟수를 반환합니다

## Splitting Strings

The split() method of a pattern splits a string apart wherever the RE matches, returning a list of the pieces. It’s similar to the split() method of strings but provides much more generality in the delimiters that you can split by; string split() only supports splitting by whitespace or by a fixed string. As you’d expect, there’s a module-level re.split() function, too.

## 문자열 분할하기

패턴의 split() 메서드는 정규 표현식이 매칭되는 곳에서 문자열을 분할하여 조각의 리스트를 반환합니다. 이는 문자열의 split() 메서드와 유사하지만, 분할할 수 있는 구분 기호에 대해 훨씬 더 일반성을 제공합니다. 문자열 split()은 공백 또는 고정 문자열로만 분할을 지원합니다. 예상대로, 모듈 수준의 re.split() 함수도 있습니다.

.split(string[, maxsplit=0])
Split string by the matches of the regular expression. If capturing parentheses are used in the RE, then their contents will also be returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits are performed.

.split(string[, maxsplit=0])
정규 표현식의 매칭으로 문자열을 분할합니다. 정규 표현식에서 캡처 괄호가 사용된 경우, 그 내용도 결과 리스트의 일부로 반환됩니다. maxsplit이 0이 아닌 경우, 최대 maxsplit 분할이 수행됩니다.

You can limit the number of splits made, by passing a value for maxsplit. When maxsplit is nonzero, at most maxsplit splits will be made, and the remainder of the string is returned as the final element of the list. In the following example, the delimiter is any sequence of non-alphanumeric characters.

maxsplit 값을 전달하여 분할 횟수를 제한할 수 있습니다. maxsplit이 0이 아닌 경우, 최대 maxsplit 분할이 수행되며, 나머지 문자열은 리스트의 마지막 요소로 반환됩니다. 다음 예제에서 구분 기호는 비영숫자 문자의 시퀀스입니다.

```python
p = re.compile(r'\W+')
p.split('This is a test, short and sweet, of split().')
['This', 'is', 'a', 'test', 'short', 'and', 'sweet', 'of', 'split', '']
p.split('This is a test, short and sweet, of split().', 3)
['This', 'is', 'a', 'test, short and sweet, of split().']
```

Sometimes you’re not only interested in what the text between delimiters is, but also need to know what the delimiter was. If capturing parentheses are used in the RE, then their values are also returned as part of the list. Compare the following calls:

때로는 구분 기호 사이의 텍스트뿐만 아니라 구분 기호가 무엇인지도 알고 싶을 수 있습니다. 정규 표현식에서 캡처 괄호가 사용된 경우, 그 값도 리스트의 일부로 반환됩니다. 다음 호출을 비교해 보세요:

```python
p = re.compile(r'\W+')
p2 = re.compile(r'(\W+)')
p.split('This... is a test.')
['This', 'is', 'a', 'test', '']
p2.split('This... is a test.')
['This', '... ', 'is', ' ', 'a', ' ', 'test', '.', '']
```

The module-level function re.split() adds the RE to be used as the first argument, but is otherwise the same.

모듈 수준의 re.split() 함수는 첫 번째 인수로 사용할 정규 표현식을 추가하지만, 그 외에는 동일합니다.

```python
re.split(r'[\W]+', 'Words, words, words.')
['Words', 'words', 'words', '']
re.split(r'([\W]+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
re.split(r'[\W]+', 'Words, words, words.', 1)
['Words', 'words, words.']
```

## Search and Replace

Another common task is to find all the matches for a pattern, and replace them with a different string. The sub() method takes a replacement value, which can be either a string or a function, and the string to be processed.

## 검색 및 대체

또 다른 일반적인 작업은 패턴에 대한 모든 매칭을 찾아 다른 문자열로 대체하는 것입니다. sub() 메서드는 문자열 또는 함수일 수 있는 대체 값과 처리할 문자열을 받습니다.

.sub(replacement, string[, count=0])
Returns the string obtained by replacing the leftmost non-overlapping occurrences of the RE in string by the replacement replacement. If the pattern isn’t found, string is returned unchanged.

.sub(replacement, string[, count=0])
문자열에서 정규 표현식의 가장 왼쪽에 있는 겹치지 않는 발생을 대체 값으로 대체하여 얻은 문자열을 반환합니다. 패턴이 발견되지 않으면, 문자열은 변경되지 않은 상태로 반환됩니다.

The optional argument count is the maximum number of pattern occurrences to be replaced; count must be a non-negative integer. The default value of 0 means to replace all occurrences.

선택적 인수 count는 대체할 패턴 발생의 최대 수입니다. count는 음수가 아닌 정수여야 합니다. 기본값 0은 모든 발생을 대체함을 의미합니다.

Here’s a simple example of using the sub() method. It replaces colour names with the word colour:

다음은 sub() 메서드를 사용하는 간단한 예입니다. 색상 이름을 colour 단어로 대체합니다:

```python
p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')
'colour socks and colour shoes'
p.sub('colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'
```

The subn() method does the same work, but returns a 2-tuple containing the new string value and the number of replacements that were performed:

subn() 메서드는 동일한 작업을 수행하지만, 새 문자열 값과 수행된 대체 횟수를 포함하는 2-튜플을 반환합니다:

```python
p = re.compile('(blue|white|red)')
p.subn('colour', 'blue socks and red shoes')
('colour socks and colour shoes', 2)
p.subn('colour', 'no colours at all')
('no colours at all', 0)
```

Empty matches are replaced only when they’re not adjacent to a previous empty match.

빈 매칭은 이전 빈 매칭과 인접하지 않은 경우에만 대체됩니다.

```python
p = re.compile('x*')
p.sub('-', 'abxd')
'-a-b--d-'
```

If replacement is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. Unknown escapes such as \& are left alone. Backreferences, such as \6, are replaced with the substring matched by the corresponding group in the RE. This lets you incorporate portions of the original text in the resulting replacement string.

대체 값이 문자열인 경우, 그 안의 모든 백슬래시 이스케이프가 처리됩니다. 즉, \n은 단일 줄 바꿈 문자로 변환되고, \r은 캐리지 리턴으로 변환됩니다. \&와 같은 알 수 없는 이스케이프는 그대로 남습니다. \6과 같은 역참조는 정규 표현식의 해당 그룹과 매칭된 부분 문자열로 대체됩니다. 이를 통해 결과 대체 문자열에 원본 텍스트의 일부를 포함할 수 있습니다.

This example matches the word section followed by a string enclosed in {, }, and changes section to subsection:

이 예제는 {, }로 둘러싸인 문자열 뒤에 오는 section 단어와 매칭되며, section을 subsection으로 변경합니다:

```python
p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First} section{second}')
'subsection{First} subsection{second}'
```

There’s also a syntax for referring to named groups as defined by the (?P<name>...) syntax. \g<name> will use the substring matched by the group named name, and \g<number> uses the corresponding group number. \g<2> is therefore equivalent to \2, but isn’t ambiguous in a replacement string such as \g<2>0. (\20 would be interpreted as a reference to group 20, not a reference to group 2 followed by the literal character '0'.) The following substitutions are all equivalent, but use all three variations of the replacement string.

(?P<name>...) 구문으로 정의된 명명된 그룹을 참조하는 구문도 있습니다. \g<name>은 name이라는 그룹과 매칭된 부분 문자열을 사용하고, \g<number>는 해당 그룹 번호를 사용합니다. 따라서 \g<2>는 \2와 동일하지만, \g<2>0과 같은 대체 문자열에서는 모호하지 않습니다. (\20은 그룹 20에 대한 참조로 해석되며, 그룹 2 뒤에 리터럴 문자 '0'이 오는 것으로 해석되지 않습니다.) 다음 대체는 모두 동일하지만, 대체 문자열의 세 가지 변형을 모두 사용합니다.

```python
p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First}')
'subsection{First}'
p.sub(r'subsection{\g<1>}','section{First}')
'subsection{First}'
p.sub(r'subsection{\g<name>}','section{First}')
'subsection{First}'
```

replacement can also be a function, which gives you even more control. If replacement is a function, the function is called for every non-overlapping occurrence of pattern. On each call, the function is passed a match object argument for the match and can use this information to compute the desired replacement string and return it.

대체 값은 함수일 수도 있으며, 이를 통해 더 많은 제어를 할 수 있습니다. 대체 값이 함수인 경우, 패턴의 겹치지 않는 발생마다 함수가 호출됩니다. 각 호출 시, 함수는 매칭에 대한 매치 객체 인수를 전달받아 원하는 대체 문자열을 계산하고 반환할 수 있습니다.

In the following example, the replacement function translates decimals into hexadecimal:

다음 예제에서 대체 함수는 십진수를 16진수로 변환합니다:

```python
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
'Call 0xffd2 for printing, 0xc000 for user code.'
```

When using the module-level re.sub() function, the pattern is passed as the first argument. The pattern may be provided as an object or as a string; if you need to specify regular expression flags, you must either use a pattern object as the first parameter, or use embedded modifiers in the pattern string, e.g. sub("(?i)b+", "x", "bbbb BBBB") returns 'x x'.

모듈 수준의 re.sub() 함수를 사용할 때, 패턴은 첫 번째 인수로 전달됩니다. 패턴은 객체 또는 문자열로 제공될 수 있습니다. 정규 표현식 플래그를 지정해야 하는 경우, 첫 번째 매개변수로 패턴 객체를 사용하거나 패턴 문자열에 내장된 수정자를 사용해야 합니다. 예를 들어, sub("(?i)b+", "x", "bbbb BBBB")는 'x x'를 반환합니다.

## Common Problems

Regular expressions are a powerful tool for some applications, but in some ways their behaviour isn't intuitive and at times they don't behave the way you may expect them to. This section will point out some of the most common pitfalls.

## 일반적인 문제점

정규 표현식은 일부 애플리케이션에 강력한 도구이지만, 어떤 면에서는 그 동작이 직관적이지 않고 때로는 예상대로 동작하지 않을 수 있습니다. 이 섹션에서는 가장 일반적인 함정 몇 가지를 지적합니다.

### Use String Methods

Sometimes using the re module is a mistake. If you're matching a fixed string, or a single character class, and you're not using any re features such as the IGNORECASE flag, then the full power of regular expressions may not be required. Strings have several methods for performing operations with fixed strings and they're usually much faster, because the implementation is a single small C loop that's been optimized for the purpose, instead of the large, more generalized regular expression engine.

### 문자열 메서드 사용하기

때로는 re 모듈을 사용하는 것이 실수일 수 있습니다. 고정된 문자열이나 단일 문자 클래스를 매칭하고 IGNORECASE 플래그와 같은 re 기능을 사용하지 않는다면, 정규 표현식의 모든 기능이 필요하지 않을 수 있습니다. 문자열에는 고정 문자열로 작업을 수행하기 위한 여러 메서드가 있으며, 이들은 일반적으로 훨씬 빠릅니다. 구현이 목적에 맞게 최적화된 단일 소형 C 루프이기 때문에, 크고 더 일반화된 정규 표현식 엔진보다 효율적입니다.

One example might be replacing a single fixed string with another one; for example, you might replace word with deed. re.sub() seems like the function to use for this, but consider the replace() method. Note that replace() will also replace word inside words, turning swordfish into sdeedfish, but the naive RE word would have done that, too. (To avoid performing the substitution on parts of words, the pattern would have to be \bword\b, in order to require that word have a word boundary on either side. This takes the job beyond replace()'s abilities.)

예를 들어, 하나의 고정된 문자열을 다른 것으로 대체하는 경우가 있습니다. 예를 들어, word를 deed로 대체할 수 있습니다. re.sub()이 이를 위한 함수처럼 보이지만, replace() 메서드를 고려해보세요. replace()는 단어 내의 word도 대체하여 swordfish를 sdeedfish로 바꾸지만, 단순한 정규식 word도 그렇게 할 것입니다. (단어의 일부에서 대체가 수행되지 않도록 하려면, 패턴이 \bword\b여야 합니다. 이는 word가 양쪽에 단어 경계를 갖도록 요구하는 것입니다. 이는 replace()의 능력을 넘어서는 작업입니다.)

Another common task is deleting every occurrence of a single character from a string or replacing it with another single character. You might do this with something like re.sub('\n', ' ', S), but translate() is capable of doing both tasks and will be faster than any regular expression operation can be.

다른 일반적인 작업은 문자열에서 단일 문자의 모든 발생을 삭제하거나 다른 단일 문자로 대체하는 것입니다. re.sub('\n', ' ', S)와 같은 방식으로 이를 수행할 수 있지만, translate()는 두 작업을 모두 수행할 수 있으며 정규 표현식 작업보다 더 빠를 것입니다.

In short, before turning to the re module, consider whether your problem can be solved with a faster and simpler string method.

요약하자면, re 모듈로 전환하기 전에 문제가 더 빠르고 간단한 문자열 메서드로 해결될 수 있는지 고려하세요.

### match() versus search()

The match() function only checks if the RE matches at the beginning of the string while search() will scan forward through the string for a match. It's important to keep this distinction in mind. Remember, match() will only report a successful match which will start at 0; if the match wouldn't start at zero, match() will not report it.

### match()와 search()의 차이

match() 함수는 정규식이 문자열의 시작 부분에서만 매칭되는지 확인하는 반면, search()는 매칭을 위해 문자열을 앞으로 스캔합니다. 이 구분을 기억하는 것이 중요합니다. match()는 0에서 시작하는 성공적인 매칭만 보고한다는 점을 기억하세요. 매칭이 0에서 시작하지 않으면, match()는 보고하지 않습니다.

```python
print(re.match('super', 'superstition').span())
(0, 5)
print(re.match('super', 'insuperable'))
None
```

On the other hand, search() will scan forward through the string, reporting the first match it finds.

반면, search()는 문자열을 앞으로 스캔하여 찾은 첫 번째 매칭을 보고합니다.

```python
print(re.search('super', 'superstition').span())
(0, 5)
print(re.search('super', 'insuperable').span())
(2, 7)
```

Sometimes you'll be tempted to keep using re.match(), and just add .* to the front of your RE. Resist this temptation and use re.search() instead. The regular expression compiler does some analysis of REs in order to speed up the process of looking for a match. One such analysis figures out what the first character of a match must be; for example, a pattern starting with Crow must match starting with a 'C'. The analysis lets the engine quickly scan through the string looking for the starting character, only trying the full match if a 'C' is found.

때로는 re.match()를 계속 사용하고 정규식 앞에 .*를 추가하고 싶을 수 있습니다. 이 유혹을 물리치고 대신 re.search()를 사용하세요. 정규 표현식 컴파일러는 매칭을 찾는 과정을 가속화하기 위해 정규식에 대한 일부 분석을 수행합니다. 이러한 분석 중 하나는 매칭의 첫 번째 문자가 무엇이어야 하는지 파악하는 것입니다. 예를 들어, Crow로 시작하는 패턴은 'C'로 시작해야 합니다. 이 분석을 통해 엔진은 시작 문자를 찾아 문자열을 빠르게 스캔하고, 'C'가 발견된 경우에만 전체 매칭을 시도합니다.

Adding .* defeats this optimization, requiring scanning to the end of the string and then backtracking to find a match for the rest of the RE. Use re.search() instead.

.*를 추가하면 이러한 최적화가 무효화되어 문자열의 끝까지 스캔한 다음 정규식의 나머지 부분에 대한 매칭을 찾기 위해 백트래킹해야 합니다. 대신 re.search()를 사용하세요.

### Greedy versus Non-Greedy

When repeating a regular expression, as in a*, the resulting action is to consume as much of the pattern as possible. This fact often bites you when you're trying to match a pair of balanced delimiters, such as the angle brackets surrounding an HTML tag. The naive pattern for matching a single HTML tag doesn't work because of the greedy nature of .*.

### 탐욕적 대 비탐욕적

a*와 같이 정규 표현식을 반복할 때, 결과 동작은 가능한 한 많은 패턴을 소비하는 것입니다. 이 사실은 HTML 태그를 둘러싼 꺾쇠 괄호와 같은 균형 잡힌 구분 기호 쌍을 매칭하려고 할 때 종종 문제가 됩니다. 단일 HTML 태그를 매칭하기 위한 단순한 패턴은 .*의 탐욕적인 특성 때문에 작동하지 않습니다.

```python
s = '<html><head><title>Title</title>'
len(s)
32
print(re.match('<.*>', s).span())
(0, 32)
print(re.match('<.*>', s).group())
<html><head><title>Title</title>
```

The RE matches the '<' in '<html>', and the .* consumes the rest of the string. There's still more left in the RE, though, and the > can't match at the end of the string, so the regular expression engine has to backtrack character by character until it finds a match for the >. The final match extends from the '<' in '<html>' to the '>' in '</title>', which isn't what you want.

정규식은 '<html>'의 '<'와 매칭되고, .*는 문자열의 나머지 부분을 소비합니다. 그러나 정규식에는 여전히 더 많은 부분이 남아있고, >는 문자열의 끝에서 매칭될 수 없으므로, 정규 표현식 엔진은 >에 대한 매칭을 찾을 때까지 문자별로 백트래킹해야 합니다. 최종 매칭은 '<html>'의 '<'에서 '</title>'의 '>'까지 확장되며, 이는 원하는 결과가 아닙니다.

In this case, the solution is to use the non-greedy quantifiers *?, +?, ??, or {m,n}?, which match as little text as possible. In the above example, the '>' is tried immediately after the first '<' matches, and when it fails, the engine advances a character at a time, retrying the '>' at every step. This produces just the right result:

이 경우, 해결책은 가능한 한 적은 텍스트를 매칭하는 비탐욕적 수량자 *?, +?, ??, 또는 {m,n}?를 사용하는 것입니다. 위의 예에서, 첫 번째 '<'가 매칭된 직후 '>'가 시도되고, 실패하면 엔진은 한 번에 한 문자씩 진행하며 각 단계에서 '>'를 다시 시도합니다. 이렇게 하면 정확한 결과가 나옵니다:

```python
print(re.match('<.*?>', s).group())
<html>
```

(Note that parsing HTML or XML with regular expressions is painful. Quick-and-dirty patterns will handle common cases, but HTML and XML have special cases that will break the obvious regular expression; by the time you've written a regular expression that handles all of the possible cases, the patterns will be very complicated. Use an HTML or XML parser module for such tasks.)

(HTML 또는 XML을 정규 표현식으로 파싱하는 것은 어렵습니다. 빠르고 간단한 패턴은 일반적인 경우를 처리할 수 있지만, HTML과 XML에는 명백한 정규 표현식을 깨뜨리는 특수한 경우가 있습니다. 가능한 모든 경우를 처리하는 정규 표현식을 작성하면, 패턴이 매우 복잡해집니다. 이러한 작업에는 HTML 또는 XML 파서 모듈을 사용하세요.)

### Using re.VERBOSE

By now you've probably noticed that regular expressions are a very compact notation, but they're not terribly readable. REs of moderate complexity can become lengthy collections of backslashes, parentheses, and metacharacters, making them difficult to read and understand.

### re.VERBOSE 사용하기

지금쯤이면 정규 표현식이 매우 간결한 표기법이지만, 읽기가 그리 쉽지 않다는 것을 눈치챘을 것입니다. 중간 정도 복잡성을 가진 정규식은 백슬래시, 괄호, 메타문자의 길고 복잡한 모음이 될 수 있어 읽고 이해하기 어려울 수 있습니다.

For such REs, specifying the re.VERBOSE flag when compiling the regular expression can be helpful, because it allows you to format the regular expression more clearly.

이러한 정규식의 경우, 정규 표현식을 컴파일할 때 re.VERBOSE 플래그를 지정하는 것이 도움이 될 수 있습니다. 이를 통해 정규 표현식을 더 명확하게 형식화할 수 있기 때문입니다.

The re.VERBOSE flag has several effects. Whitespace in the regular expression that isn't inside a character class is ignored. This means that an expression such as dog | cat is equivalent to the less readable dog|cat, but [a b] will still match the characters 'a', 'b', or a space. In addition, you can also put comments inside a RE; comments extend from a # character to the next newline. When used with triple-quoted strings, this enables REs to be formatted more neatly:

re.VERBOSE 플래그는 여러 가지 효과가 있습니다. 문자 클래스 내에 있지 않은 정규 표현식의 공백은 무시됩니다. 이는 dog | cat과 같은 표현식이 덜 읽기 쉬운 dog|cat과 동일하다는 것을 의미하지만, [a b]는 여전히 'a', 'b' 또는 공백 문자와 매칭됩니다. 또한, 정규식 내에 주석을 넣을 수도 있습니다. 주석은 # 문자에서 다음 줄바꿈까지 확장됩니다. 삼중 따옴표 문자열과 함께 사용하면, 정규식을 더 깔끔하게 형식화할 수 있습니다:

```python
pat = re.compile(r"""
 \s*                 # Skip leading whitespace
 (?P<header>[^:]+)   # Header name
 \s* :               # Whitespace, and a colon
 (?P<value>.*?)      # The header's value -- *? used to
                     # lose the following trailing whitespace
 \s*$                # Trailing whitespace to end-of-line
""", re.VERBOSE)
```

This is far more readable than:

이것은 다음보다 훨씬 더 읽기 쉽습니다:

```python
pat = re.compile(r"\s*(?P<header>[^:]+)\s*:(?P<value>.*?)\s*$")
```

## Feedback

Regular expressions are a complicated topic. Did this document help you understand them? Were there parts that were unclear, or Problems you encountered that weren't covered here? If so, please send suggestions for improvements to the author.

## 피드백

정규 표현식은 복잡한 주제입니다. 이 문서가 이해하는 데 도움이 되었나요? 명확하지 않았던 부분이나 여기서 다루지 않은 문제가 있었나요? 그렇다면, 저자에게 개선을 위한 제안을 보내주세요.

The most complete book on regular expressions is almost certainly Jeffrey Friedl's Mastering Regular Expressions, published by O'Reilly. Unfortunately, it exclusively concentrates on Perl and Java's flavours of regular expressions, and doesn't contain any Python material at all, so it won't be useful as a reference for programming in Python. (The first edition covered Python's now-removed regex module, which won't help you much.) Consider checking it out from your library.

정규 표현식에 관한 가장 완전한 책은 거의 확실히 O'Reilly에서 출판한 Jeffrey Friedl의 "Mastering Regular Expressions"입니다. 불행히도, 이 책은 Perl과 Java의 정규 표현식만을 집중적으로 다루고 있으며 Python 관련 내용은 전혀 포함하고 있지 않아, Python 프로그래밍을 위한 참고 자료로는 유용하지 않을 것입니다. (초판에는 Python의 현재 제거된 regex 모듈에 대한 내용이 포함되어 있었지만, 이는 큰 도움이 되지 않을 것입니다.) 도서관에서 이 책을 확인해 보는 것을 고려해 보세요.
