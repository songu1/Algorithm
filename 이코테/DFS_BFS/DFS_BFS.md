# DFS/BFS

## 탐색(Search)

- 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- DFS, BFS → 코딩테스트에서 매우 자주 등장하는 유형(반드시 숙지!!!)⭐

# DFS/BFS를 위해 반드시 알아야할 자료구조

## 스택

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- 입구와 출구가 동일한 형태로 시각화
- 삽입, 삭제 2가지 연산으로 구성

### 파이썬 구현

- 리스트 자료구조 사용

```python
stack=[]

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력 (먼저 나가고자하는 원소부터)
print(stack)        # 최하단 원소부터 출력
# [1,3,2,5]
# [5,2,3,1]
```

### 자바 구현

```java
import java.util.*;

public class Main {
	public static void main(String[] args){
		Stack<Integer> S = new Stack<>();
		
		s.push(5);
		s.push(2);
		s.push(3);
		s.push(7);
		s.pop();
		s.push(1);
		s.push(4);
		s.pop();

		while(!s.empty()) {
			System.out.print(s.peek() + " ");
			s.pop();
		}
	}
}
```

## 큐

- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 입구와 출구가 모두 뜷려 있는 터널과 같은 형태로 시각화

### 파이썬 구현

- deque 라이브러리 이용

```python
from collections import deque

# 큐 구현을 위해 deque 라이브러리 이용
queue=deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5) # 오른쪽에 추가
queue.append(2) # 빼는 것
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저들어온 순서대로 출력        # deque([3,7,1,4])
queue.reverse()
print(queue)  # 나중에 들어온 원소부터 출력     # deque([4,1,7,3])

```

### 자바 구현

```java
import java.util.*;

public class Main {
	public static void main(String[] args){
		Queue<Integer> q = new LinkedList<>();
		
// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
		q.offer(5);
		q.offer(2);
		q.offer(3);
		q.offer(7);
		q.poll();
		q.offer(1);
		q.offer(4);
		q.poll();

		// 먼저 들어온 원소부터 추출
		while (!q.isEmpty()){
			System.out.print(q.poll()+" ");
		}
	}
}
```

## 재귀함수(Recursive Function)

- 자기 자신을 다시 호출하는 함수
- 파이선에서 최대 재귀 깊이 제한 → 최대 재귀 깊이 초과 메세지 출력
- 단순한 현태의 재귀함수 예제
    
    ```python
    def recursive_function():
    	print('재귀함수 호출')
    	recursive_function()
    
    recursive_function()
    ```
    
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야함
- 종료 조건을 제대로 명시하지 않으면 함수가 무한히 호출될 수 있음
    - 종료조건을 포함한 재귀함수 예제
        
        ```python
        def recursive_function(i):
        	# 100번째 호출을 했을 때 종료되도록 종료조건 명시
        	if i==100:
        		return
        	print(i, '번째 재귀함수에서' i+1, '번째 재귀함수를 호출합니다')
        	recursive(i+1)
        	print(i,'번째 재귀함수를 종료합니다')
        
        recursive_funtion(1)
        
        # 1~100번째 호출
        # 99~1 종료
        ```
        

### 팩토리얼 구현 예제

```python
# 반복적으로 구현한 n!
def factorial_iterative(n):
	result=1
	# 1부터 n까지의 수를 차례대로 곱하기
	for i in range(1,n+1):
		result *= i
	return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
	if n<=1:      # n이 1이하인 경우 1을 반환
		return 1
	# n! = n * (n-1)! 을 코드로 구현
	return n * factorial_recursive(n-1)

# n! 출력
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
```

### 유클리드 호제법 예제

- 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
- 유클리드 호제법
    - 두 자연수 A, B에 대해 (A>B) A를 B로 나눈 나머지를 R이라고 하자
    - A와 B의 최대공약수는 B와 R의 최대공약수와 같다
- 유클리드 호제법의 아이디어를 그대로 재귀함수에 작성
    - GCD(192,162)
        
        
        | A | B |
        | --- | --- |
        | 192 | 162 |
        | 162 | 30 |
        | 30 | 12 |
        | 12 | 6 |
- 코드
    
    ```python
    def gcd(a,b):
    	if a%b==0:
    		return b
    	else:
    		return gcd(b,a%b)
    
    print(gcd(192,162))
    ```
    

<aside>
💡 **재귀 함수 사용의 유의사항**

- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성 가능
    - 다른 사람이 이해하기 어려운 코드가 될 수 있으므로 신중하게!
- 모든 재귀함수는 반복문을 이용하여 동일한 기능 구현 가능
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 내부의 스택 프레임이 쌓임
    - 스택을 사용 시 스택 라이브러리 대신에 재귀함수 사용하는 경우 많음
</aside>

# DFS (Depth-First Search)

- **깊이 우선 탐색**
- 그래프에서 **깊은 부분을 우선적으로 탐색**하는 알고리즘
- **스택 자료구조(재귀함수)** 이용
    1. **탐색 시작 노드**를 **스택**에 삽입, **방문처리**
    2. 스택의 최상단 노드의 인접노드 확인
        1. 방문하지 않은 **인접 노드가 하나라도 있음** : **그 노드를 스택**에 넣고 **방문 처리**
        2. 방문하지 않은 **인접 노드가 없음** : **스택에서 최상단 노드를 꺼냄**
    3. 2번의 과정을 수행할 수 없을 때까지 반복

### 파이썬 코드

```python
# DFS 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v]=True
	print(v, end=' ')
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph=[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9  # index 0을 사용하지 않기 위해 9개 선언

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

### 자바 코드

```java
import java.util.*;

public class Main {
	public static boolean[] visited = new boolean[9];
	public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

	public static void dfs(int x) {
		//현재 노드 방문 처리
		visited[x]=true;
		System.out.print(x+" ");
		// 현재 노드와 연결된 다른 노드를 재귀적으로 방문
		for (int i=0; i < graph.get(x).size(); i++) {
			int y=graph.get(x).get(i);
			if (!visited[y]) dfs(y);
		}
	}
	public static void main(String[] args) {
	// 생략
	}
}
```

# BFS (Breadth-First Search)

- **너비 우선 탐색**
- 그래프에서 **가까운 노드부터 우선적으로 탐색**하는 알고리즘
- **큐 자료구조**
    1. **탐색 시작노드를 큐에 삽입**하고 **방문처리**
    2. 큐에서 노드를 꺼낸 뒤 해당 노드의 **인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입**하고 **방문처리**
    3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복

### 파이썬 코드

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
	# 큐 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start]=True
	# 큐가 빌 때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력하기
		v=queue.popleft()
		print(v, end=' ')
		# 아직 방문하지 않은 인접한 원소들을 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i]=True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph=[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9  # index 0을 사용하지 않기 위해 9개 선언

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)
```

### 자바 코드

```java
import java.util.*;

public class Main {
	public static boolean[] visited = new boolean[9];
	public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

	public static void bfs(int start) {
		Queue<Integer> q= new LinkedList<>();
		q.offer(start);
		//현재 노드 방문 처리
		visited[start]=true;
		// 큐가 빌 때까지 반복
		while(!q.isEmpty()) {
			// 큐에서 하나의 원소를 뽑아 출력
			int x=q.poll();
			System.out.print(x+" ");
			// 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
			for (int i=0; i < graph.get(x).size(); i++) {
				int y=graph.get(x).get(i);
				if (!visited[y]) {
					q.offer(y);
					visited[y]=true;
				}
			}
		}
	}
	// 메인 함수 생략
}
```