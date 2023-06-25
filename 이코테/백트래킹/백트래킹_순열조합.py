# 백트래킹 - 순열, 중복 순열, 조합, 중복 조합

# (1) 백트래킹 순열
array = [1,2,3]
k = 2  # 선택할 숫자의 개수
used = [False for i in range(len(array))]

def backtracking_perm(arr):
	if len(arr) == k:
		print(arr, end=" ")
		return arr
	
	for i in range(len(array)):
		if used[i] == False:
			used[i] = True
			backtracking_perm(arr + [array[i]])
			used[i] = False

backtracking_perm([])
# [1, 2] [1, 3] [2, 1] [2, 3] [3, 1] [3, 2]

print()

# (2) 백트래킹 순열 조합
array = [1,2,3]
k = 2  # 선택할 숫자의 개수

def backtracking_perm2(arr):
	if len(arr) == k:
		print(arr, end=" ")
		return arr
	
	for i in range(len(array)):
		backtracking_perm2(arr + [array[i]])

backtracking_perm2([])
# [1, 1] [1, 2] [1, 3] [2, 1] [2, 2] [2, 3] [3, 1] [3, 2] [3, 3]

print()

# (3) 백트래킹 조합
array = [1,2,3,4,5]
k = 2

def backtracking_comb(idx, arr):
	if len(arr) == k:
		print(arr, end=" ")
		return arr
	
	for i in range(idx, len(array)):
		backtracking_comb(i+1, arr + [array[i]])

backtracking_comb(0, [])
# [1, 2] [1, 3] [2, 3]

print()

# (4) 백트래킹 중복 조합
array = [1,2,3]
k = 2

def backtracking_comb(idx, arr):
	if len(arr) == k:
		print(arr, end=" ")
		return arr

	for i in range(idx, len(array)):
		backtracking_comb(i, arr + [array[i]])

backtracking_comb(0, [])
# [1, 1] [1, 2] [1, 3] [2, 2] [2, 3] [3, 3]