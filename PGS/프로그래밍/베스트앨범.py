# 속한 노래가 가장 많이 재생된 장르 -> 장르 내에서 가장 많이 재생된 노래 -> 고유번호가 낮은 노래
# 장르별 가장 많은 재생된 노래 2개씩 모은 베스트 앨범에 들어갈 노래와 고유번호
# 장르에 속한 곡이 1개라면 하나의 곡만 선택 / 장르 1~99 / 모든 장르의 총 재생 횟수 다름

def solution(genres, plays):
    answer = []
    count = {}
    songs = {}
    for i in range(len(genres)):
        # 장르별 재생 횟수 구하기
        if genres[i] in count.keys():
            count[genres[i]] += plays[i]
            songs[genres[i]] += [(plays[i],i)]
        else:
            count[genres[i]] = plays[i]
            songs[genres[i]] = [(plays[i],i)]
    
    sorted_genres = sorted(count, key=lambda x:count[x])
    
    while sorted_genres:
        cur = songs[sorted_genres.pop()]
        cur.sort(key=lambda x:-x[0])
        for i in range(2):
            if i == len(cur):
                break
            answer.append(cur[i][1])
    return answer