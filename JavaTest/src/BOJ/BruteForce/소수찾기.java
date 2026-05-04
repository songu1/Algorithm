// https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=java
// 한자리 숫자가 적힌 종이 조각 -> 종이 조각을 붙여 만들 수 있는 소수의 개수
import java.util.*;
class Solution {
    static int[] input;
    static boolean[] visited;
    static HashSet<Integer> set = new HashSet<>();
    public int solution(String numbers) {  // 개수 7개 이하 + 구할 수 있는 숫자는 0 ~ 9999999
        int answer = 0;
        input = new int[numbers.length()];
        visited = new boolean[numbers.length()];
        for(int i=0; i<numbers.length(); i++) {
            input[i] = numbers.charAt(i) - '0';
        }
        backtracking("");
        for (int num:set) {
            if (isPrime(num)) {
                answer++;
            }
        }
        
        return answer;
    }
    
    // 순서가 필요
    private void backtracking(String numStr) {
        if (numStr.length() > 0) {
            set.add(Integer.parseInt(numStr));
        }
        
        for (int i=0; i<input.length; i++) {
            if(!visited[i]) {
                visited[i] = true;
                backtracking(numStr+input[i]);
                visited[i] = false;
            }
        }
    }
    
    private boolean isPrime(int number) {
        if (number < 2) return false;
        for (int i = 2; i <= (int) Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
    
}
