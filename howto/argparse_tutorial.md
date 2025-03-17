# Python Argparse Tutorial (Python Argparse 튜토리얼)

## Introduction

1. The `argparse` module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`. The module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

`argparse` 모듈은 사용자 친화적인 명령줄 인터페이스를 쉽게 작성할 수 있게 해줍니다. 프로그램은 필요한 인수를 정의하고, `argparse`는 `sys.argv`에서 이를 어떻게 구문 분석할지 파악합니다. 이 모듈은 또한 도움말과 사용법 메시지를 자동으로 생성하고 사용자가 프로그램에 잘못된 인수를 제공할 때 오류를 발생시킵니다.

2. This tutorial aims to teach you the fundamentals of `argparse` so you can create sophisticated command-line interfaces for your Python scripts.

이 튜토리얼은 Python 스크립트에 정교한 명령줄 인터페이스를 만들 수 있도록 `argparse`의 기본 사항을 가르치는 것을 목표로 합니다.

## Basic Usage

3. Let's start with a simple example that takes a filename as an argument:

간단한 예제부터 시작해보겠습니다. 파일 이름을 인수로 받는 스크립트입니다:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('filename', help='the file to process')
    args = parser.parse_args()
    
    print(f'Processing file: {args.filename}')

if __name__ == '__main__':
    main()
```

4. If you save this script as `process_file.py` and run it without arguments, you'll see an error:

이 스크립트를 `process_file.py`로 저장하고 인수 없이 실행하면 다음과 같은 오류가 표시됩니다:

```
$ python process_file.py
usage: process_file.py [-h] filename
process_file.py: error: the following arguments are required: filename
```

5. But if you provide a filename, it works as expected:

하지만 파일 이름을 제공하면 예상대로 작동합니다:

```
$ python process_file.py sample.txt
Processing file: sample.txt
```

## Positional Arguments

6. Positional arguments are those that are identified by their position in the command line. In the previous example, `filename` is a positional argument.

위치 인수는 명령줄에서 위치로 식별되는 인수입니다. 이전 예제에서 `filename`은 위치 인수입니다.

7. You can add multiple positional arguments:

여러 위치 인수를 추가할 수 있습니다:

```python
import argparse

parser = argparse.ArgumentParser(description='Process files.')
parser.add_argument('input_file', help='the input file')
parser.add_argument('output_file', help='the output file')
args = parser.parse_args()

print(f'Input file: {args.input_file}')
print(f'Output file: {args.output_file}')
```

8. Now the script requires two arguments:

이제 스크립트에는 두 개의 인수가 필요합니다:

```
$ python process_files.py input.txt output.txt
Input file: input.txt
Output file: output.txt
```

## Optional Arguments

9. Optional arguments are preceded by a flag, usually `-` or `--`. Let's add an optional argument to our example:

선택적 인수는 일반적으로 `-` 또는 `--`로 시작하는 플래그가 앞에 붙습니다. 예제에 선택적 인수를 추가해 보겠습니다:

```python
import argparse

parser = argparse.ArgumentParser(description='Process a file.')
parser.add_argument('filename', help='the file to process')
parser.add_argument('--verbose', '-v', help='increase output verbosity',
                    action='store_true')
args = parser.parse_args()

if args.verbose:
    print(f'Processing file: {args.filename} with verbose output')
else:
    print(f'Processing file: {args.filename}')
```

10. This script accepts an optional `--verbose` flag:

이 스크립트는 선택적인 `--verbose` 플래그를 허용합니다:

```
$ python process_file.py sample.txt
Processing file: sample.txt

$ python process_file.py sample.txt --verbose
Processing file: sample.txt with verbose output

$ python process_file.py sample.txt -v
Processing file: sample.txt with verbose output
```

## Help Messages

11. `argparse` automatically generates help messages for your command-line interface. Users can access this help information using `-h` or `--help`:

`argparse`는 명령줄 인터페이스에 대한 도움말 메시지를 자동으로 생성합니다. 사용자는 `-h` 또는 `--help`를 사용하여 이 도움말 정보에 접근할 수 있습니다:

```
$ python process_file.py --help
usage: process_file.py [-h] [--verbose] filename

Process a file.

positional arguments:
  filename       the file to process

optional arguments:
  -h, --help     show this help message and exit
  --verbose, -v  increase output verbosity
```

12. You can customize help messages using the `help` parameter when adding arguments, and you can set the program description when creating the parser.

인수를 추가할 때 `help` 매개변수를 사용하여 도움말 메시지를 사용자 정의할 수 있으며, 파서를 생성할 때 프로그램 설명을 설정할 수 있습니다.

## Action Options

13. The `action` parameter specifies how the command-line argument should be handled. Some common actions include:

`action` 매개변수는 명령줄 인수를 어떻게 처리해야 하는지 지정합니다. 일반적인 액션에는 다음이 포함됩니다:

14. `store`: The default action, which stores the argument value.

`store`: 기본 액션으로, 인수 값을 저장합니다.

```python
parser.add_argument('--output', action='store', dest='output_file',
                    help='output file')
```

15. `store_true` / `store_false`: Store a boolean value (True or False) if the flag is present or not:

`store_true` / `store_false`: 플래그가 있는지 여부에 따라 부울 값(True 또는 False)을 저장합니다:

```python
parser.add_argument('--verbose', action='store_true',
                    help='enable verbose output')
parser.add_argument('--quiet', action='store_false', dest='verbose',
                    help='disable verbose output')
```

16. `append`: Append the value to a list. This is useful when an option can be specified multiple times:

`append`: 값을 목록에 추가합니다. 옵션을 여러 번 지정할 수 있을 때 유용합니다:

```python
parser.add_argument('--include', action='append',
                    help='include additional files')
```

17. `count`: Count the number of times the option appears:

`count`: 옵션이 나타나는 횟수를 계산합니다:

```python
parser.add_argument('-v', action='count', default=0,
                    help='increase verbosity level')
```

## Type Conversion

18. By default, `argparse` treats all arguments as strings. You can specify a type for automatic conversion:

기본적으로 `argparse`는 모든 인수를 문자열로 취급합니다. 자동 변환을 위해 타입을 지정할 수 있습니다:

```python
import argparse

parser = argparse.ArgumentParser(description='Calculate area.')
parser.add_argument('width', type=float, help='width of the rectangle')
parser.add_argument('height', type=float, help='height of the rectangle')
args = parser.parse_args()

area = args.width * args.height
print(f'The area of the rectangle is: {area}')
```

19. Now the script will convert string arguments to floats:

이제 스크립트는 문자열 인수를 실수로 변환합니다:

```
$ python calculate_area.py 5.2 3.8
The area of the rectangle is: 19.76
```

## Choices and Defaults

20. You can restrict the possible values for an argument using `choices`:

`choices`를 사용하여 인수에 가능한 값을 제한할 수 있습니다:

```python
parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    default='INFO', help='set the logging level')
```

21. And you can set default values using `default`:

그리고 `default`를 사용하여 기본값을 설정할 수 있습니다:

```python
parser.add_argument('--port', type=int, default=8000,
                    help='port number to use (default: 8000)')
```

## Subcommands

22. For complex command-line interfaces, you can use subcommands. Think of Git commands like `git add`, `git commit`, etc.:

복잡한 명령줄 인터페이스의 경우 하위 명령을 사용할 수 있습니다. `git add`, `git commit` 등과 같은 Git 명령을 생각해보세요:

```python
import argparse

parser = argparse.ArgumentParser(description='File management utility.')
subparsers = parser.add_subparsers(dest='command', help='command to run')

# Create parser for the "copy" command
copy_parser = subparsers.add_parser('copy', help='copy files')
copy_parser.add_argument('source', help='source file')
copy_parser.add_argument('destination', help='destination file')

# Create parser for the "delete" command
delete_parser = subparsers.add_parser('delete', help='delete files')
delete_parser.add_argument('file', help='file to delete')
delete_parser.add_argument('--recursive', '-r', action='store_true',
                          help='delete directories recursively')

args = parser.parse_args()

if args.command == 'copy':
    print(f'Copying {args.source} to {args.destination}')
elif args.command == 'delete':
    if args.recursive:
        print(f'Recursively deleting {args.file}')
    else:
        print(f'Deleting {args.file}')
```

23. This creates a command-line utility with two subcommands:

이는 두 개의 하위 명령이 있는 명령줄 유틸리티를 생성합니다:

```
$ python file_util.py copy file1.txt file2.txt
Copying file1.txt to file2.txt

$ python file_util.py delete temp.txt
Deleting temp.txt

$ python file_util.py delete --recursive temp_dir
Recursively deleting temp_dir
```

## Required Optional Arguments

24. Although it might sound contradictory, you can make optional arguments (those with flags) required:

모순되게 들릴 수 있지만, 선택적 인수(플래그가 있는 인수)를 필수로 만들 수 있습니다:

```python
parser.add_argument('--config', required=True, help='configuration file')
```

25. This creates an optional argument that must be provided:

이렇게 하면 반드시 제공해야 하는 선택적 인수가 생성됩니다:

```
$ python script.py
usage: script.py [-h] --config CONFIG
script.py: error: the following arguments are required: --config
```

## Argument Groups

26. For better help output organization, you can group related arguments:

더 나은 도움말 출력 구성을 위해 관련 인수를 그룹화할 수 있습니다:

```python
import argparse

parser = argparse.ArgumentParser(description='Example program')

# Create an argument group for input options
input_group = parser.add_argument_group('input options', 'options for input control')
input_group.add_argument('--input-file', help='input file path')
input_group.add_argument('--data-source', help='data source URL')

# Create an argument group for output options
output_group = parser.add_argument_group('output options', 'options for output control')
output_group.add_argument('--output-format', choices=['json', 'csv', 'xml'],
                         help='output format')
output_group.add_argument('--output-file', help='output file path')

args = parser.parse_args()
```

27. The help output will now have clear sections:

도움말 출력에 이제 명확한 섹션이 있습니다:

```
$ python grouped_args.py -h
usage: grouped_args.py [-h] [--input-file INPUT_FILE] [--data-source DATA_SOURCE]
                       [--output-format {json,csv,xml}] [--output-file OUTPUT_FILE]

Example program

optional arguments:
  -h, --help            show this help message and exit

input options:
  options for input control
  --input-file INPUT_FILE
                        input file path
  --data-source DATA_SOURCE
                        data source URL

output options:
  options for output control
  --output-format {json,csv,xml}
                        output format
  --output-file OUTPUT_FILE
                        output file path
```

## Advanced Usage

### Custom Types

28. You can define custom types for argument conversion:

인수 변환을 위한 사용자 정의 타입을 정의할 수 있습니다:

```python
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

parser.add_argument('--count', type=positive_int, help='positive integer count')
```

### Custom Actions

29. For more complex argument handling, you can create custom action classes:

더 복잡한 인수 처리를 위해 사용자 정의 액션 클래스를 만들 수 있습니다:

```python
class KeyValueAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        key, value = values.split('=')
        if not hasattr(namespace, self.dest):
            setattr(namespace, self.dest, {})
        getattr(namespace, self.dest)[key] = value

parser.add_argument('--define', action=KeyValueAction, dest='variables',
                   help='define variables as key=value')
```

## Best Practices

30. Here are some best practices for using `argparse`:

다음은 `argparse`를 사용하기 위한 몇 가지 모범 사례입니다:

31. Provide clear help messages for all arguments.

모든 인수에 대한 명확한 도움말 메시지를 제공하세요.

32. Use short and long flags for common options (e.g., `-v` and `--verbose`).

일반적인 옵션에 짧은 플래그와 긴 플래그를 모두 사용하세요(예: `-v`와 `--verbose`).

33. Set reasonable defaults to make your program easier to use.

프로그램을 더 쉽게 사용할 수 있도록 합리적인 기본값을 설정하세요.

34. Group related arguments for better help output organization.

더 나은 도움말 출력 구성을 위해 관련 인수를 그룹화하세요.

35. Handle errors gracefully with clear error messages.

명확한 오류 메시지로 오류를 우아하게 처리하세요.

## Conclusion

36. `argparse` is a powerful module for creating user-friendly command-line interfaces in Python. It provides automatic help generation, type conversion, validation, and much more. By following the examples and best practices in this tutorial, you can create sophisticated command-line applications that are easy to use.

`argparse`는 Python에서 사용자 친화적인 명령줄 인터페이스를 만들기 위한 강력한 모듈입니다. 자동 도움말 생성, 타입 변환, 유효성 검사 등을 제공합니다. 이 튜토리얼의 예제와 모범 사례를 따르면 사용하기 쉬운 정교한 명령줄 애플리케이션을 만들 수 있습니다.

37. Remember that good command-line interfaces are consistent, intuitive, and well-documented. The `argparse` module helps you achieve these goals with minimal effort.

좋은 명령줄 인터페이스는 일관성 있고, 직관적이며, 잘 문서화되어 있다는 것을 기억하세요. `argparse` 모듈은 최소한의 노력으로 이러한 목표를 달성하는 데 도움을 줍니다.