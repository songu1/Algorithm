package BOJ.bfs;
//# 토마토 - 최단거리와 비슷
//# 익은 토마토, 안익은 토마토 -> 하루 뒤 익은 토마토 인접 토마토도 익게 됨
//# 격자 모양 상자, 토마토 정보 -> 며칠이 지나면 다 익게 되는지 최소 일수
//# 토마토가 없는 칸도 있음
//
//# 상자 가로칸의 수 m, 상자 세로칸의 수 n
//# 하나의 상자에 저장된 토마토들으리 정보(n개의 줄)
//# 익은 토마토 1 / 익지않은 토마토 0 / 토마토X -1
//
//# 토마토가 모두 익을 때 까지의 최소 날짜 출력 (다 못익으면 -1)
import java.util.*;
import java.io.*;
import java.lang.*;
public class Bfs7576 {
    public static int m, n;
    public static int[][] graph;
    public static Queue<int[]> queue = new LinkedList<>();
    public static int[] dx = {-1,1,0,0};
    public static int[] dy = {0,0,-1,1};

    public static void bfs(){
        int[] xy;
        int x,y,nx,ny;
        while(!queue.isEmpty()){
            xy = queue.poll();
            x = xy[0];
            y = xy[1];
            for(int i=0; i<4; i++){
                nx = x + dx[i];
                ny = y + dy[i];
                if(nx < 0 | nx >= n | ny < 0 | ny >= m)
                    continue;
                if(graph[nx][ny]==0 | graph[nx][ny] > graph[x][y]+1){
                    graph[nx][ny] = graph[x][y] + 1;
                    queue.offer(new int[]{nx,ny});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());   // 가로
        n = Integer.parseInt(st.nextToken());   // 세로
        graph = new int[n][m];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                graph[i][j] = Integer.parseInt(st.nextToken());
                if (graph[i][j] == 1)
                    queue.offer(new int[]{i,j});
            }
        }
        bfs();

        int maxVal = 0;
        boolean zero = false;
        for(int i=0;i<n;i++){
            for(int j=0; j<m; j++){
                if(graph[i][j] == 0){
                    maxVal = 0;
                    zero = true;
                    break;
                }
                else if(graph[i][j] > maxVal)
                    maxVal = graph[i][j];
            }
            if(zero)
                break;
        }
        System.out.println(maxVal-1);
    }
}
