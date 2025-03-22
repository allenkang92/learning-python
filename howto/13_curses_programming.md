# Curses Programming in Python

# Python에서의 Curses 프로그래밍

## Introduction

The `curses` module provides an interface to the curses library, a terminal-independent screen-painting and keyboard-handling facility for text-based terminals. It enables developers to create text-based user interfaces (TUIs) with features such as colored text, interactive menus, and responsive keyboard controls.

This guide covers how to use the curses library in Python to build terminal applications with interactive user interfaces.

## 소개

`curses` 모듈은 curses 라이브러리에 대한 인터페이스를 제공합니다. curses는 텍스트 기반 터미널을 위한 터미널 독립적인 화면 그리기 및 키보드 처리 기능입니다. 개발자가 색상 텍스트, 대화형 메뉴, 반응형 키보드 컨트롤과 같은 기능이 있는 텍스트 기반 사용자 인터페이스(TUI)를 만들 수 있게 해줍니다.

이 가이드는 대화형 사용자 인터페이스가 있는 터미널 애플리케이션을 구축하기 위해 Python에서 curses 라이브러리를 사용하는 방법을 다룹니다.

## Getting Started

### Installation

The curses module comes with the Python standard library on Unix-based systems (Linux, macOS). For Windows, you'll need to install the `windows-curses` package:

```bash
pip install windows-curses
```

### Basic Structure of a Curses Program

Every curses program follows this general structure:

```python
import curses

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()      # Clear the screen
    
    # Your code goes here
    stdscr.addstr(0, 0, "Hello, Curses World!")
    stdscr.refresh()    # Update the screen
    
    # Wait for user input
    stdscr.getch()

# Wrapper handles initialization and cleanup
curses.wrapper(main)
```

## 시작하기

### 설치

curses 모듈은 유닉스 기반 시스템(Linux, macOS)에서는 Python 표준 라이브러리와 함께 제공됩니다. Windows의 경우 `windows-curses` 패키지를 설치해야 합니다:

```bash
pip install windows-curses
```

### Curses 프로그램의 기본 구조

모든 curses 프로그램은 다음과 같은 일반적인 구조를 따릅니다:

```python
import curses

def main(stdscr):
    # curses 초기화
    curses.curs_set(0)  # 커서 숨기기
    stdscr.clear()      # 화면 지우기
    
    # 여기에 코드 작성
    stdscr.addstr(0, 0, "안녕하세요, Curses 세계!")
    stdscr.refresh()    # 화면 갱신
    
    # 사용자 입력 대기
    stdscr.getch()

# wrapper가 초기화 및 정리를 처리합니다
curses.wrapper(main)
```

## Window Concepts

### The Standard Screen (stdscr)

When you initialize curses with the `wrapper()` function, it creates the "standard screen" (`stdscr`), which represents the entire terminal window. This is the primary window you'll work with.

### Creating Windows

You can also create sub-windows to organize your interface:

```python
# Create a window with height=10, width=20, at position y=5, x=10
my_window = curses.newwin(10, 20, 5, 10)
my_window.box()  # Add a border
my_window.addstr(1, 1, "This is a window")
my_window.refresh()
```

### Window Methods

Common methods for windows include:

- `window.addstr(y, x, string)`: Add a string at position (y, x)
- `window.addch(y, x, ch)`: Add a character at position (y, x)
- `window.clear()`: Clear the window
- `window.refresh()`: Update the window
- `window.getch()`: Get a character input
- `window.getkey()`: Get a key name
- `window.box()`: Draw a border around the window

## 윈도우 개념

### 표준 화면(stdscr)

`wrapper()` 함수로 curses를 초기화하면 "표준 화면"(`stdscr`)이 생성되며, 이는 전체 터미널 창을 나타냅니다. 이것이 작업할 기본 윈도우입니다.

### 윈도우 생성하기

인터페이스를 구성하기 위해 하위 윈도우를 생성할 수도 있습니다:

```python
# 높이=10, 너비=20, 위치 y=5, x=10인 윈도우 생성
my_window = curses.newwin(10, 20, 5, 10)
my_window.box()  # 테두리 추가
my_window.addstr(1, 1, "이것은 윈도우입니다")
my_window.refresh()
```

### 윈도우 메서드

윈도우의 일반적인 메서드는 다음과 같습니다:

- `window.addstr(y, x, string)`: 위치 (y, x)에 문자열 추가
- `window.addch(y, x, ch)`: 위치 (y, x)에 문자 추가
- `window.clear()`: 윈도우 지우기
- `window.refresh()`: 윈도우 갱신
- `window.getch()`: 문자 입력 받기
- `window.getkey()`: 키 이름 받기
- `window.box()`: 윈도우 주위에 테두리 그리기

## Colors and Attributes

### Initializing Colors

To use colors, you must initialize the color system:

```python
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Define color pair 1 as green on black
```

### Using Colors and Attributes

Apply colors and attributes to text:

```python
# Use color pair 1 (green on black)
stdscr.addstr(1, 0, "Green text", curses.color_pair(1))

# Combine color with attributes
stdscr.addstr(2, 0, "Bold green text", curses.color_pair(1) | curses.A_BOLD)
```

### Available Attributes

Common text attributes include:

- `curses.A_BOLD`: Bold text
- `curses.A_UNDERLINE`: Underlined text
- `curses.A_REVERSE`: Inverted colors
- `curses.A_BLINK`: Blinking text
- `curses.A_DIM`: Dim text

## 색상 및 속성

### 색상 초기화하기

색상을 사용하려면 색상 시스템을 초기화해야 합니다:

```python
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # 색상 쌍 1을 검은색 배경에 녹색 텍스트로 정의
```

### 색상 및 속성 사용하기

텍스트에 색상과 속성을 적용합니다:

```python
# 색상 쌍 1 사용(검은색 배경에 녹색)
stdscr.addstr(1, 0, "녹색 텍스트", curses.color_pair(1))

# 색상과 속성 결합
stdscr.addstr(2, 0, "굵은 녹색 텍스트", curses.color_pair(1) | curses.A_BOLD)
```

### 사용 가능한 속성

일반적인 텍스트 속성은 다음과 같습니다:

- `curses.A_BOLD`: 굵은 텍스트
- `curses.A_UNDERLINE`: 밑줄 있는 텍스트
- `curses.A_REVERSE`: 반전된 색상
- `curses.A_BLINK`: 깜박이는 텍스트
- `curses.A_DIM`: 흐린 텍스트

## Handling Input

### Getting Input

There are several ways to get user input:

```python
# Get a single character (blocking)
ch = stdscr.getch()

# Get a key name as string
key = stdscr.getkey()

# Non-blocking input check
stdscr.nodelay(True)  # Enable non-blocking mode
ch = stdscr.getch()   # Returns -1 if no input is available
```

### Special Keys

Use the curses module constants to handle special keys:

```python
ch = stdscr.getch()
if ch == curses.KEY_UP:
    # Handle up arrow
elif ch == curses.KEY_DOWN:
    # Handle down arrow
elif ch == ord('q'):
    # Handle 'q' key
```

## 입력 처리하기

### 입력 받기

사용자 입력을 받는 여러 방법이 있습니다:

```python
# 단일 문자 받기(블로킹)
ch = stdscr.getch()

# 문자열로 키 이름 받기
key = stdscr.getkey()

# 논블로킹 입력 확인
stdscr.nodelay(True)  # 논블로킹 모드 활성화
ch = stdscr.getch()   # 사용 가능한 입력이 없으면 -1 반환
```

### 특수 키

특수 키를 처리하기 위해 curses 모듈 상수를 사용합니다:

```python
ch = stdscr.getch()
if ch == curses.KEY_UP:
    # 위쪽 화살표 처리
elif ch == curses.KEY_DOWN:
    # 아래쪽 화살표 처리
elif ch == ord('q'):
    # 'q' 키 처리
```

## Creating Interactive Interfaces

### Menus

You can create a simple menu system:

```python
def show_menu(window, selected_row_idx):
    menu_items = ["Option 1", "Option 2", "Option 3", "Exit"]
    
    for idx, item in enumerate(menu_items):
        y = idx + 1
        x = 1
        if idx == selected_row_idx:
            window.addstr(y, x, item, curses.A_REVERSE)
        else:
            window.addstr(y, x, item)
    
    window.refresh()
```

### Text Input

Create a simple text input field:

```python
def get_user_input(window, prompt, y, x):
    curses.echo()  # Show typed characters
    window.addstr(y, x, prompt)
    window.refresh()
    input_str = window.getstr(y, x + len(prompt), 20).decode('utf-8')
    curses.noecho()  # Don't show typed characters
    return input_str
```

## 대화형 인터페이스 만들기

### 메뉴

간단한 메뉴 시스템을 만들 수 있습니다:

```python
def show_menu(window, selected_row_idx):
    menu_items = ["옵션 1", "옵션 2", "옵션 3", "종료"]
    
    for idx, item in enumerate(menu_items):
        y = idx + 1
        x = 1
        if idx == selected_row_idx:
            window.addstr(y, x, item, curses.A_REVERSE)
        else:
            window.addstr(y, x, item)
    
    window.refresh()
```

### 텍스트 입력

간단한 텍스트 입력 필드 만들기:

```python
def get_user_input(window, prompt, y, x):
    curses.echo()  # 입력한 문자 표시
    window.addstr(y, x, prompt)
    window.refresh()
    input_str = window.getstr(y, x + len(prompt), 20).decode('utf-8')
    curses.noecho()  # 입력한 문자 표시하지 않음
    return input_str
```

## Advanced Features

### Pads

Pads are windows that can be larger than the screen:

```python
# Create a pad with 100 rows and 100 columns
pad = curses.newpad(100, 100)

# Fill the pad with content
for y in range(100):
    for x in range(100):
        pad.addch(y, x, ord('a') + (x * y) % 26)

# Display a portion of the pad on the screen
# Parameters: starting row on pad, starting col on pad, 
#             starting row on screen, starting col on screen,
#             ending row on screen, ending col on screen
pad.refresh(0, 0, 5, 5, 15, 45)
```

### Mouse Support

Enable and handle mouse events:

```python
# Enable mouse events
curses.mousemask(curses.ALL_MOUSE_EVENTS)

# Inside your main loop
ch = stdscr.getch()
if ch == curses.KEY_MOUSE:
    mouse_event = curses.getmouse()
    # mouse_event is a tuple: (id, x, y, z, bstate)
    y, x = mouse_event[2], mouse_event[1]
    if mouse_event[4] & curses.BUTTON1_CLICKED:
        # Handle mouse click at position (y, x)
```

## 고급 기능

### 패드

패드는 화면보다 클 수 있는 윈도우입니다:

```python
# 100행 100열의 패드 생성
pad = curses.newpad(100, 100)

# 패드에 콘텐츠 채우기
for y in range(100):
    for x in range(100):
        pad.addch(y, x, ord('a') + (x * y) % 26)

# 화면에 패드의 일부 표시
# 매개변수: 패드에서 시작 행, 패드에서 시작 열, 
#          화면에서 시작 행, 화면에서 시작 열,
#          화면에서 끝 행, 화면에서 끝 열
pad.refresh(0, 0, 5, 5, 15, 45)
```

### 마우스 지원

마우스 이벤트 활성화 및 처리:

```python
# 마우스 이벤트 활성화
curses.mousemask(curses.ALL_MOUSE_EVENTS)

# 메인 루프 내부
ch = stdscr.getch()
if ch == curses.KEY_MOUSE:
    mouse_event = curses.getmouse()
    # mouse_event는 튜플: (id, x, y, z, bstate)
    y, x = mouse_event[2], mouse_event[1]
    if mouse_event[4] & curses.BUTTON1_CLICKED:
        # 위치 (y, x)에서 마우스 클릭 처리
```

## Complete Example: Text Editor

Here's a simple text editor to demonstrate curses capabilities:

```python
import curses
import os

def display_text(window, text, top_line=0):
    """Display text in the window starting from top_line."""
    height, width = window.getmaxyx()
    
    for i, line in enumerate(text[top_line:top_line+height-2], 1):
        # Truncate the line if it's wider than the window
        if len(line) > width - 2:
            line = line[:width-5] + "..."
        
        window.addstr(i, 1, line)
    
    window.refresh()

def editor(stdscr):
    # Initialize curses
    curses.curs_set(1)  # Show cursor
    stdscr.clear()
    
    # Get terminal dimensions
    height, width = stdscr.getmaxyx()
    
    # Create a window with a border
    editor_win = curses.newwin(height, width, 0, 0)
    editor_win.box()
    editor_win.addstr(0, 2, " Simple Text Editor ")
    editor_win.refresh()
    
    # Initialize editor state
    filename = ""
    text = [""]
    current_line = 0
    top_line = 0
    cursor_y, cursor_x = 1, 1
    
    # Display instructions
    status_line = height - 1
    editor_win.addstr(status_line, 2, "Ctrl+S: Save | Ctrl+Q: Quit")
    
    # Main loop
    while True:
        # Display current text
        editor_win.clear()
        editor_win.box()
        editor_win.addstr(0, 2, f" {filename or 'Untitled'} ")
        editor_win.addstr(status_line, 2, "Ctrl+S: Save | Ctrl+Q: Quit")
        
        display_text(editor_win, text, top_line)
        
        # Position cursor
        editor_win.move(cursor_y, cursor_x)
        
        # Get user input
        ch = editor_win.getch()
        
        # Process input
        if ch == 19:  # Ctrl+S
            # Save file
            if not filename:
                editor_win.addstr(status_line, 2, "Enter filename: ")
                curses.echo()
                filename = editor_win.getstr(status_line, 17).decode('utf-8')
                curses.noecho()
            
            if filename:
                with open(filename, 'w') as f:
                    f.write('\n'.join(text))
                editor_win.addstr(status_line, 2, f"Saved to {filename}  ")
        
        elif ch == 17:  # Ctrl+Q
            break
        
        elif ch == curses.KEY_UP:
            if current_line > 0:
                current_line -= 1
                cursor_y = max(1, cursor_y - 1)
                cursor_x = min(len(text[current_line]) + 1, cursor_x)
                if cursor_y == 1 and top_line > 0:
                    top_line -= 1
        
        elif ch == curses.KEY_DOWN:
            if current_line < len(text) - 1:
                current_line += 1
                cursor_y = min(height - 2, cursor_y + 1)
                cursor_x = min(len(text[current_line]) + 1, cursor_x)
                if cursor_y == height - 2 and current_line >= top_line + height - 2:
                    top_line += 1
        
        elif ch == curses.KEY_LEFT:
            if cursor_x > 1:
                cursor_x -= 1
        
        elif ch == curses.KEY_RIGHT:
            if cursor_x <= len(text[current_line]):
                cursor_x += 1
        
        elif ch == 10:  # Enter key
            # Split the current line at cursor position
            current_text = text[current_line]
            text[current_line] = current_text[:cursor_x-1]
            text.insert(current_line + 1, current_text[cursor_x-1:])
            current_line += 1
            cursor_y = min(height - 2, cursor_y + 1)
            cursor_x = 1
            if cursor_y == height - 2:
                top_line += 1
        
        elif ch == 127 or ch == curses.KEY_BACKSPACE:  # Backspace
            if cursor_x > 1:
                # Delete the character before the cursor
                current_text = text[current_line]
                text[current_line] = current_text[:cursor_x-2] + current_text[cursor_x-1:]
                cursor_x -= 1
            elif current_line > 0:
                # Join with the previous line
                cursor_x = len(text[current_line-1]) + 1
                text[current_line-1] += text[current_line]
                text.pop(current_line)
                current_line -= 1
                cursor_y = max(1, cursor_y - 1)
                if cursor_y == 1 and top_line > 0:
                    top_line -= 1
        
        elif 32 <= ch <= 126:  # Printable characters
            # Insert character at cursor position
            current_text = text[current_line]
            text[current_line] = current_text[:cursor_x-1] + chr(ch) + current_text[cursor_x-1:]
            cursor_x += 1

# Run the editor
curses.wrapper(editor)
```

## 완전한 예제: 텍스트 에디터

다음은 curses 기능을 보여주는 간단한 텍스트 에디터입니다:

```python
import curses
import os

def display_text(window, text, top_line=0):
    """top_line부터 시작하여 윈도우에 텍스트를 표시합니다."""
    height, width = window.getmaxyx()
    
    for i, line in enumerate(text[top_line:top_line+height-2], 1):
        # 라인이 윈도우보다 넓으면 잘라냄
        if len(line) > width - 2:
            line = line[:width-5] + "..."
        
        window.addstr(i, 1, line)
    
    window.refresh()

def editor(stdscr):
    # curses 초기화
    curses.curs_set(1)  # 커서 표시
    stdscr.clear()
    
    # 터미널 크기 가져오기
    height, width = stdscr.getmaxyx()
    
    # 테두리가 있는 윈도우 생성
    editor_win = curses.newwin(height, width, 0, 0)
    editor_win.box()
    editor_win.addstr(0, 2, " 간단한 텍스트 에디터 ")
    editor_win.refresh()
    
    # 에디터 상태 초기화
    filename = ""
    text = [""]
    current_line = 0
    top_line = 0
    cursor_y, cursor_x = 1, 1
    
    # 지침 표시
    status_line = height - 1
    editor_win.addstr(status_line, 2, "Ctrl+S: 저장 | Ctrl+Q: 종료")
    
    # 메인 루프
    while True:
        # 현재 텍스트 표시
        editor_win.clear()
        editor_win.box()
        editor_win.addstr(0, 2, f" {filename or '제목 없음'} ")
        editor_win.addstr(status_line, 2, "Ctrl+S: 저장 | Ctrl+Q: 종료")
        
        display_text(editor_win, text, top_line)
        
        # 커서 위치 지정
        editor_win.move(cursor_y, cursor_x)
        
        # 사용자 입력 받기
        ch = editor_win.getch()
        
        # 입력 처리
        if ch == 19:  # Ctrl+S
            # 파일 저장
            if not filename:
                editor_win.addstr(status_line, 2, "파일 이름 입력: ")
                curses.echo()
                filename = editor_win.getstr(status_line, 17).decode('utf-8')
                curses.noecho()
            
            if filename:
                with open(filename, 'w') as f:
                    f.write('\n'.join(text))
                editor_win.addstr(status_line, 2, f"{filename}에 저장됨  ")
        
        elif ch == 17:  # Ctrl+Q
            break
        
        elif ch == curses.KEY_UP:
            if current_line > 0:
                current_line -= 1
                cursor_y = max(1, cursor_y - 1)
                cursor_x = min(len(text[current_line]) + 1, cursor_x)
                if cursor_y == 1 and top_line > 0:
                    top_line -= 1
        
        elif ch == curses.KEY_DOWN:
            if current_line < len(text) - 1:
                current_line += 1
                cursor_y = min(height - 2, cursor_y + 1)
                cursor_x = min(len(text[current_line]) + 1, cursor_x)
                if cursor_y == height - 2 and current_line >= top_line + height - 2:
                    top_line += 1
        
        elif ch == curses.KEY_LEFT:
            if cursor_x > 1:
                cursor_x -= 1
        
        elif ch == curses.KEY_RIGHT:
            if cursor_x <= len(text[current_line]):
                cursor_x += 1
        
        elif ch == 10:  # Enter 키
            # 커서 위치에서 현재 라인 분할
            current_text = text[current_line]
            text[current_line] = current_text[:cursor_x-1]
            text.insert(current_line + 1, current_text[cursor_x-1:])
            current_line += 1
            cursor_y = min(height - 2, cursor_y + 1)
            cursor_x = 1
            if cursor_y == height - 2:
                top_line += 1
        
        elif ch == 127 or ch == curses.KEY_BACKSPACE:  # Backspace
            if cursor_x > 1:
                # 커서 앞의 문자 삭제
                current_text = text[current_line]
                text[current_line] = current_text[:cursor_x-2] + current_text[cursor_x-1:]
                cursor_x -= 1
            elif current_line > 0:
                # 이전 라인과 합치기
                cursor_x = len(text[current_line-1]) + 1
                text[current_line-1] += text[current_line]
                text.pop(current_line)
                current_line -= 1
                cursor_y = max(1, cursor_y - 1)
                if cursor_y == 1 and top_line > 0:
                    top_line -= 1
        
        elif 32 <= ch <= 126:  # 출력 가능한 문자
            # 커서 위치에 문자 삽입
            current_text = text[current_line]
            text[current_line] = current_text[:cursor_x-1] + chr(ch) + current_text[cursor_x-1:]
            cursor_x += 1

# 에디터 실행
curses.wrapper(editor)
```

## Best Practices

### 1. Error Handling and Cleanup

Always use the `curses.wrapper()` function to ensure proper terminal restoration if your program crashes.

### 2. Window Management

Keep your code organized by creating window classes or functions for different UI components.

### 3. Avoid Flickering

Use `window.noutrefresh()` and `curses.doupdate()` to minimize screen flicker when updating multiple windows:

```python
# Instead of refreshing each window individually:
window1.refresh()
window2.refresh()

# Do this:
window1.noutrefresh()
window2.noutrefresh()
curses.doupdate()  # This efficiently updates the screen once
```

### 4. Terminal Size

Always check the terminal size and adjust your interface accordingly:

```python
height, width = stdscr.getmaxyx()
if height < 24 or width < 80:
    print("Terminal too small. Please resize to at least 80x24")
    exit(1)
```

### 5. User Feedback

Always provide clear feedback for user actions, especially in text-based interfaces where visual cues are limited.

## 모범 사례

### 1. 오류 처리 및 정리

프로그램이 충돌해도 터미널이 올바르게 복원되도록 항상 `curses.wrapper()` 함수를 사용하세요.

### 2. 윈도우 관리

다양한 UI 구성 요소에 대한 윈도우 클래스나 함수를 만들어 코드를 체계적으로 유지하세요.

### 3. 깜박임 방지

여러 윈도우를 업데이트할 때 화면 깜박임을 최소화하기 위해 `window.noutrefresh()`와 `curses.doupdate()`를 사용하세요:

```python
# 각 윈도우를 개별적으로 새로 고치는 대신:
window1.refresh()
window2.refresh()

# 이렇게 하세요:
window1.noutrefresh()
window2.noutrefresh()
curses.doupdate()  # 이렇게 하면 화면을 한 번에 효율적으로 업데이트합니다
```

### 4. 터미널 크기

항상 터미널 크기를 확인하고 그에 맞게 인터페이스를 조정하세요:

```python
height, width = stdscr.getmaxyx()
if height < 24 or width < 80:
    print("터미널이 너무 작습니다. 최소 80x24로 크기를 조정하세요")
    exit(1)
```

### 5. 사용자 피드백

특히 시각적 단서가 제한된 텍스트 기반 인터페이스에서는 항상 사용자 작업에 대한 명확한 피드백을 제공하세요.

## Conclusion

The curses library is a powerful tool for creating text-based user interfaces in Python. While it has a learning curve, it allows you to create sophisticated terminal applications with interactive elements, colors, and responsive designs.

By mastering the basic concepts of windows, input handling, and colors, you can build everything from simple menus to complex applications like text editors, file managers, and dashboard interfaces.

Remember that curses applications are highly portable across different terminal types and operating systems, making them excellent for command-line utilities and server administration tools.

## 결론

curses 라이브러리는 Python에서 텍스트 기반 사용자 인터페이스를 만들기 위한 강력한 도구입니다. 학습 곡선이 있지만, 대화형 요소, 색상 및 반응형 디자인을 갖춘 정교한 터미널 애플리케이션을 만들 수 있습니다.

윈도우, 입력 처리 및 색상의 기본 개념을 마스터하면 간단한 메뉴부터 텍스트 에디터, 파일 관리자 및 대시보드 인터페이스와 같은 복잡한 애플리케이션까지 모든 것을 구축할 수 있습니다.

curses 애플리케이션은 다양한 터미널 유형과 운영 체제에서 높은 이식성을 가지고 있어 명령줄 유틸리티 및 서버 관리 도구에 탁월하다는 점을 기억하세요.

