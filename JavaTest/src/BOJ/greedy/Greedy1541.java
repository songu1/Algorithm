package BOJ.greedy;
//# 잃어버린 괄호
//# 양수, +, -, 괄호로 식을 만들고 괄호를 모두 지움
//# 괄호를 적절히 쳐서 이 식의 값을 최소로 만들기
//
//# 입력 : 0~9, +, - 만으로 이루어진 식이 주어짐
//# 처음과 마지막은 숫자
//# 연속해서 2개의 연산자X
//# 5자리보다 많이 연속되는 숫자는 없음
//# 숫자 0 으로 시작 가능
//# 출력 : 정답을 출력
//
//# + 뒤의 숫자는 결과에 영향을 끼치지 않음
//# - 뒤의 숫자가 결과에 영향을 끼침 => -를 기준으로 식을 split하고 -뒤의 수들은 괄호로 묶음

import java.io.*;
import java.lang.*;

public class Greedy1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("-");

        int result = 0;
        String[] num = input[0].split("\\+");
        for(String n:num){
            result += Integer.parseInt(n);
        }

        for(int i=1;i<input.length;i++){
            String[] num2 = input[i].split("\\+");
            for(String n:num2){
                result -= Integer.parseInt(n);
            }
        }

        System.out.println(result);

    }
}
