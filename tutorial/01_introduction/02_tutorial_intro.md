## 1. Whetting Your Appetite

7. If you do much work on computers, eventually you find that there's some task you'd like to automate. For example, you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. Perhaps you'd like to write a small custom database, or a specialized GUI application, or a simple game.

컴퓨터로 많은 작업을 하다 보면, 결국에는 자동화하고 싶은 작업이 생기게 됩니다. 예를 들어, 많은 텍스트 파일에서 검색 및 교체를 수행하거나, 복잡한 방식으로 사진 파일들의 이름을 바꾸고 재배열하고 싶을 수 있습니다. 아마도 작은 사용자 정의 데이터베이스나 특수 GUI 애플리케이션, 또는 간단한 게임을 작성하고 싶을 수도 있습니다.

8. If you're a professional software developer, you may have to work with several C/C++/Java libraries but find the usual write/compile/test/re-compile cycle is too slow. Perhaps you're writing a test suite for such a library and find writing the testing code a tedious task. Or maybe you've written a program that could use an extension language, and you don't want to design and implement a whole new language for your application.

전문 소프트웨어 개발자라면, 여러 C/C++/Java 라이브러리를 사용해야 하지만 일반적인 작성/컴파일/테스트/재컴파일 주기가 너무 느리다고 느낄 수 있습니다. 아마도 이러한 라이브러리용 테스트 스위트를 작성하면서 테스트 코드 작성이 지루한 작업이라고 느낄 수 있습니다. 또는 확장 언어를 사용할 수 있는 프로그램을 작성했지만, 애플리케이션을 위한 완전히 새로운 언어를 설계하고 구현하고 싶지 않을 수도 있습니다.

9. Python is just the language for you.

파이썬은 바로 당신을 위한 언어입니다.

10. You could write a Unix shell script or Windows batch files for some of these tasks, but shell scripts are best at moving around files and changing text data, not well-suited for GUI applications or games. You could write a C/C++/Java program, but it can take a lot of development time to get even a first-draft program. Python is simpler to use, available on Windows, macOS, and Unix operating systems, and will help you get the job done more quickly.

이러한 작업 중 일부는 유닉스 셸 스크립트나 윈도우 배치 파일로 작성할 수 있지만, 셸 스크립트는 파일을 이동하고 텍스트 데이터를 변경하는 데 가장 적합하며 GUI 애플리케이션이나 게임에는 적합하지 않습니다. C/C++/Java 프로그램을 작성할 수도 있지만, 초안 프로그램을 만드는 데에도 많은 개발 시간이 소요될 수 있습니다. 파이썬은 사용하기 더 간단하고, Windows, macOS 및 Unix 운영 체제에서 사용 가능하며, 더 빠르게 작업을 완료하는 데 도움이 됩니다.

11. Python is simple to use, but it is a real programming language, offering much more structure and support for large programs than shell scripts or batch files can offer. On the other hand, Python also offers much more error checking than C, and, being a very-high-level language, it has high-level data types built in, such as flexible arrays and dictionaries. Because of its more general data types Python is applicable to a much larger problem domain than Awk or even Perl, yet many things are at least as easy in Python as in those languages.

파이썬은 사용하기 간단하지만 실제 프로그래밍 언어로, 셸 스크립트나 배치 파일이 제공할 수 있는 것보다 대규모 프로그램에 대한 훨씬 더 많은 구조와 지원을 제공합니다. 한편, 파이썬은 C보다 훨씬 더 많은 오류 검사를 제공하며, 매우 고수준 언어이기 때문에 유연한 배열과 사전과 같은 고수준 데이터 타입이 내장되어 있습니다. 더 일반적인 데이터 타입 때문에 파이썬은 Awk나 심지어 Perl보다 훨씬 더 넓은 문제 영역에 적용할 수 있으며, 많은 것들이 이러한 언어들에서처럼 파이썬에서도 최소한 동일하게 쉽습니다.

12. Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs — or as examples to start learning to program in Python. Some of these modules provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits like Tk.

파이썬을 사용하면 프로그램을 다른 파이썬 프로그램에서 재사용할 수 있는 모듈로 분할할 수 있습니다. 파이썬은 프로그램의 기초로 사용하거나 파이썬 프로그래밍을 배우기 시작하는 예제로 사용할 수 있는 많은 표준 모듈 컬렉션과 함께 제공됩니다. 이러한 모듈 중 일부는 파일 I/O, 시스템 호출, 소켓, 심지어 Tk와 같은 그래픽 사용자 인터페이스 툴킷에 대한 인터페이스와 같은 기능을 제공합니다.

Python is an interpreted language, which can save you considerable time during program development because no compilation and linking is necessary. The interpreter can be used interactively, which makes it easy to experiment with features of the language, to write throw-away programs, or to test functions during bottom-up program development. It is also a handy desk calculator.

파이썬은 인터프리터 언어로, 컴파일과 링크가 필요 없기 때문에 프로그램 개발 중에 상당한 시간을 절약할 수 있습니다. 인터프리터는 대화식으로 사용할 수 있어, 언어 기능을 실험하거나, 일회용 프로그램을 작성하거나, 상향식 프로그램 개발 중에 함수를 테스트하기 쉽습니다. 또한 편리한 책상 계산기로도 사용됩니다.

14. Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

    - the high-level data types allow you to express complex operations in a single statement;
    - statement grouping is done by indentation instead of beginning and ending brackets;
    - no variable or argument declarations are necessary.

파이썬은 프로그램을 간결하고 읽기 쉽게 작성할 수 있게 해줍니다. 파이썬으로 작성된 프로그램은 일반적으로 다음과 같은 여러 가지 이유로 동등한 C, C++ 또는 Java 프로그램보다 훨씬 짧습니다:

    - 고수준 데이터 타입을 사용하면 복잡한 연산을 단일 문장으로 표현할 수 있습니다;
    - 문장 그룹화는 시작 및 종료 괄호 대신 들여쓰기로 수행됩니다;
    - 변수나 인수 선언이 필요하지 않습니다.

15. Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may only be available in binary form (such as a vendor-specific graphics library). Once you are really hooked, you can link the Python interpreter into an application written in C and use it as an extension or command language for that application.

파이썬은 확장 가능합니다: C로 프로그래밍하는 방법을 알고 있다면 최대 속도로 중요한 작업을 수행하거나 파이썬 프로그램을 바이너리 형태로만 제공될 수 있는 라이브러리(예: 벤더별 그래픽 라이브러리)에 연결하기 위해 새로운 내장 함수나 모듈을 인터프리터에 쉽게 추가할 수 있습니다. 정말 매료되면 C로 작성된 애플리케이션에 파이썬 인터프리터를 연결하여 해당 애플리케이션의 확장이나 명령어 언어로 사용할 수 있습니다.

16. By the way, the language is named after the BBC show "Monty Python's Flying Circus" and has nothing to do with reptiles. Making references to Monty Python skits in documentation is not only allowed, it is encouraged!

참고로, 이 언어는 BBC 쇼 "몬티 파이썬의 날아다니는 서커스"에서 이름을 따온 것이며 파충류와는 아무 관련이 없습니다. 문서에서 몬티 파이썬 콩트를 언급하는 것은 허용될 뿐만 아니라 권장됩니다!

17. Now that you are all excited about Python, you'll want to examine it in some more detail. Since the best way to learn a language is to use it, the tutorial invites you to play with the Python interpreter as you read.

이제 파이썬에 대해 모두 흥미를 느꼈으니, 더 자세히 살펴보고 싶을 것입니다. 언어를 배우는 가장 좋은 방법은 그것을 사용하는 것이므로, 이 튜토리얼은 읽으면서 파이썬 인터프리터를 가지고 놀아보도록 초대합니다.

18. In the next chapter, the mechanics of using the interpreter are explained. This is rather mundane information, but essential for trying out the examples shown later.

다음 장에서는 인터프리터 사용 방법에 대해 설명합니다. 이는 다소 평범한 정보이지만, 나중에 보여질 예제들을 시도해 보기 위해 필수적입니다.

19. The rest of the tutorial introduces various features of the Python language and system through examples, beginning with simple expressions, statements and data types, through functions and modules, and finally touching upon advanced concepts like exceptions and user-defined classes.

튜토리얼의 나머지 부분에서는 간단한 표현식, 문장 및 데이터 타입부터 시작하여 함수와 모듈을 거쳐 마지막으로 예외 및 사용자 정의 클래스와 같은 고급 개념까지 예제를 통해 파이썬 언어 및 시스템의 다양한 기능을 소개합니다.
