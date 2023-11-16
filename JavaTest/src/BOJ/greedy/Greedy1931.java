package BOJ.greedy;

//# 회의실 배정
//# 1개의 회의실 - n개의 회의
//# 각 회의 i에 대해 시작시간, 끝나는 시간
//# 회의 한번 시작하면 중단 금지, 회의 끝나는 동시에 다음 회의 시작 가능
//# 회의 시작시간과 끝나는 시간이 같을 수 있음
//# 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
//
//
//# 입력 : 회의의 수 n (1~100,000)
//# 각 회의의 정보 - 회의 시작시간, 끝나는 시간 (0~ 2^31-1)
//# 출력 : 최대 사용할 수 있는 회의의 최대 개수

import java.util.*;
import java.io.*;
import java.lang.*;

public class Greedy1931 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] meeting = new int[n][2];
        StringTokenizer st;
        for(int i=0; i<n;i++){
            st = new StringTokenizer(br.readLine());
            meeting[i][0] = Integer.parseInt(st.nextToken());
            meeting[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(meeting,(o1,o2) -> {
            if(o1[0] == o2[0]){
                return o1[1]-o2[1];
            }
            return o1[0]-o2[0];
        });
//        System.out.println(Arrays.deepToString(meeting));

        int start = -1;
        int end = -1;
        int count = 0;
        for(int[] m : meeting){
            // 이전 회의 종료시 새로운 회의 찾기
            if(m[0] >= end){
                start = m[0];
                end = m[1];
                count += 1;
            }
            // 더 빨리 끝나는 회의가 있을 경우
            else if(m[0] < end & m[1] < end){
                start = m[0];
                end = m[1];
            }
        }
        System.out.println(count);
    }

}

//11
//1 4
//3 5
//0 6
//5 7
//3 8
//5 9
//6 10
//8 11
//8 12
//2 13
//12 14         // 4