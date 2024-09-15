import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static int[][] maze;
    public static boolean[][] visited;
    public static int n,m;

    public static int[] dx = {-1,1,0,0};
    public static int[] dy = {0,0,-1,1};

    public static void bfs(int x, int y){
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {x,y});
        visited[x][y] = true;
        while(!queue.isEmpty()){
            int[] xy = queue.poll();
            for(int i=0; i<4; i++){
                int nx = xy[0] + dx[i];
                int ny = xy[1] + dy[i];
                if (nx <= 0 || nx > n || ny <= 0 || ny > m)
                    continue;
                if(maze[nx][ny]==1 && !visited[nx][ny]){
                    queue.offer(new int[] {nx,ny});
                    visited[nx][ny] = true;
                    maze[nx][ny] = maze[xy[0]][xy[1]] + 1;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        maze = new int[n+1][m+1];
        visited = new boolean[n+1][m+1];

        for(int i=1 ; i<=n ;i++){
            String[] text = br.readLine().split("");
            for (int j=1;j<=m;j++){
                maze[i][j] = Integer.parseInt(text[j-1]);
            }
        }

        br.close();
        bfs(1,1);
        for(int i=1; i<=n; i++){
            System.out.println(Arrays.toString(maze[i]));
        }
        System.out.println(maze[n][m]);
    }

}
