# 1. Introduction

Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

파이썬은 배우기 쉽고 강력한 프로그래밍 언어입니다. 효율적인 고수준 데이터 구조와 객체 지향 프로그래밍에 대한 간단하면서도 효과적인 접근 방식을 갖추고 있습니다. 파이썬의 우아한 구문과 동적 타이핑, 그리고 인터프리터 특성은 대부분의 플랫폼에서 다양한 영역의 스크립팅 및 빠른 애플리케이션 개발을 위한 이상적인 언어로 만들어 줍니다.

## 2. Alternate Implementations

Though there is one Python implementation which is by far the most popular, there are some alternate implementations which are of particular interest to different audiences.

가장 널리 사용되는 Python 구현이 하나 있지만, 다양한 사용자에게 특히 유용한 몇 가지 대체 구현이 있습니다.

Known implementations include:

*   **CPython:** This is the original and most-maintained implementation of Python, written in C. New language features generally appear here first.
*   **Jython:** Python implemented in Java. This implementation can be used as a scripting language for Java applications, or can be used to create applications using the Java class libraries. It is also often used to create tests for Java libraries. More information can be found at the Jython website.
*   **Python for .NET:** This implementation actually uses the CPython implementation, but is a managed .NET application and makes .NET libraries available. It was created by Brian Lloyd. For more information, see the Python for .NET home page.
*   **IronPython:** An alternate Python for .NET. Unlike Python.NET, this is a complete Python implementation that generates IL, and compiles Python code directly to .NET assemblies. It was created by Jim Hugunin, the original creator of Jython. For more information, see the IronPython website.
*   **PyPy:** An implementation of Python written completely in Python. It supports several advanced features not found in other implementations like stackless support and a Just in Time compiler. One of the goals of the project is to encourage experimentation with the language itself by making it easier to modify the interpreter (since it is written in Python). Additional information is available on the PyPy project’s home page.

알려진 구현은 다음과 같습니다:

*   **CPython:** C로 작성된 Python의 원본이자 가장 많이 유지 관리되는 구현입니다. 일반적으로 새로운 언어 기능이 여기에 먼저 나타납니다.
*   **Jython:** Java로 구현된 Python입니다. 이 구현은 Java 애플리케이션의 스크립팅 언어로 사용하거나 Java 클래스 라이브러리를 사용하여 애플리케이션을 만드는 데 사용할 수 있습니다. Java 라이브러리 테스트를 만드는 데도 자주 사용됩니다. 자세한 내용은 Jython 웹사이트에서 확인할 수 있습니다.
*   **Python for .NET:** 이 구현은 실제로 CPython 구현을 사용하지만 관리되는 .NET 애플리케이션이며 .NET 라이브러리를 사용할 수 있습니다. Brian Lloyd가 만들었습니다. 자세한 내용은 Python for .NET 홈페이지를 참조하십시오.
*   **IronPython:** .NET을 위한 대체 Python입니다. Python.NET과 달리 IL을 생성하고 Python 코드를 .NET 어셈블리로 직접 컴파일하는 완전한 Python 구현입니다. Jython의 최초 제작자인 Jim Hugunin이 만들었습니다. 자세한 내용은 IronPython 웹사이트를 참조하십시오.
*   **PyPy:** Python으로 완전히 작성된 Python 구현입니다. 스택리스 지원 및 JIT(Just in Time) 컴파일러와 같이 다른 구현에서는 찾을 수 없는 몇 가지 고급 기능을 지원합니다. 프로젝트의 목표 중 하나는 인터프리터를 쉽게 수정할 수 있도록 하여(Python으로 작성되었기 때문에) 언어 자체에 대한 실험을 장려하는 것입니다. 추가 정보는 PyPy 프로젝트 홈페이지에서 확인할 수 있습니다.

## 3. Notation

The descriptions of lexical analysis and syntax use a modified Backus–Naur form (BNF) grammar notation. This uses the following style of definition:

어휘 분석 및 구문 설명에는 수정된 BNF(Backus–Naur Form) 문법 표기법이 사용됩니다. 다음 정의 스타일을 사용합니다.

```
name      ::= lc_letter (lc_letter | "_")*
lc_letter ::= "a"..."z"
```

The first line says that a `name` is an `lc_letter` followed by a sequence of zero or more `lc_letter`s and underscores. An `lc_letter` in turn is any of the single characters 'a' through 'z'. (This rule is actually adhered to for the names defined in lexical and grammar rules in this document.)

첫 번째 줄은 `name`이 `lc_letter` 뒤에 0개 이상의 `lc_letter`와 밑줄이 오는 시퀀스임을 나타냅니다. `lc_letter`는 'a'부터 'z'까지의 단일 문자입니다. (이 규칙은 실제로 이 문서의 어휘 및 문법 규칙에 정의된 이름에 적용됩니다.)

Each rule begins with a `name` (which is the name defined by the rule) and `::=`. A vertical bar (`|`) is used to separate alternatives; it is the least binding operator in this notation. A star (`*`) means zero or more repetitions of the preceding item; likewise, a plus (`+`) means one or more repetitions, and a phrase enclosed in square brackets (`[ ]`) means zero or one occurrences (in other words, the enclosed phrase is optional). The `*` and `+` operators bind as tightly as possible; parentheses are used for grouping. Literal strings are enclosed in quotes. White space is only meaningful to separate tokens. Rules are normally contained on a single line; rules with many alternatives may be formatted alternatively with each line after the first beginning with a vertical bar.

각 규칙은 `name`(규칙에 의해 정의된 이름)과 `::=`으로 시작합니다. 세로 막대(`|`)는 대안을 구분하는 데 사용되며, 이 표기법에서 가장 낮은 바인딩 연산자입니다. 별표(`*`)는 앞 항목의 0회 이상 반복을 의미하고, 더하기(`+`)는 1회 이상 반복을 의미하며, 대괄호(`[ ]`)로 묶인 구문은 0회 또는 1회 발생을 의미합니다(즉, 묶인 구문은 선택 사항임). `*` 및 `+` 연산자는 최대한 밀접하게 바인딩됩니다. 괄호는 그룹화에 사용됩니다. 리터럴 문자열은 따옴표로 묶습니다. 공백은 토큰을 구분하는 데만 의미가 있습니다. 규칙은 일반적으로 한 줄에 포함됩니다. 대안이 많은 규칙은 첫 번째 줄 다음에 세로 막대로 시작하는 각 줄을 사용하여 대체 형식으로 지정할 수 있습니다.

In lexical definitions (as the example above), two more conventions are used: Two literal characters separated by three dots mean a choice of any single character in the given (inclusive) range of ASCII characters. A phrase between angular brackets (`<...>`) gives an informal description of the symbol defined; e.g., this could be used to describe the notion of ‘control character’ if needed.

어휘 정의(위의 예에서와 같이)에서는 두 가지 규칙이 더 사용됩니다. 세 개의 점으로 구분된 두 개의 리터럴 문자는 주어진 (포함) ASCII 문자 범위에서 단일 문자를 선택하는 것을 의미합니다. 꺾쇠 괄호(` <...> `) 사이의 구문은 정의된 기호에 대한 비공식적인 설명을 제공합니다. 예를 들어, 필요한 경우 '제어 문자'의 개념을 설명하는 데 사용할 수 있습니다.

Even though the notation used is almost the same, there is a big difference between the meaning of lexical and syntactic definitions: a lexical definition operates on the individual characters of the input source, while a syntax definition operates on the stream of tokens generated by the lexical analysis. All uses of BNF in the next chapter (“Lexical Analysis”) are lexical definitions; uses in subsequent chapters are syntactic definitions.

사용되는 표기법은 거의 동일하지만 어휘 정의와 구문 정의의 의미에는 큰 차이가 있습니다. 어휘 정의는 입력 소스의 개별 문자에 대해 작동하는 반면 구문 정의는 어휘 분석에서 생성된 토큰 스트림에 대해 작동합니다. 다음 장("어휘 분석")의 모든 BNF 사용은 어휘 정의입니다. 이후 장에서 사용되는 것은 구문 정의입니다.
