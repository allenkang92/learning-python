# 10. Full Grammar specification

This is the full Python grammar, derived directly from the grammar used to generate the CPython parser (see Grammar/python.gram). The version here omits details related to code generation and error recovery.

# 10. 전체 문법 명세

이것은 CPython 파서를 생성하는 데 사용된 문법에서 직접 파생된 전체 Python 문법입니다(Grammar/python.gram 참조). 여기서 설명하는 버전은 코드 생성 및 오류 복구와 관련된 세부 사항을 생략합니다.

The notation is a mixture of EBNF and PEG. In particular, & followed by a symbol, token or parenthesized group indicates a positive lookahead (i.e., is required to match but not consumed), while ! indicates a negative lookahead (i.e., is required not to match). We use the | separator to mean PEG's "ordered choice" (written as / in traditional PEG grammars). See PEP 617 for more details on the grammar’s syntax.

이 표기법은 EBNF와 PEG의 혼합입니다. 특히, 기호, 토큰 또는 괄호로 묶인 그룹 다음에 오는 &는 긍정적 전방 탐색(즉, 일치해야 하지만 소비되지 않음)을 나타내고, !는 부정적 전방 탐색(즉, 일치하지 않아야 함)을 나타냅니다. 우리는 PEG의 "순서가 있는 선택"(전통적인 PEG 문법에서는 /로 표기)을 의미하는 | 구분자를 사용합니다. 문법 구문에 대한 자세한 내용은 PEP 617을 참조하십시오.

# PEG grammar for Python
# Python을 위한 PEG 문법

# ========================= START OF THE GRAMMAR =========================
# ========================= 문법의 시작 =========================

# General grammatical elements and rules:
#
# * Strings with double quotes (") denote SOFT KEYWORDS
# * Strings with single quotes (') denote KEYWORDS
# * Upper case names (NAME) denote tokens in the Grammar/Tokens file
# * Rule names starting with "invalid_" are used for specialized syntax errors
#     - These rules are NOT used in the first pass of the parser.
#     - Only if the first pass fails to parse, a second pass including the invalid
#       rules will be executed.
#     - If the parser fails in the second phase with a generic syntax error, the
#       location of the generic failure of the first pass will be used (this avoids
#       reporting incorrect locations due to the invalid rules).
#     - The order of the alternatives involving invalid rules matter
#       (like any rule in PEG).
#
# Grammar Syntax (see PEP 617 for more information):
#
# rule_name: expression
#   Optionally, a type can be included right after the rule name, which
#   specifies the return type of the C or Python function corresponding to the
#   rule:
# rule_name[return_type]: expression
#   If the return type is omitted, then a void * is returned in C and an Any in
#   Python.
# e1 e2
#   Match e1, then match e2.
# e1 | e2
#   Match e1 or e2.
#   The first alternative can also appear on the line after the rule name for
#   formatting purposes. In that case, a | must be used before the first
#   alternative, like so:
#       rule_name[return_type]:
#            | first_alt
#            | second_alt
# ( e )
#   Match e (allows also to use other operators in the group like '(e)*')
# [ e ] or e?
#   Optionally match e.
# e*
#   Match zero or more occurrences of e.
# e+
#   Match one or more occurrences of e.
# s.e+
#   Match one or more occurrences of e, separated by s. The generated parse tree
#   does not include the separator. This is otherwise identical to (e (s e)*).
# &e
#   Succeed if e can be parsed, without consuming any input.
# !e
#   Fail if e can be parsed, without consuming any input.
# ~
#   Commit to the current alternative, even if it fails to parse.
# &&e
#   Eager parse e. The parser will not backtrack and will immediately 
#   fail with SyntaxError if e cannot be parsed.
#

# 일반적인 문법 요소 및 규칙:
#
# * 쌍따옴표(")가 있는 문자열은 소프트 키워드를 나타냅니다
# * 작은따옴표(')가 있는 문자열은 키워드를 나타냅니다
# * 대문자 이름(NAME)은 Grammar/Tokens 파일의 토큰을 나타냅니다
# * "invalid_"로 시작하는 규칙 이름은 특수 구문 오류에 사용됩니다
#     - 이러한 규칙은 파서의 첫 번째 패스에서 사용되지 않습니다.
#     - 첫 번째 패스가 구문 분석에 실패한 경우에만 유효하지 않은 규칙을 포함한 두 번째 패스가 실행됩니다.
#     - 파서가 두 번째 단계에서 일반적인 구문 오류로 실패하면, 첫 번째 패스의 일반적인 실패 위치가 사용됩니다
#       (이는 유효하지 않은 규칙으로 인해 잘못된 위치가 보고되는 것을 방지합니다).
#     - 유효하지 않은 규칙과 관련된 대안의 순서가 중요합니다(PEG의 모든 규칙과 마찬가지로).
#
# 문법 구문(자세한 내용은 PEP 617 참조):
#
# rule_name: expression
#   선택적으로, 규칙 이름 바로 뒤에 타입을 포함시킬 수 있으며,
#   이는 규칙에 해당하는 C 또는 Python 함수의 반환 타입을 지정합니다:
# rule_name[return_type]: expression
#   반환 타입이 생략되면 C에서는 void *, Python에서는 Any가 반환됩니다.
# e1 e2
#   e1과 일치한 다음 e2와 일치합니다.
# e1 | e2
#   e1 또는 e2와 일치합니다.
#   첫 번째 대안은 서식 지정 목적으로 규칙 이름 다음 줄에 나타날 수도 있습니다.
#   이 경우 첫 번째 대안 앞에 |를 사용해야 합니다:
#       rule_name[return_type]:
#            | first_alt
#            | second_alt
# ( e )
#   e와 일치합니다(그룹에서 '(e)*'와 같은 다른 연산자를 사용할 수 있음)
# [ e ] 또는 e?
#   선택적으로 e와 일치합니다.
# e*
#   e가 0회 이상 발생하는 것과 일치합니다.
# e+
#   e가 1회 이상 발생하는 것과 일치합니다.
# s.e+
#   s로 구분된 e가 1회 이상 발생하는 것과 일치합니다.
#   생성된 구문 트리에는 구분자가 포함되지 않습니다.
#   이는 (e (s e)*)와 동일합니다.
# &e
#   입력을 소비하지 않고 e를 구문 분석할 수 있으면 성공합니다.
# !e
#   입력을 소비하지 않고 e를 구문 분석할 수 있으면 실패합니다.
# ~
#   구문 분석에 실패하더라도 현재 대안에 전념합니다.
# &&e
#   적극적으로 e를 구문 분석합니다. 파서는 백트래킹하지 않고
#   e를 구문 분석할 수 없으면 즉시 SyntaxError로 실패합니다.
#

# STARTING RULES
# 시작 규칙
# ==============

file: [statements] ENDMARKER 
interactive: statement_newline 
eval: expressions NEWLINE* ENDMARKER 
func_type: '(' [type_expressions] ')' '->' expression NEWLINE* ENDMARKER 

# GENERAL STATEMENTS
# 일반 문장
# ==================

statements: statement+ 

statement: compound_stmt  | simple_stmts 

statement_newline:
    | compound_stmt NEWLINE 
    | simple_stmts
    | NEWLINE 
    | ENDMARKER 

simple_stmts:
    | simple_stmt !';' NEWLINE  # Not needed, there for speedup
    | ';'.simple_stmt+ [';'] NEWLINE 

# NOTE: assignment MUST precede expression, else parsing a simple assignment
# will throw a SyntaxError.
simple_stmt:
    | assignment
    | type_alias
    | star_expressions 
    | return_stmt
    | import_stmt
    | raise_stmt
    | 'pass' 
    | del_stmt
    | yield_stmt
    | assert_stmt
    | 'break' 
    | 'continue' 
    | global_stmt
    | nonlocal_stmt

compound_stmt:
    | function_def
    | if_stmt
    | class_def
    | with_stmt
    | for_stmt
    | try_stmt
    | while_stmt
    | match_stmt

# SIMPLE STATEMENTS
# 단순 문장
# =================

# NOTE: annotated_rhs may start with 'yield'; yield_expr must start with 'yield'
assignment:
    | NAME ':' expression ['=' annotated_rhs ] 
    | ('(' single_target ')' 
         | single_subscript_attribute_target) ':' expression ['=' annotated_rhs ] 
    | (star_targets '=' )+ (yield_expr | star_expressions) !'=' [TYPE_COMMENT] 
    | single_target augassign ~ (yield_expr | star_expressions) 

annotated_rhs: yield_expr | star_expressions

augassign:
    | '+=' 
    | '-=' 
    | '*=' 
    | '@=' 
    | '/=' 
    | '%=' 
    | '&=' 
    | '|=' 
    | '^=' 
    | '<<=' 
    | '>>=' 
    | '**=' 
    | '//=' 

return_stmt:
    | 'return' [star_expressions] 

raise_stmt:
    | 'raise' expression ['from' expression ] 
    | 'raise' 

global_stmt: 'global' ','.NAME+ 

nonlocal_stmt: 'nonlocal' ','.NAME+ 

del_stmt:
    | 'del' del_targets &(';' | NEWLINE) 

yield_stmt: yield_expr 

assert_stmt: 'assert' expression [',' expression ] 

import_stmt:
    | import_name
    | import_from

# Import statements
# 임포트 문장
# -----------------

import_name: 'import' dotted_as_names 
# note below: the ('.' | '...') is necessary because '...' is tokenized as ELLIPSIS
import_from:
    | 'from' ('.' | '...')* dotted_name 'import' import_from_targets 
    | 'from' ('.' | '...')+ 'import' import_from_targets 
import_from_targets:
    | '(' import_from_as_names [','] ')' 
    | import_from_as_names !','
    | '*' 
import_from_as_names:
    | ','.import_from_as_name+ 
import_from_as_name:
    | NAME ['as' NAME ] 
dotted_as_names:
    | ','.dotted_as_name+ 
dotted_as_name:
    | dotted_name ['as' NAME ] 
dotted_name:
    | dotted_name '.' NAME 
    | NAME

# COMPOUND STATEMENTS
# 복합 문장
# ===================

# Common elements
# 공통 요소
# ---------------

block:
    | NEWLINE INDENT statements DEDENT 
    | simple_stmts

decorators: ('@' named_expression NEWLINE )+ 

# Class definitions
# 클래스 정의
# -----------------

class_def:
    | decorators class_def_raw 
    | class_def_raw

class_def_raw:
    | 'class' NAME [type_params] ['(' [arguments] ')' ] ':' block 

# Function definitions
# 함수 정의
# --------------------

function_def:
    | decorators function_def_raw 
    | function_def_raw

function_def_raw:
    | 'def' NAME [type_params] '(' [params] ')' ['->' expression ] ':' [func_type_comment] block 
    | 'async' 'def' NAME [type_params] '(' [params] ')' ['->' expression ] ':' [func_type_comment] block 

# Function parameters
# 함수 매개변수
# -------------------

params:
    | parameters

parameters:
    | slash_no_default param_no_default* param_with_default* [star_etc] 
    | slash_with_default param_with_default* [star_etc] 
    | param_no_default+ param_with_default* [star_etc] 
    | param_with_default+ [star_etc] 
    | star_etc 

# Some duplication here because we can't write (',' | &')'),
# which is because we don't support empty alternatives (yet).

slash_no_default:
    | param_no_default+ '/' ',' 
    | param_no_default+ '/' &')' 
slash_with_default:
    | param_no_default* param_with_default+ '/' ',' 
    | param_no_default* param_with_default+ '/' &')' 

star_etc:
    | '*' param_no_default param_maybe_default* [kwds] 
    | '*' param_no_default_star_annotation param_maybe_default* [kwds] 
    | '*' ',' param_maybe_default+ [kwds] 
    | kwds 

kwds:
    | '**' param_no_default 

# One parameter.  This *includes* a following comma and type comment.
#
# There are three styles:
# - No default
# - With default
# - Maybe with default
#
# There are two alternative forms of each, to deal with type comments:
# - Ends in a comma followed by an optional type comment
# - No comma, optional type comment, must be followed by close paren
# The latter form is for a final parameter without trailing comma.
#

param_no_default:
    | param ',' TYPE_COMMENT? 
    | param TYPE_COMMENT? &')' 
param_no_default_star_annotation:
    | param_star_annotation ',' TYPE_COMMENT? 
    | param_star_annotation TYPE_COMMENT? &')' 
param_with_default:
    | param default ',' TYPE_COMMENT? 
    | param default TYPE_COMMENT? &')' 
param_maybe_default:
    | param default? ',' TYPE_COMMENT? 
    | param default? TYPE_COMMENT? &')' 
param: NAME annotation? 
param_star_annotation: NAME star_annotation 
annotation: ':' expression 
star_annotation: ':' star_expression 
default: '=' expression  | invalid_default

# If statement
# If 문
# ------------

if_stmt:
    | 'if' named_expression ':' block elif_stmt 
    | 'if' named_expression ':' block [else_block] 
elif_stmt:
    | 'elif' named_expression ':' block elif_stmt 
    | 'elif' named_expression ':' block [else_block] 
else_block:
    | 'else' ':' block 

# While statement
# While 문
# ---------------

while_stmt:
    | 'while' named_expression ':' block [else_block] 

# For statement
# For 문
# -------------

for_stmt:
    | 'for' star_targets 'in' ~ star_expressions ':' [TYPE_COMMENT] block [else_block] 
    | 'async' 'for' star_targets 'in' ~ star_expressions ':' [TYPE_COMMENT] block [else_block] 

# With statement
# With 문
# --------------

with_stmt:
    | 'with' '(' ','.with_item+ ','? ')' ':' [TYPE_COMMENT] block 
    | 'with' ','.with_item+ ':' [TYPE_COMMENT] block 
    | 'async' 'with' '(' ','.with_item+ ','? ')' ':' block 
    | 'async' 'with' ','.with_item+ ':' [TYPE_COMMENT] block 

with_item:
    | expression 'as' star_target &(',' | ')' | ':') 
    | expression 

# Try statement
# Try 문
# -------------

try_stmt:
    | 'try' ':' block finally_block 
    | 'try' ':' block except_block+ [else_block] [finally_block] 
    | 'try' ':' block except_star_block+ [else_block] [finally_block] 


# Except statement
# Except 문
# ----------------

except_block:
    | 'except' expression ['as' NAME ] ':' block 
    | 'except' ':' block 
except_star_block:
    | 'except' '*' expression ['as' NAME ] ':' block 
finally_block:
    | 'finally' ':' block 

# Match statement
# Match 문
# ---------------

match_stmt:
    | "match" subject_expr ':' NEWLINE INDENT case_block+ DEDENT 

subject_expr:
    | star_named_expression ',' star_named_expressions? 
    | named_expression

case_block:
    | "case" patterns guard? ':' block 

guard: 'if' named_expression 

patterns:
    | open_sequence_pattern 
    | pattern

pattern:
    | as_pattern
    | or_pattern

as_pattern:
    | or_pattern 'as' pattern_capture_target 

or_pattern:
    | '|'.closed_pattern+ 

closed_pattern:
    | literal_pattern
    | capture_pattern
    | wildcard_pattern
    | value_pattern
    | group_pattern
    | sequence_pattern
    | mapping_pattern
    | class_pattern

# Literal patterns are used for equality and identity constraints
# 리터럴 패턴은 동등성 및 식별성 제약에 사용됩니다
literal_pattern:
    | signed_number !('+' | '-') 
    | complex_number 
    | strings 
    | 'None' 
    | 'True' 
    | 'False' 

# Literal expressions are used to restrict permitted mapping pattern keys
# 리터럴 표현식은 허용된 매핑 패턴 키를 제한하는 데 사용됩니다
literal_expr:
    | signed_number !('+' | '-')
    | complex_number
    | strings
    | 'None' 
    | 'True' 
    | 'False' 

complex_number:
    | signed_real_number '+' imaginary_number 
    | signed_real_number '-' imaginary_number  

signed_number:
    | NUMBER
    | '-' NUMBER 

signed_real_number:
    | real_number
    | '-' real_number 

real_number:
    | NUMBER 

imaginary_number:
    | NUMBER 

capture_pattern:
    | pattern_capture_target 

pattern_capture_target:
    | !"_" NAME !('.' | '(' | '=') 

wildcard_pattern:
    | "_" 

value_pattern:
    | attr !('.' | '(' | '=') 

attr:
    | name_or_attr '.' NAME 

name_or_attr:
    | attr
    | NAME

group_pattern:
    | '(' pattern ')' 

sequence_pattern:
    | '[' maybe_sequence_pattern? ']' 
    | '(' open_sequence_pattern? ')' 

open_sequence_pattern:
    | maybe_star_pattern ',' maybe_sequence_pattern? 

maybe_sequence_pattern:
    | ','.maybe_star_pattern+ ','? 

maybe_star_pattern:
    | star_pattern
    | pattern

star_pattern:
    | '*' pattern_capture_target 
    | '*' wildcard_pattern 

mapping_pattern:
    | '{' '}' 
    | '{' double_star_pattern ','? '}' 
    | '{' items_pattern ',' double_star_pattern ','? '}' 
    | '{' items_pattern ','? '}' 

items_pattern:
    | ','.key_value_pattern+

key_value_pattern:
    | (literal_expr | attr) ':' pattern 

double_star_pattern:
    | '**' pattern_capture_target 

class_pattern:
    | name_or_attr '(' ')' 
    | name_or_attr '(' positional_patterns ','? ')' 
    | name_or_attr '(' keyword_patterns ','? ')' 
    | name_or_attr '(' positional_patterns ',' keyword_patterns ','? ')' 

positional_patterns:
    | ','.pattern+ 

keyword_patterns:
    | ','.keyword_pattern+

keyword_pattern:
    | NAME '=' pattern 

# Type statement
# Type 문
# ---------------

type_alias:
    | "type" NAME [type_params] '=' expression 

# Type parameter declaration
# 타입 매개변수 선언
# --------------------------

type_params: 
    | invalid_type_params
    | '[' type_param_seq ']' 

type_param_seq: ','.type_param+ [','] 

type_param:
    | NAME [type_param_bound] [type_param_default] 
    | '*' NAME [type_param_starred_default] 
    | '**' NAME [type_param_default] 

type_param_bound: ':' expression 
type_param_default: '=' expression 
type_param_starred_default: '=' star_expression 

# EXPRESSIONS
# 표현식
# -----------

expressions:
    | expression (',' expression )+ [','] 
    | expression ',' 
    | expression

expression:
    | disjunction 'if' disjunction 'else' expression 
    | disjunction
    | lambdef

yield_expr:
    | 'yield' 'from' expression 
    | 'yield' [star_expressions] 

star_expressions:
    | star_expression (',' star_expression )+ [','] 
    | star_expression ',' 
    | star_expression

star_expression:
    | '*' bitwise_or 
    | expression

star_named_expressions: ','.star_named_expression+ [','] 

star_named_expression:
    | '*' bitwise_or 
    | named_expression

assignment_expression:
    | NAME ':=' ~ expression 

named_expression:
    | assignment_expression
    | expression !':='

disjunction:
    | conjunction ('or' conjunction )+ 
    | conjunction

conjunction:
    | inversion ('and' inversion )+ 
    | inversion

inversion:
    | 'not' inversion 
    | comparison

# Comparison operators
# 비교 연산자
# --------------------

comparison:
    | bitwise_or compare_op_bitwise_or_pair+ 
    | bitwise_or

compare_op_bitwise_or_pair:
    | eq_bitwise_or
    | noteq_bitwise_or
    | lte_bitwise_or
    | lt_bitwise_or
    | gte_bitwise_or
    | gt_bitwise_or
    | notin_bitwise_or
    | in_bitwise_or
    | isnot_bitwise_or
    | is_bitwise_or

eq_bitwise_or: '==' bitwise_or 
noteq_bitwise_or:
    | ('!=' ) bitwise_or 
lte_bitwise_or: '<=' bitwise_or 
lt_bitwise_or: '<' bitwise_or 
gte_bitwise_or: '>=' bitwise_or 
gt_bitwise_or: '>' bitwise_or 
notin_bitwise_or: 'not' 'in' bitwise_or 
in_bitwise_or: 'in' bitwise_or 
isnot_bitwise_or: 'is' 'not' bitwise_or 
is_bitwise_or: 'is' bitwise_or 

# Bitwise operators
# 비트 연산자
# -----------------

bitwise_or:
    | bitwise_or '|' bitwise_xor 
    | bitwise_xor

bitwise_xor:
    | bitwise_xor '^' bitwise_and 
    | bitwise_and

bitwise_and:
    | bitwise_and '&' shift_expr 
    | shift_expr

shift_expr:
    | shift_expr '<<' sum 
    | shift_expr '>>' sum 
    | sum

# Arithmetic operators
# 산술 연산자
# --------------------

sum:
    | sum '+' term 
    | sum '-' term 
    | term

term:
    | term '*' factor 
    | term '/' factor 
    | term '//' factor 
    | term '%' factor 
    | term '@' factor 
    | factor

factor:
    | '+' factor 
    | '-' factor 
    | '~' factor 
    | power

power:
    | await_primary '**' factor 
    | await_primary

# Primary elements
# 기본 요소
# ----------------

# Primary elements are things like "obj.something.something", "obj[something]", "obj(something)", "obj" ...
# 기본 요소는 "obj.something.something", "obj[something]", "obj(something)", "obj" 같은 것입니다...

await_primary:
    | 'await' primary 
    | primary

primary:
    | primary '.' NAME 
    | primary genexp 
    | primary '(' [arguments] ')' 
    | primary '[' slices ']' 
    | atom

slices:
    | slice !',' 
    | ','.(slice | starred_expression)+ [','] 

slice:
    | [expression] ':' [expression] [':' [expression] ] 
    | named_expression 

atom:
    | NAME
    | 'True' 
    | 'False' 
    | 'None' 
    | strings
    | NUMBER
    | (tuple | group | genexp)
    | (list | listcomp)
    | (dict | set | dictcomp | setcomp)
    | '...' 

group:
    | '(' (yield_expr | named_expression) ')' 

# Lambda functions
# 람다 함수
# ----------------

lambdef:
    | 'lambda' [lambda_params] ':' expression 

lambda_params:
    | lambda_parameters

# lambda_parameters etc. duplicates parameters but without annotations
# or type comments, and if there's no comma after a parameter, we expect
# a colon, not a close parenthesis.  (For more, see parameters above.)
#
lambda_parameters:
    | lambda_slash_no_default lambda_param_no_default* lambda_param_with_default* [lambda_star_etc] 
    | lambda_slash_with_default lambda_param_with_default* [lambda_star_etc] 
    | lambda_param_no_default+ lambda_param_with_default* [lambda_star_etc] 
    | lambda_param_with_default+ [lambda_star_etc] 
    | lambda_star_etc 

lambda_slash_no_default:
    | lambda_param_no_default+ '/' ',' 
    | lambda_param_no_default+ '/' &':' 

lambda_slash_with_default:
    | lambda_param_no_default* lambda_param_with_default+ '/' ',' 
    | lambda_param_no_default* lambda_param_with_default+ '/' &':' 

lambda_star_etc:
    | '*' lambda_param_no_default lambda_param_maybe_default* [lambda_kwds] 
    | '*' ',' lambda_param_maybe_default+ [lambda_kwds] 
    | lambda_kwds 

lambda_kwds:
    | '**' lambda_param_no_default 

lambda_param_no_default:
    | lambda_param ',' 
    | lambda_param &':' 
lambda_param_with_default:
    | lambda_param default ',' 
    | lambda_param default &':' 
lambda_param_maybe_default:
    | lambda_param default? ',' 
    | lambda_param default? &':' 
lambda_param: NAME 

# LITERALS
# 리터럴
# ========

fstring_middle:
    | fstring_replacement_field
    | FSTRING_MIDDLE 
fstring_replacement_field:
    | '{' annotated_rhs '='? [fstring_conversion] [fstring_full_format_spec] '}' 
fstring_conversion:
    | "!" NAME 
fstring_full_format_spec:
    | ':' fstring_format_spec* 
fstring_format_spec:
    | FSTRING_MIDDLE 
    | fstring_replacement_field
fstring:
    | FSTRING_START fstring_middle* FSTRING_END 

string: STRING 
strings: (fstring|string)+ 

list:
    | '[' [star_named_expressions] ']' 

tuple:
    | '(' [star_named_expression ',' [star_named_expressions]  ] ')' 

set: '{' star_named_expressions '}' 

# Dicts
# 딕셔너리
# -----

dict:
    | '{' [double_starred_kvpairs] '}' 

double_starred_kvpairs: ','.double_starred_kvpair+ [','] 

double_starred_kvpair:
    | '**' bitwise_or 
    | kvpair

kvpair: expression ':' expression 

# Comprehensions & Generators
# 컴프리헨션 및 제너레이터
# ---------------------------

for_if_clauses:
    | for_if_clause+ 

for_if_clause:
    | 'async' 'for' star_targets 'in' ~ disjunction ('if' disjunction )* 
    | 'for' star_targets 'in' ~ disjunction ('if' disjunction )* 

listcomp:
    | '[' named_expression for_if_clauses ']' 

setcomp:
    | '{' named_expression for_if_clauses '}' 

genexp:
    | '(' ( assignment_expression | expression !':=') for_if_clauses ')' 

dictcomp:
    | '{' kvpair for_if_clauses '}' 

# FUNCTION CALL ARGUMENTS
# 함수 호출 인수
# =======================

arguments:
    | args [','] &')' 

args:
    | ','.(starred_expression | ( assignment_expression | expression !':=') !'=')+ [',' kwargs ] 
    | kwargs 

kwargs:
    | ','.kwarg_or_starred+ ',' ','.kwarg_or_double_starred+ 
    | ','.kwarg_or_starred+
    | ','.kwarg_or_double_starred+

starred_expression:
    | '*' expression 

kwarg_or_starred:
    | NAME '=' expression 
    | starred_expression 

kwarg_or_double_starred:
    | NAME '=' expression 
    | '**' expression 

# ASSIGNMENT TARGETS
# 할당 대상
# ==================

# Generic targets
# 일반 대상
# ---------------

# NOTE: star_targets may contain *bitwise_or, targets may not.
star_targets:
    | star_target !',' 
    | star_target (',' star_target )* [','] 

star_targets_list_seq: ','.star_target+ [','] 

star_targets_tuple_seq:
    | star_target (',' star_target )+ [','] 
    | star_target ',' 

star_target:
    | '*' (!'*' star_target) 
    | target_with_star_atom

target_with_star_atom:
    | t_primary '.' NAME !t_lookahead 
    | t_primary '[' slices ']' !t_lookahead 
    | star_atom

star_atom:
    | NAME 
    | '(' target_with_star_atom ')' 
    | '(' [star_targets_tuple_seq] ')' 
    | '[' [star_targets_list_seq] ']' 

single_target:
    | single_subscript_attribute_target
    | NAME 
    | '(' single_target ')' 

single_subscript_attribute_target:
    | t_primary '.' NAME !t_lookahead 
    | t_primary '[' slices ']' !t_lookahead 

t_primary:
    | t_primary '.' NAME &t_lookahead 
    | t_primary '[' slices ']' &t_lookahead 
    | t_primary genexp &t_lookahead 
    | t_primary '(' [arguments] ')' &t_lookahead 
    | atom &t_lookahead 

t_lookahead: '(' | '[' | '.'

# Targets for del statements
# del 문을 위한 대상
# --------------------------

del_targets: ','.del_target+ [','] 

del_target:
    | t_primary '.' NAME !t_lookahead 
    | t_primary '[' slices ']' !t_lookahead 
    | del_t_atom

del_t_atom:
    | NAME 
    | '(' del_target ')' 
    | '(' [del_targets] ')' 
    | '[' [del_targets] ']' 

# TYPING ELEMENTS
# 타이핑 요소
# ---------------

# type_expressions allow */** but ignore them
type_expressions:
    | ','.expression+ ',' '*' expression ',' '**' expression 
    | ','.expression+ ',' '*' expression 
    | ','.expression+ ',' '**' expression 
    | '*' expression ',' '**' expression 
    | '*' expression 
    | '**' expression 
    | ','.expression+ 

func_type_comment:
    | NEWLINE TYPE_COMMENT &(NEWLINE INDENT)   # Must be followed by indented block
    | TYPE_COMMENT

# ========================= END OF THE GRAMMAR ===========================
# ========================= 문법의 끝 ===========================

# ========================= START OF INVALID RULES =======================
# ========================= 유효하지 않은 규칙의 시작 =======================

