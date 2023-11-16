package BOJ.greedy;
//빵집
//원웅이는 근처 빵집의 가스관에 몰래 파이프를 설치해 훔쳐서 사용
//빵집 위치 R*C (1열 : 근처 빵집 가스관, 마지막열 : 원웅이의 빵집)
//가스관과 빵집을 연결하는 파이프 설치(사이에 건물이 있다면 놓을 수 없음)
//가스관 - 빵집 파이프라인은 1열에서 시작, 마지막열에서 끝
//오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선 연결 / 각 칸 중심끼리 연결
//가스관과 빵집을 연결하는 파이프라인 여러개 설치, 경로 겹치거나 접할 수 X
//
//입력 : R,C(1~10000 / 5~500)
//빵집 근처의 모습 (.:빈칸 / x:건물) - 1열, 마지막열은 비어있음
//출력 : 원웅이가 놓을 수 있는 파이프라인의 최대 개수
import java.util.*;
import java.io.*;
import java.lang.*;

public class Greedy3109 {
    public static int[] dx = {-1,0,1};

    public static boolean dfs(String[][] graph, int x, int y, int r, int c){
        int nx,ny;
        if (y == c-1)
            return true;
        // 방문처리
        graph[x][y] = "x";
        for(int i=0;i<3;i++){
            nx = x + dx[i];
            ny = y + 1;
            if(nx<0 | nx>=r | ny<0 | ny>=c)
                continue;
            if (graph[nx][ny].equals(".")){
                if (dfs(graph,nx,ny,r,c))
                    return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        String[][] graph = new String[r][c];
        for(int i=0;i<r;i++){
            graph[i] = br.readLine().split("");
        }

        int count = 0;
        for(int i=0;i<r;i++){
            if (dfs(graph,i,0,r,c))
                count += 1;
        }
        System.out.println(count);

    }
}
