package BOJ.bfs;
//# 바이러스
//# 한 컴퓨터가 웜바이러스 걸림 -> 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터가 바이러스에 걸림
//# 1번 컴퓨터가 웜 바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수를 출력
//
//# 입력 : 컴퓨터의 수 m (컴퓨터 번호 1번부터~)
//# 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수 n
//# 네트워크 상에서 직접 연결되어있는 컴퓨터 번호 쌍 n개
//# 출력 : 1번 컴퓨터가 웜바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리게 되는 컴퓨터의 수 (1번 제외)
import java.util.*;
import java.io.*;
import java.lang.*;
public class Bfs2606 {
    public static boolean[] visited;
    public static int[][] graph;
    public static int m,n;
    public static int count=0;

    public static int bfs(int start){
        Queue<Integer> queue = new LinkedList<Integer>();
        int v;
        visited[start] = true;
        queue.offer(start);
        while (!queue.isEmpty()){
            v = queue.poll();
            for(int i=1;i<m+1;i++){
                if(graph[v][i]!=0 & !visited[i]){
                    visited[i] = true;
                    queue.offer(i);
                    count += 1;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        m = Integer.parseInt(br.readLine());
        n = Integer.parseInt(br.readLine());
        graph = new int[m+1][m+1];
        visited = new boolean[m+1];
        int a,b;
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        System.out.println(bfs(1));
    }
}
