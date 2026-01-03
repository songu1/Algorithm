// https://school.programmers.co.kr/learn/courses/30/lessons/161988
// 펄스 수열 : -1과 1이 번갈아 나오는 수열
// 어떤 수열의 연속 부분 수열에 같은 길이의 펄스 수열을 곱 -> 연속 펄스 부분 수열
// 정수 수열 sequence(1~500,000개, 원소 : -10만~10만) -> 연속 펄스 부분 수열의 합 중 가장 큰것을 return
import java.util.*;
class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        int n = sequence.length;
        // 수열 * 펄스수열으로 누적합 구하기
        long[] seq1 = new long[n];
        long[] seq2 = new long[n];
        int pulse = 1;
        seq1[0] = sequence[0]*pulse;
        seq2[0] = sequence[0]*pulse*(-1);
        for (int i=1; i<n; i++) {
            pulse *= -1;
            seq1[i] = seq1[i-1] + sequence[i]*pulse;
            seq2[i] = seq2[i-1] + sequence[i]*pulse*(-1);
        }

        // 누적합으로 연속 펄스 부분 수열 합이 최대인 케이스 구하기
        answer = Math.max(seq1[0], seq2[0]); // 누적합 배열 2개 중 첫 원소가 큰 값
        long min1 = Math.min(0,seq1[0]);
        long min2 = Math.min(0,seq2[0]);
        for (int i=1; i<n; i++) {
            // 현재 인덱스까지 중 구간합이 최대인 값 구하기
            answer = Math.max(answer, seq1[i]-min1);
            answer = Math.max(answer, seq2[i]-min2);
            // 현재 인덱스까지의 누적합 중 가장 작은값 구하기 (-가장작은값 = +가장 큰값)
            min1 = Math.min(min1, seq1[i]);
            min2 = Math.min(min2, seq2[i]);
        }

        return answer;
    }
}
