# 모두의 마블
# 합성 이벤트 : 순서가 매겨진 여러장의 카드, 레벨이 있음
    # 카드 A에 카드 B를 덧붙일 수 있다
    # 조건
        # 두 카드는 인접한 카드
        # 업그레이드된 카드 A의 레벨은 변하지 않음
    # 카드 합성을 할때마다 두 카드 레벨의 합만큼 골드를 받음
    # A,B는 임의로 정하면 됨 -> 둘 중 큰 값이 A로

# 입력 : 카드 개수 n(1~1000)
# 카드 레벨 Li가 순서대로 주어짐 (1~100000)
# 출력 : 영관이가 받을 수 있는 골드의 최댓값

import sys

n = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))

cards.sort(reverse=True)
gold = cards[0]*(n-1) + sum(cards[1:])

if n==1:
    print(cards[0])
else:
    print(gold)

# 3
# 40 30 30        # 140

# 4
# 10 20 70 10     # 250

# 3
# 20 70 10        # 170

# 1
# 24              # 24

# x1(40, 70) 30
# x2(40,70)