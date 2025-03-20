# 5. The import system

# 5. 임포트 시스템

Python code in one module gains access to the code in another module by the process of importing it.
한 모듈의 파이썬 코드는 다른 모듈을 임포트하는 과정을 통해 해당 모듈의 코드에 접근할 수 있습니다.
The import statement is the most common way of invoking the import machinery, but it is not the only way.
import 문은 임포트 기능을 호출하는 가장 일반적인 방법이지만, 유일한 방법은 아닙니다.
Functions such as importlib.import_module() and built-in __import__() can also be used to invoke the import machinery.
importlib.import_module()과 내장 함수 __import__()와 같은 함수들도 임포트 기능을 호출하는 데 사용될 수 있습니다.

The import statement combines two operations; it searches for the named module, then it binds the results of that search to a name in the local scope. The search operation of the import statement is defined as a call to the __import__() function, with the appropriate arguments. The return value of __import__() is used to perform the name binding operation of the import statement. See the import statement for the exact details of that name binding operation.

import 문은 두 가지 작업을 결합합니다. 먼저 지정된 모듈을 검색한 다음, 그 검색 결과를 로컬 스코프의 이름에 바인딩합니다. import 문의 검색 작업은 적절한 인수를 사용하여 __import__() 함수를 호출하는 것으로 정의됩니다. __import__()의 반환값은 import 문의 이름 바인딩 작업을 수행하는 데 사용됩니다. 이름 바인딩 작업의 정확한 세부 사항은 import 문을 참조하세요.

A direct call to __import__() performs only the module search and, if found, the module creation operation. While certain side-effects may occur, such as the importing of parent packages, and the updating of various caches (including sys.modules), only the import statement performs a name binding operation.

__import__()에 대한 직접 호출은 모듈 검색과, 모듈이 발견되었을 경우, 모듈 생성 작업만 수행합니다. 부모 패키지의 임포트나 다양한 캐시(sys.modules 포함)의 업데이트 같은 특정 부작용이 발생할 수 있지만, 이름 바인딩 작업은 import 문만 수행합니다.

When an import statement is executed, the standard builtin __import__() function is called. Other mechanisms for invoking the import system (such as importlib.import_module()) may choose to bypass __import__() and use their own solutions to implement import semantics.

import 문이 실행될 때, 표준 내장 함수 __import__()가 호출됩니다. 임포트 시스템을 호출하는 다른 메커니즘(예: importlib.import_module())은 __import__()를 우회하고 자체 솔루션을 사용하여 임포트 의미론을 구현할 수 있습니다.

When a module is first imported, Python searches for the module and if found, it creates a module object [1], initializing it. If the named module cannot be found, a ModuleNotFoundError is raised. Python implements various strategies to search for the named module when the import machinery is invoked. These strategies can be modified and extended by using various hooks described in the sections below.

모듈이 처음 임포트될 때, 파이썬은 해당 모듈을 검색하고 발견되면 모듈 객체[1]를 생성하여 초기화합니다. 지정된 모듈을 찾을 수 없는 경우 ModuleNotFoundError가 발생합니다. 파이썬은 임포트 기능이 호출될 때 지정된 모듈을 검색하기 위한 다양한 전략을 구현합니다. 이러한 전략은 아래 섹션에서 설명하는 다양한 훅을 사용하여 수정하고 확장할 수 있습니다.

Changed in version 3.3: The import system has been updated to fully implement the second phase of PEP 302. There is no longer any implicit import machinery - the full import system is exposed through sys.meta_path. In addition, native namespace package support has been implemented (see PEP 420).

버전 3.3에서 변경됨: 임포트 시스템이 PEP 302의 두 번째 단계를 완전히 구현하도록 업데이트되었습니다. 더 이상 암시적인 임포트 기능은 없으며, 전체 임포트 시스템은 sys.meta_path를 통해 노출됩니다. 또한, 네이티브 네임스페이스 패키지 지원이 구현되었습니다(PEP 420 참조).

## 5.1. importlib

The importlib module provides a rich API for interacting with the import system. For example importlib.import_module() provides a recommended, simpler API than built-in __import__() for invoking the import machinery. Refer to the importlib library documentation for additional detail.

importlib 모듈은 임포트 시스템과 상호 작용하기 위한 풍부한 API를 제공합니다. 예를 들어, importlib.import_module()은 임포트 기능을 호출하기 위해 내장 함수 __import__()보다 권장되는 더 간단한 API를 제공합니다. 추가 세부 정보는 importlib 라이브러리 문서를 참조하세요.

## 5.2. Packages

Python has only one type of module object, and all modules are of this type, regardless of whether the module is implemented in Python, C, or something else. To help organize modules and provide a naming hierarchy, Python has a concept of packages.

파이썬에는 단 하나의 모듈 객체 타입만 있으며, 모듈이 파이썬, C 또는 다른 것으로 구현되었는지 여부와 관계없이 모든 모듈은 이 타입입니다. 모듈을 구성하고 이름 계층 구조를 제공하기 위해, 파이썬에는 패키지 개념이 있습니다.

You can think of packages as the directories on a file system and modules as files within directories, but don't take this analogy too literally since packages and modules need not originate from the file system. For the purposes of this documentation, we'll use this convenient analogy of directories and files. Like file system directories, packages are organized hierarchically, and packages may themselves contain subpackages, as well as regular modules.

패키지를 파일 시스템의 디렉토리로, 모듈을 디렉토리 내의 파일로 생각할 수 있지만, 패키지와 모듈이 반드시 파일 시스템에서 비롯될 필요는 없으므로 이 비유를 너무 문자 그대로 받아들이지 마세요. 이 문서의 목적상, 우리는 디렉토리와 파일의 이 편리한 비유를 사용할 것입니다. 파일 시스템 디렉토리처럼, 패키지는 계층적으로 구성되며, 패키지 자체는 서브패키지와 일반 모듈을 포함할 수 있습니다.

It's important to keep in mind that all packages are modules, but not all modules are packages. Or put another way, packages are just a special kind of module. Specifically, any module that contains a __path__ attribute is considered a package.

모든 패키지는 모듈이지만, 모든 모듈이 패키지는 아니라는 점을 기억하는 것이 중요합니다. 다른 말로 하면, 패키지는 단지 특별한 종류의 모듈입니다. 구체적으로, __path__ 속성을 포함하는 모든 모듈은 패키지로 간주됩니다.

All modules have a name. Subpackage names are separated from their parent package name by a dot, akin to Python's standard attribute access syntax. Thus you might have a package called email, which in turn has a subpackage called email.mime and a module within that subpackage called email.mime.text.

모든 모듈에는 이름이 있습니다. 서브패키지 이름은 부모 패키지 이름과 점으로 구분되며, 이는 파이썬의 표준 속성 접근 구문과 유사합니다. 따라서 email이라는 패키지가 있을 수 있으며, 이 패키지에는 email.mime이라는 서브패키지와 그 서브패키지 내에 email.mime.text라는 모듈이 있을 수 있습니다.

### 5.2.1. Regular packages

Python defines two types of packages, regular packages and namespace packages. Regular packages are traditional packages as they existed in Python 3.2 and earlier. A regular package is typically implemented as a directory containing an __init__.py file. When a regular package is imported, this __init__.py file is implicitly executed, and the objects it defines are bound to names in the package's namespace. The __init__.py file can contain the same Python code that any other module can contain, and Python will add some additional attributes to the module when it is imported.

파이썬은 일반 패키지와 네임스페이스 패키지라는 두 가지 유형의 패키지를 정의합니다. 일반 패키지는 파이썬 3.2 이전에 존재했던 전통적인 패키지입니다. 일반 패키지는 일반적으로 __init__.py 파일을 포함하는 디렉토리로 구현됩니다. 일반 패키지가 임포트되면, 이 __init__.py 파일이 암시적으로 실행되고, 이 파일이 정의하는 객체는 패키지의 네임스페이스에 있는 이름에 바인딩됩니다. __init__.py 파일은 다른 모듈이 포함할 수 있는 것과 동일한 파이썬 코드를 포함할 수 있으며, 파이썬은 모듈이 임포트될 때 일부 추가 속성을 모듈에 추가합니다.

For example, the following file system layout defines a top level parent package with three subpackages:

예를 들어, 다음 파일 시스템 레이아웃은 세 개의 서브패키지가 있는 최상위 부모 패키지를 정의합니다:

```
spam/
    __init__.py
    foo/
        __init__.py
        bar/
            __init__.py
            baz.py
```

## 5.3. Searching

To begin the search, Python needs the fully qualified name of the module (or package, but for the purposes of this discussion, the difference is immaterial) being imported.  
검색을 시작하기 위해, 파이썬은 임포트되는 모듈(또는 패키지이지만, 이 논의의 목적상 차이는 중요하지 않음)의 완전히 정규화된 이름이 필요합니다. This name may come from various arguments to the import statement, or from the parameters to the importlib.import_module() or __import__() functions.  
이 이름은 import 문에 대한 다양한 인수에서 오거나, importlib.import_module() 또는 __import__() 함수에 대한 매개변수에서 올 수 있습니다.

### 5.3.3. Import hooks

The import machinery is designed to be extensible; the primary mechanism for this are the import hooks. There are two types of import hooks: meta hooks and import path hooks.  
임포트 기능은 확장 가능하도록 설계되었습니다. 이를 위한 주요 메커니즘은 임포트 훅입니다. 임포트 훅에는 메타 훅과 임포트 경로 훅이라는 두 가지 유형이 있습니다.

Meta hooks are called at the start of import processing, before any other import processing has occurred, other than sys.modules cache look up. This allows meta hooks to override sys.path processing, frozen modules, or even built-in modules. Meta hooks are registered by adding new finder objects to sys.meta_path, as described below.  
메타 훅은 sys.modules 캐시 조회를 제외한 다른 임포트 처리가 발생하기 전, 임포트 처리의 시작 시점에 호출됩니다. 이를 통해 메타 훅은 sys.path 처리, 동결된 모듈, 심지어 내장 모듈도 재정의할 수 있습니다. 메타 훅은 아래에 설명된 대로 sys.meta_path에 새로운 파인더 객체를 추가하여 등록됩니다.

Import path hooks are called as part of sys.path (or package.__path__) processing, at the point where their associated path item is encountered. Import path hooks are registered by adding new callables to sys.path_hooks as described below.  
임포트 경로 훅은 sys.path(또는 package.__path__) 처리의 일부로, 관련 경로 항목이 발견되는 시점에 호출됩니다. 임포트 경로 훅은 아래 설명된 대로 sys.path_hooks에 새로운 호출 가능 객체를 추가하여 등록됩니다.

### 5.3.4. The meta path

When the named module is not found in sys.modules, Python next searches sys.meta_path, which contains a list of meta path finder objects. These finders are queried in order to see if they know how to handle the named module. Meta path finders must implement a method called find_spec() which takes three arguments: a name, an import path, and (optionally) a target module. The meta path finder can use any strategy it wants to determine whether it can handle the named module or not.  
명명된 모듈이 sys.modules에서 발견되지 않으면, 파이썬은 다음으로 메타 경로 파인더 객체 목록을 포함하는 sys.meta_path를 검색합니다. 이 파인더들은 명명된 모듈을 처리하는 방법을 알고 있는지 확인하기 위해 순서대로 쿼리됩니다. 메타 경로 파인더는 이름, 임포트 경로, 그리고 (선택적으로) 대상 모듈이라는 세 가지 인수를 받는 find_spec()이라는 메서드를 구현해야 합니다. 메타 경로 파인더는 명명된 모듈을 처리할 수 있는지 여부를 결정하기 위해 원하는 전략을 사용할 수 있습니다.

If the meta path finder knows how to handle the named module, it returns a spec object. If it cannot handle the named module, it returns None. If sys.meta_path processing reaches the end of its list without returning a spec, then a ModuleNotFoundError is raised. Any other exceptions raised are simply propagated up, aborting the import process.  
명명된 모듈을 처리할 수 있으면 메타 경로 파인더는 스펙 객체를 반환하고, 그렇지 않으면 None을 반환합니다. sys.meta_path 처리가 스펙 반환 없이 끝나면 ModuleNotFoundError가 발생하며, 발생한 다른 예외는 위로 전파되어 임포트 과정을 중단합니다.

The find_spec() method of meta path finders is called with two or three arguments. The first is the fully qualified name of the module being imported, for example foo.bar.baz. The second argument is the path entries to use for the module search. For top-level modules, the second argument is None, but for submodules or subpackages, the second argument is the value of the parent package's __path__ attribute. If the appropriate __path__ attribute cannot be accessed, a ModuleNotFoundError is raised. The third argument is an existing module object that will be the target of loading later. The import system passes in a target module only during reload.  
메타 경로 파인더의 find_spec() 메서드는 두 개 또는 세 개의 인수로 호출됩니다. 첫 번째 인수는 임포트되는 모듈의 정규화된 이름(예: foo.bar.baz)이고, 두 번째 인수는 모듈 검색에 사용할 경로 항목입니다. 최상위 모듈인 경우 두 번째 인수는 None이며, 하위 모듈이나 서브패키지의 경우 두 번째 인수는 부모 패키지의 __path__ 속성 값이 전달됩니다. 적절한 __path__ 속성에 접근할 수 없으면 ModuleNotFoundError가 발생하고, 세 번째 인수는 나중에 로딩의 대상이 될 기존 모듈 객체입니다. 임포트 시스템은 재로드 시에만 이 대상 모듈을 전달합니다.

The meta path may be traversed multiple times for a single import request. For example, assuming none of the modules involved has already been cached, importing foo.bar.baz will first perform a top level import, calling mpf.find_spec("foo", None, None) on each meta path finder. After foo has been imported, foo.bar will be imported by traversing the meta path a second time, calling mpf.find_spec("foo.bar", foo.__path__, None). Once foo.bar has been imported, the final traversal will call mpf.find_spec("foo.bar.baz", foo.bar.__path__, None).  
단일 임포트 요청의 경우 메타 경로는 여러 번 순회될 수 있습니다. 예를 들어, 관련된 모듈 중 어느 것도 이미 캐시되지 않은 경우, foo.bar.baz를 임포트하면 먼저 최상위 임포트를 수행하여 각 메타 경로 파인더에서 mpf.find_spec("foo", None, None)을 호출합니다. 이후 foo가 임포트된 후에는 foo.bar가, 마지막으로 foo.bar가 임포트되면 mpf.find_spec("foo.bar.baz", foo.bar.__path__, None)이 호출됩니다.

Some meta path finders only support top level imports. These importers will always return None when anything other than None is passed as the second argument.  
일부 메타 경로 파인더는 최상위 임포트만 지원합니다. 이러한 임포터는 두 번째 인수로 None이 아닌 것이 전달되면 항상 None을 반환합니다.

Python's default sys.meta_path has three meta path finders, one that knows how to import built-in modules, one that knows how to import frozen modules, and one that knows how to import modules from an import path (i.e. the path based finder).  
파이썬의 기본 sys.meta_path에는 내장 모듈, 동결 모듈, 그리고 임포트 경로(경로 기반 파인더)의 모듈을 임포트하는 방법을 아는 세 개의 메타 경로 파인더가 포함되어 있습니다.

Changed in version 3.4: The find_spec() method of meta path finders replaced find_module(), which is now deprecated. While it will continue to work without change, the import machinery will try it only if the finder does not implement find_spec().  
버전 3.4에서 변경됨: 메타 경로 파인더의 find_spec() 메서드가 find_module()을 대체하였으며, find_module()은 더 이상 사용되지 않습니다.

Changed in version 3.10: Use of find_module() by the import system now raises ImportWarning.  
버전 3.10에서 변경됨: 임포트 시스템에서 find_module()을 사용하면 ImportWarning이 발생합니다.

Changed in version 3.12: find_module() has been removed. Use find_spec() instead.  
버전 3.12에서 변경됨: find_module()은 제거되었으므로 대신 find_spec()을 사용하세요.

### 5.5. The Path Based Finder

A word of warning: this section and the previous both use the term finder, distinguishing between them by using the terms meta path finder and path entry finder. These two types of finders are very similar, support similar protocols, and function in similar ways during the import process, but it’s important to keep in mind that they are subtly different. In particular, meta path finders operate at the beginning of the import process, as keyed off the sys.meta_path traversal.  
주의할 점: 이 섹션과 이전 섹션 모두 '파인더'라는 용어를 사용하지만, 이를 메타 경로 파인더와 경로 엔트리 파인더로 구분합니다. 이 두 종류의 파인더는 매우 유사하며, 유사한 프로토콜을 지원하고, 임포트 과정에서 비슷하게 동작하지만 미묘한 차이가 있음을 유념해야 합니다. 특히, 메타 경로 파인더는 sys.meta_path 순회를 기반으로 임포트 과정의 시작 부분에서 동작합니다.

By contrast, path entry finders are in a sense an implementation detail of the path based finder, and in fact, if the path based finder were to be removed from sys.meta_path, none of the path entry finder semantics would be invoked.  
반면, 경로 엔트리 파인더는 경로 기반 파인더의 구현 세부 사항에 가깝고, 만약 경로 기반 파인더가 sys.meta_path에서 제거된다면 경로 엔트리 파인더 관련 의미 체계는 전혀 호출되지 않습니다.

네트워크 URL, 데이터베이스 쿼리 등 파일 시스템에 국한되지 않은 위치에서도 모듈을 검색할 수 있도록 경로 엔트리는 사용자가 지정한 문자열을 참조할 수 있습니다.
Path entries need not be limited to file system locations. They can refer to URLs, database queries, or any other location that can be specified as a string.

웹에서 모듈을 찾기 위해 HTTP 의미 체계를 구현하는 훅(호출 가능 객체)을 작성할 수 있으며, 이 훅은 해당 프로토콜을 지원하는 경로 엔트리 파인더를 반환하여 모듈 로더를 얻는 데 사용됩니다.
The path based finder provides additional hooks and protocols so that you can extend and customize the types of searchable path entries. For example, if you wanted to support path entries as network URLs, you could write a hook that implements HTTP semantics to find modules on the web. This hook (a callable) would return a path entry finder supporting the protocol described below, which was then used to get a loader for the module from the web.

5.6. Replacing the standard import system  
5.6. 표준 임포트 시스템 교체  
The most reliable mechanism for replacing the entire import system is to delete the default contents of sys.meta_path, replacing them entirely with a custom meta path hook.  
전체 임포트 시스템을 교체하는 가장 신뢰할 수 있는 방법은 sys.meta_path의 기본 내용을 삭제하고, 이를 완전히 사용자 정의 메타 경로 훅으로 대체하는 것입니다.  
If it is acceptable to only alter the behaviour of import statements without affecting other APIs that access the import system, then replacing the builtin __import__() function may be sufficient.  
임포트 시스템에 접근하는 다른 API에 영향을 주지 않고 임포트 문의 동작만 변경해도 괜찮다면, 내장 함수 __import__()를 교체하는 것으로 충분할 수 있습니다.  
This technique may also be employed at the module level to only alter the behaviour of import statements within that module.  
이 기술은 모듈 수준에서 사용되어 해당 모듈 내의 임포트 문의 동작만 변경하는 데에도 사용할 수 있습니다.  
To selectively prevent the import of some modules from a hook early on the meta path (rather than disabling the standard import system entirely), it is sufficient to raise ModuleNotFoundError directly from find_spec() instead of returning None.  
표준 임포트 시스템 전체를 비활성화하는 대신, 메타 경로 초반의 훅에서 일부 모듈의 임포트를 선택적으로 방지하려면, None을 반환하는 대신 find_spec()에서 직접 ModuleNotFoundError를 발생시키면 충분합니다.  
The latter indicates that the meta path search should continue, while raising an exception terminates it immediately.  
후자는 메타 경로 검색이 계속되어야 함을 나타내고, 예외를 발생시키면 즉시 종료됨을 의미합니다.

## 5.7. Package Relative Imports  
5.7. 패키지 상대 임포트  
Relative imports use leading dots.  
상대 임포트는 선행 점을 사용합니다.  
A single leading dot indicates a relative import, starting with the current package.  
하나의 선행 점은 현재 패키지를 기준으로 한 상대 임포트를 나타냅니다.  
Two or more leading dots indicate a relative import to the parent(s) of the current package, one level per dot after the first.  
두 개 이상의 선행 점은 현재 패키지의 상위 패키지로의 상대 임포트를 의미하며, 첫 번째 점 이후의 각 점마다 한 단계씩 상위로 이동함을 나타냅니다.  
For example, given the following package layout:  
예를 들어, 다음과 같은 패키지 구조가 있을 경우:  
  package/  
    __init__.py  
    subpackage1/  
      __init__.py  
      moduleX.py  
      moduleY.py  
    subpackage2/  
      __init__.py  
      moduleZ.py  
    moduleA.py  
In either subpackage1/moduleX.py or subpackage1/__init__.py, the following are valid relative imports:  
subpackage1/moduleX.py 또는 subpackage1/__init__.py 내에서 다음 구문들은 유효한 상대 임포트입니다:  
  from .moduleY import spam  
  from .moduleY import spam as ham  
  from . import moduleY  
  from ..subpackage1 import moduleY  
  from ..subpackage2.moduleZ import eggs  
  from ..moduleA import foo  
Absolute imports may use either the import <> or from <> import <> syntax, but relative imports may only use the second form;  
절대 임포트는 import <>나 from <> import <> 구문을 사용할 수 있지만, 상대 임포트는 두 번째 형식만 사용할 수 있습니다;  
the reason for this is that:  
그 이유는 다음과 같습니다:  
  import XXX.YYY.ZZZ  
should expose XXX.YYY.ZZZ as a usable expression, but .moduleY is not a valid expression.  
  import XXX.YYY.ZZZ 는 XXX.YYY.ZZZ를 사용 가능한 표현식으로 노출해야 하지만, .moduleY는 유효한 표현식이 아닙니다.

## 5.8. Special considerations for __main__  
5.8. __main__에 대한 특별 고려 사항  
The __main__ module is a special case relative to Python’s import system.  
__main__ 모듈은 파이썬의 임포트 시스템에 대해 특별한 사례입니다.  
As noted elsewhere, the __main__ module is directly initialized at interpreter startup, much like sys and builtins.  
다른 곳에서 언급한 바와 같이, __main__ 모듈은 sys와 builtins처럼 인터프리터 시작 시 직접 초기화됩니다.  
However, unlike those two, it doesn’t strictly qualify as a built-in module.  
그러나 이 둘과 달리, __main__은 엄격한 내장 모듈로 간주되지 않습니다.  
This is because the manner in which __main__ is initialized depends on the flags and other options with which the interpreter is invoked.  
이는 __main__의 초기화 방식이 인터프리터가 호출될 때 사용된 플래그 및 기타 옵션에 따라 달라지기 때문입니다.

5.8.1. __main__.__spec__  
5.8.1. __main__.__spec__  
Depending on how __main__ is initialized, __main__.__spec__ gets set appropriately or to None.  
__main__이 어떻게 초기화되느냐에 따라, __main__.__spec__은 적절히 설정되거나 None으로 설정됩니다.  
When Python is started with the -m option, __spec__ is set to the module spec of the corresponding module or package.  
파이썬이 -m 옵션으로 시작되면, __spec__은 해당 모듈 또는 패키지의 모듈 스펙으로 설정됩니다.  
__spec__ is also populated when the __main__ module is loaded as part of executing a directory, zipfile or other sys.path entry.  
또한 __main__ 모듈이 디렉토리, zip파일 또는 기타 sys.path 항목의 일부로 실행될 때 __spec__이 채워집니다.  
In the remaining cases __main__.__spec__ is set to None, as the code used to populate the __main__ does not correspond directly with an importable module:  
나머지 경우, __main__을 채우기 위해 사용된 코드가 직접 임포트 가능한 모듈과 일치하지 않으므로 __main__.__spec__은 None으로 설정됩니다:  
  interactive prompt  
  대화형 프롬프트  
  -c option  
  -c 옵션  
  running from stdin  
  stdin에서 실행  
  running directly from a source or bytecode file  
  소스 또는 바이트코드 파일에서 직접 실행  
Note that __main__.__spec__ is always None in the last case, even if the file could technically be imported directly as a module instead.  
마지막 경우에 __main__.__spec__은 파일이 기술적으로 모듈로 직접 임포트될 수 있음에도 불구하고 항상 None임에 주의하세요.  
Use the -m switch if valid module metadata is desired in __main__.  
__main__에 유효한 모듈 메타데이터가 필요하면 -m 스위치를 사용하세요.  
Note also that even when __main__ corresponds with an importable module and __main__.__spec__ is set accordingly, they’re still considered distinct modules.  
또한, __main__이 임포트 가능한 모듈과 일치하고 __main__.__spec__이 그에 맞게 설정되더라도, 이들은 여전히 별개의 모듈로 간주됩니다.  
This is due to the fact that blocks guarded by if __name__ == "__main__": checks only execute when the module is used to populate the __main__ namespace, and not during normal import.  
이는 if __name__ == "__main__": 검사로 보호된 블록이 모듈이 __main__ 네임스페이스를 채우는 경우에만 실행되고, 일반 임포트 시에는 실행되지 않기 때문입니다.

## 5.9. References  
5.9. 참고 문헌  
The import machinery has evolved considerably since Python’s early days.  
파이썬의 초기 시절 이후로 임포트 메커니즘은 크게 발전했습니다.  
The original specification for packages is still available to read, although some details have changed since the writing of that document.  
패키지에 대한 원래 명세는 여전히 읽을 수 있지만, 해당 문서가 작성된 이후로 일부 세부 사항이 변경되었습니다.  
The original specification for sys.meta_path was PEP 302, with subsequent extension in PEP 420.  
sys.meta_path에 대한 원래 명세는 PEP 302였으며, 이후 PEP 420으로 확장되었습니다.  
PEP 420 introduced namespace packages for Python 3.3. PEP 420 also introduced the find_loader() protocol as an alternative to find_module().  
PEP 420은 Python 3.3에서 네임스페이스 패키지를 도입했고, 또한 find_module()의 대안으로 find_loader() 프로토콜을 도입했습니다.  
PEP 366 describes the addition of the __package__ attribute for explicit relative imports in main modules.  
PEP 366은 메인 모듈에서 명시적 상대 임포트를 위한 __package__ 속성의 추가를 설명합니다.  
PEP 328 introduced absolute and explicit relative imports and initially proposed __name__ for semantics PEP 366 would eventually specify for __package__.  
PEP 328은 절대 및 명시적 상대 임포트를 도입했으며, 처음에는 __name__을 제안했으나 이후 PEP 366에서 __package__에 대한 의미를 명시하게 됩니다.  
PEP 338 defines executing modules as scripts.  
PEP 338은 모듈을 스크립트로 실행하는 것을 정의합니다.  
PEP 451 adds the encapsulation of per-module import state in spec objects. It also off-loads most of the boilerplate responsibilities of loaders back onto the import machinery.  
PEP 451은 spec 객체 내에서 모듈별 임포트 상태를 캡슐화하며, 로더의 대부분 상용구 작업을 임포트 메커니즘으로 다시 넘깁니다.  
These changes allow the deprecation of several APIs in the import system and also addition of new methods to finders and loaders.  
이러한 변경은 임포트 시스템 내 여러 API의 사용 중단 및 파인더와 로더에 새로운 메서드 추가를 가능하게 합니다.
