# 2. Using the Python Interpreter
## 2.1. Invoking the Interpreter

1. The Python interpreter is usually installed as /usr/local/bin/python3.13 on those machines where it is available; putting /usr/local/bin in your Unix shell's search path makes it possible to start it by typing the command:

파이썬 인터프리터는 일반적으로 사용 가능한 기기에서 /usr/local/bin/python3.13으로 설치됩니다. 유닉스 셸의 검색 경로에 /usr/local/bin을 추가하면 다음 명령을 입력하여 시작할 수 있습니다:

```
python3.13
```

2. to the shell. [1] Since the choice of the directory where the interpreter lives is an installation option, other places are possible; check with your local Python guru or system administrator. (E.g., /usr/local/python is a popular alternative location.)

셸에 입력하면 됩니다. [1] 인터프리터가 위치한 디렉토리는 설치 옵션이므로 다른 위치도 가능합니다. 로컬 파이썬 전문가나 시스템 관리자에게 문의하세요. (예: /usr/local/python은 인기 있는 대체 위치입니다.)

3. On Windows machines where you have installed Python from the Microsoft Store, the python3.13 command will be available. If you have the py.exe launcher installed, you can use the py command. See Excursus: Setting environment variables for other ways to launch Python.

Microsoft Store에서 파이썬을 설치한 Windows 기기에서는 python3.13 명령을 사용할 수 있습니다. py.exe 실행기가 설치되어 있다면 py 명령을 사용할 수 있습니다. 파이썬을 실행하는 다른 방법에 대해서는 '보충 설명: 환경 변수 설정'을 참조하세요.

4. Typing an end-of-file character (Control-D on Unix, Control-Z on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn't work, you can exit the interpreter by typing the following command: quit().
주 프롬프트에서 파일 끝(EOF) 문자(Unix에서는 Control-D, Windows에서는 Control-Z)를 입력하면 인터프리터가 0 상태로 종료됩니다. 이 방법이 작동하지 않으면 quit() 명령을 입력하여 인터프리터를 종료할 수 있습니다.

5. The interpreter's line-editing features include interactive editing, history substitution and code completion on systems that support the GNU Readline library. Perhaps the quickest check to see whether command line editing is supported is typing Control-P to the first Python prompt you get. If it beeps, you have command line editing; see Appendix Interactive Input Editing and History Substitution for an introduction to the keys. If nothing appears to happen, or if ^P is echoed, command line editing isn't available; you'll only be able to use backspace to remove characters from the current line.

인터프리터의 행 편집 기능에는 대화식 편집, 히스토리 대체, GNU Readline 라이브러리를 지원하는 시스템에서의 코드 완성이 포함됩니다. 명령줄 편집 지원 여부를 가장 빠르게 확인하는 방법은 처음 파이썬 프롬프트에서 Control-P를 입력하는 것입니다. 삐 소리가 나면 명령줄 편집이 지원됩니다. 키에 대한 소개는 부록 '대화형 입력 편집 및 히스토리 대체'를 참조하세요. 아무 일도 일어나지 않거나 ^P가 화면에 표시되면 명령줄 편집을 사용할 수 없습니다. 이 경우 백스페이스만 사용하여 현재 줄에서 문자를 제거할 수 있습니다.

6. The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.

인터프리터는 유닉스 셸과 비슷하게 작동합니다. 표준 입력이 tty 장치에 연결된 상태로 호출되면 대화형으로 명령을 읽고 실행합니다. 파일 이름 인수나 표준 입력으로 파일이 제공되면 해당 파일에서 스크립트를 읽고 실행합니다.

7. A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell's -c option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote command in its entirety.

인터프리터를 시작하는 두 번째 방법은 python -c command [arg] ... 입니다. 이 방법은 셸의 -c 옵션과 유사하게 command에 있는 명령문을 실행합니다. 파이썬 명령문에는 공백이나 셸에서 특별한 의미를 갖는 다른 문자가 포함되는 경우가 많으므로, 일반적으로 command 전체를 따옴표로 묶는 것이 좋습니다.

8. Some Python modules are also useful as scripts. These can be invoked using python -m module [arg] ..., which executes the source file for module as if you had spelled out its full name on the command line.

일부 파이썬 모듈은 스크립트로도 유용합니다. 이러한 모듈은 python -m module [arg] ... 를 사용하여 호출할 수 있습니다. 이 방법은 명령줄에서 모듈의 전체 이름을 입력한 것처럼 모듈의 소스 파일을 실행합니다.

9. When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing -i before the script.

스크립트 파일을 사용할 때 스크립트를 실행한 후 대화형 모드로 들어가는 것이 유용할 때가 있습니다. 이는 스크립트 전에 -i를 전달하여 수행할 수 있습니다.

10. All command line options are described in Command line and environment.

모든 명령줄 옵션은 '명령줄 및 환경'에 설명되어 있습니다.

## 2.1.1. Argument Passing

11. When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the argv variable in the sys module. You can access this list by executing import sys. The length of the list is at least one; when no script and no arguments are given, sys.argv[0] is an empty string. When the script name is given as '-' (meaning standard input), sys.argv[0] is set to '-'. When -c command is used, sys.argv[0] is set to '-c'. When -m module is used, sys.argv[0] is set to the full name of the located module. Options found after -c command or -m module are not consumed by the Python interpreter's option processing but left in sys.argv for the command or module to handle.

인터프리터가 인식하면 스크립트 이름과 그 이후의 추가 인수는 문자열 목록으로 변환되어 sys 모듈의 argv 변수에 할당됩니다. import sys를 실행하여 이 목록에 접근할 수 있습니다. 목록의 길이는 최소 1입니다. 스크립트와 인수가 제공되지 않으면 sys.argv[0]은 빈 문자열입니다. 스크립트 이름이 '-'(표준 입력을 의미)로 주어지면 sys.argv[0]은 '-'로 설정됩니다. -c command가 사용되면 sys.argv[0]은 '-c'로 설정됩니다. -m module이 사용되면 sys.argv[0]은 찾은 모듈의 전체 이름으로 설정됩니다. -c command나 -m module 뒤에 있는 옵션은 파이썬 인터프리터의 옵션 처리에 의해 소비되지 않고 명령이나 모듈이 처리할 수 있도록 sys.argv에 남아 있습니다.

## 2.1.2. Interactive Mode

12. When commands are read from a tty, the interpreter is said to be in interactive mode. In this mode it prompts for the next command with the primary prompt, usually three greater-than signs (>>>); for continuation lines it prompts with the secondary prompt, by default three dots (...). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt:

명령이 tty에서 읽혀질 때, 인터프리터는 대화형 모드에 있다고 합니다. 이 모드에서는 주 프롬프트로 다음 명령을 입력하라는 메시지가 표시되는데, 보통 꺾쇠 괄호 세 개(>>>)로 표시됩니다. 연속 줄에서는 보조 프롬프트로 기본적으로 점 세 개(...)가 표시됩니다. 인터프리터는 첫 프롬프트를 출력하기 전에 버전 번호와 저작권 공지를 명시한 환영 메시지를 출력합니다:

```
python3.13
Python 3.13 (default, April 4 2023, 09:25:04)
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

13. Continuation lines are needed when entering a multi-line construct. As an example, take a look at this if statement:

여러 줄 구성을 입력할 때는 연속 줄이 필요합니다. 예를 들어, 다음 if 문을 살펴보세요:

```
>>>
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

Be careful not to fall off!
```

14. For more on interactive mode, see Interactive Mode.

대화형 모드에 대한 자세한 내용은 '대화형 모드'를 참조하세요.

## 2.2. The Interpreter and Its Environment

## 2.2.1. Source Code Encoding

15. By default, Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.

기본적으로 파이썬 소스 파일은 UTF-8로 인코딩된 것으로 처리됩니다. 이 인코딩에서는 전 세계 대부분 언어의 문자를 문자열 리터럴, 식별자 및 주석에 동시에 사용할 수 있습니다. 다만, 표준 라이브러리는 식별자에 ASCII 문자만 사용하며, 이는 모든 이식 가능한 코드가 따라야 하는 관례입니다. 이러한 모든 문자를 올바르게 표시하려면 편집기가 해당 파일이 UTF-8임을 인식하고 파일의 모든 문자를 지원하는 글꼴을 사용해야 합니다.

16. To declare an encoding other than the default one, a special comment line should be added as the first line of the file. The syntax is as follows:

기본값 이외의 인코딩을 선언하려면 파일의 첫 번째 줄로 특별한 주석 줄을 추가해야 합니다. 구문은 다음과 같습니다:

```
# -*- coding: encoding -*-
```

17. where encoding is one of the valid codecs supported by Python.

여기서 encoding은 파이썬이 지원하는 유효한 코덱 중 하나입니다.

18. For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:

예를 들어, Windows-1252 인코딩을 사용한다고 선언하려면 소스 코드 파일의 첫 번째 줄은 다음과 같아야 합니다:

```
# -*- coding: cp1252 -*-
```

19. One exception to the first line rule is when the source code starts with a UNIX "shebang" line. In this case, the encoding declaration should be added as the second line of the file. For example:

첫 번째 줄 규칙의 한 가지 예외는 소스 코드가 UNIX "셔뱅" 줄로 시작하는 경우입니다. 이 경우 인코딩 선언은 파일의 두 번째 줄로 추가되어야 합니다. 예:

```
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```

**Footnotes**

[1] 유닉스에서는 파이썬 3.x 인터프리터가 기본적으로 python이라는 이름의 실행 파일로 설치되지 않습니다. 이는 동시에 설치된 파이썬 2.x 실행 파일과 충돌하지 않도록 하기 위함입니다.
