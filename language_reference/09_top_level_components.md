9. Top-level components
========================

The Python interpreter can get its input from a number of sources: from a script passed to it as standard input or as program argument, typed in interactively, from a module source file, etc. This chapter gives the syntax used in these cases.

9. 최상위 컴포넌트
========================

파이썬 인터프리터는 다양한 소스에서 입력을 받을 수 있습니다: 표준 입력이나 프로그램 인수로 전달된 스크립트, 대화식으로 입력된 내용, 모듈 소스 파일 등이 있습니다. 이 장에서는 이러한 경우에 사용되는 구문을 설명합니다.

9.1. Complete Python programs
-----------------------------

While a language specification need not prescribe how the language interpreter is invoked, it is useful to have a notion of a complete Python program. A complete Python program is executed in a minimally initialized environment: all built-in and standard modules are available, but none have been initialized, except for sys (various system services), builtins (built-in functions, exceptions and None) and __main__. The latter is used to provide the local and global namespace for execution of the complete program.

9.1. 완전한 파이썬 프로그램
-----------------------------

언어 명세는 언어 인터프리터가 어떻게 호출되는지 규정할 필요는 없지만, 완전한 파이썬 프로그램의 개념을 갖는 것이 유용합니다. 완전한 파이썬 프로그램은 최소한으로 초기화된 환경에서 실행됩니다: 모든 내장 및 표준 모듈이 사용 가능하지만, sys(다양한 시스템 서비스), builtins(내장 함수, 예외 및 None) 및 __main__을 제외하고는 어떤 것도 초기화되지 않습니다. 후자는 완전한 프로그램의 실행을 위한 지역 및 전역 네임스페이스를 제공하는 데 사용됩니다.

The syntax for a complete Python program is that for file input, described in the next section.

완전한 파이썬 프로그램의 구문은 다음 섹션에서 설명하는 파일 입력에 대한 것입니다.

The interpreter may also be invoked in interactive mode; in this case, it does not read and execute a complete program but reads and executes one statement (possibly compound) at a time. The initial environment is identical to that of a complete program; each statement is executed in the namespace of __main__.

인터프리터는 대화형 모드로도 호출될 수 있습니다. 이 경우, 완전한 프로그램을 읽고 실행하는 것이 아니라 한 번에 하나의 문장(복합일 수도 있음)을 읽고 실행합니다. 초기 환경은 완전한 프로그램의 환경과 동일합니다. 각 문장은 __main__의 네임스페이스에서 실행됩니다.

A complete program can be passed to the interpreter in three forms: with the -c string command line option, as a file passed as the first command line argument, or as standard input. If the file or standard input is a tty device, the interpreter enters interactive mode; otherwise, it executes the file as a complete program.

완전한 프로그램은 세 가지 형태로 인터프리터에 전달될 수 있습니다: -c 문자열 명령줄 옵션을 사용하여, 첫 번째 명령줄 인수로 전달된 파일로, 또는 표준 입력으로. 파일이나 표준 입력이 tty 장치인 경우, 인터프리터는 대화형 모드로 진입합니다. 그렇지 않으면 파일을 완전한 프로그램으로 실행합니다.

9.2. File input
--------------

All input read from non-interactive files has the same form:

9.2. 파일 입력
--------------

비대화형 파일에서 읽는 모든 입력은 동일한 형태를 갖습니다:

```
file_input ::= (NEWLINE | statement)*
```

This syntax is used in the following situations:

- when parsing a complete Python program (from a file or from a string);
- when parsing a module;
- when parsing a string passed to the exec() function;

이 구문은 다음과 같은 상황에서 사용됩니다:

- 완전한 파이썬 프로그램(파일이나 문자열에서)을 파싱할 때;
- 모듈을 파싱할 때;
- exec() 함수에 전달된 문자열을 파싱할 때;

9.3. Interactive input
---------------------

Input in interactive mode is parsed using the following grammar:

9.3. 대화형 입력
---------------------

대화형 모드의 입력은 다음 문법을 사용하여 파싱됩니다:

```
interactive_input ::= [stmt_list] NEWLINE | compound_stmt NEWLINE
```

Note that a (top-level) compound statement must be followed by a blank line in interactive mode; this is needed to help the parser detect the end of the input.

대화형 모드에서는 (최상위) 복합 문장 다음에 빈 줄이 와야 합니다. 이는 파서가 입력의 끝을 감지하는 데 도움이 됩니다.

9.4. Expression input
-------------------

eval() is used for expression input. It ignores leading whitespace. The string argument to eval() must have the following form:

9.4. 표현식 입력
-------------------

eval()은 표현식 입력에 사용됩니다. 이는 선행 공백을 무시합니다. eval()에 대한 문자열 인수는 다음 형식이어야 합니다:

```
eval_input ::= expression_list NEWLINE*
```
