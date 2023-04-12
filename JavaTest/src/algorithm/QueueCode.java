package algorithm;
import java.util.*;
/*
    큐
    offer(item) : item을 큐의 가장 끝부분에 삽입
    poll() : 큐에서 가장 앞의 값을 삭제 (비어있다면 null)
    peek() : 큐의 첫번째 값 참조
    clear() : queue 초기화
 */
public class QueueCode {
    public static void main(String[] args) {
        Queue<Integer> q = new LinkedList<>();

        q.offer(5);     // q.offer() : 삽입
        q.offer(2);
        q.offer(3);
        q.offer(7);
        q.poll();           // q.poll() : 삭제
        q.offer(1);
        q.offer(4);
        q.poll();

        // 먼저 들어온 원소부터 추출
        while (!q.isEmpty()){
            System.out.print(q.poll()+" ");
        }

    }
}
