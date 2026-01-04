// https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=java#
// 조이스틱으로 알파벳 이름 완성 (초기 : A로만 이루어짐)
// 상 : 다음, 하 : 이전, 좌 : 커서 왼쪽 이동, 우 : 커서 오른쪽 이동
// 만들고자하는 이름 name(1~20길이) -> 조이스틱 조작횟수의 최솟값
// 풀이
    // 상하 개수 : A와 name 알파벳의 최소 차이
    // 좌우 개수 : (1)좌 (2)우 (3)좌->우(시작점 거침) (4)우->좌(시작점 거침)
        // 시작지점으로 부터의 좌방향/우방향 이동 시 거리 구하기
        // 단방향(좌/우) : 좌방향이동시 제일 낮은 인덱스 , 우방향이동시 제일 높은 인덱스
        // 방향전환 : 방향 전환 시 무조건 시작지점을 거쳐 이동함
            // "우방향i번째값 * 2 + 좌방향i+1번째값" 과 "우방향i번째 값 + 좌방향i+1번째값 * 2" 중 최소 
// 엣지케이스 고려! : 모든값이 A인 경우
import java.util.*;
class Solution {
    int a = (int) 'A';
    int z = (int) 'Z';
    public int solution(String name) {
        int answer = 0;
        int n = name.length();
        List<Integer> rDist = new ArrayList<>();    // 우 방향 거리
        List<Integer> lDist = new ArrayList<>();    // 좌 방향 거리
        // 상하 개수 구하기
        for(int i=0; i<n;i++) {
            if (name.charAt(i) != 'A') {
                int current = (int) name.charAt(i);
                answer += Math.min(current-a, z+1-current);
                // 시작 지점 제외 A가 아닌 지점의 좌/우 방향 거리 구하기
                if (i != 0) {
                    rDist.add(i);
                    lDist.add(n-i);
                }
            }
        }
        // A로만 이루어진 값
        int nn = rDist.size();
        if (nn==0)
            return answer;
        // 좌우 개수(좌우 왔다갔다하면 오히려 횟수가 커짐)
        // 좌/우 단방향 최소거리 구하기
        int minDist = Math.min(rDist.get(nn-1), lDist.get(0));  // rDist 마지막값, lDist 처음값 : 가장 끝 지점
        // 방향 전환(좌->우 / 우->좌) 시 최소 거리 구하기 (가장 끝 지점 가능 경우 제외)
        for (int i=0; i<nn-1; i++) {
            minDist = Math.min(minDist, rDist.get(i)*2 + lDist.get(i+1));
            minDist = Math.min(minDist, rDist.get(i) + lDist.get(i+1)*2);
        }
        answer += minDist;
        return answer;
    }
    
}
