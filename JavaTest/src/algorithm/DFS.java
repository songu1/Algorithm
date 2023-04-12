package algorithm;
import java.lang.reflect.Array;
import java.util.*;

/*
    DFS

 */
public class DFS {
    // 방문한 노드를 확인하는 boolean 배열
    public static boolean[] visited = new boolean[9];
    // 방문할 배열
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void dfs(int x){
        //현재 노드 방문 처리
        visited[x]=true;
        System.out.print(x+" ");
        // 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for (int i=0; i<graph.get(x).size();i++){
            int y=graph.get(x).get(i);
            if (!visited[y]) dfs(y);
        }
    }

    public static void main(String[] args) {
        // 생략
    }
}
