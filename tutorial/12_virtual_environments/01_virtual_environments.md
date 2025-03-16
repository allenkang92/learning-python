# 12. Virtual Environments and Packages

## 12.1. Introduction

1. Python applications will often use packages and modules that don't come as part of the standard library. Applications will sometimes need a specific version of a library, because the application may require that a particular bug has been fixed or the application may be written using an obsolete version of the library's interface.

파이썬 애플리케이션은 종종 표준 라이브러리의 일부로 제공되지 않는 패키지와 모듈을 사용합니다. 애플리케이션은 때로 특정 버그가 수정되었거나 라이브러리 인터페이스의 구버전을 사용하여 작성되었기 때문에 라이브러리의 특정 버전이 필요할 수 있습니다.

2. This means it may not be possible for one Python installation to meet the requirements of every application. If application A needs version 1.0 of a particular module but application B needs version 2.0, then the requirements are in conflict and installing either version 1.0 or 2.0 will leave one application unable to run.

이는 하나의 파이썬 설치로 모든 애플리케이션의 요구 사항을 충족시키는 것이 불가능할 수 있음을 의미합니다. 애플리케이션 A가 특정 모듈의 버전 1.0이 필요하지만 애플리케이션 B는 버전 2.0이 필요한 경우, 요구 사항이 충돌하여 버전 1.0 또는 2.0을 설치하면 한 애플리케이션은 실행할 수 없게 됩니다.

3. The solution for this problem is to create a virtual environment, a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

이 문제의 해결책은 가상 환경을 만드는 것입니다. 가상 환경은 특정 버전의 파이썬 설치와 여러 추가 패키지를 포함하는 독립적인 디렉토리 트리입니다.

4. Different applications can then use different virtual environments. To resolve the earlier example of conflicting requirements, application A can have its own virtual environment with version 1.0 installed while application B has another virtual environment with version 2.0. If application B requires a library be upgraded to version 3.0, this will not affect application A's environment.

서로 다른 애플리케이션은 서로 다른 가상 환경을 사용할 수 있습니다. 앞서 언급한 충돌하는 요구 사항의 예를 해결하기 위해, 애플리케이션 A는 버전 1.0이 설치된 자체 가상 환경을 가질 수 있고, 애플리케이션 B는 버전 2.0이 설치된 다른 가상 환경을 가질 수 있습니다. 애플리케이션 B가 라이브러리를 버전 3.0으로 업그레이드해야 하는 경우, 이는 애플리케이션 A의 환경에 영향을 미치지 않습니다.

## 12.2. Creating Virtual Environments

5. The module used to create and manage virtual environments is called venv. venv will install the Python version from which the command was run (as reported by the --version option). For instance, executing the command with python3.12 will install version 3.12.

가상 환경을 생성하고 관리하는 데 사용되는 모듈은 venv입니다. venv는 명령이 실행된 파이썬 버전을 설치합니다(--version 옵션으로 보고되는 것처럼). 예를 들어, python3.12로 명령을 실행하면 버전 3.12가 설치됩니다.

6. To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

가상 환경을 만들려면, 배치할 디렉토리를 결정하고 디렉토리 경로와 함께 venv 모듈을 스크립트로 실행하세요:

```python
python -m venv tutorial-env
```

7. This will create the tutorial-env directory if it doesn't exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

이것은 tutorial-env 디렉토리가 존재하지 않으면 생성하고, 그 안에 파이썬 인터프리터의 복사본과 다양한 지원 파일을 포함하는 디렉토리도 만듭니다.

8. A common directory location for a virtual environment is .venv. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.

가상 환경에 대한 일반적인 디렉토리 위치는 .venv입니다. 이 이름은 디렉토리를 쉘에서 일반적으로 숨겨두어 방해가 되지 않게 하면서도 디렉토리가 존재하는 이유를 설명하는 이름을 제공합니다. 또한 일부 도구가 지원하는 .env 환경 변수 정의 파일과의 충돌을 방지합니다.

9. Once you've created a virtual environment, you may activate it.

가상 환경을 만든 후에는 활성화할 수 있습니다.

10. On Windows, run:

Windows에서는 다음을 실행하세요:

```
tutorial-env\Scripts\activate
```

11. On Unix or MacOS, run:

Unix나 MacOS에서는 다음을 실행하세요:

```
source tutorial-env/bin/activate
```

12. (This script is written for the bash shell. If you use the csh or fish shells, there are alternate activate.csh and activate.fish scripts you should use instead.)

(이 스크립트는 bash 쉘용으로 작성되었습니다. csh나 fish 쉘을 사용하는 경우, 대신 activate.csh 및 activate.fish 스크립트를 사용해야 합니다.)

13. Activating the virtual environment will change your shell's prompt to show what virtual environment you're using, and modify the environment so that running python will get you that particular version and installation of Python. For example:

가상 환경을 활성화하면 사용 중인 가상 환경을 표시하기 위해 쉘 프롬프트가 변경되고, python을 실행하면 해당 특정 버전과 파이썬 설치를 사용하도록 환경이 수정됩니다. 예를 들어:

```
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

14. To deactivate a virtual environment, type:

가상 환경을 비활성화하려면 다음을 입력하세요:

```
deactivate
```

15. into the terminal.

터미널에 입력하세요.

## 12.3. Managing Packages with pip

16. You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the Python Package Index. You can browse the Python Package Index by going to it in your web browser.

pip라는 프로그램을 사용하여 패키지를 설치, 업그레이드 및 제거할 수 있습니다. 기본적으로 pip는 Python Package Index에서 패키지를 설치합니다. 웹 브라우저에서 Python Package Index를 탐색할 수 있습니다.

17. pip has a number of subcommands: "install", "uninstall", "freeze", etc. (Consult the Installing Python Modules guide for complete documentation for pip.)

pip에는 "install", "uninstall", "freeze" 등의 여러 하위 명령이 있습니다. (pip에 대한 전체 문서는 Python 모듈 설치 가이드를 참조하세요.)

18. You can install the latest version of a package by specifying a package's name:

패키지 이름을 지정하여 패키지의 최신 버전을 설치할 수 있습니다:

```
(tutorial-env) $ python -m pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

19. You can also install a specific version of a package by giving the package name followed by == and the version number:

패키지 이름과 == 다음에 버전 번호를 입력하여 패키지의 특정 버전을 설치할 수도 있습니다:

```
(tutorial-env) $ python -m pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

20. If you re-run this command, pip will notice that the requested version is already installed and do nothing. You can supply a different version number to get that version, or you can run python -m pip install --upgrade to upgrade the package to the latest version:

이 명령을 다시 실행하면, pip는 요청된 버전이 이미 설치되어 있음을 알고 아무 작업도 하지 않습니다. 다른 버전 번호를 제공하여 해당 버전을 얻거나, python -m pip install --upgrade를 실행하여 패키지를 최신 버전으로 업그레이드할 수 있습니다:

```
(tutorial-env) $ python -m pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

21. python -m pip uninstall followed by one or more package names will remove the packages from the virtual environment.

python -m pip uninstall 다음에 하나 이상의 패키지 이름을 입력하면 가상 환경에서 패키지가 제거됩니다.

22. python -m pip show will display information about a particular package:

python -m pip show는 특정 패키지에 대한 정보를 표시합니다:

```
(tutorial-env) $ python -m pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

23. python -m pip list will display all of the packages installed in the virtual environment:

python -m pip list는 가상 환경에 설치된 모든 패키지를 표시합니다:

```
(tutorial-env) $ python -m pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

24. python -m pip freeze will produce a similar list of the installed packages, but the output uses the format that python -m pip install expects. A common convention is to put this list in a requirements.txt file:

python -m pip freeze는 설치된 패키지의 유사한 목록을 생성하지만, 출력은 python -m pip install이 예상하는 형식을 사용합니다. 일반적인 관례는 이 목록을 requirements.txt 파일에 넣는 것입니다:

```
(tutorial-env) $ python -m pip freeze > requirements.txt
(tutorial-env) $ cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

25. The requirements.txt can then be committed to version control and shipped as part of an application. Users can then install all the necessary packages with install -r:

requirements.txt는 버전 관리에 커밋되고 애플리케이션의 일부로 배포될 수 있습니다. 사용자는 install -r로 필요한 모든 패키지를 설치할 수 있습니다:

```
(tutorial-env) $ python -m pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

26. pip has many more options. Consult the Installing Python Modules guide for complete documentation for pip. When you've written a package and want to make it available on the Python Package Index, consult the Python packaging user guide.

pip에는 더 많은 옵션이 있습니다. pip에 대한 전체 문서는 Python 모듈 설치 가이드를 참조하세요. 패키지를 작성하고 Python Package Index에서 사용할 수 있게 하려면, Python 패키징 사용자 가이드를 참조하세요.
