# 겹치는 건 싫어
# 수열에서 같은 원소가 여러개 들어잇는 수열 싫어함
# 같은 원소가 k개 이하로 들어있는 최장 연속 부분 수열의 길이
# 100,000 이하 양의 정수로 이루어진 길이가 n인 수열
    # => 같은 정수를 k개 이하로 포함한 최장 연속 부분 수열의 길이

# 입력 : 정수 n(1~200,000), k(1~100)
# a1 ~ an (1~100,000)
# 출력 : 조건을 만족하는 최장 연속 부분 수열의 길이

# 1차시도 : 42% 실패
# 2차시도 : 

import sys

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

count = [0]*100001
# count = [0]*(max(arr)+1)
length = 0
maxLen = 0
j = 0   # 현재 end 위치
end = arr[0]
for start in arr:
    if count[end] < k:
        while j < n:
            end = arr[j]
            if count[end] < k:
                count[end] += 1
                length += 1
                j += 1
            else:
                maxLen = max(maxLen, length)
                break
        if j >= n:
            maxLen = max(maxLen,length)
            break
    count[start] -= 1
    length -= 1

print(maxLen)     


# 9 2
# 3 2 5 5 6 4 4 5 7       # 7

# 10 1
# 1 2 3 4 5 6 6 7 8 9     # 6