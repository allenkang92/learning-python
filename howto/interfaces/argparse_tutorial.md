# Command-Line Parsing with argparse

# argparse를 이용한 명령줄 인자 파싱

## Introduction

The `argparse` module is the recommended command-line parsing module in the Python standard library. It makes it easy to write user-friendly command-line interfaces, automatically generating help and usage messages and handling various argument types. This guide covers how to use `argparse` effectively in your Python programs.

## 소개

`argparse` 모듈은 Python 표준 라이브러리에서 권장하는 명령줄 파싱 모듈입니다. 이 모듈을 사용하면 사용자 친화적인 명령줄 인터페이스를 쉽게 작성할 수 있으며, 도움말과 사용 메시지를 자동으로 생성하고 다양한 인자 유형을 처리합니다. 이 가이드에서는 Python 프로그램에서 `argparse`를 효과적으로 사용하는 방법을 다룹니다.

## Basic Usage

The most basic example of using `argparse` involves just a few steps:

```python
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='A simple example program')

# Add arguments
parser.add_argument('--number', type=int, default=10, help='A number to use')

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"The number is: {args.number}")
```

When you run this program, you can provide the `--number` argument:

```
$ python program.py --number 42
The number is: 42
```

If you run it without arguments, it uses the default:

```
$ python program.py
The number is: 10
```

And if you use the `--help` flag, it shows a helpful message:

```
$ python program.py --help
usage: program.py [-h] [--number NUMBER]

A simple example program

options:
  -h, --help       show this help message and exit
  --number NUMBER  A number to use
```

## 기본 사용법

`argparse`의 가장 기본적인 사용 예제는 다음과 같은 몇 가지 단계로 이루어집니다:

```python
import argparse

# 인자 파서 생성
parser = argparse.ArgumentParser(description='간단한 예제 프로그램')

# 인자 추가
parser.add_argument('--number', type=int, default=10, help='사용할 숫자')

# 인자 파싱
args = parser.parse_args()

# 인자 사용
print(f"숫자는: {args.number}")
```

이 프로그램을 실행할 때 `--number` 인자를 제공할 수 있습니다:

```
$ python program.py --number 42
숫자는: 42
```

인자 없이 실행하면 기본값을 사용합니다:

```
$ python program.py
숫자는: 10
```

그리고 `--help` 플래그를 사용하면 도움말 메시지가 표시됩니다:

```
$ python program.py --help
usage: program.py [-h] [--number NUMBER]

간단한 예제 프로그램

options:
  -h, --help       도움말 표시 및 종료
  --number NUMBER  사용할 숫자
```

## Positional and Optional Arguments

`argparse` supports two main types of arguments:

1. **Positional arguments**: Required arguments that don't use a prefix like `--`
2. **Optional arguments**: Arguments that are prefixed with `--` or `-` and are optional by default

### Positional Arguments

```python
parser.add_argument('filename', help='File to process')
```

### Optional Arguments

```python
parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
```

Here's an example combining both:

```python
import argparse

parser = argparse.ArgumentParser(description='Process a file')
parser.add_argument('filename', help='File to process')
parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')

args = parser.parse_args()

print(f"Processing file: {args.filename}")
if args.verbose:
    print("Verbose mode enabled")
```

## 위치 인자와 선택적 인자

`argparse`는 두 가지 주요 유형의 인자를 지원합니다:

1. **위치 인자(Positional arguments)**: `--`와 같은 접두사를 사용하지 않는 필수 인자
2. **선택적 인자(Optional arguments)**: `--` 또는 `-`로 시작하며 기본적으로 선택 사항인 인자

### 위치 인자

```python
parser.add_argument('filename', help='처리할 파일')
```

### 선택적 인자

```python
parser.add_argument('--verbose', '-v', action='store_true', help='상세 출력 활성화')
```

다음은 두 가지를 모두 결합한 예제입니다:

```python
import argparse

parser = argparse.ArgumentParser(description='파일 처리')
parser.add_argument('filename', help='처리할 파일')
parser.add_argument('--verbose', '-v', action='store_true', help='상세 출력 활성화')

args = parser.parse_args()

print(f"파일 처리 중: {args.filename}")
if args.verbose:
    print("상세 모드 활성화됨")
```

## Argument Types and Actions

`argparse` allows you to specify the type of arguments and how they should be handled:

### Types

You can specify a type for arguments:

```python
parser.add_argument('--count', type=int, help='Number of times to repeat')
parser.add_argument('--temperature', type=float, help='Temperature in Celsius')
parser.add_argument('--names', type=str, nargs='+', help='List of names')
```

### Actions

Actions determine what happens when an argument is encountered:

- `store` - Default action, stores the value
- `store_true` / `store_false` - Stores True/False when the flag is present/absent
- `append` - Appends the value to a list
- `count` - Counts the number of times the argument appears

```python
parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')
parser.add_argument('--quiet', action='store_false', dest='verbose', help='Disable verbose mode')
parser.add_argument('--file', action='append', help='Add a file (can be used multiple times)')
parser.add_argument('-v', action='count', default=0, help='Increase verbosity')
```

## 인자 타입과 액션

`argparse`를 사용하면 인자의 유형과 처리 방법을 지정할 수 있습니다:

### 타입

인자의 타입을 지정할 수 있습니다:

```python
parser.add_argument('--count', type=int, help='반복할 횟수')
parser.add_argument('--temperature', type=float, help='섭씨 온도')
parser.add_argument('--names', type=str, nargs='+', help='이름 목록')
```

### 액션

액션은 인자가 발견될 때 어떤 일이 발생하는지 결정합니다:

- `store` - 기본 액션, 값을 저장
- `store_true` / `store_false` - 플래그가 있을 때/없을 때 True/False 저장
- `append` - 값을 리스트에 추가
- `count` - 인자가 나타난 횟수를 계산

```python
parser.add_argument('--verbose', action='store_true', help='상세 모드 활성화')
parser.add_argument('--quiet', action='store_false', dest='verbose', help='상세 모드 비활성화')
parser.add_argument('--file', action='append', help='파일 추가 (여러 번 사용 가능)')
parser.add_argument('-v', action='count', default=0, help='상세도 증가')
```

## Mutually Exclusive Groups

Sometimes you want to ensure that certain arguments can't be used together. Use mutually exclusive groups for this:

```python
import argparse

parser = argparse.ArgumentParser(description='Volume control')
group = parser.add_mutually_exclusive_group()
group.add_argument('--increase', action='store_true', help='Increase volume')
group.add_argument('--decrease', action='store_true', help='Decrease volume')

args = parser.parse_args()

if args.increase:
    print("Increasing volume")
elif args.decrease:
    print("Decreasing volume")
else:
    print("Volume unchanged")
```

If you try to use both flags, you'll get an error:

```
$ python volume.py --increase --decrease
usage: volume.py [-h] [--increase | --decrease]
volume.py: error: argument --decrease: not allowed with argument --increase
```

## 상호 배타적 그룹

때로는 특정 인자들이 함께 사용되지 않도록 해야 할 때가 있습니다. 이를 위해 상호 배타적 그룹을 사용하세요:

```python
import argparse

parser = argparse.ArgumentParser(description='볼륨 제어')
group = parser.add_mutually_exclusive_group()
group.add_argument('--increase', action='store_true', help='볼륨 증가')
group.add_argument('--decrease', action='store_true', help='볼륨 감소')

args = parser.parse_args()

if args.increase:
    print("볼륨 증가 중")
elif args.decrease:
    print("볼륨 감소 중")
else:
    print("볼륨 변경 없음")
```

두 플래그를 모두 사용하려고 하면 오류가 발생합니다:

```
$ python volume.py --increase --decrease
usage: volume.py [-h] [--increase | --decrease]
volume.py: error: argument --decrease: not allowed with argument --increase
```

## Subcommands

For complex CLI applications, you might want to use subcommands, similar to what tools like `git` use (e.g., `git commit`, `git push`):

```python
import argparse

parser = argparse.ArgumentParser(description='File manager')
subparsers = parser.add_subparsers(dest='command', help='Commands')

# Create command
create_parser = subparsers.add_parser('create', help='Create a file')
create_parser.add_argument('filename', help='Name of the file to create')
create_parser.add_argument('--content', help='Content to write to the file')

# Delete command
delete_parser = subparsers.add_parser('delete', help='Delete a file')
delete_parser.add_argument('filename', help='Name of the file to delete')
delete_parser.add_argument('--force', action='store_true', help='Force deletion')

args = parser.parse_args()

if args.command == 'create':
    print(f"Creating file: {args.filename}")
    if args.content:
        print(f"With content: {args.content}")
elif args.command == 'delete':
    print(f"Deleting file: {args.filename}")
    if args.force:
        print("With force option")
```

Now you can use the program with subcommands:

```
$ python filemanager.py create myfile.txt --content "Hello, World!"
Creating file: myfile.txt
With content: Hello, World!

$ python filemanager.py delete myfile.txt --force
Deleting file: myfile.txt
With force option
```

## 하위 명령어

복잡한 CLI 애플리케이션의 경우, `git`과 같은 도구가 사용하는 것과 유사한 하위 명령어(예: `git commit`, `git push`)를 사용하고 싶을 수 있습니다:

```python
import argparse

parser = argparse.ArgumentParser(description='파일 관리자')
subparsers = parser.add_subparsers(dest='command', help='명령어')

# 생성 명령어
create_parser = subparsers.add_parser('create', help='파일 생성')
create_parser.add_argument('filename', help='생성할 파일 이름')
create_parser.add_argument('--content', help='파일에 쓸 내용')

# 삭제 명령어
delete_parser = subparsers.add_parser('delete', help='파일 삭제')
delete_parser.add_argument('filename', help='삭제할 파일 이름')
delete_parser.add_argument('--force', action='store_true', help='강제 삭제')

args = parser.parse_args()

if args.command == 'create':
    print(f"파일 생성 중: {args.filename}")
    if args.content:
        print(f"내용: {args.content}")
elif args.command == 'delete':
    print(f"파일 삭제 중: {args.filename}")
    if args.force:
        print("강제 옵션 사용")
```

이제 하위 명령어로 프로그램을 사용할 수 있습니다:

```
$ python filemanager.py create myfile.txt --content "안녕하세요!"
파일 생성 중: myfile.txt
내용: 안녕하세요!

$ python filemanager.py delete myfile.txt --force
파일 삭제 중: myfile.txt
강제 옵션 사용
```

## Advanced Customization

The `argparse` module offers many ways to customize your command-line interface:

### Custom Help Formatting

```python
parser = argparse.ArgumentParser(
    description='My Program',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='Example:\n  python program.py --input file.txt'
)
```

### Custom Validation

You can validate arguments with a custom function:

```python
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

parser.add_argument('--count', type=positive_int, help='A positive integer')
```

### Default Values from Environment Variables

```python
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--api-key', default=os.environ.get('API_KEY'), help='API key')
```

## 고급 사용자 정의

`argparse` 모듈은 명령줄 인터페이스를 사용자 정의하는 많은 방법을 제공합니다:

### 사용자 정의 도움말 형식

```python
parser = argparse.ArgumentParser(
    description='내 프로그램',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog='예제:\n  python program.py --input file.txt'
)
```

### 사용자 정의 유효성 검사

사용자 정의 함수로 인자의 유효성을 검사할 수 있습니다:

```python
def positive_int(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value}는 양의 정수가 아닙니다")
    return ivalue

parser.add_argument('--count', type=positive_int, help='양의 정수')
```

### 환경 변수에서 기본값 가져오기

```python
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--api-key', default=os.environ.get('API_KEY'), help='API 키')
```

## Best Practices

1. **Provide descriptive help messages**: Help users understand what each argument does.

2. **Use meaningful default values**: Choose sensible defaults to make your program easier to use.

3. **Follow CLI conventions**: Use `-h` and `--help` for help, single dash (`-v`) for short options, double dash (`--verbose`) for long options.

4. **Keep it simple**: Don't overwhelm users with too many options. Group related options with subcommands if necessary.

5. **Validate early**: Check for invalid combinations of arguments as early as possible.

6. **Handle errors gracefully**: Provide helpful error messages when something goes wrong.

7. **Test with edge cases**: Make sure your program handles unexpected input properly.

## Complete Example

Here's a complete example that incorporates many of the concepts discussed:

```python
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(
        description='File processing utility',
        epilog='Example: python fileutil.py process input.txt --output result.txt'
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    subparsers.required = True
    
    # Process command
    process_parser = subparsers.add_parser('process', help='Process a file')
    process_parser.add_argument('input', help='Input file path')
    process_parser.add_argument('--output', '-o', help='Output file path')
    process_parser.add_argument('--verbose', '-v', action='count', default=0, help='Increase verbosity')
    process_parser.add_argument('--strict', action='store_true', help='Enable strict mode')
    
    # Check command
    check_parser = subparsers.add_parser('check', help='Check a file')
    check_parser.add_argument('files', nargs='+', help='Files to check')
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.command == 'process':
        if not os.path.exists(args.input):
            print(f"Error: Input file '{args.input}' not found")
            return 1
        
        print(f"Processing '{args.input}'")
        if args.output:
            print(f"Output will be written to '{args.output}'")
        
        if args.verbose >= 1:
            print("Verbose mode enabled")
        if args.verbose >= 2:
            print("Extra verbose information")
        if args.strict:
            print("Strict mode enabled")
            
    elif args.command == 'check':
        print(f"Checking {len(args.files)} files:")
        for f in args.files:
            exists = os.path.exists(f)
            status = "exists" if exists else "not found"
            print(f"  {f}: {status}")
    
    return 0

if __name__ == "__main__":
    exit(main())
```

## 모범 사례

1. **설명적인 도움말 메시지 제공**: 각 인자가 무엇을 하는지 사용자가 이해할 수 있도록 합니다.

2. **의미 있는 기본값 사용**: 프로그램을 더 쉽게 사용할 수 있도록 합리적인 기본값을 선택합니다.

3. **CLI 규칙 따르기**: 도움말에는 `-h`와 `--help`를, 짧은 옵션에는 단일 대시(`-v`), 긴 옵션에는 이중 대시(`--verbose`)를 사용합니다.

4. **단순하게 유지**: 너무 많은 옵션으로 사용자를 압도하지 마세요. 필요한 경우 하위 명령어로 관련 옵션을 그룹화하세요.

5. **조기 검증**: 가능한 빨리 잘못된 인자 조합을 확인하세요.

6. **오류를 우아하게 처리**: 문제가 발생했을 때 유용한 오류 메시지를 제공하세요.

7. **엣지 케이스 테스트**: 프로그램이 예상치 못한 입력을 적절히 처리하는지 확인하세요.

## 완전한 예제

다음은 논의된 많은 개념을 통합한 완전한 예제입니다:

```python
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(
        description='파일 처리 유틸리티',
        epilog='예제: python fileutil.py process input.txt --output result.txt'
    )
    
    # 다양한 명령어에 대한 하위 파서 생성
    subparsers = parser.add_subparsers(dest='command', help='명령어')
    subparsers.required = True
    
    # 처리 명령어
    process_parser = subparsers.add_parser('process', help='파일 처리')
    process_parser.add_argument('input', help='입력 파일 경로')
    process_parser.add_argument('--output', '-o', help='출력 파일 경로')
    process_parser.add_argument('--verbose', '-v', action='count', default=0, help='상세도 증가')
    process_parser.add_argument('--strict', action='store_true', help='엄격 모드 활성화')
    
    # 확인 명령어
    check_parser = subparsers.add_parser('check', help='파일 확인')
    check_parser.add_argument('files', nargs='+', help='확인할 파일들')
    
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.command == 'process':
        if not os.path.exists(args.input):
            print(f"오류: 입력 파일 '{args.input}'을(를) 찾을 수 없습니다")
            return 1
        
        print(f"'{args.input}' 처리 중")
        if args.output:
            print(f"출력은 '{args.output}'에 기록됩니다")
        
        if args.verbose >= 1:
            print("상세 모드 활성화됨")
        if args.verbose >= 2:
            print("추가 상세 정보")
        if args.strict:
            print("엄격 모드 활성화됨")
            
    elif args.command == 'check':
        print(f"{len(args.files)}개 파일 확인 중:")
        for f in args.files:
            exists = os.path.exists(f)
            status = "존재함" if exists else "찾을 수 없음"
            print(f"  {f}: {status}")
    
    return 0

if __name__ == "__main__":
    exit(main())
```

## Conclusion

The `argparse` module is a powerful tool that makes it easy to create user-friendly command-line interfaces. By learning its features and following best practices, you can build robust CLI applications that are intuitive and easy to use.

Remember that a good CLI design focuses on the user experience. Clear documentation, meaningful defaults, and consistent behavior will make your command-line tools more valuable to users.

## 결론

`argparse` 모듈은 사용자 친화적인 명령줄 인터페이스를 쉽게 만들 수 있는 강력한 도구입니다. 그 기능을 배우고 모범 사례를 따르면 직관적이고 사용하기 쉬운 강력한 CLI 애플리케이션을 구축할 수 있습니다.

좋은 CLI 설계는 사용자 경험에 중점을 둔다는 것을 기억하세요. 명확한 문서, 의미 있는 기본값, 일관된 동작은 명령줄 도구를 사용자에게 더 가치 있게 만들 것입니다.