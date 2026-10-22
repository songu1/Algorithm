# 알고리즘 코드 템플릿


### (1) DFS

#### DFS - 재귀 방식 ⇒ depth가 깊으면 stackoverflow 발생 가능

```java
// 입력값
List<List<Integer>> graph = new ArrayList<>();
for (int i=0; i<=n; i++) graph.add(new ArrayList<>());
// 알고리즘
boolean[] visited = new boolean[n+1];
void dfs(int cur) {
	visited[cur] = true;
	for (int next : graph.get(cur)) {
		if (!visited[next]) {
			dfs(next);
		}
	}
}
```

#### DFS - 스택방식 (재귀없이) - Deque 사용

```java
boolean[] visited = new boolean[n+1];
Deque<Integer> stack = new ArrayDeque<>();
stack.push(start);

while(!stack.isEmpty()) {
	int cur = stack.pop();
	if (visited[cur])
		continue;
	visited[cur] = true;
	for (int next : graph.get(cur)) {
		if (!visited[next]) {
			stack.push(next);
		}
	}
}
```

### (2) BFS

#### BFS - 큐 방식

```java
boolean[] visited = new boolean[n+1];
Queue<Integer> queue = new LinkedList<>();
queue.offer(start);
visited[start] = true;

while (!queue.isEmpty() {
	int cur = queue.poll();
	for (int next : graph.get(cur)) {
		if (!visited[next]) {
			visited[next] = true;
			queue.offer(next);
		}
	}
}
```

💡 BFS는 최단 거리(간선 가중치가 모두 1일 때)를 구할 때 자주 씁니다. `dist[]` 배열을 하나 더 두고 `dist[next] = dist[cur] + 1`로 갱신하면 최단거리까지 구할 수 있습니다.

### (3) 이분 탐색

#### 이분 탐색 - 정렬된 배열에서 target의 위치 찾기

```java
int left=0, right = arr.length -1;
while (left <= right) {
		int mid = left + (right - left) / 2;  // (left+right)/2를 오버플로우 나지 않게 수정한 버전
		if (arr[mid] == target) {
				break;
		} else if (arr[mid] < target) {
				left = mid + 1;
		} else {
				right = mid - 1;
		}
}
```

#### 파라메트릭 서치 - 답이 될 수 있는 최댓값/최솟값을 이분탐색으로 찾기

- 이 경우 isPossible 은 단조성을 가져야함 - mid가 특정 값 이상/이하이면 무조건 true, mid가 그 미만/초과이면 항상 false형태여야함
    - "예산 M 이하로 물건을 살 수 있는 최소 개수" → 개수가 커질수록 비용이 늘어나니 특정 지점부터 true
    - "며칠 안에 배송을 마칠 수 있는 최소 트럭 대수" → 트럭이 많을수록 가능해지니 특정 대수부터 true

```java
int left = 최소 가능값, right = 최대 가능값;
int answer = 0;

// case 1) 할 수 있는 최댓값
while (left <= right) {
		int mid = left + (right-left)/2;
		if (isPossible(mid)) {  // mid가 조건을 만족하는지 판별
				answer = mid;
				left = mid + 1;     // 더 큰 값도 가능한지 탐색
		} else {
				right = mid - 1;
		}
}

// case 2) 할 수 있는 최솟값
while(left <= right) {
		int mid = left + (right-left)/2;
		if (isPossible(mid)) {
				answer = mid;
				right = mid - 1;     // 더 작은 값도 가능한지 탐색
		} else {
				left = mid + 1;
		}
}
```

### (4) 우선순위큐 + 다익스트라 (최단경로)

```java
int[] dist = new int[n+1];
Arrays.fill(dist, Integer.MAX_VALUE);
dist[start] = 0;

// graph.get(a) = List<int[]>, int[]는 {목적지, 가중치}
PriorityQueue<int[]> pg = new PriorityQueue<>((x,y) -> x[1] - y[1]);  // 오름차순
pq.offer(new int[] {start,0});

while(!pq.isEmpty()) {
		int[] cur = pq.poll();
		int node = cur[0], curDist = cur[1];
		// "지금 꺼낸 이 정보가 이미 더 나은 경로로 갱신된 뒤에 남아있는 낡은(stale) 정보인가" 를 체크
		if (curDist > dist[node]) continue;  // 이미 더 짧은 경로로 처리된 노드이면 스킵 - 빼먹으면 시간초과
		for (int[] edge : graph.get(node)) {
				int next = edge[0], weight = edge[1];
				int newDist = curDist + weight;
				if (newDist < dist[next]) {
						dist[next] = newDist;
						pq.offer(new int[]{next, newDist});
				}
		}
		// node 다음 위치 중 거리가 가장 짧은게 가장 높은 우선순위
}
		
```

### (5) Union-Find (분리 집합)

- 여러 원소들이 같은 그룹 안에 속해있는지를 확인하고 관리하는 자료구조

```java
// 각 원소마다 내 그룹의 대표가 누구인지를 가리키는 포인터를 가짐
int[] parent = new int[n+1];
for (int i=0; i <= n; i++)
		parent[i] = i;     // 초기화 : 처음엔 모두가 자기자신의 대표 

// find(x) : x가 속한 그룹의 대표가 누구인지
int find(int x) {
		if (parent[x] == x) return x;  // 내가 대표(대표의 parent는 자기자신)면 나를 반환
		return parent[x] = find(parent[x]);  // 아니면 부모를 따라 올라가서 대표를 찾기
}

// union(a,b) : a,b를 같은 그룹으로 합치
void union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		if (rootA != rootB) {
				parent[rootA] = rootB;  // 한쪽 그룹의 대표를 다른 쪽 대표 밑으로 붙임
		}
}

boolean isSameSet(int a, int b) {
		return find(a) == find(b);
```

💡 사이클 판별, 최소 신장 트리(크루스칼), 그룹 나누기 문제에서 자주 쓰입니다.

- 같은 그룹에 속해있는지 확인하고 싶을
- 여러 노드를 하나씩 연결해나가면서, **연결할 때마다 사이클(순환)이 생기는지 확인**하고 싶을 때 (크루스칼 최소신장트리 알고리즘의 핵심 부품)
- 그룹을 몇개로 나눌 수 있는지 세고 싶을때

### (6) DP (다이나믹 프로그래밍)

#### 1차원 DP - 타부턴 방식

```java
int[] dp = new int[n+1];
dp[0] = 0;  // 초기값은 문제에 따라 설정
dp[1] = ...;   // 필요하면 초기값 더 설정

for (int i=2; i<=n; i++) {
		dp[i] = dp[i-1] + dp[i-2];  // 점화식 예시 (피보나치 등)
}
return dp[n];

```

#### 2차원 DP - 배낭/경로형

- 배낭 문제 : dp[i][w] = i번째 물건까지 고려해 무게 w일때 최대 가치

```java
int[][] dp = new int[n+1][capacity+1];

for (int i=1; i<=n; i++) {
		for (int w=0; w <= capacity; w++) {
				if (weight[i] > w) {
						dp[i][w] = dp[i-1][w];
				} else {
						dp[i][w] = Math.max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i]);
				}
		}
}
```

- 경로형 DP(격자에서 최소/최다 경로 구하기) : 같은 2차원 패턴. `dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + cost[i][j]` 형태로 자주 변형되어 나옴

#### 메모이제이션(하향식, 재귀+캐시)

```java
Integer[] memo = new Integer[n+1];

int solve(int i) {
		if (i <= 1) return i;
		if (memo[i] != null) return memo[i];   // 이미 계산한 값이면 재계산 안함
		return memo[i] = solve(i-1) + solve(i-2);
		
```

🔧 **자주 하는 실수**: 메모이제이션에서 `memo` 배열을 `int[]`로 선언하면 기본값이 0이라 "아직 계산 안함"과 "계산해보니 값이 0임"을 구분하지 못합니다. `Integer[]`로 선언하면 초기값이 `null`이라 구분이 가능합니다.

### (7) 트리 순회

```java
class Node {
		int val;
		Node left, right;
}

// 전위 순회 (루트 -> 왼쪽 -> 오른쪽)
void preorder(Node node) {
		if (node == null) return;
		System.out.println(node.val + " ");  // 루트
		preorder(node.left);
		preorder(node.right);
}

// 중위 순회 (왼쪽 -> 루트 -> 오른쪽)
void inorder(Node node) {
		if (node == null) return;
		inorder(node.left);
		System.out.println(node.val + " ");  // 루트
		inorder(node.right);
}

// 후위 순회 (왼쪽 -> 오른쪽 -> 루트)
void postorder(Node node) {
		if (node == null) return;
		postorder(node.left);
		postorder(node.right);
		System.out.println(node.val + " ");  // 루트
}
```

💡 트리도 결국 DFS의 특수한 형태입니다. 순서(전위/중위/후위)만 상황에 맞게 조절하면 됩니다. BFS로 구하는 레벨순회(층순회)도 종종 나오는데, 이건 위의 BFS 템플릿을 그대로 쓰면 됩니다.

### (8) 그리디 체크리스트

1. 정렬하면 풀릴지를 의심하기 - 가장 흔한 패턴이 정렬 후 앞(또는 뒤)부터 하나씩 선택
2. 정렬 기준을 정하기 - 오름차순/내림차순, 어떤 값(비율, 차이, 끝나는 시간 등) 기준으로 정렬할지가 핵심
3. “매 순간 최적의 선택 = 전체 최적”이 증명되는지 확인 - 이게 안되면 그리디가 아니라 DP일 가능성이 높음. 그리디로 풀었는데 반례 테스트 케이스가 있다면 DP
4. 자주 나오는 기본 패턴 : 우선순위큐로 가장 

### (9) 백트래킹

#### 순열

```java
boolean[] used = new boolean[n];
int[] path = new int[n];

void permutation(int depth) {
		if (depth == n) {
				// path 배열이 완성된 순열 하나
				return;
		}
		for (int i=0; i<n; i++) {
				if (!used[i]) {
						used[i] = true;
						path[depth] = arr[i];
						permutation(depth+1);
						used[i] = false;
				}
		}
}
```

#### 조합

```java
int[] path = new int[r];

void combination(int start, int depth) {
		if (depth == r) {
				// path에 r개의 조합이 완성됨
				return ;
		}
		for (int i=start; i<n; i++) {
				path[depth] = arr[i];
				combination(i+1, depth+1);  // i+1부터 시작해야 중복 조합이 안 나오므이 역할
		}
}
```

🔧 **순열 vs 조합 헷갈림**: 순열은 다음 재귀에서 `i=0`부터 다시 훑는데(순서 구별), 조합은 `start`부터만 훑습니다(이미 고른 원소는 다시 안 밥음). 이 차이를 놓치면 중복이나 누락이 생깁니다.

#### 완전탐색 가지치기 (조기종료)

```java
void backtracking(int depth, int sum) {
		if (sum > target) return  // 가지치기: 더 진행해도 답이 될 수 없으면 즉시 리턴
		if (depth == n) {
				if (sum == target) {
						// 정답 처리
				}
				return;
		}
		// 배열의 각 원소를 부분집합에 넣을지 말지" 를 하나씩 결정해나가는 완전탐색(부분집합 생성)
		backtracking(depth+1, sum+arr[depth]);  // 포함 - 이 원소를 부분집합에 넣음
		backtracking(depth+1, sum);             // 미포함 - 이 원소를 부분집합에 넣지 않음
}
```

💡 완전탐색 문제는 가지치기(pruning) 없이 다 돌리면 시간초과가 나기 쉽습니다. "더 이상 진행해도 의미가 없다"는 조건을 최대한 일찍 찾아 return으로 끝내는 게 핵심입니다.

### (10) 투 포인터

💡 반드시 **정렬된 배열**에서만 쓸 수 있습니다. 정렬 안 된 배열이면 먼저 `Arrays.sort()` 하고 시작하세요.

```java
// 정렬된 배열에서 합이 target인 두 수 찾기
int left = 0, right arr.length - 1;
while (left < right) {
		int sum = arr[left] = arr[right];
		if (sum == target) {
				// 정답처리
				break;
		} else if (sum < target) {
				left++;
		} else {
				right--;
		}
}
```

- 서로 다른 pair를 구하기 때문에 while(left < right)
- 만약 자기 자신과 pair을 해도 된다면 while (left ≤ right)

### (11) 슬라이딩 윈도우

```java
// 예: 길이 k짜리 연속 부분배열 중 최대합
int sum = 0;
for (int i=0; i<k; i++) {
		sum += arr[i];   // 처음 창 채우기
}
int maxSum = sum;

for (int i=k; i < arr.length; i++) {
		sum += arr[i] - arr[i-k];   // 오른쪽 하나 추가, 왼쪽 하나 제거 (창 이동)
		maxSum = Math.max(maxSum, sum);
}
```

💡 매번 구간합을 다시 계산하면 O(n·k)인데, 이 방식으로 하면 O(n)으로 줄어듭니다. "연속된 구간" 키워드가 보이면 이 패턴을 의심하세요.

### (12) 소수 판별 (에라토스테네스의 체)

```java
// n이하의 수 중 소수 찾기
boolean[] isComposite = new boolean[n+1];  // true면 합성수(소수 아님)
List<Integer> primes = new ArrayList<>();

for (int i=2; i<=n; i++) {
		// 합성수이면 패스
		if (isComposite[i])
				continue;
		// 여기 도달했다는 건 i보다 작은 어떤 소수의 배수로도 지워지지 않았다는 뜻
		primes.add(i);  // i는 확정적으로 소수
		
		// 
		long start = (long) i*i  // i*i부터 시작 -> 그 전 배수는 더 작은 소수가 이미 지웠음
		for (long j=start; j<=n; j += i) {
				isComposite[(int) j] = true;
		}
} 
```

💡 하나씩 소수 판별(`isPrime()` 함수)은 O(√n)이지만, 여러 개 1~n 범위의 소수를 한꺼번에 구해야 하면 체가 훨씬 빠릅니다.

### (13) 누적합

#### 1차원 누적합

```java
int[] arr = {3,1,4,1,5,9,2,6};
int[] prefix = new int[arr.length+1];  // prefix[i] = arr[0] ~ arr[i-1]까지의 합

for (int i=0; i<arr.length; i++) {
		prefix[i+1] = prefix[i] + arr[i];
}

// arr[l] ~ arr[r] 구간합 (l,r 포함
int rangeSume = prefix[r+1] - prefix[l];
```

#### 2차원 누적합 (구상)

!image.png

!image.png

```java
int n = arr.length, m = arr[0].length;
int[][] prefix = new int[n+1][m+1];

for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        prefix[i + 1][j + 1] = arr[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
    }
}

// (r1,c1) ~ (r2,c2) 직사각형 구간합 (인덱스 포함)
int result = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1];
```

🔧 **외워두면 좋은 공식**: 포함-배제 원리입니다. 오른쪽 아래까지 다 더하면 왜쪽상단 구역이 두 번 곐치므로 한 번 빼줘야 합니다.

#### 합계가 특정값인 구간 개수 구하기 (누적합 + 해시맵 응용)

```java
// 예: 합계가 k인 연속 부분배열의 개수
// count 최종 answer
Map<Integer, Integer> countMap = new HashMap<>();  // 키 : 누적합 값 자체 , value : 값이 등장한 횟수
countMap.put(0,1);  // 누적합 0이 1번 등장했다고 미리 설정 (처음부터 합이 k인 경우를 위함)

int sum = 0, count = 0;
for (int num : arr) {
		sum += num;
		// 이 부분이 누적합으로 
		count += countMap.getOrDefault(sum-k, 0);  // (현재 누적합-k)가 이전에 몇번 등장했는지
		countMap.put(sum, countMap.getOrDefault(sum,0)+1); // 지금 이 sum의 값이 몇번나왔는지 조회에서 한번 더 나왔으니 +1하기
}
```

💡 "연속한 구간의 합이 k"를 구하는 문제는 누적합과 해시맵을 함께 쓰면 O(N)에 풀립니다. 투포인터로도 풀 수 있지만, 배열에 음수가 있으면 투포인터는 안 되고 이 방식만 됩니다.

### (14) 힙 (Top-K 패턴)

💡 **다 정렬해서 상위 K개를 찾는 것보다 훨씬 빠릅니다.** 전체 정렬은 O(N log N)인데, 힙을 크기 K로 유지하면 O(N log K)로 줄어듭니다. N이 크고 K가 작을수록 차이가 커집니다.

🔧 **최소힙 vs 최대힙 헷갈림**: "가장 큰 K개"를 찾을 때는 역설적으로 **최소힙**을 씁니다 (크기를 K로 유지하다가 가장 작은 값부터 밀어내기 위해). 반대로 "가장 작은 K개"를 찾을 때는 **최대힙**을 씁니다.

```java
// 예: 배열에서 가장 큰 K개의 값 찾기 — 최소힙 사용
PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // 기본이 최소합
for (int num : arr) {
		minHeap.offer(num);
		if (minHeap.size() > k) {
				minHeap.poll();  // 힙 크기가 k를 넘으면 가장 작은 값을 제거
		}
}

// 반복이 끝나면 minHeap에는 상위 K개만 남아있음
int kthLargest = minHeap.peek();  // 그 중 가장 작은 값 = 전체에서 k번째로 큰 값
```

```java
// 가장 작은 K개(꼴찌 K명) 찾기 — 최대힙 사용
PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

for (int num : arr) {
    maxHeap.offer(num);
    if (maxHeap.size() > k) {
        maxHeap.poll();   // 힙 크기가 k를 넘으면 가장 큰 값을 제거
    }
}
// 반복이 끝나면 maxHeap에는 하위 K개만 남아있음
int kthSmallest = maxHeap.peek();   // 그 중 가장 큰 값 = 전체에서 K번째로 작은 값
```

💡 "가장 작은 두 개를 계속 합치기" 유형(허프만 코딩 등)은 최소힙을 쓰는 대표적인 패턴입니다.

```java
// 두 개를 합치는 비용이 가장 적은 순서로 모두 합치기 (허프만 트리 등)
PriorityQueue<Integer> minHeap = new PriorityQueue<>();
for (int num : arr) minHeap.offer(num);

int totalCost = 0;
while (minHeap.size() > 1) {
  int a = minHeap.poll();
  int b = minHeap.poll();
  int merged = a + b;
  totalCost += merged;
  minHeap.offer(merged);
}
```

### (15) 위상정렬 - 공부 필

!image.png

```java
// 선수과목·작업 순서가 있는 문제 — 진입차수(indegree) 기반 Kahn's algorithm
int[] indegree = new int[n+1];
List<List<Integer>> graph = new ArrayList<>();
for (int i=0; i<=n; i++) graph.add(new ArrayList<>());

===================================
// 간선 추가 시: graph.get(a).add(b); indegree[b]++;  (a를 먼저 해야 b를 할 수 있음)

Queue<Integer> queue = new LinkedList<>();
for (int i = 1; i <= n; i++) {
    if (indegree[i] == 0) queue.offer(i);   // 선행 조건이 없는 노드부터 시작
}

List<Integer> result = new ArrayList<>();
while (!queue.isEmpty()) {
    int cur = queue.poll();
    result.add(cur);
    for (int next : graph.get(cur)) {
        indegree[next]--;
        if (indegree[next] == 0) {
            queue.offer(next);   // 진입차수가 0이 되면 이제 할 수 있는 상태
        }
    }
}

// result.size() != n 이면 사이클이 있어서 순서를 정할 수 없는 경우
```

> 💡 BFS와 거의 동일한 구조입니다. 차이는 `visited` 대신 **진입차수**를 쓰고, 진입차수가 0이 된(자기를 가로막는 선행 작업이 모두 끝난) 노드부터 처리한다는 점입니다.
> 

> 🔧 **사이클 판별**: 마지막에 `result.size()`가 노드 수 `n`과 다르면, 순환 구조(서로 맞물려 선행하는 관계)가 있어서 순서를 매길 수 없다는 뜻입니다. "이 작업이 가능한가?"를 물어보는 문제에서 이 판단이 핵심입니다.
> 

### (16) 크루스칼(MST)

모든 노드를 연결하되 간선의 총 가중치가 최소가 되도록 하는 문제에서 씁니다. 위에 있는 Union-Find를 그대로 재사용합니다.

!image.png

```java
// 간선을 {가중치, 노드A, 노드B} 형태로 저장
int[][] edges = new int[edgeCount][3];
// edges[i] = {weight, a, b};

Arrays.sort(edges, (x, y) -> x[0] - y[0]);   // 가중치 오름차순 정렬

int[] parent = new int[n + 1];
for (int i = 0; i <= n; i++) parent[i] = i;

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void union(int a, int b) {
    parent[find(a)] = find(b);
}

int totalWeight = 0;
int usedEdges = 0;

for (int[] edge : edges) {
    int weight = edge[0], a = edge[1], b = edge[2];
    if (find(a) != find(b)) {          // 사이클이 생기지 않는 경우만 선택
        union(a, b);
        totalWeight += weight;
        usedEdges++;
        if (usedEdges == n - 1) break;  // 노드 n개를 연결하려면 간선 n-1개면 충분
    }
}
```

> 💡 **핵심 아이디어는 그리디 + Union-Find입니다.** 가중치가 작은 간선부터 순서대로 보면서, "이 간선을 추가해도 사이클이 안 생기면(=아직 연결 안 된 두 그룹이면) 추가한다"만 반복합니다. 사이클 체크를 `find(a) != find(b)`로 O(거의 1)에 판별할 수 있어서 Union-Find와 세트로 씁니다.
> 

> 🔧 **간선 수 n-1개에서 멈추는 이유**: 노드가 n개인 트리는 간선이 정확히 n-1개일 때 모든 노드가 연결되면서 사이클도 없습니다. 그 이상 볼 필요가 없으니 일찍 끝내면 됩니다.
> 

> 💡 "네트워크 구축 비용 최소화", "모든 섬을 다리로 연결하는 최소 비용" 같은 문제에서 이 패턴이 자주 나옵니다.
> 

### 공통 주의사항

- 전역/static 변수 초기화 : 함수를 여러번 호출하는 문제에서 visited배열이나 카운터를 매번 초기화하지 않으면 이전 호출의 값이 남아있어 틀리게 된다.
- 오버플로우 : 값이 커질 수 있는 연산(곱셈, 누적합)은 `int` 대신 `long`을 쓰거나, `Integer.MAX_VALUE` 근처 연산을 할 때는 특히 주의하세요.
- for-each 도중 리스트 삭제
