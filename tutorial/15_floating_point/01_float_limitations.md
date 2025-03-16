# 15. Floating-Point Arithmetic: Issues and Limitations

1. Floating-point numbers are represented in computer hardware as base 2 (binary) fractions. For example, the decimal fraction 0.625 has value 6/10 + 2/100 + 5/1000, and in the same way the binary fraction 0.101 has value 1/2 + 0/4 + 1/8. These two fractions have identical values, the only real difference being that the first is written in base 10 fractional notation, and the second in base 2.

부동 소수점 수는 컴퓨터 하드웨어에서 2진수(이진) 분수로 표현됩니다. 예를 들어, 십진 소수 0.625는 6/10 + 2/100 + 5/1000의 값을 가지며, 마찬가지로 이진 분수 0.101은 1/2 + 0/4 + 1/8의 값을 가집니다. 이 두 분수는 동일한 값을 가지며, 유일한 실제 차이는 첫 번째는 10진수 분수 표기법으로 쓰여졌고, 두 번째는 2진수로 쓰여졌다는 점입니다.

2. Unfortunately, most decimal fractions cannot be represented exactly as binary fractions. A consequence is that, in general, the decimal floating-point numbers you enter are only approximated by the binary floating-point numbers actually stored in the machine.

불행히도, 대부분의 10진 분수는 이진 분수로 정확하게 표현될 수 없습니다. 결과적으로, 일반적으로 입력한 10진 부동 소수점 숫자는 실제로 기계에 저장된 이진 부동 소수점 숫자에 의해 근사화될 뿐입니다.

3. The problem is easier to understand at first in base 10. Consider the fraction 1/3. You can approximate that as a base 10 fraction:

이 문제는 처음에는 10진수로 이해하기 쉽습니다. 분수 1/3을 생각해보세요. 이것을 10진 분수로 근사화할 수 있습니다:

```
0.3
```

4. or, better,

또는, 더 나은 방법으로,

```
0.33
```

5. or, better,

또는, 더 나은 방법으로,

```
0.333
```

6. and so on. No matter how many digits you're willing to write down, the result will never be exactly 1/3, but will be an increasingly better approximation of 1/3.

등등. 얼마나 많은 자릿수를 적을 의향이 있든, 결과는 결코 정확히 1/3이 될 수 없으며, 1/3에 점점 더 가까운 근사값이 될 것입니다.

7. In the same way, no matter how many base 2 digits you're willing to use, the decimal value 0.1 cannot be represented exactly as a base 2 fraction. In base 2, 1/10 is the infinitely repeating fraction

마찬가지로, 사용하고자 하는 2진수 자릿수가 얼마나 많든, 십진수 값 0.1은 2진 분수로 정확하게 표현될 수 없습니다. 2진수에서 1/10은 무한히 반복되는 소수입니다:

```
0.0001100110011001100110011001100110011001100110011...
```

8. Stop at any finite number of bits, and you get an approximation. On most machines today, floats are approximated using a binary fraction with the numerator using the first 53 bits starting with the most significant bit and with the denominator as a power of two. In the case of 1/10, the binary fraction is 3602879701896397 / 2 ** 55 which is close to but not exactly equal to the true value of 1/10.

어떤 유한한 비트 수에서 멈추더라도, 근사값을 얻게 됩니다. 오늘날 대부분의 기계에서, 부동 소수점은 가장 중요한 비트부터 시작하는 첫 53비트를 사용하는 분자와 2의 거듭제곱을 분모로 하는 이진 분수를 사용하여 근사화됩니다. 1/10의 경우, 이진 분수는 3602879701896397 / 2 ** 55이며, 이는 1/10의 실제 값에 가깝지만 정확히 같지는 않습니다.

9. Many users are not aware of the approximation because of the way values are displayed. Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine. On most machines, if Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display:

많은 사용자는 값이 표시되는 방식 때문에 근사값임을 인식하지 못합니다. Python은 기계에 저장된 이진 근사값의 실제 10진 값에 대한 10진 근사값만 출력합니다. 대부분의 기계에서, Python이 0.1에 대해 저장된 이진 근사값의 실제 10진 값을 출력한다면, 다음과 같이 표시해야 할 것입니다:

```python
>>> 0.1
0.1000000000000000055511151231257827021181583404541015625
```

10. That is more digits than most people find useful, so Python keeps the number of digits manageable by displaying a rounded value instead:

이는 대부분의 사람들이 유용하다고 생각하는 것보다 더 많은 자릿수입니다. 따라서 Python은 대신 반올림된 값을 표시하여 자릿수를 관리하기 쉽게 유지합니다:

```python
>>> 1 / 10
0.1
```

11. Just remember, even though the printed result looks like the exact value of 1/10, the actual stored value is the nearest representable binary fraction.

기억해야 할 것은, 출력된 결과가 1/10의 정확한 값처럼 보이지만, 실제 저장된 값은 표현 가능한 가장 가까운 이진 분수라는 것입니다.

12. Interestingly, there are many different decimal numbers that share the same nearest approximate binary fraction. For example, the numbers 0.1 and 0.10000000000000001 and 0.1000000000000000055511151231257827021181583404541015625 are all approximated by 3602879701896397 / 2 ** 55. Since all of these decimal values share the same approximation, any one of them could be displayed while still preserving the invariant eval(repr(x)) == x.

흥미롭게도, 동일한 가장 가까운 근사 이진 분수를 공유하는 많은 다른 10진수가 있습니다. 예를 들어, 숫자 0.1과 0.10000000000000001과 0.1000000000000000055511151231257827021181583404541015625는 모두 3602879701896397 / 2 ** 55로 근사화됩니다. 이러한 모든 10진값이 동일한 근사값을 공유하기 때문에, 이들 중 어느 하나라도 eval(repr(x)) == x 불변성을 유지하면서 표시될 수 있습니다.

13. Historically, the Python prompt and built-in repr() function would choose the one with 17 significant digits, 0.10000000000000001. Starting with Python 3.1, Python (on most systems) is now able to choose the shortest of these and simply display 0.1.

역사적으로, Python 프롬프트와 내장 repr() 함수는 17개의 유효 숫자를 가진 0.10000000000000001을 선택했습니다. Python 3.1부터, Python은 (대부분의 시스템에서) 이들 중 가장 짧은 것을 선택하여 단순히 0.1을 표시할 수 있게 되었습니다.

14. Note that this is in the very nature of binary floating point: this is not a bug in Python, and it is not a bug in your code either. You'll see the same kind of thing in all languages that support your hardware's floating-point arithmetic (although some languages may not display the difference by default, or in all output modes).

이것은 이진 부동 소수점의 본질적인 성질입니다: 이는 Python의 버그가 아니며, 당신의 코드의 버그도 아닙니다. 하드웨어의 부동 소수점 연산을 지원하는 모든 언어에서 동일한 종류의 현상을 볼 수 있습니다(일부 언어는 기본적으로 또는 모든 출력 모드에서 차이를 표시하지 않을 수 있습니다).

15. For more pleasant output, you may wish to use string formatting to produce a limited number of significant digits:

더 보기 좋은 출력을 위해, 문자열 포매팅을 사용하여 제한된 수의 유효 숫자를 생성할 수 있습니다:

```python
>>> import math
>>> format(math.pi, '.12g')  # give 12 significant digits
'3.14159265359'
>>> 
>>> format(math.pi, '.2f')   # give 2 digits after the point
'3.14'
>>> 
>>> repr(math.pi)
'3.141592653589793'
```

16. It's important to realize that this is, in a real sense, an illusion: you're simply rounding the display of the true machine value.

이것이 실제로는 환상에 불과하다는 것을 인식하는 것이 중요합니다: 단순히 실제 기계 값의 표시를 반올림하는 것일 뿐입니다.

17. One illusion may beget another. For example, since 0.1 is not exactly 1/10, summing three values of 0.1 may not yield exactly 0.3, either:

하나의 환상이 다른 환상을 낳을 수 있습니다. 예를 들어, 0.1이 정확히 1/10이 아니기 때문에, 0.1의 세 값을 합해도 정확히 0.3이 되지 않을 수 있습니다:

```python
>>> 0.1 + 0.1 + 0.1 == 0.3
False
```

18. Also, since the 0.1 cannot get any closer to the exact value of 1/10 and 0.3 cannot get any closer to the exact value of 3/10, then pre-rounding with round() function cannot help:

또한, 0.1이 1/10의 정확한 값에 더 가까워질 수 없고 0.3이 3/10의 정확한 값에 더 가까워질 수 없기 때문에, round() 함수로 미리 반올림하는 것도 도움이 되지 않습니다:

```python
>>> round(0.1, 1) + round(0.1, 1) + round(0.1, 1) == round(0.3, 1)
False
```

19. Though the numbers cannot be made closer to their intended exact values, the math.isclose() function can be useful for comparing inexact values:

숫자들이 의도한 정확한 값에 더 가까워질 수 없지만, 부정확한 값들을 비교하는 데 math.isclose() 함수가 유용할 수 있습니다:

```python
>>> import math
>>> math.isclose(0.1 + 0.1 + 0.1, 0.3)
True
```

20. Alternatively, the round() function can be used to compare rough approximations:

대안으로, round() 함수를 사용하여 대략적인 근사치를 비교할 수 있습니다:

```python
>>> round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
True
```

21. Binary floating-point arithmetic holds many surprises like this. The problem with "0.1" is explained in precise detail below, in the "Representation Error" section. See Examples of Floating Point Problems for a pleasant summary of how binary floating point works and the kinds of problems commonly encountered in practice. Also see The Perils of Floating Point for a more complete account of other common surprises.

이진 부동 소수점 연산은 이와 같은 많은 놀라운 점을 가지고 있습니다. "0.1"의 문제는 아래 "표현 오차" 섹션에서 정밀하게 설명됩니다. 이진 부동 소수점이 어떻게 작동하는지와 실제로 흔히 마주치는 문제의 종류에 대한 간략한 요약은 "부동 소수점 문제의 예"를 참조하십시오. 또한 다른 일반적인 놀라운 점들에 대한 더 완전한 설명은 "부동 소수점의 위험"을 참조하십시오.

22. As that says near the end, "there are no easy answers." Still, don't be unduly wary of floating point! The errors in Python float operations are inherited from the floating-point hardware, and on most machines are on the order of no more than 1 part in 2**53 per operation. That's more than adequate for most tasks, but you do need to keep in mind that it's not decimal arithmetic and that every float operation can suffer a new rounding error.

끝 부분에서 언급한 대로, "쉬운 답은 없습니다." 그럼에도 불구하고, 부동 소수점을 지나치게 경계하지 마세요! Python 부동 소수점 연산의 오류는 부동 소수점 하드웨어에서 상속된 것이며, 대부분의 기계에서 연산당 2**53분의 1 이하의 크기입니다. 이는 대부분의 작업에 충분하지만, 10진 산술이 아니며 모든 부동 소수점 연산이 새로운 반올림 오류를 겪을 수 있다는 점을 명심해야 합니다.

23. While pathological cases do exist, for most casual use of floating-point arithmetic you'll see the result you expect in the end if you simply round the display of your final results to the number of decimal digits you expect. str() usually suffices, and for finer control see the str.format() method's format specifiers in Format String Syntax.

병리학적인 경우가 존재하기는 하지만, 부동 소수점 산술의 대부분의 일상적인 사용에서는 최종 결과의 표시를 예상하는 십진수 자릿수로 반올림하면 결국 기대하는 결과를 볼 수 있습니다. 보통은 str()로 충분하며, 더 세밀한 제어를 위해서는 형식 문자열 구문의 str.format() 메서드 형식 지정자를 참조하십시오.

24. For use cases which require exact decimal representation, try using the decimal module which implements decimal arithmetic suitable for accounting applications and high-precision applications.

정확한 십진수 표현이 필요한 사용 사례의 경우, 회계 응용 프로그램 및 고정밀 응용 프로그램에 적합한 십진 산술을 구현하는 decimal 모듈을 사용해 보세요.

25. Another form of exact arithmetic is supported by the fractions module which implements arithmetic based on rational numbers (so the numbers like 1/3 can be represented exactly).

또 다른 형태의 정확한 산술은 유리수에 기반한 산술을 구현하는 fractions 모듈에 의해 지원됩니다(따라서 1/3과 같은 숫자를 정확히 표현할 수 있습니다).

26. If you are a heavy user of floating-point operations you should take a look at the NumPy package and many other packages for mathematical and statistical operations supplied by the SciPy project. See <https://scipy.org>.

부동 소수점 연산을 많이 사용한다면 NumPy 패키지와 SciPy 프로젝트에서 제공하는 많은 수학 및 통계 연산 패키지를 살펴봐야 합니다. <https://scipy.org>를 참조하십시오.

27. Python provides tools that may help on those rare occasions when you really do want to know the exact value of a float. The float.as_integer_ratio() method expresses the value of a float as a fraction:

Python은 부동 소수점의 정확한 값을 알고 싶은 드문 경우에 도움이 될 수 있는 도구를 제공합니다. float.as_integer_ratio() 메서드는 부동 소수점의 값을 분수로 표현합니다:

```python
>>> x = 3.14159
>>> x.as_integer_ratio()
(3537115888337719, 1125899906842624)
```

28. Since the ratio is exact, it can be used to losslessly recreate the original value:

이 비율은 정확하므로, 원래 값을 손실 없이 재창조하는 데 사용될 수 있습니다:

```python
>>> x == 3537115888337719 / 1125899906842624
True
```

29. The float.hex() method expresses a float in hexadecimal (base 16), again giving the exact value stored by your computer:

float.hex() 메서드는 부동 소수점을 16진수(기수 16)로 표현하며, 다시 한 번 컴퓨터에 저장된 정확한 값을 제공합니다:

```python
>>> x.hex()
'0x1.921f9f01b866ep+1'
```

30. This precise hexadecimal representation can be used to reconstruct the float value exactly:

이 정확한 16진 표현은 부동 소수점 값을 정확히 재구성하는 데 사용될 수 있습니다:

```python
>>> x == float.fromhex('0x1.921f9f01b866ep+1')
True
```

31. Since the representation is exact, it is useful for reliably porting values across different versions of Python (platform independence) and exchanging data with other languages that support the same format (such as Java and C99).

표현이 정확하기 때문에, 이는 다른 버전의 Python 간에 값을 신뢰성 있게 이식하고(플랫폼 독립성) 동일한 형식을 지원하는 다른 언어(Java 및 C99와 같은)와 데이터를 교환하는 데 유용합니다.

32. Another helpful tool is the sum() function which helps mitigate loss-of-precision during summation. It uses extended precision for intermediate rounding steps as values are added onto a running total. That can make a difference in overall accuracy so that the errors do not accumulate to the point where they affect the final total:

또 다른 유용한 도구는 합산 중 정밀도 손실을 완화하는 데 도움이 되는 sum() 함수입니다. 값이 누적 합계에 추가될 때 중간 반올림 단계에서 확장된 정밀도를 사용합니다. 이는 전체 정확도에 차이를 만들어 오류가 최종 합계에 영향을 미치는 지점까지 누적되지 않도록 합니다:

```python
>>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
False
>>> sum([0.1] * 10) == 1.0
True
```

33. The math.fsum() goes further and tracks all of the "lost digits" as values are added onto a running total so that the result has only a single rounding. This is slower than sum() but will be more accurate in uncommon cases where large magnitude inputs mostly cancel each other out leaving a final sum near zero:

math.fsum()는 더 나아가 값이 누적 합계에 추가될 때 모든 "손실된 자릿수"를 추적하여 결과에 단 한 번의 반올림만 있도록 합니다. 이는 sum()보다 느리지만, 크기가 큰 입력이 대부분 서로 상쇄되어 최종 합계가 0에 가까운 드문 경우에서 더 정확합니다:

```python
>>> import math
>>> from fractions import Fraction
>>> arr = [-0.10430216751806065, -266310978.67179024, 143401161448607.16,
...        -143401161400469.7, 266262841.31058735, -0.003244936839808227]
>>> float(sum(map(Fraction, arr)))   # Exact summation with single rounding
8.042173697819788e-13
>>> math.fsum(arr)                   # Single rounding
8.042173697819788e-13
>>> sum(arr)                         # Multiple roundings in extended precision
8.042178034628478e-13
>>> total = 0.0
>>> for x in arr:
...     total += x                   # Multiple roundings in standard precision
... 
>>> total                            # Straight addition has no correct digits!
-0.0051575902860057365
```

## 15.1. Representation Error

34. This section explains the "0.1" example in detail, and shows how you can perform an exact analysis of cases like this yourself. Basic familiarity with binary floating-point representation is assumed.

이 섹션에서는 "0.1" 예제를 상세히 설명하고, 이와 같은 경우에 대해 어떻게 정확한 분석을 수행할 수 있는지 보여줍니다. 이진 부동 소수점 표현에 대한 기본 지식을 전제로 합니다.

35. Representation error refers to the fact that some (most, actually) decimal fractions cannot be represented exactly as binary (base 2) fractions. This is the chief reason why Python (or Perl, C, C++, Java, Fortran, and many others) often won't display the exact decimal number you expect.

표현 오차는 일부(사실은 대부분의) 10진 분수가 이진(기수 2) 분수로 정확히 표현될 수 없다는 사실을 말합니다. 이는 Python(또는 Perl, C, C++, Java, Fortran 등 많은 언어)이 종종 예상하는 정확한 10진수를 표시하지 않는 주요 이유입니다.

36. Why is that? 1/10 is not exactly representable as a binary fraction. Since at least 2000, almost all machines use IEEE 754 binary floating-point arithmetic, and almost all platforms map Python floats to IEEE 754 binary64 "double precision" values. IEEE 754 binary64 values contain 53 bits of precision, so on input the computer strives to convert 0.1 to the closest fraction it can of the form J/2**N where J is an integer containing exactly 53 bits. Rewriting

왜 그럴까요? 1/10은 이진 분수로 정확히 표현될 수 없습니다. 적어도 2000년부터, 거의 모든 기계는 IEEE 754 이진 부동 소수점 연산을 사용하고, 거의 모든 플랫폼은 Python 부동 소수점을 IEEE 754 binary64 "배정밀도" 값에 매핑합니다. IEEE 754 binary64 값은 53비트의 정밀도를 포함하므로, 입력 시 컴퓨터는 0.1을 J/2**N 형태의 가장 가까운 분수로 변환하려고 노력하며, 여기서 J는 정확히 53비트를 포함하는 정수입니다. 다시 쓰면:

```
1 / 10 ~= J / (2**N)
```

37. as

다음과 같이:

```
J ~= 2**N / 10
```

38. and recalling that J has exactly 53 bits (is >= 2**52 but < 2**53), the best value for N is 56:

그리고 J가 정확히 53비트(>= 2**52이지만 < 2**53)라는 것을 상기하면, N에 대한 최선의 값은 56입니다:

```python
>>> 2**52 <=  2**56 // 10  < 2**53
True
```

39. That is, 56 is the only value for N that leaves J with exactly 53 bits. The best possible value for J is then that quotient rounded:

즉, 56은 J를 정확히 53비트로 남기는 N의 유일한 값입니다. J에 대한 가능한 최선의 값은 그 몫을 반올림한 것입니다:

```python
>>> q, r = divmod(2**56, 10)
>>> r
6
```

40. Since the remainder is more than half of 10, the best approximation is obtained by rounding up:

나머지가 10의 절반보다 크기 때문에, 최선의 근사치는 올림을 통해 얻어집니다:

```python
>>> q+1
7205759403792794
```

41. Therefore the best possible approximation to 1/10 in IEEE 754 double precision is:

따라서 IEEE 754 배정밀도에서 1/10에 대한 가능한 최선의 근사치는 다음과 같습니다:

```
7205759403792794 / 2 ** 56
```

42. Dividing both the numerator and denominator by two reduces the fraction to:

분자와 분모를 둘 다 2로 나누면 분수가 다음과 같이 축소됩니다:

```
3602879701896397 / 2 ** 55
```

43. Note that since we rounded up, this is actually a little bit larger than 1/10; if we had not rounded up, the quotient would have been a little bit smaller than 1/10. But in no case can it be exactly 1/10!

우리가 올림을 했기 때문에, 이것은 실제로 1/10보다 약간 큽니다. 만약 올림을 하지 않았다면, 몫은 1/10보다 약간 작았을 것입니다. 그러나 어떤 경우에도 정확히 1/10일 수는 없습니다!

44. So the computer never "sees" 1/10: what it sees is the exact fraction given above, the best IEEE 754 double approximation it can get:

따라서 컴퓨터는 결코 1/10을 "보지" 않습니다: 컴퓨터가 보는 것은 위에서 주어진 정확한 분수, 즉 얻을 수 있는 최선의 IEEE 754 배정밀도 근사치입니다:

```python
>>> 0.1 * 2 ** 55
3602879701896397.0
```

45. If we multiply that fraction by 10**55, we can see the value out to 55 decimal digits:

그 분수에 10**55를 곱하면, 55개의 10진수 자릿수까지 값을 볼 수 있습니다:

```python
>>> 3602879701896397 * 10 ** 55 // 2 ** 55
1000000000000000055511151231257827021181583404541015625
```

46. meaning that the exact number stored in the computer is equal to the decimal value 0.1000000000000000055511151231257827021181583404541015625. Instead of displaying the full decimal value, many languages (including older versions of Python), round the result to 17 significant digits:

즉, 컴퓨터에 저장된 정확한 숫자는 10진수 값 0.1000000000000000055511151231257827021181583404541015625와 같습니다. 전체 10진수 값을 표시하는 대신, 많은 언어(Python의 이전 버전 포함)는 결과를 17개의 유효 숫자로 반올림합니다:

```python
>>> format(0.1, '.17f')
'0.10000000000000001'
```

47. The fractions and decimal modules make these calculations easy:

fractions와 decimal 모듈은 이러한 계산을 쉽게 만듭니다:

```python
>>> from decimal import Decimal
>>> from fractions import Fraction
>>>
>>> Fraction.from_float(0.1)
Fraction(3602879701896397, 36028797018963968)
>>>
>>> (0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)
>>>
>>> Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')
>>>
>>> format(Decimal.from_float(0.1), '.17')
'0.10000000000000001'
```
