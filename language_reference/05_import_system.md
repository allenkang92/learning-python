# 5. The import system

# 5. 임포트 시스템

Python code in one module gains access to the code in another module by the process of importing it. The import statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as importlib.import_module() and built-in __import__() can also be used to invoke the import machinery.

한 모듈의 파이썬 코드는 다른 모듈을 임포트하는 과정을 통해 해당 모듈의 코드에 접근할 수 있습니다. import 문은 임포트 기능을 호출하는 가장 일반적인 방법이지만, 유일한 방법은 아닙니다. importlib.import_module()과 내장 함수 __import__()와 같은 함수들도 임포트 기능을 호출하는 데 사용될 수 있습니다.

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

To begin the search, Python needs the fully qualified name of the module (or package, but for the purposes of this discussion, the difference is immaterial) being imported. This name may come from various arguments to the import statement, or from the parameters to the importlib.import_module() or __import__() functions.

검색을 시작하기 위해, 파이썬은 임포트되는 모듈(또는 패키지이지만, 이 논의의 목적상 차이는 중요하지 않음)의 완전히 정규화된 이름이 필요합니다. 이 이름은 import 문에 대한 다양한 인수에서 오거나, importlib.import_module() 또는 __import__() 함수에 대한 매개변수에서 올 수 있습니다.

### 5.3.3. Import hooks

The import machinery is designed to be extensible; the primary mechanism for this are the import hooks. There are two types of import hooks: meta hooks and import path hooks.

Meta hooks are called at the start of import processing, before any other import processing has occurred, other than sys.modules cache look up. This allows meta hooks to override sys.path processing, frozen modules, or even built-in modules. Meta hooks are registered by adding new finder objects to sys.meta_path, as described below.

Import path hooks are called as part of sys.path (or package.__path__) processing, at the point where their associated path item is encountered. Import path hooks are registered by adding new callables to sys.path_hooks as described below.

### 5.3.3. 임포트 훅

임포트 기능은 확장 가능하도록 설계되었습니다. 이를 위한 주요 메커니즘은 임포트 훅입니다. 임포트 훅에는 메타 훅과 임포트 경로 훅이라는 두 가지 유형이 있습니다.

메타 훅은 sys.modules 캐시 조회를 제외한 다른 임포트 처리가 발생하기 전, 임포트 처리의 시작 시점에 호출됩니다. 이를 통해 메타 훅은 sys.path 처리, 동결된 모듈, 심지어 내장 모듈도 재정의할 수 있습니다. 메타 훅은 아래에 설명된 대로 sys.meta_path에 새로운 파인더 객체를 추가하여 등록됩니다.

임포트 경로 훅은 sys.path(또는 package.__path__) 처리의 일부로, 관련 경로 항목이 발견되는 시점에 호출됩니다. 임포트 경로 훅은 아래 설명된 대로 sys.path_hooks에 새로운 호출 가능 객체를 추가하여 등록됩니다.

### 5.3.4. The meta path

When the named module is not found in sys.modules, Python next searches sys.meta_path, which contains a list of meta path finder objects. These finders are queried in order to see if they know how to handle the named module. Meta path finders must implement a method called find_spec() which takes three arguments: a name, an import path, and (optionally) a target module. The meta path finder can use any strategy it wants to determine whether it can handle the named module or not.

If the meta path finder knows how to handle the named module, it returns a spec object. If it cannot handle the named module, it returns None. If sys.meta_path processing reaches the end of its list without returning a spec, then a ModuleNotFoundError is raised. Any other exceptions raised are simply propagated up, aborting the import process.

The find_spec() method of meta path finders is called with two or three arguments. The first is the fully qualified name of the module being imported, for example foo.bar.baz. The second argument is the path entries to use for the module search. For top-level modules, the second argument is None, but for submodules or subpackages, the second argument is the value of the parent package's __path__ attribute. If the appropriate __path__ attribute cannot be accessed, a ModuleNotFoundError is raised. The third argument is an existing module object that will be the target of loading later. The import system passes in a target module only during reload.

The meta path may be traversed multiple times for a single import request. For example, assuming none of the modules involved has already been cached, importing foo.bar.baz will first perform a top level import, calling mpf.find_spec("foo", None, None) on each meta path finder (mpf). After foo has been imported, foo.bar will be imported by traversing the meta path a second time, calling mpf.find_spec("foo.bar", foo.__path__, None). Once foo.bar has been imported, the final traversal will call mpf.find_spec("foo.bar.baz", foo.bar.__path__, None).

Some meta path finders only support top level imports. These importers will always return None when anything other than None is passed as the second argument.

Python's default sys.meta_path has three meta path finders, one that knows how to import built-in modules, one that knows how to import frozen modules, and one that knows how to import modules from an import path (i.e. the path based finder).

Changed in version 3.4: The find_spec() method of meta path finders replaced find_module(), which is now deprecated. While it will continue to work without change, the import machinery will try it only if the finder does not implement find_spec().

Changed in version 3.10: Use of find_module() by the import system now raises ImportWarning.

Changed in version 3.12: find_module() has been removed. Use find_spec() instead.

### 5.3.4. 메타 경로

명명된 모듈이 sys.modules에서 발견되지 않으면, 파이썬은 다음으로 메타 경로 파인더 객체 목록을 포함하는 sys.meta_path를 검색합니다. 이 파인더들은 명명된 모듈을 처리하는 방법을 알고 있는지 확인하기 위해 순서대로 쿼리됩니다. 메타 경로 파인더는 이름, 임포트 경로, 그리고 (선택적으로) 대상 모듈이라는 세 가지 인수를 받는 find_spec()이라는 메서드를 구현해야 합니다. 메타 경로 파인더는 명명된 모듈을 처리할 수 있는지 여부를 결정하기 위해 원하는 전략을 사용할 수 있습니다.

메타 경로 파인더가 명명된 모듈을 처리하는 방법을 알고 있으면 스펙 객체를 반환합니다. 명명된 모듈을 처리할 수 없으면 None을 반환합니다. sys.meta_path 처리가 스펙을 반환하지 않고 목록의 끝에 도달하면 ModuleNotFoundError가 발생합니다. 발생한 다른 예외는 단순히 위로 전파되어 임포트 프로세스를 중단합니다.

메타 경로 파인더의 find_spec() 메서드는 두 개 또는 세 개의 인수로 호출됩니다. 첫 번째는 임포트되는 모듈의 정규화된 이름입니다(예: foo.bar.baz). 두 번째 인수는 모듈 검색에 사용할 경로 항목입니다. 최상위 모듈의 경우 두 번째 인수는 None이지만, 하위 모듈이나 하위 패키지의 경우 두 번째 인수는 부모 패키지의 __path__ 속성 값입니다. 적절한 __path__ 속성에 접근할 수 없는 경우 ModuleNotFoundError가 발생합니다. 세 번째 인수는 나중에 로딩의 대상이 될 기존 모듈 객체입니다. 임포트 시스템은 재로드 중에만 대상 모듈을 전달합니다.

단일 임포트 요청에 대해 메타 경로는 여러 번 순회될 수 있습니다. 예를 들어, 관련된 모듈 중 어느 것도 아직 캐시되지 않았다고 가정하면, foo.bar.baz를 임포트하는 것은 먼저 최상위 임포트를 수행하여 각 메타 경로 파인더(mpf)에 대해 mpf.find_spec("foo", None, None)을 호출합니다. foo가 임포트된 후, foo.bar는 메타 경로를 두 번째로 순회하여 mpf.find_spec("foo.bar", foo.__path__, None)을 호출하여 임포트됩니다. foo.bar가 임포트되면, 최종 순회는 mpf.find_spec("foo.bar.baz", foo.bar.__path__, None)을 호출합니다.

일부 메타 경로 파인더는 최상위 임포트만 지원합니다. 이러한 임포터는 두 번째 인수로 None 이외의 것이 전달되면 항상 None을 반환합니다.

파이썬의 기본 sys.meta_path에는 세 개의 메타 경로 파인더가 있습니다. 하나는 내장 모듈을 임포트하는 방법을 알고 있고, 하나는 동결된 모듈을 임포트하는 방법을 알고 있으며, 하나는 임포트 경로에서 모듈을 임포트하는 방법을 알고 있습니다(즉, 경로 기반 파인더).

버전 3.4에서 변경됨: 메타 경로 파인더의 find_spec() 메서드가 find_module()을 대체했으며, 이제 find_module()은 더 이상 사용되지 않습니다. 변경 없이 계속 작동하지만, 임포트 기계는 파인더가 find_spec()을 구현하지 않는 경우에만 find_module()을 시도합니다.

버전 3.10에서 변경됨: 임포트 시스템에 의한 find_module() 사용은 이제 ImportWarning을 발생시킵니다.

버전 3.12에서 변경됨: find_module()이 제거되었습니다. 대신 find_spec()을 사용하세요.

## 5.4. Loading

If and when a module spec is found, the import machinery will use it (and the loader it contains) when loading the module. Here is an approximation of what happens during the loading portion of import:

```python
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
    # It is assumed 'exec_module' will also be defined on the loader.
    module = spec.loader.create_module(spec)
if module is None:
    module = ModuleType(spec.name)
# The import-related module attributes get set here:
_init_module_attrs(spec, module)

if spec.loader is None:
    # unsupported
    raise ImportError
if spec.origin is None and spec.submodule_search_locations is not None:
    # namespace package
    sys.modules[spec.name] = module
elif not hasattr(spec.loader, 'exec_module'):
    module = spec.loader.load_module(spec.name)
else:
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        try:
            del sys.modules[spec.name]
        except KeyError:
            pass
        raise
return sys.modules[spec.name]
```

Note the following details:

- If there is an existing module object with the given name in sys.modules, import will have already returned it.
- The module will exist in sys.modules before the loader executes the module code. This is crucial because the module code may (directly or indirectly) import itself; adding it to sys.modules beforehand prevents unbounded recursion in the worst case and multiple loading in the best.
- If loading fails, the failing module – and only the failing module – gets removed from sys.modules. Any module already in the sys.modules cache, and any module that was successfully loaded as a side-effect, must remain in the cache. This contrasts with reloading where even the failing module is left in sys.modules.
- After the module is created but before execution, the import machinery sets the import-related module attributes ("_init_module_attrs" in the pseudo-code example above), as summarized in a later section.
- Module execution is the key moment of loading in which the module's namespace gets populated. Execution is entirely delegated to the loader, which gets to decide what gets populated and how.
- The module created during loading and passed to exec_module() may not be the one returned at the end of import [2].

Changed in version 3.4: The import system has taken over the boilerplate responsibilities of loaders. These were previously performed by the importlib.abc.Loader.load_module() method.

## 5.4. 로딩

모듈 스펙이 발견되면, 임포트 기능은 모듈을 로딩할 때 이를(그리고 그 안에 포함된 로더를) 사용합니다. 다음은 임포트의 로딩 부분에서 일어나는 일의 근사치입니다:

```python
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
    # 로더에 'exec_module'도 정의되어 있다고 가정합니다.
    module = spec.loader.create_module(spec)
if module is None:
    module = ModuleType(spec.name)
# 임포트 관련 모듈 속성이 여기서 설정됩니다:
_init_module_attrs(spec, module)

if spec.loader is None:
    # 지원되지 않음
    raise ImportError
if spec.origin is None and spec.submodule_search_locations is not None:
    # 네임스페이스 패키지
    sys.modules[spec.name] = module
elif not hasattr(spec.loader, 'exec_module'):
    module = spec.loader.load_module(spec.name)
else:
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        try:
            del sys.modules[spec.name]
        except KeyError:
            pass
        raise
return sys.modules[spec.name]
```

다음 세부 사항에 유의하세요:

- sys.modules에 주어진 이름을 가진 기존 모듈 객체가 있으면, 임포트는 이미 그것을 반환했을 것입니다.
- 로더가 모듈 코드를 실행하기 전에 모듈은 sys.modules에 존재합니다. 이는 모듈 코드가 (직접 또는 간접적으로) 자기 자신을 가져올 수 있기 때문에 중요합니다. 미리 sys.modules에 추가하면 최악의 경우 무한 재귀를 방지하고 최선의 경우 다중 로딩을 방지합니다.
- 로딩이 실패하면, 실패한 모듈 - 그리고 오직 실패한 모듈만 - sys.modules에서 제거됩니다. sys.modules 캐시에 이미 있는 모듈과 부작용으로 성공적으로 로드된 모듈은 캐시에 남아 있어야 합니다. 이는 실패한 모듈도 sys.modules에 남아 있는 재로딩과 대조됩니다.
- 모듈이 생성된 후 실행 전에, 임포트 기능은 임포트 관련 모듈 속성(위의 의사 코드 예제에서 "_init_module_attrs")을 설정합니다. 이는 나중 섹션에 요약되어 있습니다.
- 모듈 실행은 모듈의 네임스페이스가 채워지는 로딩의 핵심 순간입니다. 실행은 전적으로 로더에 위임되며, 로더는 무엇이 채워지고 어떻게 채워지는지 결정합니다.
- 로딩 중에 생성되어 exec_module()에 전달된 모듈은 임포트 끝에 반환되는 모듈이 아닐 수 있습니다 [2].

버전 3.4에서 변경됨: 임포트 시스템이 로더의 상용구 책임을 맡았습니다. 이전에는 importlib.abc.Loader.load_module() 메서드에 의해 수행되었습니다.

### 5.4.1. Loaders

Module loaders provide the critical function of loading: module execution. The import machinery calls the importlib.abc.Loader.exec_module() method with a single argument, the module object to execute. Any value returned from exec_module() is ignored.

모듈 로더는 로딩의 중요한 기능을 제공합니다: 모듈 실행. 임포트 기능은 실행할 모듈 객체라는 단일 인수와 함께 importlib.abc.Loader.exec_module() 메서드를 호출합니다. exec_module()에서 반환된 값은 무시됩니다.

Loaders must satisfy the following requirements:

로더는 다음 요구 사항을 충족해야 합니다:

If the module is a Python module (as opposed to a built-in module or a dynamically loaded extension), the loader should execute the module's code in the module's global name space (module.__dict__).

모듈이 파이썬 모듈인 경우(내장 모듈이나 동적으로 로드된 확장이 아닌 경우), 로더는 모듈의 전역 네임스페이스(module.__dict__)에서 모듈의 코드를 실행해야 합니다.

If the loader cannot execute the module, it should raise an ImportError, although any other exception raised during exec_module() will be propagated.

로더가 모듈을 실행할 수 없는 경우, ImportError를 발생시켜야 합니다. 그러나 exec_module() 중에 발생하는 다른 예외는 전파됩니다.

In many cases, the finder and loader can be the same object; in such cases the find_spec() method would just return a spec with the loader set to self.

많은 경우, 파인더와 로더는 동일한 객체일 수 있습니다. 이러한 경우 find_spec() 메서드는 로더가 self로 설정된 스펙을 반환합니다.

Module loaders may opt in to creating the module object during loading by implementing a create_module() method. It takes one argument, the module spec, and returns the new module object to use during loading. create_module() does not need to set any attributes on the module object. If the method returns None, the import machinery will create the new module itself.

모듈 로더는 create_module() 메서드를 구현하여 로딩 중에 모듈 객체를 생성하도록 선택할 수 있습니다. 이 메서드는 모듈 스펙이라는 하나의 인수를 받고, 로딩 중에 사용할 새 모듈 객체를 반환합니다. create_module()은 모듈 객체에 어떤 속성도 설정할 필요가 없습니다. 이 메서드가 None을 반환하면, 임포트 기능이 새 모듈 자체를 생성합니다.

Added in version 3.4: The create_module() method of loaders.

버전 3.4에서 추가됨: 로더의 create_module() 메서드.

Changed in version 3.4: The load_module() method was replaced by exec_module() and the import machinery assumed all the boilerplate responsibilities of loading.

버전 3.4에서 변경됨: load_module() 메서드가 exec_module()로 대체되었으며, 임포트 기능이 로딩의 모든 상용구 책임을 담당하게 되었습니다.

For compatibility with existing loaders, the import machinery will use the load_module() method of loaders if it exists and the loader does not also implement exec_module(). However, load_module() has been deprecated and loaders should implement exec_module() instead.

기존 로더와의 호환성을 위해, 임포트 기능은 로더의 load_module() 메서드가 존재하고 로더가 exec_module()도 구현하지 않는 경우 이를 사용합니다. 그러나 load_module()은 더 이상 사용되지 않으며, 로더는 대신 exec_module()을 구현해야 합니다.

The load_module() method must implement all the boilerplate loading functionality described above in addition to executing the module. All the same constraints apply, with some additional clarification:

load_module() 메서드는 모듈 실행 외에도 위에서 설명한 모든 상용구 로딩 기능을 구현해야 합니다. 추가 설명과 함께 동일한 제약 조건이 적용됩니다:

If there is an existing module object with the given name in sys.modules, the loader must use that existing module. (Otherwise, importlib.reload() will not work correctly.) If the named module does not exist in sys.modules, the loader must create a new module object and add it to sys.modules.

sys.modules에 주어진 이름을 가진 기존 모듈 객체가 있는 경우, 로더는 해당 기존 모듈을 사용해야 합니다. (그렇지 않으면 importlib.reload()가 올바르게 작동하지 않습니다.) 명명된 모듈이 sys.modules에 존재하지 않는 경우, 로더는 새 모듈 객체를 생성하고 sys.modules에 추가해야 합니다.

버전 3.5에서 변경됨: exec_module()이 정의되었지만 create_module()이 정의되지 않은 경우 DeprecationWarning이 발생합니다.

Changed in version 3.6: An ImportError is raised when exec_module() is defined but create_module() is not.

버전 3.6에서 변경됨: exec_module()이 정의되었지만 create_module()이 정의되지 않은 경우 ImportError가 발생합니다.

Changed in version 3.10: Use of load_module() will raise ImportWarning.

버전 3.10에서 변경됨: load_module() 사용은 ImportWarning을 발생시킵니다.

### 5.4.2. Submodules

When a submodule is loaded using any mechanism (e.g. importlib APIs, the import or import-from statements, or built-in __import__()) a binding is placed in the parent module's namespace to the submodule object. For example, if package spam has a submodule foo, after importing spam.foo, spam will have an attribute foo which is bound to the submodule. Let's say you have the following directory structure:

서브모듈이 어떤 메커니즘(예: importlib API, import 또는 import-from 문, 또는 내장 __import__())을 사용하여 로드될 때, 서브모듈 객체에 대한 바인딩이 부모 모듈의 네임스페이스에 배치됩니다. 예를 들어, 패키지 spam에 서브모듈 foo가 있는 경우, spam.foo를 가져온 후, spam은 서브모듈에 바인딩된 속성 foo를 갖게 됩니다. 다음과 같은 디렉토리 구조가 있다고 가정해 봅시다:
```

