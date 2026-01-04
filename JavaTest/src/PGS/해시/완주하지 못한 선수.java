// https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=java 
// 1명을 제외한 선수 마라톤 완주
// 마라톤 참여 선수 이름 배열 , 완주한 선수 이름 배열 -> 완주하지 못한 선수 이름 return
// participant 수 1~100,000 
// 참가자 중 동명이인 존재
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String,Integer> map = new HashMap<>();
        
        for (String p : participant) {
            map.put(p, map.getOrDefault(p,0)+1);
        }
        
        for (String c : completion) {
            map.put(c,map.getOrDefault(c,0)-1);
        }
        
        for (Map.Entry<String,Integer> entry : map.entrySet()) {
            if (entry.getValue() > 0) {
                answer = entry.getKey();
                break;
            }
        }
        
        return answer;
    }
}
