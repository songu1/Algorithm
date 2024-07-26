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

    public static void dfs(int x, int y) {
        visited[x][y] = true;
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(nx>0 && nx <=n && ny>0 && ny<=m){
                if(maze[nx][ny]==1 & !visited[nx][ny]){
                    maze[nx][ny] = maze[x][y]+1;
                    dfs(nx,ny);
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
        dfs(1,1);
        for(int i=1; i<=n; i++){
            System.out.println(Arrays.toString(maze[i]));
        }
        System.out.println(maze[n][m]);
    }

}
