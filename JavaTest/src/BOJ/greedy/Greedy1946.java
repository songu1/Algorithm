package BOJ.greedy;
//# 신입 사원
//# 1차 서류 심사, 2차 면접 시험
//# 서류심사 성적, 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자 선발
//# A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류, 면접 성적이 떨어지면 선발 X
//# 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원
//
//# 입력 : 테케 수 t(1~20)
//# 각 테스트케이스
//# 지원자 숫자 n(1~100000)
//# 각 지원자의 서류심사, 면접 성적의 순위(1~n위, 동석차 없음)
//# 출력 : 각 테스트케이스에 대해 회사가 선발할 수 있는 신입사원의 최대 인원수
//
//# 알고리즘
//# 풀이 : sort 후 무조건 앞의 rank[i][1] 값보다 뒤의 rank[i][1]값이 작아야함 (모두와 비교해야하므로)
//# 앞의 값보다 크다면 무조건 제외

import java.util.*;
import java.io.*;
import java.lang.*;

public class Greedy1946 {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for(int t=0;t<tc;t++){
            int n = Integer.parseInt(br.readLine());
            int[][] rank = new int[n][2];
            StringTokenizer st;
            for(int i=0;i<n;i++){
                st = new StringTokenizer(br.readLine());
                rank[i][0] = Integer.parseInt(st.nextToken());
                rank[i][1] = Integer.parseInt(st.nextToken());
            }
            // 서류점수를 기준으로 오름차순 정렬
            Arrays.sort(rank,(o1,o2) -> {
                return o1[0]-o2[0];
            });
            int count = 1;
            int pre = rank[0][1];
            for(int i=1; i<n; i++){
                if (rank[i][1] < pre){
                    count += 1;
                    pre = rank[i][1];
                }
            }
            System.out.println(count);
        }
    }
}
