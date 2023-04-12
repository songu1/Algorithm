package algorithm;
import java.lang.*;
import java.util.*;


/* 스택 */
/*
    pop() : 스택에서 가장 위에 있는 항목을 제거
    push(item) : item하나를 스택의 가장 윗 부분에 추가
    peek() : 스택의 가장 위에 있는 항목을 반환
    isEmpty() : 스택이 비어있을 때에 true를 반환
*/
public class StackCode {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();

        s.push(5);
        s.push(2);
        s.push(3);
        s.push(7);
        s.pop();
        s.push(1);
        s.push(4);
        s.pop();

        while(!s.empty()){
            System.out.print(s.peek()+" ");
            s.pop();
        }
    }
}
