package BOJ.greedy;
//# 단어 수학 - 힌트 보고 풂!!
//# n개의 알파벳 대문자로 이루어짐
//# 각 알파벳 대문자를 0~9 중 하나로 바꿔서 n개의 수를 합하는 문제
//# 같은 알파벳은 같은 숫자로 바꿔야하며, 여러개의 알파벳이 같은 숫자X
//# n개의 단어 -> 그 수의 합을 최대로 만드는 프로그램
//# 예시
//# GCF + ACDEB (783 + 98654) = 99437
//
//# 입력 : 단어의 개수 N(1~10)
//# N개의 단어가 주어짐 (모든 단어에 포함된 알파벳은 최대 10개, 수의 길이는 8)
//# 출력 : 주어진 단어의 합의 최댓값
//
//# 큰 자리수부터 선택하는 문제풀이 X
//# 우선순위 결정 후 숫자 순서대로 넣기
import java.util.*;
import java.io.*;
import java.lang.*;

public class Greedy1339 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] words = new String[n];
        int[] alpha = new int[26];       // 0~25 : ord(문자)-65
        for(int i=0;i<n;i++){
            words[i] = br.readLine();
            for(int j=0;j<words[i].length();j++){
                int ch = (int) words[i].charAt(j);
                alpha[ch-65] += Math.pow(10,words[i].length()-j-1);
            }
        }
        Arrays.sort(alpha);
        int result = 0;
        for(int i=0;i<10;i++){
            if (alpha[25-i]==0)
                break;
            result += alpha[25-i]*(9-i);
        }
        System.out.println(result);
    }
}
