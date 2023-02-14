# 전자 매장의 부품 n개(각 부품은 정수형태의 고유한 번호 존재)
# 손님이 m개 종류의 부품을 대량 구매, 견적서 요구
# 가게 안에 부품이 모두 있는지 확인하는 프로그램

# 입력 : 전자매장의 부품 n (100만개)
# n개의 정수로 전재매장의 부품번호
# 손님이 원하는 부품 종류수 m (100만개)
# 손님이 원하는 종류의 부품번호

# 각 부품 번호별 yes/no 값

def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid = (start+end) //2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
    

import sys
n=int(sys.stdin.readline())
store=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
customer=list(map(int,sys.stdin.readline().split()))

store.sort()
resultList=[]

for i in customer:
    result=binary_search(store,i,0,n-1)
    if result is None:
        resultList.append('no')
    else:
        resultList.append('yes')

print(*resultList,sep=' ')



# 5
# 8 3 7 9 2
# 3
# 5 7 9           # no yes yes