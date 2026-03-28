# 2주차: 입출력 고급

이번 주에는 Python에서 입출력(I/O)을 더 빠르고 효율적으로 처리하는 방법에 대해 알아봅니다. 특히, 대용량 데이터 처리 시 유용한 `sys.stdin`, `sys.stdout` 사용법, 입력 속도 개선, EOFError 처리, 여러 줄 입력 처리(map, split 활용)에 대해 다룹니다.

---

## 1. sys 모듈과 빠른 입출력

- `sys` 모듈은 파이썬 표준 라이브러리로, 표준 입출력(키보드 입력, 화면 출력) 등 다양한 시스템 관련 기능을 제공합니다. 대용량 데이터 처리나 입력 속도 개선이 필요할 때 자주 사용됩니다.
- 기본적으로 `input()` 함수는 느릴 수 있습니다. 많은 데이터를 입력받을 때는 `sys.stdin.readline()`을 사용하는 것이 훨씬 빠릅니다.
- 출력도 마찬가지로, `print()` 대신 `sys.stdout.write()`를 사용하면 속도 개선에 도움이 됩니다.

아래는 대용량 입력을 빠르게 처리하는 예시입니다.

```python
import sys
input = sys.stdin.readline

for _ in range(n):
    data = input().strip()  # 개행 문자 제거

    print(data)
```

여러 줄을 한 번에 입력받아 처리할 때는 다음과 같이 할 수 있습니다.

```python
import sys
lines = sys.stdin.read().splitlines()

for line in lines:
    print(line)
```

---

## 2. split과 map의 활용

- 여러 개의 값을 한 줄에 입력받을 때는 `split()`과 `map()`을 함께 사용하면 편리합니다.
- `문자열.split()`은 입력받은 문자열을 공백 기준으로 나누어 리스트로 만들어주고, `map(적용할 함수, 데이터 집합)`은 리스트의 각 요소를 지정한 함수로 변환해줍니다.

예를 들어, 아래와 같이 한 줄에 여러 정수를 입력받아 각각 변수에 저장할 수 있습니다.

```python
a, b = map(int, input().split())
# a, b의 값을 각각 받지 않고 split() 함수를 통해 한번에 input 받기
# 입력 받은 값들을 map() 함수를 통해 int의 형태로 각각 저장
```

또는 여러 숫자를 리스트로 받을 수도 있습니다.

```python
nums = list(map(int, input().split()))

print(nums)
```

여러 줄에 걸쳐 여러 개의 값을 입력받아 처리해야 할 때도 split()과 map()을 활용할 수 있습니다.

```python
import sys
lines = sys.stdin.read().splitlines()

for line in lines:
    nums = list(map(int, line.split()))

    print(nums)
```

---

## 3. EOF(End Of File) 처리

- 입력의 끝(EOF, End Of File)에 도달하면 더 이상 읽을 데이터가 없어 에러가 발생할 수 있습니다.
- while문과 try/except 구문을 사용하여 안전하게 입력을 처리할 수 있습니다.

아래 예시처럼 입력이 끝날 때까지 반복해서 값을 받고, 더 이상 입력이 없으면 EOFError를 감지해 반복문을 종료할 수 있습니다.

```python
import sys
input = sys.stdin.readline

while True:
    try:
        a = int(input())

        if (a == 0):
            break

        print(a)

    except EOFError:
        break
```

또는 아래와 같이 입력이 끝날 때까지 한 줄씩 받아 출력할 수도 있습니다.

```python
import sys
input = sys.stdin.readline

while True:
    try:
        line = input()
        print(line)

    except EOFError:
        break
```

---

## 4. 자주 하는 실수/주의점

- `sys.stdin.readline()`은 입력 끝에 개행문자(`\n`)가 포함되므로, `.strip()`을 꼭 사용해야 합니다.
- `print()`는 출력 후 자동으로 줄바꿈을 하지만, `sys.stdout.write()`는 줄바꿈이 없으니 필요하면 `"\n"`을 직접 붙여야 합니다.
- `input()`과 `sys.stdin.readline()`은 속도 차이가 크므로, 반복문에서 많은 입력을 받을 때는 반드시 `sys.stdin.readline()`을 사용하세요.
- `sys.stdin.read()`는 모든 입력을 한 번에 읽으므로, 데이터가 너무 많으면 메모리 사용량이 커질 수 있습니다.
- 입력 예시를 테스트할 때, 입력이 끝나지 않으면 프로그램이 멈춰 있을 수 있으니 주의하세요.

---

## 5. 종합 요약

- 대용량 입력: `sys.stdin.readline()` 또는 `sys.stdin.read()`
- 출력 속도 개선: `sys.stdout.write()`
- EOF 처리: try-except EOFError
- 여러 줄/여러 값 입력: `split()`, `map()` 활용