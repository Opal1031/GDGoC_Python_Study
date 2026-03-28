# 2주차: 자료구조 (해시, 스택, 큐, 덱, 힙)

이번 주에는 Python에서 자주 사용하는 기본 자료구조인 해시, 스택, 큐, 덱, 힙에 대해 알아봅니다. 각 자료구조의 특징과 Python에서의 사용법, 그리고 간단한 예시 코드를 다룹니다.

---

## 1. 해시 (Hash, 딕셔너리)

- 해시는 키-값 쌍으로 데이터를 저장하는 자료구조입니다.
- Python에서는 `dict` 타입으로 구현되어 있습니다.

**시간복잡도**
- 삽입: 평균 O(1), 최악 O(n)
- 삭제: 평균 O(1), 최악 O(n)
- 탐색: 평균 O(1), 최악 O(n)

```python
d = {'apple': 3, 'banana': 5}
print(d['apple'])  # 3

d['orange'] = 7  # 값 추가

for key, value in d.items():
	print(key, value)
```

---

## 2. 스택 (Stack)

- 스택은 LIFO(Last-In, First-Out) 구조로, 마지막에 넣은 데이터가 가장 먼저 나옵니다.
- Python에서는 리스트(`list`)의 `append()`와 `pop()`을 사용해 구현할 수 있습니다.

**시간복잡도**
- 삽입(맨 뒤): O(1)
- 삭제(맨 뒤): O(1)
- 탐색(임의 위치): O(n)

```python
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())  # 3
print(stack)        # [1, 2]
```

---

## 3. 큐 (Queue)

- 큐는 FIFO(First-In, First-Out) 구조로, 먼저 넣은 데이터가 먼저 나옵니다.
- Python에서는 `collections.deque`를 사용하면 효율적으로 큐를 구현할 수 있습니다.

**시간복잡도**
- 삽입(뒤): O(1) (`deque` 기준)
- 삭제(앞): O(1) (`deque` 기준)
- 탐색(임의 위치): O(n)

```python
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())  # 1
print(queue)            # deque([2, 3])
```

---

## 4. 덱 (Deque)

- 덱은 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조입니다.
- Python의 `collections.deque`로 쉽게 구현할 수 있습니다.

**시간복잡도**
- 양쪽 삽입: O(1)
- 양쪽 삭제: O(1)
- 탐색(임의 위치): O(n)

```python
from collections import deque

dq = deque([1, 2, 3])

dq.appendleft(0)
dq.append(4)

print(dq)  # deque([0, 1, 2, 3, 4])

dq.pop()   # 4 제거
dq.popleft()  # 0 제거

print(dq)  # deque([1, 2, 3])
```

---

## 5. 힙 (Heap)

- 힙은 우선순위 큐를 구현할 때 사용하는 자료구조로, 최소값 또는 최대값을 빠르게 꺼낼 수 있습니다.
- Python에서는 `heapq` 모듈을 사용해 최소 힙을 구현할 수 있습니다.

**시간복잡도**
- 삽입: O(log n)
- 삭제(최솟값 추출): O(log n)
- 최솟값 확인: O(1)

```python
import heapq

heap = []

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # 1 (가장 작은 값)
print(heap)  # [2, 3]
```

---

## 6. 종합 요약

- 해시: dict, 키-값 쌍 저장, 빠른 접근
- 스택: list, append/pop, LIFO
- 큐: deque, append/popleft, FIFO
- 덱: deque, 양쪽 삽입/삭제
- 힙: heapq, 우선순위 큐, 최소/최대값 빠른 접근