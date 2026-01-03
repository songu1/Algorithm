// https://school.programmers.co.kr/learn/courses/30/lessons/92344
// n*m(최대 1000*1000) 맵의 내구도를 가진 건물을 적이 공격하여 파괴
// 적 : 공격 -> 내구도 감소, 내구도<=0이면 파괴
// 아군 : 회복 스킬 -> 내구도 증가
// 건물의 내구v도(1~1000) 배열 board , 적의 공격 or 아군 회복스키 배열 skill(1~250000) -> 최종적으로 파괴되지 않은 건물의 개수
// skill [type(1:적,2:아군), r1, c1, r2, c2,degree(내구도 변화;1~500)]

// 풀이 : 차분배열 + 2차원 누적합 
// 2차원 누적합 : prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] -prefix[i][j]
    // prefix[i-1][j] = arr[i-1][j] + prefix[i][j]
    // prefix[i][j-1] = arr[i][j-1] + prefix[i][j]
    // => prefix[i][j]가 중복됨
// 2차원 차분 배열 : 시작점에 +, 오른쪽 끝 다음/아래쪽 끝 다음에 -, 끝점 아래 대각선에 +(중복)
    // (r1, c2+1) 부터 오른쪽 전체 -k , (r2+1,c1)부터 아래쪽 전체 -k => (r2+1, c2+1) 위치는 2번 빠짐

import java.util.*;
class Solution {
    public int solution(int[][] board, int[][] skill) {
        int answer = 0;   
        int n = board.length;
        int m = board[0].length;
        // 차분 배열 생성
        int[][] diffArray = new int[n+1][m+1];
        for (int[] s : skill) { // type, r1,c1,r2,c2 , degree
            int degree = (s[0]==1) ? (-1)*s[5] : s[5];
            diffArray[s[1]][s[2]] += degree;
            diffArray[s[1]][s[4]+1] += (-1)*degree;
            diffArray[s[3]+1][s[2]] += (-1)*degree;
            diffArray[s[3]+1][s[4]+1] += degree;
        }
        
        // 차분 배열의 누적합 구하기
        for (int i=1; i<n+1; i++) {
            diffArray[i][0] += diffArray[i-1][0];
        }
        for (int j=1; j<m+1; j++) {
            diffArray[0][j] += diffArray[0][j-1];
        }
        for (int i=1; i<n+1; i++) {
            for (int j=1; j<m+1; j++) {
                diffArray[i][j] += diffArray[i-1][j] + diffArray[i][j-1] - diffArray[i-1][j-1];
            }
        }
                        
        // 결과값 구하기
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (board[i][j]+diffArray[i][j] > 0) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}
