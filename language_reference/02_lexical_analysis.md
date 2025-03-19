# 2. Lexical analysis

파이썬 프로그램은 파서에 의해 읽힙니다. 파서에 대한 입력은 어휘 분석기(토크나이저라고도 함)에 의해 생성된 토큰 스트림입니다. 이 장에서는 어휘 분석기가 파일을 토큰으로 나누는 방법을 설명합니다.

Python reads program text as Unicode code points; the encoding of a source file can be given by an encoding declaration and defaults to UTF-8, see PEP 3120 for details. If the source file cannot be decoded, a SyntaxError is raised.

파이썬은 프로그램 텍스트를 유니코드 코드 포인트로 읽습니다. 소스 파일의 인코딩은 인코딩 선언에 의해 지정될 수 있으며 기본값은 UTF-8입니다(자세한 내용은 PEP 3120 참조). 소스 파일을 디코딩할 수 없는 경우 SyntaxError가 발생합니다.

## 2.1. Line structure

## 2.1. 라인 구조

A Python program is divided into a number of logical lines.

파이썬 프로그램은 여러 논리적 라인으로 나뉘어집니다.

### 2.1.1. Logical lines

### 2.1.1. 논리적 라인

The end of a logical line is represented by the token NEWLINE. Statements cannot cross logical line boundaries except where NEWLINE is allowed by the syntax (e.g., between statements in compound statements). A logical line is constructed from one or more physical lines by following the explicit or implicit line joining rules.

논리적 라인의 끝은 NEWLINE 토큰으로 표시됩니다. 구문에서 NEWLINE이 허용되는 경우(예: 복합 문장 내의 문장 사이)를 제외하고, 문장은 논리적 라인 경계를 넘을 수 없습니다. 논리적 라인은 명시적 또는 암시적 라인 결합 규칙에 따라 하나 이상의 물리적 라인으로 구성됩니다.

### 2.1.2. Physical lines

### 2.1.2. 물리적 라인

A physical line is a sequence of characters terminated by an end-of-line sequence. In source files and strings, any of the standard platform line termination sequences can be used - the Unix form using ASCII LF (linefeed), the Windows form using the ASCII sequence CR LF (return followed by linefeed), or the old Macintosh form using the ASCII CR (return) character. All of these forms can be used equally, regardless of platform. The end of input also serves as an implicit terminator for the final physical line.

물리적 라인은 줄 끝 시퀀스로 끝나는 문자 시퀀스입니다. 소스 파일과 문자열에서는 표준 플랫폼 줄 종료 시퀀스인 Unix 형식의 ASCII LF(linefeed), Windows 형식의 ASCII 시퀀스 CR LF(return 다음에 linefeed), 또는 오래된 Macintosh 형식의 ASCII CR(return) 문자 중 어느 것이든 사용될 수 있습니다. 플랫폼에 관계없이 이러한 모든 형식을 동등하게 사용할 수 있습니다. 입력의 끝은 최종 물리적 라인의 암시적 종결자 역할도 합니다.

When embedding Python, source code strings should be passed to Python APIs using the standard C conventions for newline characters (the \n character, representing ASCII LF, is the line terminator).

파이썬을 임베딩할 때, 소스 코드 문자열은 개행 문자에 대한 표준 C 규칙을 사용하여 파이썬 API에 전달되어야 합니다(ASCII LF를 나타내는 \n 문자가 라인 종결자입니다).

### 2.1.3. Comments

### 2.1.3. 주석

A comment starts with a hash character (#) that is not part of a string literal, and ends at the end of the physical line. A comment signifies the end of the logical line unless the implicit line joining rules are invoked. Comments are ignored by the syntax.

주석은 문자열 리터럴의 일부가 아닌 해시 문자(#)로 시작하여 물리적 라인의 끝에서 끝납니다. 암시적 라인 결합 규칙이 호출되지 않는 한 주석은 논리적 라인의 끝을 의미합니다. 주석은 구문에 의해 무시됩니다.

### 2.1.4. Encoding declarations

### 2.1.4. 인코딩 선언

If a comment in the first or second line of the Python script matches the regular expression coding[=:]\s*([-\w.]+), this comment is processed as an encoding declaration; the first group of this expression names the encoding of the source code file. The encoding declaration must appear on a line of its own. If it is the second line, the first line must also be a comment-only line. The recommended forms of an encoding expression are

파이썬 스크립트의 첫 번째 또는 두 번째 줄에 있는 주석이 정규 표현식 coding[=:]\s*([-\w.]+)과 일치하면, 이 주석은 인코딩 선언으로 처리됩니다. 이 표현식의 첫 번째 그룹은 소스 코드 파일의 인코딩을 지정합니다. 인코딩 선언은 별도의 줄에 나타나야 합니다. 두 번째 줄에 있는 경우 첫 번째 줄도 주석만 있는 줄이어야 합니다. 권장되는 인코딩 표현식 형식은 다음과 같습니다:

# -*- coding: <encoding-name> -*-
which is recognized also by GNU Emacs, and

# -*- coding: <encoding-name> -*-
GNU Emacs에서도 인식되는 형식이며,

# vim:fileencoding=<encoding-name>
which is recognized by Bram Moolenaar's VIM.

# vim:fileencoding=<encoding-name>
Bram Moolenaar의 VIM에서 인식되는 형식입니다.

If no encoding declaration is found, the default encoding is UTF-8. If the implicit or explicit encoding of a file is UTF-8, an initial UTF-8 byte-order mark (b'xefxbbxbf') is ignored rather than being a syntax error.

인코딩 선언이 없으면 기본 인코딩은 UTF-8입니다. 파일의 암시적 또는 명시적 인코딩이 UTF-8인 경우, 초기 UTF-8 바이트 순서 표시(BOM, b'xefxbbxbf')는 구문 오류가 아닌 무시됩니다.

If an encoding is declared, the encoding name must be recognized by Python (see Standard Encodings). The encoding is used for all lexical analysis, including string literals, comments and identifiers.

인코딩이 선언된 경우, 인코딩 이름은 파이썬이 인식할 수 있어야 합니다(표준 인코딩 참조). 인코딩은 문자열 리터럴, 주석 및 식별자를 포함한 모든 어휘 분석에 사용됩니다.

### 2.1.5. Explicit line joining

### 2.1.5. 명시적 라인 결합

Two or more physical lines may be joined into logical lines using backslash characters (\), as follows: when a physical line ends in a backslash that is not part of a string literal or comment, it is joined with the following forming a single logical line, deleting the backslash and the following end-of-line character. For example:

두 개 이상의 물리적 라인은 다음과 같이 백슬래시 문자(\)를 사용하여 논리적 라인으로 결합될 수 있습니다: 물리적 라인이 문자열 리터럴이나 주석의 일부가 아닌 백슬래시로 끝나면, 다음 라인과 결합되어 하나의 논리적 라인을 형성하며, 백슬래시와 다음 줄 끝 문자는 삭제됩니다. 예를 들면:

```python
if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1
```

A line ending in a backslash cannot carry a comment. A backslash does not continue a comment. A backslash does not continue a token except for string literals (i.e., tokens other than string literals cannot be split across physical lines using a backslash). A backslash is illegal elsewhere on a line outside a string literal.

백슬래시로 끝나는 줄에는 주석을 달 수 없습니다. 백슬래시는 주석을 계속하지 않습니다. 백슬래시는 문자열 리터럴을 제외한 토큰을 계속하지 않습니다(즉, 문자열 리터럴 이외의 토큰은 백슬래시를 사용하여 물리적 라인 간에 분할될 수 없습니다). 문자열 리터럴 외부의 줄에서 백슬래시는 다른 곳에서 불법입니다.

### 2.1.6. Implicit line joining

### 2.1.6. 암시적 라인 결합

Expressions in parentheses, square brackets or curly braces can be split over more than one physical line without using backslashes. For example:

괄호, 대괄호 또는 중괄호 안의 표현식은 백슬래시를 사용하지 않고도 여러 물리적 라인에 걸쳐 분할될 수 있습니다. 예를 들면:

```python
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year
```

Implicitly continued lines can carry comments. The indentation of the continuation lines is not important. Blank continuation lines are allowed. There is no NEWLINE token between implicit continuation lines. Implicitly continued lines can also occur within triple-quoted strings (see below); in that case they cannot carry comments.

암시적으로 계속되는 라인에는 주석이 포함될 수 있습니다. 연속 라인의 들여쓰기는 중요하지 않습니다. 빈 연속 라인도 허용됩니다. 암시적 연속 라인 사이에는 NEWLINE 토큰이 없습니다. 암시적 연속 라인은 삼중 따옴표 문자열(아래 참조) 내에서도 발생할 수 있습니다. 이 경우에는 주석을 포함할 수 없습니다.

### 2.1.7. Blank lines

### 2.1.7. 빈 라인

A logical line that contains only spaces, tabs, formfeeds and possibly a comment, is ignored (i.e., no NEWLINE token is generated). During interactive input of statements, handling of a blank line may differ depending on the implementation of the read-eval-print loop. In the standard interactive interpreter, an entirely blank logical line (i.e. one containing not even whitespace or a comment) terminates a multi-line statement.

공백, 탭, 폼피드 및 가능한 주석만 포함하는 논리적 라인은 무시됩니다(즉, NEWLINE 토큰이 생성되지 않음). 문장의 대화형 입력 중, 빈 라인의 처리는 read-eval-print 루프의 구현에 따라 다를 수 있습니다. 표준 대화형 인터프리터에서는 완전히 빈 논리적 라인(즉, 공백이나 주석조차 포함하지 않는 라인)이 여러 줄 문장을 종료합니다.

### 2.1.8. Indentation

### 2.1.8. 들여쓰기

Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.

논리적 라인 시작 부분의 선행 공백(스페이스 및 탭)은 라인의 들여쓰기 수준을 계산하는 데 사용되며, 이는 다시 문장의 그룹화를 결정하는 데 사용됩니다.

Tabs are replaced (from left to right) by one to eight spaces such that the total number of characters up to and including the replacement is a multiple of eight (this is intended to be the same rule as used by Unix). The total number of spaces preceding the first non-blank character then determines the line's indentation. Indentation cannot be split over multiple physical lines using backslashes; the whitespace up to the first backslash determines the indentation.

탭은 (왼쪽에서 오른쪽으로) 대체를 포함하여 총 문자 수가 8의 배수가 되도록 1~8개의 공백으로 대체됩니다(이것은 Unix에서 사용하는 규칙과 동일하게 적용하기 위한 것임). 그런 다음 첫 번째 공백이 아닌 문자 앞에 오는 총 공백 수가 라인의 들여쓰기를 결정합니다. 들여쓰기는 백슬래시를 사용하여 여러 물리적 라인에 걸쳐 분할될 수 없습니다. 첫 번째 백슬래시까지의 공백이 들여쓰기를 결정합니다.

Indentation is rejected as inconsistent if a source file mixes tabs and spaces in a way that makes the meaning dependent on the worth of a tab in spaces; a TabError is raised in that case.

소스 파일이 탭과 스페이스를 혼합하여 의미가 탭의 스페이스 가치에 의존하게 되는 경우, 들여쓰기는 일관성이 없다고 거부됩니다. 이 경우 TabError가 발생합니다.

Cross-platform compatibility note: because of the nature of text editors on non-UNIX platforms, it is unwise to use a mixture of spaces and tabs for the indentation in a single source file. It should also be noted that different platforms may explicitly limit the maximum indentation level.

크로스 플랫폼 호환성 참고: 비 유닉스 플랫폼의 텍스트 편집기 특성으로 인해 단일 소스 파일에서 들여쓰기에 공백과 탭을 혼합하여 사용하는 것은 현명하지 않습니다. 또한 다른 플랫폼은 최대 들여쓰기 수준을 명시적으로 제한할 수 있다는 점에 유의해야 합니다.

A formfeed character may be present at the start of the line; it will be ignored for the indentation calculations above. Formfeed characters occurring elsewhere in the leading whitespace have an undefined effect (for instance, they may reset the space count to zero).

폼피드 문자는 라인의 시작 부분에 있을 수 있으며, 위의 들여쓰기 계산에서는 무시됩니다. 선행 공백의 다른 부분에 있는 폼피드 문자는 정의되지 않은 효과를 가집니다(예를 들어, 공백 카운트를 0으로 재설정할 수 있음).

The indentation levels of consecutive lines are used to generate INDENT and DEDENT tokens, using a stack, as follows.

연속된 라인의 들여쓰기 수준은 다음과 같이 스택을 사용하여 INDENT 및 DEDENT 토큰을 생성하는 데 사용됩니다.

Before the first line of the file is read, a single zero is pushed on the stack; this will never be popped off again. The numbers pushed on the stack will always be strictly increasing from bottom to top. At the beginning of each logical line, the line's indentation level is compared to the top of the stack. If it is equal, nothing happens. If it is larger, it is pushed on the stack, and one INDENT token is generated. If it is smaller, it must be one of the numbers occurring on the stack; all numbers on the stack that are larger are popped off, and for each number popped off a DEDENT token is generated. At the end of the file, a DEDENT token is generated for each number remaining on the stack that is larger than zero.

파일의 첫 번째 라인을 읽기 전에, 스택에 단일 0이 푸시됩니다. 이것은 다시 빠져나가지 않습니다. 스택에 푸시된 숫자는 항상 아래에서 위로 엄격히 증가합니다. 각 논리적 라인의 시작 부분에서, 라인의 들여쓰기 수준은 스택의 맨 위와 비교됩니다. 같으면 아무 일도 일어나지 않습니다. 더 크면 스택에 푸시되고 하나의 INDENT 토큰이 생성됩니다. 더 작으면 스택에 있는 숫자 중 하나여야 합니다. 더 큰 스택의 모든 숫자는 빠져나가고, 빠져나간 각 숫자에 대해 DEDENT 토큰이 생성됩니다. 파일 끝에서, 0보다 큰 스택에 남아 있는 각 숫자에 대해 DEDENT 토큰이 생성됩니다.

Here is an example of a correctly (though confusingly) indented piece of Python code:

다음은 올바르게(다소 혼란스럽게) 들여쓰기된 파이썬 코드의 예입니다:

```python
def perm(l):
        # Compute the list of all permutations of l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r
```

The following example shows various indentation errors:

다음 예는 다양한 들여쓰기 오류를 보여줍니다:

```python
 def perm(l):                       # error: first line indented
for i in range(len(l)):             # error: not indented
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:])   # error: unexpected indent
        for x in p:
                r.append(l[i:i+1] + x)
            return r                # error: inconsistent dedent
```

(Actually, the first three errors are detected by the parser; only the last error is found by the lexical analyzer — the indentation of return r does not match a level popped off the stack.)

(실제로 처음 세 오류는 파서에 의해 감지됩니다. 마지막 오류만 어휘 분석기에 의해 발견됩니다 - return r의 들여쓰기가 스택에서 빠져나간 수준과 일치하지 않습니다.)

### 2.1.9. Whitespace between tokens

### 2.1.9. 토큰 간 공백

Except at the beginning of a logical line or in string literals, the whitespace characters space, tab and formfeed can be used interchangeably to separate tokens. Whitespace is needed between two tokens only if their concatenation could otherwise be interpreted as a different token (e.g., ab is one token, but a b is two tokens).

논리적 라인의 시작이나 문자열 리터럴에서 제외하고, 공백 문자인 스페이스, 탭 및 폼피드는 토큰을 구분하기 위해 서로 바꿔서 사용할 수 있습니다. 두 토큰 사이에는 연결 시 다른 토큰으로 해석될 수 있는 경우에만 공백이 필요합니다(예: ab는 하나의 토큰이지만, a b는 두 개의 토큰입니다).

## 2.2. Other tokens

## 2.2. 기타 토큰

Besides NEWLINE, INDENT and DEDENT, the following categories of tokens exist: identifiers, keywords, literals, operators, and delimiters. Whitespace characters (other than line terminators, discussed earlier) are not tokens, but serve to delimit tokens. Where ambiguity exists, a token comprises the longest possible string that forms a legal token, when read from left to right.

NEWLINE, INDENT 및 DEDENT 외에도 다음과 같은 토큰 카테고리가 존재합니다: 식별자, 키워드, 리터럴, 연산자 및 구분자. 공백 문자(앞서 논의한 줄 종결자 제외)는 토큰이 아니지만, 토큰을 구분하는 역할을 합니다. 모호성이 존재하는 경우, 토큰은 왼쪽에서 오른쪽으로 읽을 때 합법적인 토큰을 형성하는 가능한 가장 긴 문자열로 구성됩니다.

## 2.3. Identifiers and keywords

## 2.3. 식별자와 키워드

Identifiers (also referred to as names) are described by the following lexical definitions.

식별자(이름이라고도 함)는 다음의 어휘적 정의에 의해 설명됩니다.

The syntax of identifiers in Python is based on the Unicode standard annex UAX-31, with elaboration and changes as defined below; see also PEP 3131 for further details.

파이썬의 식별자 구문은 유니코드 표준 부록 UAX-31을 기반으로 하며, 아래에 정의된 대로 상세 설명 및 변경 사항이 있습니다. 자세한 내용은 PEP 3131을 참조하십시오.

Within the ASCII range (U+0001..U+007F), the valid characters for identifiers include the uppercase and lowercase letters A through Z, the underscore _ and, except for the first character, the digits 0 through 9. Python 3.0 introduced additional characters from outside the ASCII range (see PEP 3131). For these characters, the classification uses the version of the Unicode Character Database as included in the unicodedata module.

ASCII 범위(U+0001..U+007F) 내에서, 식별자에 유효한 문자는 대문자 및 소문자 A부터 Z까지, 밑줄(_), 그리고 첫 번째 문자를 제외하고는 숫자 0부터 9까지를 포함합니다. 파이썬 3.0은 ASCII 범위 외부의 추가 문자를 도입했습니다(PEP 3131 참조). 이러한 문자들에 대해, 분류는 unicodedata 모듈에 포함된 유니코드 문자 데이터베이스 버전을 사용합니다.

Identifiers are unlimited in length. Case is significant.

식별자의 길이는 제한이 없습니다. 대소문자가 구별됩니다.

```
identifier   ::= xid_start xid_continue*
id_start     ::= <all characters in general categories Lu, Ll, Lt, Lm, Lo, Nl, the underscore, and characters with the Other_ID_Start property>
id_continue  ::= <all characters in id_start, plus characters in the categories Mn, Mc, Nd, Pc and others with the Other_ID_Continue property>
xid_start    ::= <all characters in id_start whose NFKC normalization is in "id_start xid_continue*">
xid_continue ::= <all characters in id_continue whose NFKC normalization is in "id_continue*">
```

The Unicode category codes mentioned above stand for:

위에서 언급한 유니코드 카테고리 코드는 다음을 나타냅니다:

Lu - uppercase letters

Lu - 대문자 알파벳

Ll - lowercase letters

Ll - 소문자 알파벳

Lt - titlecase letters

Lt - 타이틀케이스 문자

Lm - modifier letters

Lm - 수정자 문자

Lo - other letters

Lo - 기타 문자

Nl - letter numbers

Nl - 문자 숫자

Mn - nonspacing marks

Mn - 비공백 마크

Mc - spacing combining marks

Mc - 공백 결합 마크

Nd - decimal numbers

Nd - 십진수 숫자

Pc - connector punctuations

Pc - 연결 구두점

Other_ID_Start - explicit list of characters in PropList.txt to support backwards compatibility

Other_ID_Start - 이전 버전과의 호환성을 지원하기 위한 PropList.txt의 명시적 문자 목록

Other_ID_Continue - likewise

Other_ID_Continue - 마찬가지

All identifiers are converted into the normal form NFKC while parsing; comparison of identifiers is based on NFKC.

모든 식별자는 구문 분석 중에 정규형 NFKC로 변환됩니다. 식별자 비교는 NFKC를 기반으로 합니다.

A non-normative HTML file listing all valid identifier characters for Unicode 15.1.0 can be found at https://www.unicode.org/Public/15.1.0/ucd/DerivedCoreProperties.txt

유니코드 15.1.0에 대한 모든 유효한 식별자 문자를 나열한 비표준 HTML 파일은 https://www.unicode.org/Public/15.1.0/ucd/DerivedCoreProperties.txt 에서 찾을 수 있습니다.

### 2.3.1. Keywords

### 2.3.1. 키워드

The following identifiers are used as reserved words, or keywords of the language, and cannot be used as ordinary identifiers. They must be spelled exactly as written here:

다음 식별자들은 언어의 예약어 또는 키워드로 사용되며, 일반적인 식별자로 사용될 수 없습니다. 여기에 쓰여진 대로 정확하게 철자를 맞춰야 합니다:

```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### 2.3.2. Soft Keywords

### 2.3.2. 소프트 키워드

Added in version 3.10.

버전 3.10에서 추가됨.

Some identifiers are only reserved under specific contexts. These are known as soft keywords. The identifiers match, case, type and _ can syntactically act as keywords in certain contexts, but this distinction is done at the parser level, not when tokenizing.

일부 식별자는 특정 컨텍스트에서만 예약됩니다. 이를 소프트 키워드라고 합니다. 식별자 match, case, type 및 _는 특정 컨텍스트에서 구문적으로 키워드로 작동할 수 있지만, 이 구분은 토큰화할 때가 아니라 파서 수준에서 이루어집니다.

As soft keywords, their use in the grammar is possible while still preserving compatibility with existing code that uses these names as identifier names.

소프트 키워드이므로, 이러한 이름을 식별자 이름으로 사용하는 기존 코드와의 호환성을 유지하면서도 문법에서 사용할 수 있습니다.

match, case, and _ are used in the match statement. type is used in the type statement.

match, case 및 _는 match 문에서 사용됩니다. type은 type 문에서 사용됩니다.

Changed in version 3.12: type is now a soft keyword.

버전 3.12에서 변경됨: type이 이제 소프트 키워드입니다.

### 2.3.3. Reserved classes of identifiers

### 2.3.3. 예약된 식별자 클래스

Certain classes of identifiers (besides keywords) have special meanings. These classes are identified by the patterns of leading and trailing underscore characters:

특정 식별자 클래스(키워드 외에)는 특별한 의미를 가집니다. 이러한 클래스는 선행 및 후행 밑줄 문자의 패턴으로 식별됩니다:

`_*`
Not imported by from module import *.

`_*`
from module import * 에 의해 가져오지 않음.

`_`
In a case pattern within a match statement, _ is a soft keyword that denotes a wildcard.

`_`
match 문 내의 case 패턴에서, _는 와일드카드를 나타내는 소프트 키워드입니다.

Separately, the interactive interpreter makes the result of the last evaluation available in the variable _. (It is stored in the builtins module, alongside built-in functions like print.)

별도로, 대화형 인터프리터는 마지막 평가 결과를 변수 _에서 사용할 수 있게 합니다. (이는 print와 같은 내장 함수와 함께 builtins 모듈에 저장됩니다.)

Elsewhere, _ is a regular identifier. It is often used to name "special" items, but it is not special to Python itself.

다른 곳에서, _는 일반적인 식별자입니다. 종종 "특별한" 항목의 이름을 지정하는 데 사용되지만, 파이썬 자체에는 특별한 의미가 없습니다.

Note The name _ is often used in conjunction with internationalization; refer to the documentation for the gettext module for more information on this convention.
It is also commonly used for unused variables.

참고 이름 _는 종종 국제화와 함께 사용됩니다. 이 관례에 대한 자세한 정보는 gettext 모듈의 설명서를 참조하십시오.
또한 일반적으로 사용되지 않는 변수에 사용됩니다.

`__*__`
System-defined names, informally known as "dunder" names. These names are defined by the interpreter and its implementation (including the standard library). Current system names are discussed in the Special method names section and elsewhere. More will likely be defined in future versions of Python. Any use of __*__ names, in any context, that does not follow explicitly documented use, is subject to breakage without warning.

`__*__`
비공식적으로 "던더(dunder)" 이름으로 알려진 시스템 정의 이름. 이 이름들은 인터프리터와 그 구현(표준 라이브러리 포함)에 의해 정의됩니다. 현재 시스템 이름은 특별 메서드 이름 섹션과 다른 곳에서 논의됩니다. 더 많은 이름이 향후 파이썬 버전에서 정의될 가능성이 있습니다. 명시적으로 문서화된 사용법을 따르지 않는, 어떤 맥락에서든 __*__ 이름을 사용하면 경고 없이 손상될 수 있습니다.

`__*`
Class-private names. Names in this category, when used within the context of a class definition, are re-written to use a mangled form to help avoid name clashes between "private" attributes of base and derived classes. See section Identifiers (Names).

`__*`
클래스 전용 이름. 이 카테고리의 이름은 클래스 정의 컨텍스트 내에서 사용될 때, 기본 클래스와 파생 클래스의 "전용" 속성 사이의 이름 충돌을 피하기 위해 변형된 형태를 사용하도록 다시 작성됩니다. 식별자(이름) 섹션을 참조하십시오.

## 2.4. Literals

## 2.4. 리터럴

Literals are notations for constant values of some built-in types.

리터럴은 일부 내장 타입의 상수 값에 대한 표기법입니다.

### 2.4.1. String and Bytes literals

### 2.4.1. 문자열 및 바이트 리터럴

String literals are described by the following lexical definitions:

문자열 리터럴은 다음의 어휘적 정의에 의해 설명됩니다:

```
stringliteral   ::= [stringprefix](shortstring | longstring)
stringprefix    ::= "r" | "u" | "R" | "U" | "f" | "F"
                    | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
shortstring     ::= "'" shortstringitem* "'" | '"' shortstringitem* '"'
longstring      ::= "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
shortstringitem ::= shortstringchar | stringescapeseq
longstringitem  ::= longstringchar | stringescapeseq
shortstringchar ::= <any source character except "\" or newline or the quote>
longstringchar  ::= <any source character except "\">
stringescapeseq ::= "\" <any source character>
bytesliteral   ::= bytesprefix(shortbytes | longbytes)
bytesprefix    ::= "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"
shortbytes     ::= "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
longbytes      ::= "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
shortbytesitem ::= shortbyteschar | bytesescapeseq
longbytesitem  ::= longbyteschar | bytesescapeseq
shortbyteschar ::= <any ASCII character except "\" or newline or the quote>
longbyteschar  ::= <any ASCII character except "\">
bytesescapeseq ::= "\" <any ASCII character>
```

One syntactic restriction not indicated by these productions is that whitespace is not allowed between the stringprefix or bytesprefix and the rest of the literal. The source character set is defined by the encoding declaration; it is UTF-8 if no encoding declaration is given in the source file; see section Encoding declarations.

이러한 문법에서 표시되지 않은 한 가지 구문적 제한은 문자열 접두사(stringprefix) 또는 바이트 접두사(bytesprefix)와 리터럴의 나머지 부분 사이에 공백이 허용되지 않는다는 것입니다. 소스 문자 집합은 인코딩 선언에 의해 정의됩니다. 소스 파일에 인코딩 선언이 없으면 UTF-8입니다. 인코딩 선언 섹션을 참조하세요.

In plain English: Both types of literals can be enclosed in matching single quotes (') or double quotes ("). They can also be enclosed in matching groups of three single or double quotes (these are generally referred to as triple-quoted strings). The backslash (\) character is used to give special meaning to otherwise ordinary characters like n, which means 'newline' when escaped (\n). It can also be used to escape characters that otherwise have a special meaning, such as newline, backslash itself, or the quote character. See escape sequences below for examples.

쉽게 말하자면: 두 유형의 리터럴 모두 일치하는 작은따옴표(') 또는 큰따옴표(")로 둘러싸일 수 있습니다. 또한 세 개의 작은따옴표 또는 큰따옴표 그룹으로 둘러싸일 수도 있습니다(이를 일반적으로 삼중 따옴표 문자열이라고 함). 백슬래시(\) 문자는 일반적인 문자에 특별한 의미를 부여하는 데 사용됩니다. 예를 들어 n은 이스케이프 처리되면(\n) '개행'을 의미합니다. 또한 개행, 백슬래시 자체, 따옴표 문자와 같이 특별한 의미를 갖는 문자를 이스케이프하는 데 사용할 수도 있습니다. 예시는 아래 이스케이프 시퀀스를 참조하세요.

Bytes literals are always prefixed with 'b' or 'B'; they produce an instance of the bytes type instead of the str type. They may only contain ASCII characters; bytes with a numeric value of 128 or greater must be expressed with escapes.

바이트 리터럴은 항상 'b' 또는 'B'로 접두사를 붙입니다. 이들은 str 타입 대신 bytes 타입의 인스턴스를 생성합니다. ASCII 문자만 포함할 수 있으며, 숫자 값이 128 이상인 바이트는 이스케이프로 표현해야 합니다.

Both string and bytes literals may optionally be prefixed with a letter 'r' or 'R'; such constructs are called raw string literals and raw bytes literals respectively and treat backslashes as literal characters. As a result, in raw string literals, '\U' and '\u' escapes are not treated specially.

문자열과 바이트 리터럴 모두 선택적으로 'r' 또는 'R' 문자를 접두사로 사용할 수 있습니다. 이러한 구성을 각각 원시 문자열 리터럴(raw string literals)과 원시 바이트 리터럴(raw bytes literals)이라고 하며, 백슬래시를 문자 그대로 취급합니다. 그 결과, 원시 문자열 리터럴에서는 '\U'와 '\u' 이스케이프가 특별히 처리되지 않습니다.

Added in version 3.3: The 'rb' prefix of raw bytes literals has been added as a synonym of 'br'.

버전 3.3에서 추가됨: 원시 바이트 리터럴의 'rb' 접두사가 'br'의 동의어로 추가되었습니다.

Support for the unicode legacy literal (u'value') was reintroduced to simplify the maintenance of dual Python 2.x and 3.x codebases. See PEP 414 for more information.

유니코드 레거시 리터럴(u'value')에 대한 지원이 파이썬 2.x와 3.x 코드베이스의 유지 관리를 단순화하기 위해 재도입되었습니다. 자세한 내용은 PEP 414를 참조하세요.

A string literal with 'f' or 'F' in its prefix is a formatted string literal; see f-strings. The 'f' may be combined with 'r', but not with 'b' or 'u', therefore raw formatted strings are possible, but formatted bytes literals are not.

접두사에 'f' 또는 'F'가 있는 문자열 리터럴은 형식화된 문자열 리터럴입니다. f-문자열을 참조하세요. 'f'는 'r'과 결합할 수 있지만 'b' 또는 'u'와는 결합할 수 없으므로, 원시 형식화 문자열은 가능하지만 형식화된 바이트 리터럴은 불가능합니다.

In triple-quoted literals, unescaped newlines and quotes are allowed (and are retained), except that three unescaped quotes in a row terminate the literal. (A "quote" is the character used to open the literal, i.e. either ' or ".)

삼중 따옴표 리터럴에서는 이스케이프되지 않은 줄바꿈과 따옴표가 허용되며(유지됨), 단 연속된 세 개의 이스케이프되지 않은 따옴표는 리터럴을 종료합니다. ("따옴표"는 리터럴을 열기 위해 사용된 문자, 즉 ' 또는 "를 말합니다.)

#### 2.4.1.1. Escape sequences

#### 2.4.1.1. 이스케이프 시퀀스

Unless an 'r' or 'R' prefix is present, escape sequences in string and bytes literals are interpreted according to rules similar to those used by Standard C. The recognized escape sequences are:

'r' 또는 'R' 접두사가 없는 한, 문자열 및 바이트 리터럴의 이스케이프 시퀀스는 표준 C에서 사용되는 규칙과 유사하게 해석됩니다. 인식되는 이스케이프 시퀀스는 다음과 같습니다:

| 이스케이프 시퀀스 | 의미 | 참고 |
| --- | --- | --- |
| \<newline> | 백슬래시와 줄바꿈 무시 | (1) |
| \\ | 백슬래시 (\\) | |
| \' | 작은따옴표 (') | |
| \" | 큰따옴표 (") | |
| \a | ASCII 벨 (BEL) | |
| \b | ASCII 백스페이스 (BS) | |
| \f | ASCII 폼피드 (FF) | |
| \n | ASCII 라인피드 (LF) | |
| \r | ASCII 캐리지 리턴 (CR) | |
| \t | ASCII 수평 탭 (TAB) | |
| \v | ASCII 수직 탭 (VT) | |
| \ooo | 8진수 값 ooo를 가진 문자 | (2,4) |
| \xhh | 16진수 값 hh를 가진 문자 | (3,4) |

Escape sequences only recognized in string literals are:

문자열 리터럴에서만 인식되는 이스케이프 시퀀스는 다음과 같습니다:

| 이스케이프 시퀀스 | 의미 | 참고 |
| --- | --- | --- |
| \N{name} | 유니코드 데이터베이스의 이름이 name인 문자 | (5) |
| \uxxxx | 16비트 16진수 값 xxxx를 가진 문자 | (6) |
| \Uxxxxxxxx | 32비트 16진수 값 xxxxxxxx를 가진 문자 | (7) |

Notes:

참고:

1. A backslash can be added at the end of a line to ignore the newline:

1. 줄 끝에 백슬래시를 추가하여 줄바꿈을 무시할 수 있습니다:

```python
'This string will not include \
backslashes or newline characters.'
'This string will not include backslashes or newline characters.'
```

The same result can be achieved using triple-quoted strings, or parentheses and string literal concatenation.

동일한 결과는 삼중 따옴표 문자열 또는 괄호와 문자열 리터럴 연결을 사용하여 얻을 수 있습니다.

2. As in Standard C, up to three octal digits are accepted.

2. 표준 C와 마찬가지로 최대 3개의 8진수 숫자가 허용됩니다.

Changed in version 3.11: Octal escapes with value larger than 0o377 produce a DeprecationWarning.

버전 3.11에서 변경됨: 0o377보다 큰 값을 가진 8진수 이스케이프는 DeprecationWarning을 발생시킵니다.

Changed in version 3.12: Octal escapes with value larger than 0o377 produce a SyntaxWarning. In a future Python version they will be eventually a SyntaxError.

버전 3.12에서 변경됨: 0o377보다 큰 값을 가진 8진수 이스케이프는 SyntaxWarning을 발생시킵니다. 향후 파이썬 버전에서는 결국 SyntaxError가 될 것입니다.

3. Unlike in Standard C, exactly two hex digits are required.

3. 표준 C와 달리 정확히 두 개의 16진수 숫자가 필요합니다.

4. In a bytes literal, hexadecimal and octal escapes denote the byte with the given value. In a string literal, these escapes denote a Unicode character with the given value.

4. 바이트 리터럴에서 16진수 및 8진수 이스케이프는 주어진 값을 가진 바이트를 나타냅니다. 문자열 리터럴에서 이러한 이스케이프는 주어진 값을 가진 유니코드 문자를 나타냅니다.

5. Changed in version 3.3: Support for name aliases [1] has been added.

5. 버전 3.3에서 변경됨: 이름 별칭[1]에 대한 지원이 추가되었습니다.

6. Exactly four hex digits are required.

6. 정확히 네 개의 16진수 숫자가 필요합니다.

7. Any Unicode character can be encoded this way. Exactly eight hex digits are required.

7. 모든 유니코드 문자는 이 방법으로 인코딩할 수 있습니다. 정확히 8개의 16진수 숫자가 필요합니다.

Unlike Standard C, all unrecognized escape sequences are left in the string unchanged, i.e., the backslash is left in the result. (This behavior is useful when debugging: if an escape sequence is mistyped, the resulting output is more easily recognized as broken.) It is also important to note that the escape sequences only recognized in string literals fall into the category of unrecognized escapes for bytes literals.

표준 C와 달리, 인식되지 않는 모든 이스케이프 시퀀스는 문자열에서 변경되지 않고 그대로 유지됩니다. 즉, 백슬래시가 결과에 남아 있습니다. (이 동작은 디버깅 시 유용합니다. 이스케이프 시퀀스를 잘못 입력하면 결과 출력이 더 쉽게 잘못된 것으로 인식됩니다.) 또한 문자열 리터럴에서만 인식되는 이스케이프 시퀀스는 바이트 리터럴에 대해 인식되지 않는 이스케이프 범주에 속한다는 점에 유의하는 것이 중요합니다.

Changed in version 3.6: Unrecognized escape sequences produce a DeprecationWarning.

버전 3.6에서 변경됨: 인식되지 않는 이스케이프 시퀀스는 DeprecationWarning을 발생시킵니다.

Changed in version 3.12: Unrecognized escape sequences produce a SyntaxWarning. In a future Python version they will be eventually a SyntaxError.

버전 3.12에서 변경됨: 인식되지 않는 이스케이프 시퀀스는 SyntaxWarning을 발생시킵니다. 향후 파이썬 버전에서는 결국 SyntaxError가 될 것입니다.

Even in a raw literal, quotes can be escaped with a backslash, but the backslash remains in the result; for example, r"\"" is a valid string literal consisting of two characters: a backslash and a double quote; r"\" is not a valid string literal (even a raw string cannot end in an odd number of backslashes). Specifically, a raw literal cannot end in a single backslash (since the backslash would escape the following quote character). Note also that a single backslash followed by a newline is interpreted as those two characters as part of the literal, not as a line continuation.

원시 리터럴에서도 따옴표는 백슬래시로 이스케이프될 수 있지만, 백슬래시는 결과에 남아 있습니다. 예를 들어, r"\""는 백슬래시와 큰따옴표 두 문자로 구성된 유효한 문자열 리터럴입니다. r"\"는 유효한 문자열 리터럴이 아닙니다(원시 문자열도 홀수 개의 백슬래시로 끝날 수 없음). 특히, 원시 리터럴은 단일 백슬래시로 끝날 수 없습니다(백슬래시가 다음 따옴표 문자를 이스케이프하기 때문). 또한 백슬래시 하나 다음에 줄바꿈이 오면 이는 줄 연속이 아닌 리터럴의 일부로 두 문자로 해석됩니다.

### 2.4.2. String literal concatenation

### 2.4.2. 문자열 리터럴 연결

Multiple adjacent string or bytes literals (delimited by whitespace), possibly using different quoting conventions, are allowed, and their meaning is the same as their concatenation. Thus, "hello" 'world' is equivalent to "helloworld". This feature can be used to reduce the number of backslashes needed, to split long strings conveniently across long lines, or even to add comments to parts of strings, for example:

공백으로 구분된 여러 인접한 문자열 또는 바이트 리터럴(다양한 따옴표 규칙 사용 가능)은 허용되며, 그 의미는 연결된 것과 같습니다. 따라서, "hello" 'world'는 "helloworld"와 동일합니다. 이 기능은 필요한 백슬래시 수를 줄이거나, 긴 문자열을 긴 줄에 걸쳐 편리하게 분할하거나, 문자열의 일부에 주석을 추가하는 데 사용할 수 있습니다. 예를 들면:

```python
re.compile("[A-Za-z_]"       # letter or underscore
           "[A-Za-z0-9_]*"   # letter, digit or underscore
          )
```

Note that this feature is defined at the syntactical level, but implemented at compile time. The '+' operator must be used to concatenate string expressions at run time. Also note that literal concatenation can use different quoting styles for each component (even mixing raw strings and triple quoted strings), and formatted string literals may be concatenated with plain string literals.

이 기능은 구문 수준에서 정의되지만 컴파일 시간에 구현된다는 점에 유의하세요. 런타임에 문자열 표현식을 연결하려면 '+' 연산자를 사용해야 합니다. 또한 리터럴 연결은 각 구성 요소에 대해 다른 따옴표 스타일을 사용할 수 있으며(원시 문자열과 삼중 따옴표 문자열을 혼합하는 것도 가능), 형식화된 문자열 리터럴은 일반 문자열 리터럴과 연결될 수 있습니다.

### 2.4.3. f-strings

### 2.4.3. f-문자열

Added in version 3.6.

버전 3.6에서 추가됨.

A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really expressions evaluated at run time.

형식화된 문자열 리터럴 또는 f-문자열은 'f' 또는 'F'로 접두사가 붙은 문자열 리터럴입니다. 이러한 문자열은 중괄호 {}로 구분된 표현식인 대체 필드를 포함할 수 있습니다. 다른 문자열 리터럴은 항상 상수 값을 가지는 반면, 형식화된 문자열은 실제로 런타임에 평가되는 표현식입니다.

Escape sequences are decoded like in ordinary string literals (except when a literal is also marked as a raw string). After decoding, the grammar for the contents of the string is:

이스케이프 시퀀스는 일반 문자열 리터럴과 같이 디코딩됩니다(리터럴이 원시 문자열로도 표시된 경우 제외). 디코딩 후, 문자열 내용에 대한 문법은 다음과 같습니다:

```
f_string          ::= (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::= "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::= (conditional_expression | "*" or_expr)
                      ("," conditional_expression | "," "*" or_expr)* [","]
                      | yield_expression
conversion        ::= "s" | "r" | "a"
format_spec       ::= (literal_char | replacement_field)*
literal_char      ::= <any code point except "{", "}" or NULL>
```

The parts of the string outside curly braces are treated literally, except that any doubled curly braces '{{' or '}}' are replaced with the corresponding single curly brace. A single opening curly bracket '{' marks a replacement field, which starts with a Python expression. To display both the expression text and its value after evaluation, (useful in debugging), an equal sign '=' may be added after the expression. A conversion field, introduced by an exclamation point '!' may follow. A format specifier may also be appended, introduced by a colon ':'. A replacement field ends with a closing curly bracket '}'.

중괄호 외부의 문자열 부분은 문자 그대로 처리되며, 이중 중괄호 '{{'나 '}}'는 해당하는 단일 중괄호로 대체됩니다. 단일 여는 중괄호 '{'는 파이썬 표현식으로 시작하는 대체 필드를 표시합니다. 표현식 텍스트와 평가 후 값을 모두 표시하려면(디버깅에 유용), 표현식 뒤에 등호 '='를 추가할 수 있습니다. 느낌표 '!'로 시작하는 변환 필드가 이어질 수 있습니다. 또한 콜론 ':'으로 시작하는 형식 지정자가 추가될 수 있습니다. 대체 필드는 닫는 중괄호 '}'로 끝납니다.

Expressions in formatted string literals are treated like regular Python expressions surrounded by parentheses, with a few exceptions. An empty expression is not allowed, and both lambda and assignment expressions := must be surrounded by explicit parentheses. Each expression is evaluated in the context where the formatted string literal appears, in order from left to right. Replacement expressions can contain newlines in both single-quoted and triple-quoted f-strings and they can contain comments. Everything that comes after a # inside a replacement field is a comment (even closing braces and quotes). In that case, replacement fields must be closed in a different line.

형식화된 문자열 리터럴의 표현식은 몇 가지 예외를 제외하고 괄호로 둘러싸인 일반 파이썬 표현식처럼 처리됩니다. 빈 표현식은 허용되지 않으며, lambda와 할당 표현식 :=는 명시적인 괄호로 둘러싸여야 합니다. 각 표현식은 형식화된 문자열 리터럴이 나타나는 컨텍스트에서 왼쪽에서 오른쪽으로 평가됩니다. 대체 표현식은 작은따옴표와 삼중 따옴표 f-문자열 모두에서 줄바꿈을 포함할 수 있으며 주석을 포함할 수 있습니다. 대체 필드 내 # 뒤에 오는 모든 것은 주석입니다(닫는 괄호와 따옴표 포함). 이 경우 대체 필드는 다른 줄에서 닫아야 합니다.

```python
>>> f"abc{a # This is a comment }"
... + 3}"
'abc5'
```

Changed in version 3.7: Prior to Python 3.7, an await expression and comprehensions containing an async for clause were illegal in the expressions in formatted string literals due to a problem with the implementation.

버전 3.7에서 변경됨: 파이썬 3.7 이전에는 구현 문제로 인해 형식화된 문자열 리터럴의 표현식에 await 표현식과 async for 절을 포함하는 컴프리헨션이 허용되지 않았습니다.

Changed in version 3.12: Prior to Python 3.12, comments were not allowed inside f-string replacement fields.

버전 3.12에서 변경됨: 파이썬 3.12 이전에는 f-문자열 대체 필드 내부에 주석이 허용되지 않았습니다.

When the equal sign '=' is provided, the output will have the expression text, the '=' and the evaluated value. Spaces after the opening brace '{', within the expression and after the '=' are all retained in the output. By default, the '=' causes the repr() of the expression to be provided, unless there is a format specified. When a format is specified it defaults to the str() of the expression unless a conversion '!r' is declared.

등호 '='가 제공되면, 출력에는 표현식 텍스트, '=' 및 평가된 값이 포함됩니다. 여는 중괄호 '{' 뒤, 표현식 내부 및 '=' 뒤의 공백은 모두 출력에 유지됩니다. 기본적으로, 형식이 지정되지 않은 한 '='는 표현식의 repr()을 제공합니다. 형식이 지정된 경우, 변환 '!r'이 선언되지 않은 한 기본적으로 표현식의 str()을 사용합니다.

Added in version 3.8: The equal sign '='.

버전 3.8에서 추가됨: 등호 '='.

If a conversion is specified, the result of evaluating the expression is converted before formatting. Conversion '!s' calls str() on the result, '!r' calls repr(), and '!a' calls ascii().

변환이 지정된 경우, 표현식 평가 결과는 형식화 전에 변환됩니다. 변환 '!s'는 결과에 str()을 호출하고, '!r'은 repr()을 호출하며, '!a'는 ascii()를 호출합니다.

The result is then formatted using the format() protocol. The format specifier is passed to the __format__() method of the expression or conversion result. An empty string is passed when the format specifier is omitted. The formatted result is then included in the final value of the whole string.

그런 다음 결과는 format() 프로토콜을 사용하여 형식화됩니다. 형식 지정자는 표현식 또는 변환 결과의 __format__() 메서드에 전달됩니다. 형식 지정자가 생략된 경우 빈 문자열이 전달됩니다. 형식화된 결과는 전체 문자열의 최종 값에 포함됩니다.

Top-level format specifiers may include nested replacement fields. These nested fields may include their own conversion fields and format specifiers, but may not include more deeply nested replacement fields. The format specifier mini-language is the same as that used by the str.format() method.

최상위 형식 지정자는 중첩된 대체 필드를 포함할 수 있습니다. 이러한 중첩된 필드는 자체 변환 필드와 형식 지정자를 포함할 수 있지만, 더 깊게 중첩된 대체 필드는 포함할 수 없습니다. 형식 지정자 미니 언어는 str.format() 메서드에서 사용되는 것과 동일합니다.

Formatted string literals may be concatenated, but replacement fields cannot be split across literals.

형식화된 문자열 리터럴은 연결될 수 있지만, 대체 필드는 리터럴 간에 분할될 수 없습니다.

Some examples of formatted string literals:

형식화된 문자열 리터럴의 몇 가지 예:

```python
>>>
name = "Fred"
f"He said his name is {name!r}."
"He said his name is 'Fred'."
f"He said his name is {repr(name)}."  # repr() is equivalent to !r
"He said his name is 'Fred'."
width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
today = datetime(year=2017, month=1, day=27)
f"{today:%B %d, %Y}"  # using date format specifier
'January 27, 2017'
f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
number = 1024
f"{number:#0x}"  # using integer format specifier
'0x400'
foo = "bar"
f"{ foo = }" # preserves whitespace
" foo = 'bar'"
line = "The mill's closed"
f"{line = }"
'line = "The mill\'s closed"'
f"{line = :20}"
"line = The mill's closed   "
f"{line = !r:20}"
'line = "The mill\'s closed" '
```

Reusing the outer f-string quoting type inside a replacement field is permitted:

대체 필드 내부에서 외부 f-문자열 따옴표 유형을 재사용하는 것이 허용됩니다:

```python
>>>
a = dict(x=2)
f"abc {a["x"]} def"
'abc 2 def'
```

Changed in version 3.12: Prior to Python 3.12, reuse of the same quoting type of the outer f-string inside a replacement field was not possible.

버전 3.12에서 변경됨: 파이썬 3.12 이전에는 대체 필드 내에서 외부 f-문자열과 동일한 따옴표 유형을 재사용하는 것이 불가능했습니다.

Backslashes are also allowed in replacement fields and are evaluated the same way as in any other context:

백슬래시도 대체 필드에서 허용되며 다른 컨텍스트와 동일한 방식으로 평가됩니다:

```python
>>>
a = ["a", "b", "c"]
print(f"List a contains:\n{"\n".join(a)}")
List a contains:
a
b
c
```

Changed in version 3.12: Prior to Python 3.12, backslashes were not permitted inside an f-string replacement field.

버전 3.12에서 변경됨: 파이썬 3.12 이전에는 f-문자열 대체 필드 내에 백슬래시가 허용되지 않았습니다.

Formatted string literals cannot be used as docstrings, even if they do not include expressions.

형식화된 문자열 리터럴은 표현식을 포함하지 않더라도 독스트링으로 사용될 수 없습니다.

```python
>>>
def foo():
    f"Not a docstring"

foo.__doc__ is None
True
```

See also PEP 498 for the proposal that added formatted string literals, and str.format(), which uses a related format string mechanism.

형식화된 문자열 리터럴을 추가한 제안인 PEP 498과 관련 형식 문자열 메커니즘을 사용하는 str.format()도 참조하세요.

### 2.4.4. Numeric literals

### 2.4.4. 숫자 리터럴

There are three types of numeric literals: integers, floating-point numbers, and imaginary numbers. There are no complex literals (complex numbers can be formed by adding a real number and an imaginary number).

숫자 리터럴에는 세 가지 유형이 있습니다: 정수, 부동 소수점 수, 허수입니다. 복소수 리터럴은 없습니다(복소수는 실수와 허수를 더하여 형성될 수 있습니다).

Note that numeric literals do not include a sign; a phrase like -1 is actually an expression composed of the unary operator '-' and the literal 1.

숫자 리터럴에는 부호가 포함되지 않는다는 점에 유의하세요. -1과 같은 구문은 실제로 단항 연산자 '-'와 리터럴 1로 구성된 표현식입니다.

### 2.4.5. Integer literals

### 2.4.5. 정수 리터럴

Integer literals are described by the following lexical definitions:

정수 리터럴은 다음의 어휘적 정의에 의해 설명됩니다:

```
integer      ::= decinteger | bininteger | octinteger | hexinteger
decinteger   ::= nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger   ::= "0" ("b" | "B") (["_"] bindigit)+
octinteger   ::= "0" ("o" | "O") (["_"] octdigit)+
hexinteger   ::= "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit ::= "1"..."9"
digit        ::= "0"..."9"
bindigit     ::= "0" | "1"
octdigit     ::= "0"..."7"
hexdigit     ::= digit | "a"..."f" | "A"..."F"
```

There is no limit for the length of integer literals apart from what can be stored in available memory.

사용 가능한 메모리에 저장할 수 있는 것 외에는 정수 리터럴의 길이에 대한 제한이 없습니다.

Underscores are ignored for determining the numeric value of the literal. They can be used to group digits for enhanced readability. One underscore can occur between digits, and after base specifiers like 0x.

리터럴의 숫자 값을 결정할 때 밑줄은 무시됩니다. 밑줄은 가독성을 높이기 위해 숫자를 그룹화하는 데 사용할 수 있습니다. 밑줄은 숫자 사이와 0x와 같은 기수 지정자 뒤에 하나씩 올 수 있습니다.

Note that leading zeros in a non-zero decimal number are not allowed. This is for disambiguation with C-style octal literals, which Python used before version 3.0.

0이 아닌 십진수에서 선행 0은 허용되지 않습니다. 이는 파이썬 버전 3.0 이전에 사용했던 C 스타일의 8진수 리터럴과의 모호성을 해소하기 위한 것입니다.

Some examples of integer literals:

정수 리터럴의 몇 가지 예:

```
7     2147483647                        0o177    0b100110111
3     79228162514264337593543950336     0o377    0xdeadbeef
      100_000_000_000                   0b_1110_0101
```

Changed in version 3.6: Underscores are now allowed for grouping purposes in literals.

버전 3.6에서 변경됨: 이제 밑줄을 리터럴에서 그룹화 목적으로 사용할 수 있습니다.

### 2.4.6. Floating-point literals

### 2.4.6. 부동 소수점 리터럴

Floating-point literals are described by the following lexical definitions:

부동 소수점 리터럴은 다음의 어휘적 정의에 의해 설명됩니다:

```
floatnumber   ::= pointfloat | exponentfloat
pointfloat    ::= [digitpart] fraction | digitpart "."
exponentfloat ::= (digitpart | pointfloat) exponent
digitpart     ::= digit (["_"] digit)*
fraction      ::= "." digitpart
exponent      ::= ("e" | "E") ["+" | "-"] digitpart
```

Note that the integer and exponent parts are always interpreted using radix 10. For example, 077e010 is legal, and denotes the same number as 77e10. The allowed range of floating-point literals is implementation-dependent. As in integer literals, underscores are supported for digit grouping.

정수 부분과 지수 부분은 항상 기수 10을 사용하여 해석된다는 점에 유의하세요. 예를 들어, 077e010은 유효하며 77e10과 동일한 숫자를 나타냅니다. 부동 소수점 리터럴의 허용 범위는 구현에 따라 다릅니다. 정수 리터럴과 마찬가지로 숫자 그룹화를 위해 밑줄이 지원됩니다.

Some examples of floating-point literals:

부동 소수점 리터럴의 몇 가지 예:

```
3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93
```

Changed in version 3.6: Underscores are now allowed for grouping purposes in literals.

버전 3.6에서 변경됨: 이제 밑줄을 리터럴에서 그룹화 목적으로 사용할 수 있습니다.

### 2.4.7. Imaginary literals

### 2.4.7. 허수 리터럴

Imaginary literals are described by the following lexical definitions:

허수 리터럴은 다음의 어휘적 정의에 의해 설명됩니다:

```
imagnumber ::= (floatnumber | digitpart) ("j" | "J")
```

An imaginary literal yields a complex number with a real part of 0.0. Complex numbers are represented as a pair of floating-point numbers and have the same restrictions on their range. To create a complex number with a nonzero real part, add a floating-point number to it, e.g., (3+4j). Some examples of imaginary literals:

허수 리터럴은 실수부가 0.0인 복소수를 생성합니다. 복소수는 부동 소수점 숫자의 쌍으로 표현되며 범위에 동일한 제한이 있습니다. 0이 아닌 실수부를 가진 복소수를 만들려면 부동 소수점 숫자를 더하세요. 예를 들어 (3+4j). 허수 리터럴의 몇 가지 예:

```
3.14j   10.j    10j     .001j   1e100j   3.14e-10j   3.14_15_93j
```

## 2.5. Operators

## 2.5. 연산자

The following tokens are operators:

다음 토큰들은 연산자입니다:

```
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

## 2.6. Delimiters

## 2.6. 구분자

The following tokens serve as delimiters in the grammar:

다음 토큰들은 문법에서 구분자 역할을 합니다:

```
(       )       [       ]       {       }
,       :       !       .       ;       @       =
->      +=      -=      *=      /=      //=     %=
@=      &=      |=      ^=      >>=     <<=     **=
```

The period can also occur in floating-point and imaginary literals. A sequence of three periods has a special meaning as an ellipsis literal. The second half of the list, the augmented assignment operators, serve lexically as delimiters, but also perform an operation.

마침표는 부동 소수점 및 허수 리터럴에도 나타날 수 있습니다. 세 개의 마침표 시퀀스는 생략 부호 리터럴로 특별한 의미를 갖습니다. 목록의 후반부인 증강 할당 연산자는 어휘적으로 구분자 역할을 하지만, 연산도 수행합니다.

The following printing ASCII characters have special meaning as part of other tokens or are otherwise significant to the lexical analyzer:

다음 출력 가능한 ASCII 문자들은 다른 토큰의 일부로서 특별한 의미를 갖거나 어휘 분석기에 중요합니다:

```
'       "       #       \
```

The following printing ASCII characters are not used in Python. Their occurrence outside string literals and comments is an unconditional error:

다음 출력 가능한 ASCII 문자들은 파이썬에서 사용되지 않습니다. 문자열 리터럴과 주석 외부에서 이러한 문자가 나타나면 무조건적인 오류가 발생합니다:

```
$       ?       `
```


