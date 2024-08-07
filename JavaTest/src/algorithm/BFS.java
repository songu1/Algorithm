package algorithm;
import java.util.*;

public class BFS {
    public static boolean[] visited=new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        // 현재 노드 방문 처리
        visited[start]=true;
        //큐가 빌 때까지 반복
        while(!q.isEmpty()){
            // 큐에서 하나의 원소를 뽑아 출력
            int x=q.poll();
            System.out.print(x+" ");
            // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for (int i=0; i<graph.get(x).size(); i++){
                int y=graph.get(x).get(i);
                if(!visited[y]){
                    q.offer(y);
                    visited[y]=true;
                }
            }
        }
    }

    public static void bfs2(int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;
        while(!q.isEmpty()) {
            int x = queue.poll();
            for(int i:graph.get(x)){
                if(!visited[i]){
                    queue.offer(i);
                    visited[i] = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        // 생략
    }
}
