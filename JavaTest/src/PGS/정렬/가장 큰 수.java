// 0, 양의정수 -> 정수를 이어붙여 만들수 있는 가장 큰 수
// numbers -> 순서를 재배치하여 만들 수 있는 가장 큰수를 문자열로 바꾸어 return
// 자릿수대로 sort할 필요o
// 숫자는 0~1000 => 각 숫자를 3자리수로 임의로 만들기
import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        int n = numbers.length;
        String[] strArr = new String[n];
        for (int i=0; i<n; i++) {
            strArr[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(strArr, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2+o1).compareTo(o1+o2);
            }
        });
            
        if(strArr[0].equals("0"))  // 값으로 0이 들어오는 경우
            answer = "0";
        else {
            StringBuilder sb = new StringBuilder();
            for (String x:strArr) {
                sb.append(x);
            }
            answer = sb.toString();
        }
        return answer;
    }

}
