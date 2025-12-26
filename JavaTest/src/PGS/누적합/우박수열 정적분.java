// 콜라츠 추측 : 모든 자연수 k에 대해 다음 작업 반복 시 항상 1 생성 가능
    // (n%2==0) -> n/2
    // (n%2==1) -> n*3+1
    // 결과값 > 1 -> 반복
// 우박수열 -> 꺾은선 그래프를 정적분 (모든 입력에 대한 결과는 2*27)
    // [a,-b] 범위 정적분 결과 = 꺾은선 그래프, x=a, y=n-b, y=0으로 둘러쌓인 공간의 면적 (n : 우박수열이 1이 될때까지의 횟수)
// 우박수의 초항 k(2~10000), 정적분 구하는 구간 목록 ranges(1~20000개) : a(0~200),-b(-200~0) -> 정적분 결과 목록
// 시작점 > 끝점 이라 유효하지 않은 구간 : -1
import java.util.*;
class Solution {
    static ArrayList<Double> singleAreas = new ArrayList<>(); // 0~n-2
    public double[] solution(int k, int[][] ranges) {
        double[] answer = new double[ranges.length];
        
        // 우박 수열 꺾은선 그래프 찾기 + 정적분 계산 (대각선 넓이 (욋변+아랫변)*높이/2)
        findSequence(k);
        int n = singleAreas.size()+1;
        
        // 범위 계산
        for(int i=0; i<ranges.length; i++) {
            int x = ranges[i][0];       // a    
            int y = n + ranges[i][1];   // n-b
            // 구간 [a,n-b] => a ~ n-b-1
            if (x>y-1)
                answer[i] = -1.0;
            else {
                for (int j=x; j<y-1; j++) {
                    answer[i] += singleAreas.get(j);
                }
            }
        }
        
        return answer;
    }
    
    private static void findSequence(int k) {
        int next = k;
        while (k>1) {
            if (k%2==0)
                next = k/2;
            else
                next = k * 3 + 1;
            singleAreas.add(calculateSingleIntegral(k,next));
            k = next;
        }
    }
    
    private static double calculateSingleIntegral(int h1, int h2) {
        return ((double)h1 + (double)h2)/2;
    }
}


// 이후 파괴되지 않은 건물 -> 연속 펄스 부분 수열의 합 문제 풀기 (누적합 문제)
