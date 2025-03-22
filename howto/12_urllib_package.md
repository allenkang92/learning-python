# Python's urllib Package Guide

# Python의 urllib 패키지 가이드

## Introduction

The `urllib` package is a collection of modules for working with URLs in Python. It provides tools for URL parsing, request handling, error management, and more. While there are more modern alternatives like the `requests` library, understanding `urllib` is valuable because it's part of Python's standard library and requires no external dependencies.

## 소개

`urllib` 패키지는 Python에서 URL을 다루기 위한 모듈의 모음입니다. URL 파싱, 요청 처리, 오류 관리 등을 위한 도구를 제공합니다. `requests` 라이브러리와 같은 더 현대적인, 대안이 있지만, `urllib`을 이해하는 것은 Python 표준 라이브러리의 일부이며 외부 의존성이 필요 없기 때문에 가치가 있습니다.

## The urllib Package Structure

The `urllib` package in Python is organized into several submodules:

1. **urllib.request**: Opening and reading URLs
2. **urllib.error**: Exception classes for urllib.request
3. **urllib.parse**: Parsing URLs
4. **urllib.robotparser**: Parsing `robots.txt` files

Let's explore each of these modules in detail.

## urllib 패키지 구조

Python의 `urllib` 패키지는 여러 하위 모듈로 구성되어 있습니다:

1. **urllib.request**: URL을 열고 읽는 기능
2. **urllib.error**: urllib.request를 위한 예외 클래스
3. **urllib.parse**: URL 파싱
4. **urllib.robotparser**: `robots.txt` 파일 파싱

각 모듈에 대해 자세히 살펴보겠습니다.

## urllib.request - Opening and Reading URLs

The `urllib.request` module defines functions and classes to help with URL actions, primarily opening and reading URLs.

### Basic URL Retrieval

The simplest way to retrieve data from a URL:

```python
import urllib.request

# Open a URL and read its content
response = urllib.request.urlopen('https://www.python.org/')
html = response.read()  # Returns the HTML as bytes
decoded_html = html.decode('utf-8')  # Convert bytes to string

# Basic information about the response
print(f"Status: {response.status}")  # HTTP status code
print(f"Headers: {response.getheaders()}")  # List of headers

# Close the response when done
response.close()
```

### Using a Request Object

For more complex requests, you can use a `Request` object:

```python
import urllib.request

# Create a Request object with custom headers
req = urllib.request.Request(
    'https://www.python.org/',
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.9'
    }
)

# Open the request
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

# Process the response
# ...
```

## urllib.request - URL 열기 및 읽기

`urllib.request` 모듈은 주로 URL을 열고 읽는 등의 URL 작업을 돕기 위한 함수와 클래스를 정의합니다.

### 기본 URL 검색

URL에서 데이터를 검색하는 가장 간단한 방법:

```python
import urllib.request

# URL을 열고 내용 읽기
response = urllib.request.urlopen('https://www.python.org/')
html = response.read()  # HTML을 바이트로 반환
decoded_html = html.decode('utf-8')  # 바이트를 문자열로 변환

# 응답에 대한 기본 정보
print(f"상태: {response.status}")  # HTTP 상태 코드
print(f"헤더: {response.getheaders()}")  # 헤더 목록

# 완료 시 응답 닫기
response.close()
```

### Request 객체 사용하기

더 복잡한 요청의 경우 `Request` 객체를 사용할 수 있습니다:

```python
import urllib.request

# 사용자 정의 헤더로 Request 객체 생성
req = urllib.request.Request(
    'https://www.python.org/',
    headers={
        'User-Agent': 'Mozilla/5.0',
        'Accept-Language': 'en-US,en;q=0.9'
    }
)

# 요청 열기
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

# 응답 처리
# ...
```

### HTTP Methods (GET, POST)

By default, `urlopen()` uses the GET method. For POST requests, you need to provide data:

```python
import urllib.request
import urllib.parse

# Data to send in a POST request
data = {
    'username': 'user',
    'password': 'pass123'
}

# Encode the data for POST
data = urllib.parse.urlencode(data).encode('utf-8')

# Create a POST request
req = urllib.request.Request('https://httpbin.org/post', data=data, method='POST')

# Add headers if needed
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

# Send the request and read the response
with urllib.request.urlopen(req) as response:
    response_data = response.read().decode('utf-8')
    print(response_data)
```

### HTTP 메서드 (GET, POST)

기본적으로 `urlopen()`은 GET 메서드를 사용합니다. POST 요청의 경우 데이터를 제공해야 합니다:

```python
import urllib.request
import urllib.parse

# POST 요청에서 보낼 데이터
data = {
    'username': 'user',
    'password': 'pass123'
}

# POST용 데이터 인코딩
data = urllib.parse.urlencode(data).encode('utf-8')

# POST 요청 생성
req = urllib.request.Request('https://httpbin.org/post', data=data, method='POST')

# 필요한 경우 헤더 추가
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

# 요청을 보내고 응답 읽기
with urllib.request.urlopen(req) as response:
    response_data = response.read().decode('utf-8')
    print(response_data)
```

### Handling Timeouts

Set a timeout to prevent your program from hanging indefinitely:

```python
import urllib.request
import urllib.error
import socket

try:
    # Set timeout to 10 seconds
    response = urllib.request.urlopen('https://www.python.org/', timeout=10)
    html = response.read().decode('utf-8')
except socket.timeout:
    print("Request timed out")
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
```

### 타임아웃 처리

프로그램이 무기한 중단되는 것을 방지하기 위해 타임아웃을 설정합니다:

```python
import urllib.request
import urllib.error
import socket

try:
    # 타임아웃을 10초로 설정
    response = urllib.request.urlopen('https://www.python.org/', timeout=10)
    html = response.read().decode('utf-8')
except socket.timeout:
    print("요청 시간 초과")
except urllib.error.URLError as e:
    print(f"URL 오류: {e.reason}")
```

### Using Proxies

You can route your requests through a proxy:

```python
import urllib.request

# Setup proxy handler
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
})

# Build and install opener
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

# Now all urlopen calls will use the proxy
response = urllib.request.urlopen('https://www.python.org/')
```

### 프록시 사용하기

프록시를 통해 요청을 라우팅할 수 있습니다:

```python
import urllib.request

# 프록시 핸들러 설정
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
})

# 오프너 구축 및 설치
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

# 이제 모든 urlopen 호출이 프록시를 사용합니다
response = urllib.request.urlopen('https://www.python.org/')
```

### Authentication

For Basic HTTP Authentication:

```python
import urllib.request
import base64

# Setup authentication details
username = 'user'
password = 'pass123'
auth_string = f"{username}:{password}"
auth_bytes = auth_string.encode('utf-8')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

# Create a request with authentication header
url = 'https://httpbin.org/basic-auth/user/pass123'
req = urllib.request.Request(url)
req.add_header('Authorization', f'Basic {auth_b64}')

# Send the request
try:
    with urllib.request.urlopen(req) as response:
        print(f"Status: {response.status}")
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
```

For sites requiring more complex authentication, you might need to use cookies or session handling.

### 인증

기본 HTTP 인증을 위해:

```python
import urllib.request
import base64

# 인증 세부 정보 설정
username = 'user'
password = 'pass123'
auth_string = f"{username}:{password}"
auth_bytes = auth_string.encode('utf-8')
auth_b64 = base64.b64encode(auth_bytes).decode('ascii')

# 인증 헤더가 있는 요청 생성
url = 'https://httpbin.org/basic-auth/user/pass123'
req = urllib.request.Request(url)
req.add_header('Authorization', f'Basic {auth_b64}')

# 요청 보내기
try:
    with urllib.request.urlopen(req) as response:
        print(f"상태: {response.status}")
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"HTTP 오류: {e.code} - {e.reason}")
```

더 복잡한 인증이 필요한 사이트의 경우, 쿠키나 세션 처리를 사용해야 할 수 있습니다.

### Downloading Files

To download a file:

```python
import urllib.request

# Download a file to the local filesystem
url = 'https://www.python.org/static/img/python-logo.png'
local_filename, headers = urllib.request.urlretrieve(url, 'python-logo.png')

print(f"Downloaded to: {local_filename}")
print(f"Headers: {headers}")
```

For larger files, it's better to stream the download:

```python
import urllib.request

url = 'https://www.python.org/static/img/python-logo.png'
with urllib.request.urlopen(url) as response:
    with open('python-logo.png', 'wb') as out_file:
        # Read and write in chunks (8KB chunks)
        block_size = 8192
        while True:
            block = response.read(block_size)
            if not block:
                break
            out_file.write(block)
```

### 파일 다운로드

파일을 다운로드하려면:

```python
import urllib.request

# 파일을 로컬 파일 시스템에 다운로드
url = 'https://www.python.org/static/img/python-logo.png'
local_filename, headers = urllib.request.urlretrieve(url, 'python-logo.png')

print(f"다운로드 위치: {local_filename}")
print(f"헤더: {headers}")
```

더 큰 파일의 경우, 스트리밍 방식으로 다운로드하는 것이 좋습니다:

```python
import urllib.request

url = 'https://www.python.org/static/img/python-logo.png'
with urllib.request.urlopen(url) as response:
    with open('python-logo.png', 'wb') as out_file:
        # 청크 단위로 읽고 쓰기 (8KB 청크)
        block_size = 8192
        while True:
            block = response.read(block_size)
            if not block:
                break
            out_file.write(block)
```

## urllib.error - Exception Handling

The `urllib.error` module defines exceptions raised by `urllib.request`. The most common ones are:

### HTTPError

Raised when the server returns an HTTP error status:

```python
import urllib.request
import urllib.error

try:
    # Try to access a URL that returns a 404 error
    response = urllib.request.urlopen('https://www.python.org/nonexistent')
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
    # You can also access the response headers and data if available
    print(f"Headers: {e.headers}")
    # The error response body can be read with e.read()
```

### URLError

Raised when there's a problem with the URL or network itself:

```python
import urllib.request
import urllib.error

try:
    # Try to access a non-existent server
    response = urllib.request.urlopen('https://nonexistent-server.org/', timeout=5)
except urllib.error.URLError as e:
    print(f"URL Error: {e.reason}")
```

## urllib.error - 예외 처리

`urllib.error` 모듈은 `urllib.request`에 의해 발생하는 예외를 정의합니다. 가장 일반적인 것들은 다음과 같습니다:

### HTTPError

서버가 HTTP 오류 상태를 반환할 때 발생합니다:

```python
import urllib.request
import urllib.error

try:
    # 404 오류를 반환하는 URL에 접근 시도
    response = urllib.request.urlopen('https://www.python.org/nonexistent')
except urllib.error.HTTPError as e:
    print(f"HTTP 오류: {e.code} - {e.reason}")
    # 사용 가능한 경우 응답 헤더와 데이터에도 액세스할 수 있습니다
    print(f"헤더: {e.headers}")
    # 오류 응답 본문은 e.read()로 읽을 수 있습니다
```

### URLError

URL이나 네트워크 자체에 문제가 있을 때 발생합니다:

```python
import urllib.request
import urllib.error

try:
    # 존재하지 않는 서버에 접근 시도
    response = urllib.request.urlopen('https://nonexistent-server.org/', timeout=5)
except urllib.error.URLError as e:
    print(f"URL 오류: {e.reason}")
```

## urllib.parse - URL Parsing and Manipulation

The `urllib.parse` module provides functions for parsing URLs and working with them.

### Parsing URLs

```python
import urllib.parse

# Parse a URL into components
url = "https://www.example.com:8080/path?query=value#fragment"
parsed_url = urllib.parse.urlparse(url)

print(f"Scheme: {parsed_url.scheme}")  # https
print(f"Netloc: {parsed_url.netloc}")  # www.example.com:8080
print(f"Path: {parsed_url.path}")      # /path
print(f"Query: {parsed_url.query}")    # query=value
print(f"Fragment: {parsed_url.fragment}")  # fragment

# You can also use urlsplit which is similar but doesn't split params
split_url = urllib.parse.urlsplit(url)
```

### URL Joining

```python
import urllib.parse

# Combine a base URL with a relative URL
base = "https://www.example.com/path/"
relative = "../other/file.html"
joined_url = urllib.parse.urljoin(base, relative)

print(f"Joined URL: {joined_url}")  # https://www.example.com/other/file.html
```

### Query String Manipulation

```python
import urllib.parse

# Parse query string to a dictionary
query_string = "name=John&age=30"
parsed_query = urllib.parse.parse_qs(query_string)
print(parsed_query)  # {'name': ['John'], 'age': ['30']}

# Or parse to a list of tuples
parsed_query_list = urllib.parse.parse_qsl(query_string)
print(parsed_query_list)  # [('name', 'John'), ('age', '30')]

# Build a query string from a dictionary
params = {'name': 'John', 'age': '30'}
query_string = urllib.parse.urlencode(params)
print(query_string)  # name=John&age=30

# Build a query string from a list of tuples
params_list = [('name', 'John'), ('age', '30')]
query_string = urllib.parse.urlencode(params_list)
print(query_string)  # name=John&age=30
```

## urllib.parse - URL 파싱 및 조작

`urllib.parse` 모듈은 URL을 파싱하고 작업하기 위한 함수를 제공합니다.

### URL 파싱

```python
import urllib.parse

# URL을 구성 요소로 파싱
url = "https://www.example.com:8080/path?query=value#fragment"
parsed_url = urllib.parse.urlparse(url)

print(f"스킴: {parsed_url.scheme}")  # https
print(f"넷록: {parsed_url.netloc}")  # www.example.com:8080
print(f"경로: {parsed_url.path}")      # /path
print(f"쿼리: {parsed_url.query}")    # query=value
print(f"프래그먼트: {parsed_url.fragment}")  # fragment

# urlsplit도 사용할 수 있으며 이는 비슷하지만 params를 분할하지 않습니다
split_url = urllib.parse.urlsplit(url)
```

### URL 결합

```python
import urllib.parse

# 기본 URL과 상대 URL 결합
base = "https://www.example.com/path/"
relative = "../other/file.html"
joined_url = urllib.parse.urljoin(base, relative)

print(f"결합된 URL: {joined_url}")  # https://www.example.com/other/file.html
```

### 쿼리 문자열 조작

```python
import urllib.parse

# 쿼리 문자열을 사전으로 파싱
query_string = "name=John&age=30"
parsed_query = urllib.parse.parse_qs(query_string)
print(parsed_query)  # {'name': ['John'], 'age': ['30']}

# 또는 튜플 목록으로 파싱
parsed_query_list = urllib.parse.parse_qsl(query_string)
print(parsed_query_list)  # [('name', 'John'), ('age', '30')]

# 사전에서 쿼리 문자열 생성
params = {'name': 'John', 'age': '30'}
query_string = urllib.parse.urlencode(params)
print(query_string)  # name=John&age=30

# 튜플 목록에서 쿼리 문자열 생성
params_list = [('name', 'John'), ('age', '30')]
query_string = urllib.parse.urlencode(params_list)
print(query_string)  # name=John&age=30
```

### URL Encoding and Decoding

```python
import urllib.parse

# Encode special characters in a URL component
original = "path with spaces and $ymbols"
encoded = urllib.parse.quote(original)
print(f"Encoded: {encoded}")  # path%20with%20spaces%20and%20%24ymbols

# Decode back to original
decoded = urllib.parse.unquote(encoded)
print(f"Decoded: {decoded}")  # path with spaces and $ymbols

# Encode an entire URL
url = "https://example.com/path with spaces"
encoded_url = urllib.parse.quote_plus(url)
print(f"Encoded URL: {encoded_url}")  # https%3A%2F%2Fexample.com%2Fpath+with+spaces
```

### URL 인코딩 및 디코딩

```python
import urllib.parse

# URL 구성 요소에서 특수 문자 인코딩
original = "path with spaces and $ymbols"
encoded = urllib.parse.quote(original)
print(f"인코딩됨: {encoded}")  # path%20with%20spaces%20and%20%24ymbols

# 원래대로 디코딩
decoded = urllib.parse.unquote(encoded)
print(f"디코딩됨: {decoded}")  # path with spaces and $ymbols

# 전체 URL 인코딩
url = "https://example.com/path with spaces"
encoded_url = urllib.parse.quote_plus(url)
print(f"인코딩된 URL: {encoded_url}")  # https%3A%2F%2Fexample.com%2Fpath+with+spaces
```

## urllib.robotparser - Working with robots.txt

The `urllib.robotparser` module provides a class to check if a user agent can fetch a URL according to the rules in a `robots.txt` file.

```python
import urllib.robotparser

# Create a RobotFileParser instance
rp = urllib.robotparser.RobotFileParser()

# Set the URL of the robots.txt file
rp.set_url('https://www.python.org/robots.txt')

# Read and parse the robots.txt file
rp.read()

# Check if a user agent can fetch a URL
can_fetch = rp.can_fetch('MyBot', 'https://www.python.org/downloads/')
print(f"Can fetch: {can_fetch}")

# Check a disallowed URL
can_fetch = rp.can_fetch('MyBot', 'https://www.python.org/private/')
print(f"Can fetch private area: {can_fetch}")

# Get the crawl delay for a user agent
crawl_delay = rp.crawl_delay('MyBot')
print(f"Crawl delay: {crawl_delay}")
```

## urllib.robotparser - robots.txt 작업하기

`urllib.robotparser` 모듈은 사용자 에이전트가 `robots.txt` 파일의 규칙에 따라 URL을 가져올 수 있는지 확인하는 클래스를 제공합니다.

```python
import urllib.robotparser

# RobotFileParser 인스턴스 생성
rp = urllib.robotparser.RobotFileParser()

# robots.txt 파일의 URL 설정
rp.set_url('https://www.python.org/robots.txt')

# robots.txt 파일 읽기 및 파싱
rp.read()

# 사용자 에이전트가 URL을 가져올 수 있는지 확인
can_fetch = rp.can_fetch('MyBot', 'https://www.python.org/downloads/')
print(f"가져올 수 있음: {can_fetch}")

# 허용되지 않은 URL 확인
can_fetch = rp.can_fetch('MyBot', 'https://www.python.org/private/')
print(f"비공개 영역 가져올 수 있음: {can_fetch}")

# 사용자 에이전트의 크롤링 지연 획득
crawl_delay = rp.crawl_delay('MyBot')
print(f"크롤링 지연: {crawl_delay}")
```

## Practical Examples

### Example 1: Web Scraping with urllib

Here's a simple example of how to scrape a webpage:

```python
import urllib.request
import urllib.error
from html.parser import HTMLParser

class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self.reading_title = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.reading_title = True
            
    def handle_endtag(self, tag):
        if tag == 'title':
            self.reading_title = False
            
    def handle_data(self, data):
        if self.reading_title:
            self.title = data

def get_page_title(url):
    try:
        # Create a request with a user-agent header
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        # Open the URL
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Parse the HTML to extract the title
            parser = TitleParser()
            parser.feed(html)
            
            return parser.title
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function
url = 'https://www.python.org/'
title = get_page_title(url)
print(f"The title of {url} is: {title}")
```

## 실용적인 예제

### 예제 1: urllib을 사용한 웹 스크래핑

다음은 웹 페이지를 스크래핑하는 간단한 예제입니다:

```python
import urllib.request
import urllib.error
from html.parser import HTMLParser

class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = None
        self.reading_title = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.reading_title = True
            
    def handle_endtag(self, tag):
        if tag == 'title':
            self.reading_title = False
            
    def handle_data(self, data):
        if self.reading_title:
            self.title = data

def get_page_title(url):
    try:
        # 사용자 에이전트 헤더가 있는 요청 생성
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        
        # URL 열기
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # HTML 파싱하여 제목 추출
            parser = TitleParser()
            parser.feed(html)
            
            return parser.title
    except urllib.error.URLError as e:
        print(f"URL 가져오기 오류: {e.reason}")
    except Exception as e:
        print(f"오류 발생: {e}")

# 함수 테스트
url = 'https://www.python.org/'
title = get_page_title(url)
print(f"{url}의 제목은: {title}")
```

### Example 2: Downloading Files with Progress

Here's how to download a file while showing a progress indicator:

```python
import urllib.request
import os
import sys

def download_with_progress(url, destination):
    def report_progress(block_num, block_size, total_size):
        # Calculate the progress as a percentage
        read_so_far = block_num * block_size
        if total_size > 0:
            percent = read_so_far * 100 / total_size
            # Display progress bar
            bar_length = 50
            filled_length = int(bar_length * read_so_far // total_size)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            sys.stdout.write(f"\r|{bar}| {percent:.1f}% ({read_so_far}/{total_size} bytes)")
            sys.stdout.flush()
            if read_so_far >= total_size:
                # Add a newline after the progress bar when done
                sys.stdout.write('\n')
        else:
            # If total_size is unknown, just show the downloaded amount
            sys.stdout.write(f"\rDownloaded {read_so_far} bytes")
            sys.stdout.flush()

    print(f"Downloading {url} to {destination}...")
    
    try:
        # Use the reporthook parameter to track progress
        urllib.request.urlretrieve(url, destination, reporthook=report_progress)
        print(f"Download complete: {destination}")
        return True
    except urllib.error.URLError as e:
        print(f"Error during download: {e.reason}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
download_with_progress(
    'https://www.python.org/static/img/python-logo.png', 
    'python-logo.png'
)
```

### 예제 2: 진행 상황을 보여주며 파일 다운로드하기

다음은 진행 상황 표시기를 보여주면서 파일을 다운로드하는 방법입니다:

```python
import urllib.request
import os
import sys

def download_with_progress(url, destination):
    def report_progress(block_num, block_size, total_size):
        # 진행 상황을 백분율로 계산
        read_so_far = block_num * block_size
        if total_size > 0:
            percent = read_so_far * 100 / total_size
            # 진행 막대 표시
            bar_length = 50
            filled_length = int(bar_length * read_so_far // total_size)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            sys.stdout.write(f"\r|{bar}| {percent:.1f}% ({read_so_far}/{total_size} 바이트)")
            sys.stdout.flush()
            if read_so_far >= total_size:
                # 완료 시 진행 막대 뒤에 줄바꿈 추가
                sys.stdout.write('\n')
        else:
            # total_size를 알 수 없는 경우 다운로드된 양만 표시
            sys.stdout.write(f"\r{read_so_far} 바이트 다운로드됨")
            sys.stdout.flush()

    print(f"{url}을(를) {destination}(으)로 다운로드 중...")
    
    try:
        # 진행 상황을 추적하기 위해 reporthook 매개변수 사용
        urllib.request.urlretrieve(url, destination, reporthook=report_progress)
        print(f"다운로드 완료: {destination}")
        return True
    except urllib.error.URLError as e:
        print(f"다운로드 중 오류: {e.reason}")
        return False
    except Exception as e:
        print(f"오류 발생: {e}")
        return False

# 사용 예
download_with_progress(
    'https://www.python.org/static/img/python-logo.png', 
    'python-logo.png'
)
```

### Example 3: Create a URL Shortener

This example simulates a URL shortener service using the bitly API:

```python
import urllib.request
import urllib.parse
import urllib.error
import json

def shorten_url(long_url, access_token):
    # API endpoint for creating a bitlink
    api_url = "https://api-ssl.bitly.com/v4/shorten"
    
    # Prepare the payload
    payload = {
        "long_url": long_url
    }
    payload_json = json.dumps(payload).encode('utf-8')
    
    # Create the request
    req = urllib.request.Request(api_url, data=payload_json, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', f'Bearer {access_token}')
    
    try:
        # Send the request
        with urllib.request.urlopen(req) as response:
            # Parse the JSON response
            response_data = response.read().decode('utf-8')
            data = json.loads(response_data)
            return data.get('link')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        # Read and print the error response
        error_data = e.read().decode('utf-8')
        print(f"Error details: {error_data}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage (you would need a valid access token)
if __name__ == "__main__":
    # Replace with your actual access token
    access_token = "YOUR_ACCESS_TOKEN"
    url_to_shorten = "https://www.python.org/doc/essays/blurb/"
    
    shortened_url = shorten_url(url_to_shorten, access_token)
    if shortened_url:
        print(f"Shortened URL: {shortened_url}")
    else:
        print("Failed to shorten URL")
```

### 예제 3: URL 단축기 만들기

이 예제는 bitly API를 사용하여 URL 단축 서비스를 시뮬레이션합니다:

```python
import urllib.request
import urllib.parse
import urllib.error
import json

def shorten_url(long_url, access_token):
    # bitlink 생성을 위한 API 엔드포인트
    api_url = "https://api-ssl.bitly.com/v4/shorten"
    
    # 페이로드 준비
    payload = {
        "long_url": long_url
    }
    payload_json = json.dumps(payload).encode('utf-8')
    
    # 요청 생성
    req = urllib.request.Request(api_url, data=payload_json, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Authorization', f'Bearer {access_token}')
    
    try:
        # 요청 보내기
        with urllib.request.urlopen(req) as response:
            # JSON 응답 파싱
            response_data = response.read().decode('utf-8')
            data = json.loads(response_data)
            return data.get('link')
    except urllib.error.HTTPError as e:
        print(f"HTTP 오류: {e.code} - {e.reason}")
        # 오류 응답 읽고 출력
        error_data = e.read().decode('utf-8')
        print(f"오류 세부 정보: {error_data}")
        return None
    except urllib.error.URLError as e:
        print(f"URL 오류: {e.reason}")
        return None
    except Exception as e:
        print(f"오류 발생: {e}")
        return None

# 사용 예 (유효한 액세스 토큰이 필요합니다)
if __name__ == "__main__":
    # 실제 액세스 토큰으로 대체
    access_token = "YOUR_ACCESS_TOKEN"
    url_to_shorten = "https://www.python.org/doc/essays/blurb/"
    
    shortened_url = shorten_url(url_to_shorten, access_token)
    if shortened_url:
        print(f"단축된 URL: {shortened_url}")
    else:
        print("URL 단축 실패")
```

## Best Practices and Tips

1. **Use context managers** (`with` statements) when opening URLs to ensure connections are properly closed:
   ```python
   with urllib.request.urlopen(url) as response:
       data = response.read()
   ```

2. **Always handle exceptions** when making network requests:
   ```python
   try:
       response = urllib.request.urlopen(url)
   except urllib.error.HTTPError as e:
       # Handle HTTP errors (e.g., 404, 500)
   except urllib.error.URLError as e:
       # Handle URL errors (e.g., network issues)
   ```

3. **Set timeouts** to prevent your program from hanging indefinitely:
   ```python
   response = urllib.request.urlopen(url, timeout=10)
   ```

4. **Use a custom user-agent** to identify your application:
   ```python
   req = urllib.request.Request(url, headers={'User-Agent': 'MyApp/1.0'})
   ```

5. **Respect robots.txt** for web crawling:
   ```python
   rp = urllib.robotparser.RobotFileParser()
   rp.set_url(f"{base_url}/robots.txt")
   rp.read()
   if rp.can_fetch('MyBot', url):
       # Proceed with fetching the URL
   ```

6. **Consider rate limiting** to avoid overwhelming servers:
   ```python
   import time
   for url in urls:
       response = urllib.request.urlopen(url)
       # Process response
       time.sleep(1)  # Wait 1 second between requests
   ```

7. **Use the `requests` library** for more complex applications. While `urllib` is part of the standard library, `requests` provides a more user-friendly API:
   ```python
   # Install with: pip install requests
   import requests
   response = requests.get(url)
   data = response.json()
   ```

## 모범 사례 및 팁

1. **컨텍스트 관리자** (`with` 문) 사용하여 URL을 열 때 연결이 적절히 닫히도록 보장:
   ```python
   with urllib.request.urlopen(url) as response:
       data = response.read()
   ```

2. **네트워크 요청을 할 때 항상 예외 처리**:
   ```python
   try:
       response = urllib.request.urlopen(url)
   except urllib.error.HTTPError as e:
       # HTTP 오류 처리 (예: 404, 500)
   except urllib.error.URLError as e:
       # URL 오류 처리 (예: 네트워크 문제)
   ```

3. **타임아웃 설정**하여 프로그램이 무기한 중단되는 것 방지:
   ```python
   response = urllib.request.urlopen(url, timeout=10)
   ```

4. **사용자 정의 사용자 에이전트**를 사용하여 애플리케이션 식별:
   ```python
   req = urllib.request.Request(url, headers={'User-Agent': 'MyApp/1.0'})
   ```

5. **웹 크롤링을 위한 robots.txt 존중**:
   ```python
   rp = urllib.robotparser.RobotFileParser()
   rp.set_url(f"{base_url}/robots.txt")
   rp.read()
   if rp.can_fetch('MyBot', url):
       # URL 가져오기 진행
   ```

6. **서버 과부하를 방지하기 위한 속도 제한 고려**:
   ```python
   import time
   for url in urls:
       response = urllib.request.urlopen(url)
       # 응답 처리
       time.sleep(1)  # 요청 사이에 1초 대기
   ```

7. **더 복잡한 애플리케이션을 위한 `requests` 라이브러리 사용**. `urllib`은 표준 라이브러리의 일부이지만, `requests`는 더 사용자 친화적인 API를 제공합니다:
   ```python
   # 설치: pip install requests
   import requests
   response = requests.get(url)
   data = response.json()
   ```

## Conclusion

The `urllib` package is a versatile tool for working with URLs and network requests in Python. It provides all the essential functionality needed for fetching web resources, handling errors, parsing URLs, and working with query parameters. While modern alternatives like the `requests` library offer a more streamlined API, understanding `urllib` is beneficial for Python developers because it's part of the standard library and doesn't require external dependencies.

By mastering the various submodules of `urllib`, you can build robust applications that interact with web services, scrape websites, download files, and process URLs efficiently.

## 결론

`urllib` 패키지는 Python에서 URL 및 네트워크 요청을 다루기 위한 다재다능한 도구입니다. 웹 리소스 가져오기, 오류 처리, URL 파싱, 쿼리 매개변수 작업에 필요한 모든 필수 기능을 제공합니다. `requests` 라이브러리와 같은 현대적인 대안이 더 간소화된 API를 제공하지만, `urllib`을 이해하는 것은 Python 개발자에게 유익합니다. 이는 표준 라이브러리의 일부이며 외부 의존성이 필요 없기 때문입니다.

`urllib`의 다양한 하위 모듈을 마스터함으로써, 웹 서비스와 상호 작용하고, 웹사이트를 스크래핑하고, 파일을 다운로드하고, URL을 효율적으로 처리하는 강력한 애플리케이션을 구축할 수 있습니다.
