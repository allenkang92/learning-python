# Python Logging HOWTO

# Python 로깅 사용 가이드

## Introduction

The `logging` module in Python's standard library provides a flexible framework for emitting log messages from Python programs. It's a powerful tool that allows developers to track events that happen when software runs, which is crucial for debugging, monitoring, and maintaining applications.

This guide will walk you through the basics of using the logging module, configuring it effectively, and adopting best practices to make your code more maintainable and your debugging sessions more productive.

## 소개

Python 표준 라이브러리의 `logging` 모듈은 Python 프로그램에서 로그 메시지를 출력하기 위한 유연한 프레임워크를 제공합니다. 이는 소프트웨어 실행 시 발생하는 이벤트를 추적할 수 있게 해주는 강력한 도구로, 디버깅, 모니터링 및 애플리케이션 유지 관리에 중요합니다.

이 가이드는 로깅 모듈 사용의 기본, 효과적인 구성 방법, 그리고 코드를 더 유지보수하기 쉽게 만들고 디버깅 세션을 더 생산적으로 만들기 위한 모범 사례를 설명합니다.

## Why Use Logging?

You might wonder why you should use the logging module instead of simply using `print()` statements. Here are a few key advantages:

1. **Categorization**: Log messages can be categorized by their severity level.
2. **Flexibility**: Logging output can be directed to different destinations (console, files, network, etc.)
3. **Configurability**: The logging behavior can be configured without modifying the application code.
4. **Standardization**: It provides a standardized way to produce log messages across your application.
5. **Context**: Log messages can include contextual information like timestamps, line numbers, etc.

## 왜 로깅을 사용해야 하나요?

단순히 `print()` 문을 사용하는 대신 로깅 모듈을 사용해야 하는 이유가 궁금할 수 있습니다. 다음은 몇 가지 주요 장점입니다:

1. **분류**: 로그 메시지는 심각도 수준에 따라 분류될 수 있습니다.
2. **유연성**: 로깅 출력은 다양한 대상(콘솔, 파일, 네트워크 등)으로 전달될 수 있습니다.
3. **구성 가능성**: 애플리케이션 코드를 수정하지 않고도 로깅 동작을 구성할 수 있습니다.
4. **표준화**: 애플리케이션 전체에서 로그 메시지를 생성하는 표준화된 방법을 제공합니다.
5. **컨텍스트**: 로그 메시지에는 타임스탬프, 라인 번호 등의 컨텍스트 정보가 포함될 수 있습니다.

## Basic Logging

Let's start with a simple example:

```python
import logging

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# Log some messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

When you run this code, the messages at INFO level and above will be written to the file `app.log`. The DEBUG message won't be recorded because we set the log level to INFO.

## 기본 로깅

간단한 예제로 시작해 보겠습니다:

```python
import logging

# 로깅 시스템 구성
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

# 로그 메시지 생성
logging.debug('디버그 메시지입니다')
logging.info('정보 메시지입니다')
logging.warning('경고 메시지입니다')
logging.error('오류 메시지입니다')
logging.critical('심각한 메시지입니다')
```

이 코드를 실행하면 INFO 레벨 이상의 메시지가 `app.log` 파일에 기록됩니다. DEBUG 메시지는 로그 레벨을 INFO로 설정했기 때문에 기록되지 않습니다.

## Log Levels

The logging module provides several levels to categorize the severity of log messages:

| Level | Numeric Value | Description |
|-------|--------------|-------------|
| DEBUG | 10 | Detailed information, typically only valuable when diagnosing problems |
| INFO | 20 | Confirmation that things are working as expected |
| WARNING | 30 | Indication that something unexpected happened, or may happen in the near future |
| ERROR | 40 | Due to a more serious problem, the software has not been able to perform a function |
| CRITICAL | 50 | A very serious error, indicating that the program itself may be unable to continue running |

You can set the log level when configuring the logging system, which will determine which messages get recorded:

```python
# Only show WARNING and above
logging.basicConfig(level=logging.WARNING)

# This will be ignored
logging.info("This won't be printed")

# These will be shown
logging.warning("This will be printed")
logging.error("So will this")
```

## 로그 레벨

로깅 모듈은 로그 메시지의 심각도를 분류하기 위한 여러 레벨을 제공합니다:

| 레벨 | 숫자 값 | 설명 |
|-------|--------------|-------------|
| DEBUG | 10 | 문제 진단에 주로 유용한 상세 정보 |
| INFO | 20 | 예상대로 작동하고 있다는 확인 |
| WARNING | 30 | 예상치 못한 일이 발생했거나 가까운 미래에 발생할 수 있다는 표시 |
| ERROR | 40 | 더 심각한 문제로 인해 소프트웨어가 기능을 수행할 수 없음 |
| CRITICAL | 50 | 프로그램 자체가 실행을 계속할 수 없을 정도로 매우 심각한 오류 |

로깅 시스템을 구성할 때 로그 레벨을 설정할 수 있으며, 이는 어떤 메시지가 기록될지 결정합니다:

```python
# WARNING 이상만 표시
logging.basicConfig(level=logging.WARNING)

# 이것은 무시됩니다
logging.info("이것은 출력되지 않습니다")

# 이것들은 표시됩니다
logging.warning("이것은 출력됩니다")
logging.error("이것도 마찬가지입니다")
```

## Configuring Logging

The `basicConfig()` function provides a simple way to configure the root logger. Here are some common configuration options:

```python
logging.basicConfig(
    level=logging.INFO,  # Set the log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Format of log messages
    datefmt='%Y-%m-%d %H:%M:%S',  # Format of the timestamp
    filename='app.log',  # Send log messages to a file
    filemode='w',  # 'w' to overwrite, 'a' to append
    stream=sys.stdout  # Used instead of filename to log to stdout
)
```

Note that `basicConfig()` can only be called once in your application. If the root logger already has handlers configured, subsequent calls will have no effect.

## 로깅 구성

`basicConfig()` 함수는 루트 로거를 구성하는 간단한 방법을 제공합니다. 다음은 몇 가지 일반적인 구성 옵션입니다:

```python
logging.basicConfig(
    level=logging.INFO,  # 로그 레벨 설정
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # 로그 메시지 형식
    datefmt='%Y-%m-%d %H:%M:%S',  # 타임스탬프 형식
    filename='app.log',  # 로그 메시지를 파일로 보냄
    filemode='w',  # 'w'는 덮어쓰기, 'a'는 추가
    stream=sys.stdout  # filename 대신 사용하여 stdout으로 로깅
)
```

`basicConfig()`는 애플리케이션에서 한 번만 호출할 수 있습니다. 루트 로거에 이미 핸들러가 구성되어 있으면 이후 호출은 효과가 없습니다.

## Using Loggers

In a larger application, it's usually better to use named loggers instead of the root logger:

```python
# Create a logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# Create a handler
handler = logging.FileHandler('my_app.log')
handler.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Log some messages
logger.info('Starting my_app')
logger.warning('Something might be wrong')
```

Using named loggers gives you more control over the logging behavior of different parts of your application.

## 로거 사용하기

대규모 애플리케이션에서는 일반적으로 루트 로거 대신 명명된 로거를 사용하는 것이
좋습니다:

```python
# 로거 생성
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# 핸들러 생성
handler = logging.FileHandler('my_app.log')
handler.setLevel(logging.INFO)

# 포맷터 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 로거에 핸들러 추가
logger.addHandler(handler)

# 로그 메시지 생성
logger.info('my_app 시작 중')
logger.warning('문제가 있을 수 있습니다')
```

명명된 로거를 사용하면 애플리케이션의 다양한 부분에 대한 로깅 동작을 더 잘 제어할 수 있습니다.

## Log Handlers

Handlers send the log records to the appropriate destination. The logging module provides several built-in handler classes:

1. **StreamHandler**: Sends log messages to streams such as `sys.stdout`, `sys.stderr` or any file-like object.
2. **FileHandler**: Sends log messages to a disk file.
3. **RotatingFileHandler**: Sends log messages to a disk file, rotating the log file at certain times or sizes.
4. **TimedRotatingFileHandler**: Similar to RotatingFileHandler, but rotating happens based on time.
5. **SocketHandler**: Sends log messages to a network socket.
6. **SMTPHandler**: Sends log messages to an email address via SMTP.
7. **SysLogHandler**: Sends log messages to a Unix syslog daemon.
8. **NTEventLogHandler**: Sends log messages to a Windows NT/2000/XP event log.
9. **MemoryHandler**: Buffers log records in memory.
10. **HTTPHandler**: Sends log messages to an HTTP server using either GET or POST.

You can use multiple handlers to send log messages to different destinations:

```python
# Create logger
logger = logging.getLogger('my_app')

# File handler for all logs
file_handler = logging.FileHandler('all_logs.log')
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# Stream handler for error and above
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
logger.addHandler(stream_handler)

# Now log messages will go to the appropriate handlers
logger.debug('Debug message - goes only to file')
logger.error('Error message - goes to both file and console')
```

## 로그 핸들러

핸들러는 로그 레코드를 적절한 대상으로 전송합니다. 로깅 모듈은 여러 내장 핸들러 클래스를 제공합니다:

1. **StreamHandler**: 로그 메시지를 `sys.stdout`, `sys.stderr` 또는 파일과 유사한 객체와 같은 스트림으로 보냅니다.
2. **FileHandler**: 로그 메시지를 디스크 파일로 보냅니다.
3. **RotatingFileHandler**: 로그 메시지를 디스크 파일로 보내고, 특정 시간이나 크기에 도달하면 로그 파일을 회전시킵니다.
4. **TimedRotatingFileHandler**: RotatingFileHandler와 유사하지만, 회전이 시간을 기준으로 발생합니다.
5. **SocketHandler**: 로그 메시지를 네트워크 소켓으로 보냅니다.
6. **SMTPHandler**: SMTP를 통해 로그 메시지를 이메일 주소로 보냅니다.
7. **SysLogHandler**: 로그 메시지를 Unix syslog 데몬으로 보냅니다.
8. **NTEventLogHandler**: 로그 메시지를 Windows NT/2000/XP 이벤트 로그로 보냅니다.
9. **MemoryHandler**: 로그 레코드를 메모리에 버퍼링합니다.
10. **HTTPHandler**: GET 또는 POST를 사용하여 로그 메시지를 HTTP 서버로 보냅니다.

여러 핸들러를 사용하여 로그 메시지를 다양한 대상으로 보낼 수 있습니다:

```python
# 로거 생성
logger = logging.getLogger('my_app')

# 모든 로그를 위한 파일 핸들러
file_handler = logging.FileHandler('all_logs.log')
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# 오류 이상을 위한 스트림 핸들러
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
logger.addHandler(stream_handler)

# 이제 로그 메시지는 적절한 핸들러로 전송됩니다
logger.debug('디버그 메시지 - 파일에만 기록됩니다')
logger.error('오류 메시지 - 파일과 콘솔 모두에 기록됩니다')
```

## Log Formatters

Formatters specify the layout of log messages. They use a string with certain placeholders:

```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

Common placeholders include:

| Attribute name | Format | Description |
|----------------|--------|-------------|
| asctime | %(asctime)s | Human-readable time |
| created | %(created)f | Time when the LogRecord was created (as returned by time.time()) |
| filename | %(filename)s | Filename portion of pathname |
| funcName | %(funcName)s | Name of function containing the logging call |
| levelname | %(levelname)s | Text logging level ('DEBUG', 'INFO', etc.) |
| levelno | %(levelno)s | Numeric logging level (10, 20, etc.) |
| lineno | %(lineno)d | Source line number where the logging call was issued |
| message | %(message)s | The logged message |
| module | %(module)s | Module (name portion of filename) |
| name | %(name)s | Name of the logger |
| pathname | %(pathname)s | Full pathname of the source file |
| process | %(process)d | Process ID |
| processName | %(processName)s | Process name |
| thread | %(thread)d | Thread ID |
| threadName | %(threadName)s | Thread name |

You can assign different formatters to different handlers:

```python
# Create formatters
simple_formatter = logging.Formatter('%(levelname)s - %(message)s')
detailed_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Apply formatters to handlers
console_handler.setFormatter(simple_formatter)
file_handler.setFormatter(detailed_formatter)
```

## 로그 포맷터

포맷터는 로그 메시지의 레이아웃을 지정합니다. 특정 자리 표시자가 있는 문자열을 사용합니다:

```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

일반적인 자리 표시자는 다음과 같습니다:

| 속성 이름 | 형식 | 설명 |
|----------------|--------|-------------|
| asctime | %(asctime)s | 사람이 읽을 수 있는 시간 |
| created | %(created)f | LogRecord가 생성된 시간(time.time()이 반환한 값) |
| filename | %(filename)s | 경로 이름의 파일 이름 부분 |
| funcName | %(funcName)s | 로깅 호출을 포함하는 함수 이름 |
| levelname | %(levelname)s | 텍스트 로깅 레벨('DEBUG', 'INFO' 등) |
| levelno | %(levelno)s | 숫자 로깅 레벨(10, 20 등) |
| lineno | %(lineno)d | 로깅 호출이 발생한 소스 라인 번호 |
| message | %(message)s | 기록된 메시지 |
| module | %(module)s | 모듈(파일 이름의 이름 부분) |
| name | %(name)s | 로거의 이름 |
| pathname | %(pathname)s | 소스 파일의 전체 경로 이름 |
| process | %(process)d | 프로세스 ID |
| processName | %(processName)s | 프로세스 이름 |
| thread | %(thread)d | 스레드 ID |
| threadName | %(threadName)s | 스레드 이름 |

다른 핸들러에 다른 포맷터를 할당할 수 있습니다:

```python
# 포맷터 생성
simple_formatter = logging.Formatter('%(levelname)s - %(message)s')
detailed_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 핸들러에 포맷터 적용
console_handler.setFormatter(simple_formatter)
file_handler.setFormatter(detailed_formatter)
```

## Logger Hierarchy

Loggers are organized in a hierarchical namespace. For example, a logger named 'parent' is the parent of a logger named 'parent.child'. This allows for effective control over logging behaviors in different parts of your application.

```python
# Create parent logger
parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.ERROR)

# Create child logger
child_logger = logging.getLogger('parent.child')
child_logger.setLevel(logging.INFO)

# Create handler and attach to parent
handler = logging.StreamHandler()
parent_logger.addHandler(handler)

# Log messages
parent_logger.info('This will not be logged - level too low')
parent_logger.error('This will be logged')

child_logger.info('This will be logged - child has INFO level')
child_logger.error('This will be logged too - through parent handler')
```

Loggers pass log messages up to their parent loggers. This "propagation" can be turned off by setting the `propagate` attribute to `False`:

```python
child_logger.propagate = False
child_logger.error('This will NOT be logged by the parent handler')
```

## 로거 계층 구조

로거는 계층적 네임스페이스로 구성됩니다. 예를 들어, 'parent'라는 이름의 로거는 'parent.child'라는 이름의 로거의 부모입니다. 이를 통해 애플리케이션의 다양한 부분에서 로깅 동작을 효과적으로 제어할 수 있습니다.

```python
# 부모 로거 생성
parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.ERROR)

# 자식 로거 생성
child_logger = logging.getLogger('parent.child')
child_logger.setLevel(logging.INFO)

# 핸들러 생성 및 부모에 연결
handler = logging.StreamHandler()
parent_logger.addHandler(handler)

# 로그 메시지
parent_logger.info('이것은 기록되지 않음 - 레벨이 너무 낮음')
parent_logger.error('이것은 기록됨')

child_logger.info('이것은 기록됨 - 자식은 INFO 레벨임')
child_logger.error('이것도 기록됨 - 부모 핸들러를 통해')
```

로거는 로그 메시지를 부모 로거로 전달합니다. 이 "전파"는 `propagate` 속성을 `False`로 설정하여 끌 수 있습니다:

```python
child_logger.propagate = False
child_logger.error('이것은 부모 핸들러에 의해 기록되지 않음')
```

## Configuration Using a File

For more complex applications, it's often best to configure logging using a configuration file:

```python
import logging
import logging.config

# Load the logging configuration from a file
logging.config.fileConfig('logging.conf')

# Get a logger
logger = logging.getLogger('root')
logger.debug('Debug message')
```

A sample configuration file (`logging.conf`) might look like:

```ini
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=fileHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('app.log', 'w')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levellevel)s - %(message)s
datefmt=
```

You can also use a dictionary for configuration:

```python
import logging
import logging.config

config_dict = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'app.log',
            'mode': 'w'
        }
    },
    'loggers': {
        '': {  # Root logger
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(config_dict)
logger = logging.getLogger()
logger.info('Logging configured using a dictionary')
```

## 파일을 사용한 구성

더 복잡한 애플리케이션의 경우, 구성 파일을 사용하여 로깅을 구성하는 것이 가장 좋습니다:

```python
import logging
import logging.config

# 파일에서 로깅 구성 로드
logging.config.fileConfig('logging.conf')

# 로거 가져오기
logger = logging.getLogger('root')
logger.debug('디버그 메시지')
```

샘플 구성 파일(`logging.conf`)은 다음과 같을 수 있습니다:

```ini
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=fileHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('app.log', 'w')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

구성에 사전을 사용할 수도 있습니다:

```python
import logging
import logging.config

config_dict = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'app.log',
            'mode': 'w'
        }
    },
    'loggers': {
        '': {  # 루트 로거
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(config_dict)
logger = logging.getLogger()
logger.info('사전을 사용하여 로깅 구성됨')
```

## Capturing Stack Traces

The logging module can automatically include stack trace information when logging exceptions:

```python
try:
    # Some code that might raise an exception
    x = 1 / 0
except Exception as e:
    # The exc_info=True parameter captures the stack trace
    logging.error("An error occurred", exc_info=True)

# Or more simply
try:
    x = 1 / 0
except Exception:
    logging.exception("An error occurred")  # This automatically adds exc_info=True
```

## 스택 트레이스 캡처

로깅 모듈은 예외를 로깅할 때 자동으로 스택 트레이스 정보를 포함할 수 있습니다:

```python
try:
    # 예외를 발생시킬 수 있는 코드
    x = 1 / 0
except Exception as e:
    # exc_info=True 매개변수는 스택 트레이스를 캡처합니다
    logging.error("오류가 발생했습니다", exc_info=True)

# 또는 더 간단하게
try:
    x = 1 / 0
except Exception:
    logging.exception("오류가 발생했습니다")  # 이것은 자동으로 exc_info=True를 추가합니다
```

## Best Practices

Here are some best practices for using the logging module effectively:

1. **Use the appropriate log level**: Reserve DEBUG for detailed diagnostic information, INFO for general information, WARNING for unexpected events, ERROR for errors that prevent normal function, and CRITICAL for very severe errors.

2. **Use named loggers**: Create a logger for each module or component of your application. This provides better control and organization of logs.

3. **Configure logging early**: Configure logging at the start of your application, before any loggers are created.

4. **Use structured logging**: Consider using a structured logging format like JSON for complex applications, which makes logs easier to parse and analyze.

5. **Use context information**: Include context that will help in debugging, like request IDs in a web application.

6. **Don't log sensitive information**: Be cautious not to log sensitive data like passwords, credit card numbers, etc.

7. **Handle logging exceptions**: Make sure your application handles exceptions that might be raised by the logging system.

## 모범 사례

다음은 로깅 모듈을 효과적으로 사용하기 위한 몇 가지 모범 사례입니다:

1. **적절한 로그 레벨 사용**: DEBUG는 자세한 진단 정보용, INFO는 일반 정보용, WARNING은 예상치 못한 이벤트용, ERROR는 정상 기능을 방해하는 오류용, CRITICAL은 매우 심각한 오류용으로 예약하세요.

2. **명명된 로거 사용**: 애플리케이션의 각 모듈이나 구성 요소에 대한 로거를 만드세요. 이는 로그의 더 나은 제어와 구성을 제공합니다.

3. **로깅 조기 구성**: 로거가 생성되기 전에 애플리케이션 시작 시 로깅을 구성하세요.

4. **구조화된 로깅 사용**: 복잡한 애플리케이션의 경우 JSON과 같은 구조화된 로깅 형식을 사용하는 것을 고려하세요. 이는 로그를 파싱하고 분석하기 쉽게 만듭니다.

5. **컨텍스트 정보 사용**: 웹 애플리케이션의 요청 ID와 같이 디버깅에 도움이 될 컨텍스트를 포함하세요.

6. **민감한 정보 로깅 금지**: 비밀번호, 신용 카드 번호 등과 같은 민감한 데이터를 로깅하지 않도록 주의하세요.

7. **로깅 예외 처리**: 애플리케이션이 로깅 시스템에 의해 발생할 수 있는 예외를 처리하도록 하세요.

## Example: Logging in a Flask Application

Here's an example of configuring logging in a Flask web application:

```python
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request

app = Flask(__name__)

# Configure logging
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('App startup')

@app.route('/')
def index():
    app.logger.info('Index page requested')
    return "Hello, World!"

@app.route('/error')
def error():
    app.logger.error('Error route triggered')
    return "Error page", 500

@app.before_request
def log_request_info():
    app.logger.info('Request: %s %s', request.method, request.path)

if __name__ == '__main__':
    app.run(debug=True)
```

## 예시: Flask 애플리케이션에서의 로깅

다음은 Flask 웹 애플리케이션에서 로깅을 구성하는 예입니다:

```python
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, request

app = Flask(__name__)

# 로깅 구성
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('앱 시작')

@app.route('/')
def index():
    app.logger.info('인덱스 페이지 요청됨')
    return "Hello, World!"

@app.route('/error')
def error():
    app.logger.error('오류 경로 트리거됨')
    return "오류 페이지", 500

@app.before_request
def log_request_info():
    app.logger.info('요청: %s %s', request.method, request.path)

if __name__ == '__main__':
    app.run(debug=True)
```

## Conclusion

Python's logging module provides a flexible and powerful way to record messages and events in your applications. By using the appropriate levels, handlers, and formatters, you can create a robust logging system that helps with debugging, monitoring, and troubleshooting your code.

Remember that proper logging is an essential part of professional software development, especially for applications that run in production environments. Invest time in setting up a good logging infrastructure from the beginning of your project, and you'll save countless hours when trying to diagnose issues later.

## 결론

Python의 로깅 모듈은 애플리케이션에서 메시지와 이벤트를 기록하는 유연하고 강력한 방법을 제공합니다. 적절한 레벨, 핸들러, 포맷터를 사용함으로써 코드의 디버깅, 모니터링, 문제 해결에 도움이 되는 견고한 로깅 시스템을 만들 수 있습니다.

적절한 로깅은 특히 프로덕션 환경에서 실행되는 애플리케이션에서 전문적인 소프트웨어 개발의 필수적인 부분임을 기억하세요. 프로젝트 시작부터 좋은 로깅 인프라를 구축하는 데 시간을 투자하면 나중에 문제를 진단할 때 수많은 시간을 절약할 수 있습니다.

